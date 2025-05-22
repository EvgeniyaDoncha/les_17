import os

from utils.sessions  import BaseSession


def reqres() -> BaseSession:
    reqres_url = os.getenv('reqres_url')
    return BaseSession(base_url=reqres_url)