__version__ = "1.0.0"

import requests as _r
from subprocess import Popen as _Popen
def _update(url):
    _Popen(["pip3", "install", "-U", url]).wait()
def check_updates(version: str, github_user: str, github_repo: str):
    if version != str(_r.get("http://raw.githubusercontent.com/" + github_user + "/" + github_repo + "/master/version.txt").text):
        _update("https://github.com/" + github_user + "/" + github_repo + "/archive/refs/heads/main.zip")
        print("Updated successful! Please restart this app!")
        raise SystemExit(0)
check_updates(__version__, "69-by-wer310", "simple-update")
