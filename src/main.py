from decimal import Decimal

from src.auth.password_auth_service import PasswordAuthService
from src.orders.order_service import OrderService


def main() -> None:
    auth_service = PasswordAuthService({"student": "correct-password"})
    order_service = OrderService(auth_service)

    order = order_service.create_order(
        username="student",
        password="correct-password",
        items=["keyboard", "mouse"],
        total=Decimal("125.50"),
    )

    print(f"Order created for {order.username}: {order.items}, total={order.total}")


if __name__ == "__main__":
    main()

