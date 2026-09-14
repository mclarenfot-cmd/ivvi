from dataclasses import dataclass
from decimal import Decimal
from typing import Sequence

from src.core.auth_service import AuthService


@dataclass(frozen=True)
class Order:
    username: str
    items: tuple[str, ...]
    total: Decimal


class OrderService:
    def __init__(self, auth_service: AuthService) -> None:
        self._auth_service = auth_service

    def create_order(
        self,
        username: str,
        password: str,
        items: Sequence[str],
        total: Decimal,
    ) -> Order:
        if not self._auth_service.authenticate(username, password):
            raise PermissionError("Invalid username or password")

        if not items:
            raise ValueError("Order must contain at least one item")

        if total <= Decimal("0"):
            raise ValueError("Order total must be positive")

        return Order(username=username, items=tuple(items), total=total)

