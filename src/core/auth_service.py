from abc import ABC, abstractmethod


class AuthService(ABC):
    """Contract for services that verify user credentials."""

    @abstractmethod
    def authenticate(self, username: str, password: str) -> bool:
        """Return True when the provided credentials are valid."""

