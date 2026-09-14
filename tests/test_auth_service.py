import unittest

from src.auth.password_auth_service import PasswordAuthService


class PasswordAuthServiceTest(unittest.TestCase):
    def test_authenticate_accepts_valid_credentials(self) -> None:
        service = PasswordAuthService({"student": "correct-password"})

        self.assertTrue(service.authenticate("student", "correct-password"))

    def test_authenticate_rejects_invalid_password(self) -> None:
        service = PasswordAuthService({"student": "correct-password"})

        self.assertFalse(service.authenticate("student", "wrong-password"))

    def test_authenticate_rejects_unknown_user(self) -> None:
        service = PasswordAuthService({"student": "correct-password"})

        self.assertFalse(service.authenticate("admin", "correct-password"))


if __name__ == "__main__":
    unittest.main()

