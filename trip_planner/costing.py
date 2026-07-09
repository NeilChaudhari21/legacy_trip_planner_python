def calculate_route_cost(route, settings, pricing_plugin):
    fuel_cost = round((route.miles / settings.miles_per_gallon) * settings.fuel_price_per_gallon, 2)
    base_total = round(fuel_cost + route.toll, 2)
    adjusted_total = pricing_plugin.adjust_total(route.name, base_total)
    cost_per_mile = round(adjusted_total / route.miles, 2)

    return {
        "fuel_cost": fuel_cost,
        "toll": route.toll,
        "total": adjusted_total,
        "cost_per_mile": cost_per_mile,
        "status": "OK" if cost_per_mile <= settings.budget_per_mile else "OVER",
    }


def find_best_value(routes, settings, pricing_plugin):
    priced_routes = [
        (route, calculate_route_cost(route, settings, pricing_plugin))
        for route in routes
    ]
    return min(priced_routes, key=lambda item: item[1]["cost_per_mile"])

