from abc import ABC, abstractmethod
from requests import Session


class SessionManagerSingleton(type):
    """
    Singleton metaclass for SessionManager
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SessionManager(metaclass=SessionManagerSingleton):

    def __init__(self, headers: dict = None, timeout: int = 10):
        self.headers = headers
        self.timeout = timeout
        self.session = self.get_session()

    def get_session(self):
        s = Session()
        if self.headers:
            s.headers.update(self.headers)
        s.timeout = self.timeout
        return s

    def authenticate(self, username, password):
        to_b64 = f"{username}:{password}".encode("utf-8")
        self.headers.update({"Authorization": f"Basic {to_b64}"})

    def set_header(self, key, value):
        self.headers.update({key: value})

    def request(self, method: str, url: str, params: dict = None, **kwargs):
        s = self.get_session()
        response = s.request(method=method, url=url, params=params, **kwargs)
        return response


class BaseApi(ABC):
    """
    Base class for all APIs in the project
    Takes care of the session management and the base url to be used in the requests
    """
    def __init__(self, base_url: str = None, session_manager: SessionManager = None):
        self.base_url = base_url
        self.session_manager = session_manager

    @property
    def session(self):
        return self.session_manager.get_session()


if __name__ == '__main__':
    sm = SessionManager()
    session = sm.get_session()
