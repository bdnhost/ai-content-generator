
from abc import ABC, abstractmethod
from typing import Dict, Any

class GenericCMSConnector(ABC):
    def __init__(self, base_url: str):
        self.base_url = base_url

    @abstractmethod
    def create_post(self, title: str, content: str, status: str = 'draft') -> Dict[str, Any]:
        pass

    @abstractmethod
    def update_post(self, post_id: int, title: str = None, content: str = None, status: str = None) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_post(self, post_id: int) -> Dict[str, Any]:
        pass

    @abstractmethod
    def delete_post(self, post_id: int) -> Dict[str, Any]:
        pass
