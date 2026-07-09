import configparser

from trip_planner.models import PricingSettings


def load_settings(path):
    parser = configparser.SafeConfigParser()
    parser.read(path)

    return PricingSettings(
        fuel_price_per_gallon=parser.getfloat("pricing", "fuel_price_per_gallon"),
        miles_per_gallon=parser.getfloat("pricing", "miles_per_gallon"),
        budget_per_mile=parser.getfloat("pricing", "budget_per_mile"),
    )

