import random
import time
from datetime import datetime

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from linkebot.handlers import retrieve_company_data, retrieve_people_data
from linkebot.utils import check_exists_by_class_name

from .settings import BASEDIR, DRIVERNAME, HEADLESS, LINKEDIN_BASE, OUTPUTDIR, logger

# from selenium.common.exceptions import TimeoutException

options = Options()
DELAY = 3  # seconds
# options.headless = HEADLESS
if HEADLESS:
    options.add_argument("--headless")


class LinkeBot:
    # does login with credential taken from external file (more actions in the future)
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.bot: WebDriver = None
        self.__enter__()

    def __enter__(self):
        if not self.bot:
            self.bot: WebDriver = webdriver.Firefox(
                options=options,
                executable_path=BASEDIR / "drivers" / DRIVERNAME,
            )

        return self

    def terminate(self):
        self.bot.close()
        self.bot.quit()

    def __exit__(self, type, value, traceback):
        self.terminate()

    def login(self) -> bool:
        is_error = False
        bot: WebDriver = self.bot
        bot.get(LINKEDIN_BASE)
        login_page: WebDriver = WebDriverWait(bot, DELAY).until(
            EC.presence_of_element_located((By.CLASS_NAME, "sign-in-form-container"))
        )

        username = login_page.find_element_by_id("session_key")
        password = login_page.find_element_by_id("session_password")
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

        is_error = check_exists_by_class_name(self.bot, "alert")

        if is_error:
            logger.error("Error while using credentials.")
            return not is_error

        is_error = check_exists_by_class_name(self.bot, "form__label--error")
        if is_error:
            logger.error("Error while using credentials.")

            return not is_error

        title_el = WebDriverWait(bot, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/head/title"))
        )
        title = title_el.get_attribute("innerHTML")
        if "security verification" in str(title).lower():
            is_error = True

        if is_error:
            logger.error("Security verification needed. Please use VPN if requried.")

            return not is_error

        time.sleep(2)
        remember_prompt = check_exists_by_class_name(
            self.bot, "remember-me-prompt__title"
        )
        if remember_prompt:
            logger.warning("Remember prompt encountered.")

            self.bot.find_element_by_class_name("btn__primary--large").click()

        main_el = WebDriverWait(bot, 15).until(
            EC.presence_of_element_located((By.ID, "main"))
        )
        user_el = WebDriverWait(main_el.parent, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "profile-rail-card__actor-link")
            )
        )

        logger.info(f"Logged in as '{user_el.text}'")

        return not is_error

    def like_random_posts(self, targets) -> None:
        for i, target in enumerate(targets):
            logger.info(f"Linking random posts of target {target}")
            self.bot.get(LINKEDIN_BASE + target + "/detail/recent-activity/shares/")
            post_el = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.ID, "main"))
            )

            elements = post_el.find_element_by_xpath(
                "//div[contains(@class, 'pv-recent-activity-detail__outlet-container')]"
            )
            div_child = elements.find_element_by_xpath("./child::*")
            childrens = div_child.find_elements_by_xpath("./child::*")
            logger.info(f"User has {len(childrens)} posts")
            random_post = random.choice(childrens)
            logger.info("Randomly chosing 1 post")

            for c in [random_post]:
                _id = c.get_attribute("id")
                logger.info(f"Liking post with id {_id}")
                btn = c.find_element_by_xpath(
                    "//button[contains(@class, 'artdeco-button')]"
                )

                btn.find_element_by_xpath(
                    "//div[contains(@class, 'artdeco-button__text')]"
                ).click()
                time.sleep(1)

    def search(self, targets, progress_callback=None):
        # search for a specific "target", like a company or a person, within LinkedIn

        records = []

        for i, target in enumerate(targets):
            if progress_callback:
                progress_callback.emit((i / len(targets)) * 100)

            self.bot.get(LINKEDIN_BASE + target)
            identity, handle = target.split("/")
            main_el = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.ID, "main"))
            )

            agg_dir = OUTPUTDIR / str(datetime.now().date())
            target_dir = agg_dir / identity
            target_dir.mkdir(parents=True, exist_ok=True)

            if identity == "company":
                logger.info(f"Scraping company '{handle}'")
                data = retrieve_company_data(main_el)
                data.to_csv(target_dir / f"{handle}.csv", index=False)

            elif identity == "in":
                logger.info(f"Scraping people '{handle}'")
                data = retrieve_people_data(main_el)

                data.to_csv(target_dir / f"{handle}.csv", index=False)

            records.append(data.copy())
            logger.info(f"Individual output saved at: {target_dir}/{handle}.csv")

        pd.concat(records).to_csv(f"{agg_dir}/output.csv", index=False)
        logger.info(f"Agg output saved at: {agg_dir}/output.csv")
