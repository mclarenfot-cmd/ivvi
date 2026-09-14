from decimal import Decimal
import unittest

from src.core.auth_service import AuthService
from src.orders.order_service import OrderService


class StubAuthService(AuthService):
    def __init__(self, allowed: bool) -> None:
        self._allowed = allowed

    def authenticate(self, username: str, password: str) -> bool:
        return self._allowed


class OrderServiceTest(unittest.TestCase):
    def test_create_order_returns_order_for_authorized_user(self) -> None:
        service = OrderService(StubAuthService(allowed=True))

        order = service.create_order(
            username="student",
            password="correct-password",
            items=["notebook"],
            total=Decimal("20.00"),
        )

        self.assertEqual(order.username, "student")
        self.assertEqual(order.items, ("notebook",))
        self.assertEqual(order.total, Decimal("20.00"))

    def test_create_order_rejects_unauthorized_user(self) -> None:
        service = OrderService(StubAuthService(allowed=False))

        with self.assertRaises(PermissionError):
            service.create_order(
                username="student",
                password="wrong-password",
                items=["notebook"],
                total=Decimal("20.00"),
            )

    def test_create_order_rejects_empty_items(self) -> None:
        service = OrderService(StubAuthService(allowed=True))

        with self.assertRaises(ValueError):
            service.create_order(
                username="student",
                password="correct-password",
                items=[],
                total=Decimal("20.00"),
            )

    def test_create_order_rejects_non_positive_total(self) -> None:
        service = OrderService(StubAuthService(allowed=True))

        with self.assertRaises(ValueError):
            service.create_order(
                username="student",
                password="correct-password",
                items=["notebook"],
                total=Decimal("0"),
            )


if __name__ == "__main__":
    unittest.main()

