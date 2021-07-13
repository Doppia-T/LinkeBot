import logging
import random
import time

import yaml


def random_nap():
    nap_time = random.randint(30, 300)
    time.sleep(nap_time)


def yaml_loader(yaml_path):
    with open(yaml_path, "r") as d:
        try:
            return yaml.safe_load(d)
        except yaml.YAMLError as exc:
            logging.error(f"There was an error {exc}")
            return None
