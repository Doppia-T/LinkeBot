from typing import Tuple

from .settings import CONFIGDIR
from .utils import yaml_loader


def get_linkedin_creds() -> Tuple[str, str]:
    # gets username from an external file called "credentials"
    email, password = ("", "")

    creds = yaml_loader(CONFIGDIR / "credentials.yaml")
    if creds:
        email = creds.get("email", None)  # type: ignore
        password = creds.get("password", None)  # type: ignore

    return email, password


def get_targets():
    # get page to search from external file called "targets"
    return yaml_loader(CONFIGDIR / "targets.yaml")["pages"]
