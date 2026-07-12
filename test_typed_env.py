import unittest
from typed_env import validate


class TypedEnvTests(unittest.TestCase):
    def test_validates_integer(self): self.assertTrue(validate({"PORT": {"type": "integer", "required": True}}, {"PORT": "8080"}, "dev")["valid"])
    def test_reports_missing_required(self): self.assertIn("missing:PORT", validate({"PORT": {"required": True}}, {}, "dev")["errors"])
    def test_hides_sensitive_value(self):
        report = validate({"TOKEN": {"sensitive": True}}, {"TOKEN": "private-value"}, "dev")
        self.assertEqual(report["diagnostics"]["TOKEN"], "set")


if __name__ == "__main__": unittest.main()
