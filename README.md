# Legacy Trip Planner

This is a small Python 3.10 demo application for migration testing. It has a
single visible entry point, `driver.py`, plus supporting modules, data files,
tests, packaging metadata, and a plugin.

The program reads route data from CSV, reads cost settings from INI, loads a
pricing plugin, and prints a deterministic trip cost report.

## Run on Python 3.10

From this folder:

```powershell
py -3.10 driver.py
```

Expected output:

```text
LEGACY TRIP PLANNER
Budget target: $0.85 per mile

Route                 Miles  Minutes   Fuel    Toll   Total  Status
Harbor Run             18.4       34 $ 4.65 $  2.50 $  7.15  OK
Airport Connector      27.8       42 $ 7.02 $  4.75 $ 11.77  OK
Mountain Detour        41.2       71 $10.41 $  0.00 $ 10.38  OK

Best value: Mountain Detour at $0.25 per mile
Loaded plugin: weekend_discount
Quoted report name: trip_report.csv
```

## Run Tests

```powershell
py -3.10 -m unittest discover -s tests
```

