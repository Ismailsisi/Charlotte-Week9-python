
import unittest
from student_telemetry_parser import parse_line


class TestTelemetryParser(unittest.TestCase):

    def test_psi_and_fahrenheit(self):
        result = parse_line(
            "WELL-21|2026-11-10T08:00:00|3100|psi|176|F|ACTIVE"
        )
        self.assertEqual(result["pressure_kpa"], 21373.75)
        self.assertEqual(result["temperature_c"], 80.0)

    def test_kpa_and_celsius(self):
        result = parse_line(
            "WELL-22|2026-11-10T08:10:00|22000|kPa|79|C|ACTIVE"
        )
        self.assertEqual(result["pressure_kpa"], 22000)
        self.assertEqual(result["temperature_c"], 79)

    def test_bad_numeric_value(self):
        with self.assertRaises(ValueError):
            parse_line(
                "WELL-23|2026-11-10T08:15:00|bad|psi|181|F|ACTIVE"
            )

    def test_missing_field(self):
        with self.assertRaises(ValueError):
            parse_line(
                "WELL-26|2026-11-10T08:35:00|2950|psi|177|F"
            )

    def test_unsupported_unit(self):
        with self.assertRaises(ValueError):
            parse_line(
                "WELL-25|2026-11-10T08:30:00|3500|bar|185|F|ACTIVE"
            )

    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            parse_line(
                "WELL-21|2026-11-10T08:00:00|3100|psi|176|F|UNKNOWN"
            )


if __name__ == "__main__":
    unittest.main()
