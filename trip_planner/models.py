from dataclasses import dataclass


@dataclass(frozen=True)
class Route:
    name: str
    miles: float
    minutes: int
    toll: float


@dataclass(frozen=True)
class PricingSettings:
    fuel_price_per_gallon: float
    miles_per_gallon: float
    budget_per_mile: float

