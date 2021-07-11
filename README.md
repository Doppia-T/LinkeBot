# LinkeBot

**A small bot for automating a Linkedin profile**

This is a first attempt to create a bot capable of managing a LinkedIn profile. It uses [Selenium WebDriver package](https://pypi.org/project/selenium/) and, since it is written for being used with [Mozilla Firefox](https://www.mozilla.org/it/firefox/new/) browser, [GeckoDriver](https://github.com/mozilla/geckodriver/releases).

This bot is designed to get the credentials of the LinkedIn profile from an external `.txt` file so that anyone can change the used profile -or its password - without the need of modifying the source code. Said file has to be put in the same folder with the others LinkeBot's `.py` files.

# Bot Setup

## Requirements

Use following comamnd for the requirements installation.

```bash
pip install -r requirements.txt
```

For the development requirements use:

```bash
pip install -r requirements.dev.txt
```

## Driver Setup

Linkebot uses `geckodriver` so download the latest driver from following link and set that up inside the `drivers` directory. Change the file name to `geckodriver`.

## Additional requiements setup

Since Linkebot requires user's credentials and targets to operate. You have to setup the credentials in `config/credentials.yaml` file.

Sample:

```yaml
# linkebot/config/credentials.yaml

email: myemail@email.com
password: mystrongpassword
```

For the target setup, edit the `targets.yaml` file inside the same directory.

```yaml
pages: # Do not change this key
  - "Amazon"
  - "Apple"
```

## Run

To run the Linkebot use the following commands:

```bash
python main.py
```

## RUN GUI

Run the GUI application using following command:
From the root directory.

```
python -m gui.linkebot_gui
```

Or just go into the `gui` directory and run:

```
python -m linkebot_gui.py
```

# Legal notes

**Warnings and disclaimer**

LinkeBot is not affiliated with, sponsored, authorised or endorsed by Microsoft Corporation, LinkedIn or any of their affiliates or subsidiaries. This is an independent and unofficial project.

LinkeBot violates LinkedIn's User Agreement Section 8.2 ("_Don’ts_"), paragraphs 2 and 13, and, for this reason, LinkedIn may temporarily or even permanently ban accounts using LinkeBot.
