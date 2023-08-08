from abc import ABC, abstractmethod
from requests import Session


class SessionManager:

    def __init__(self, headers=None, timeout=10):
        self.headers = headers
        self.timeout = timeout

    def get_session(self):
        session = Session()
        session.headers.update(self.headers)
        session.timeout = self.timeout
        return session

    def authenticate(self, username, password):
        to_b64 = f"{username}:{password}".encode("utf-8")
        self.headers.update({"Authorization": f"Basic {to_b64}"})

    def set_header(self, key, value):
        self.headers.update({key: value})


class BaseApi(ABC):
    """
    Base class for all APIs in the project
    Takes care of the session management and the base url to be used in the requests
    """
    def __init__(self, base_url=None, session_manager=None):
        self.base_url = base_url
        self.session_manager = session_manager

    @property
    def session(self):
        return self.session_manager.get_session()

    @abstractmethod
    def get(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def post(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def put(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete(self, **kwargs):
        raise NotImplementedError
