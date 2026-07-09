import subprocess
import sys
import unittest
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]


EXPECTED_OUTPUT = """LEGACY TRIP PLANNER
Budget target: $0.85 per mile

Route                 Miles  Minutes   Fuel    Toll   Total  Status
Harbor Run             18.4       34 $ 4.65 $  2.50 $  7.15  OK
Airport Connector      27.8       42 $ 7.02 $  4.75 $ 11.77  OK
Mountain Detour        41.2       71 $10.41 $  0.00 $ 10.38  OK

Best value: Mountain Detour at $0.25 per mile
Loaded plugin: weekend_discount
Quoted report name: trip_report.csv
"""


class DriverOutputTests(unittest.TestCase):
    def test_driver_prints_expected_report(self):
        result = subprocess.run(
            [sys.executable, "driver.py"],
            cwd=PROJECT_DIR,
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual(EXPECTED_OUTPUT, result.stdout)


if __name__ == "__main__":
    unittest.main()
