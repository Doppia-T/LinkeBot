import time
from datetime import datetime
from typing import Tuple

import pandas as pd
from selenium.webdriver.firefox.webdriver import WebDriver

from .settings import CONFIGDIR
from .utils import yaml_loader

# from selenium.webdriver.support.wait import WebDriverWait


# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By


def get_linkedin_creds(config_path=None) -> Tuple[str, str]:
    # gets username from an external file called "linkebot.yaml"
    if config_path is None:
        config_path = CONFIGDIR / "linkebot.yaml"
    email, password = ("", "")

    creds = yaml_loader(config_path)
    if creds:
        email = creds.get("email", None)  # type: ignore
        password = creds.get("password", None)  # type: ignore

    return email, password


def get_targets(config_path=None):
    # get page to search from external file called "linkebot"
    if config_path is None:
        config_path = CONFIGDIR / "linkebot.yaml"
    return yaml_loader(config_path)["targets"]


def retrieve_people_data(el_handle: WebDriver) -> pd.DataFrame:
    data = pd.DataFrame(
        data=[
            {"title": "test", "sub_title": "test", "ingestion_timestap": datetime.now()}
        ]
    )
    time.sleep(2)

    title = el_handle.find_element_by_class_name("text-heading-xlarge")
    data["title"] = title.text

    sub_title = el_handle.find_element_by_class_name("text-body-medium")
    data["sub_title"] = sub_title.text
    data["ingestion_timestamp"] = datetime.now()
    try:
        data["bio"] = el_handle.find_element_by_css_selector(
            ".inline-show-more-text.t-14"
        ).text
    except Exception:
        data["bio"] = ""

    return data.copy()


def retrieve_company_data(el_handle) -> pd.DataFrame:

    return pd.DataFrame(
        data=[{"title": "", "sub_title": "", "ingestion_timestap": datetime.now()}]
    )
