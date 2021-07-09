import logging
from typing import Tuple

import yaml

from .settings import CONFIGDIR


def get_linkedin_creds() -> Tuple[str, str]:
    # gets username from an external file called "credentials"
    email, password = ("", "")

    with open(CONFIGDIR / "credentials.yaml", "r") as creds:
        try:
            creds = yaml.safe_load(creds)
            email = creds.get("email", None)  # type: ignore
            password = creds.get("password", None)  # type: ignore
        except yaml.YAMLError as exc:
            logging.error(f"There was an error {exc}")

    return email, password


def get_targets():
    # get page to search from external file called "targets"
    with open(CONFIGDIR / "targets.yaml", "r") as targets:
        try:
            return yaml.safe_load(targets)
        except yaml.YAMLError as exc:
            logging.error(f"There was an error {exc}")
