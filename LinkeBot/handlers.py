from typing import Tuple

from .settings import CONFIGDIR
from .utils import yaml_loader


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
    return yaml_loader(config_path)["pages"]
