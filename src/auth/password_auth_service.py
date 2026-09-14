from hashlib import sha256
from typing import Mapping

from src.core.auth_service import AuthService


class PasswordAuthService(AuthService):
    def __init__(self, users: Mapping[str, str]) -> None:
        self._password_hashes = {
            username: self.__hash_password(password)
            for username, password in users.items()
        }

    def authenticate(self, username: str, password: str) -> bool:
        expected_hash = self._password_hashes.get(username)
        if expected_hash is None:
            return False

        return expected_hash == self.__hash_password(password)

    def __hash_password(self, password: str) -> str:
        return sha256(password.encode("utf-8")).hexdigest()

