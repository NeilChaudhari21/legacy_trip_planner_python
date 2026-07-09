import csv

from trip_planner.models import Route


def load_routes(path):
    with open(path, newline="", encoding="utf-8") as route_file:
        reader = csv.DictReader(route_file)
        return [
            Route(
                name=row["name"],
                miles=float(row["miles"]),
                minutes=int(row["minutes"]),
                toll=float(row["toll"]),
            )
            for row in reader
        ]

