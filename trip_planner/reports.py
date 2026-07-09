from trip_planner.costing import calculate_route_cost, find_best_value


def build_report(routes, settings, pricing_plugin):
    lines = [
        "LEGACY TRIP PLANNER",
        f"Budget target: ${settings.budget_per_mile:.2f} per mile",
        "",
        f"{'Route':<20} {'Miles':>6} {'Minutes':>8} {'Fuel':>6} {'Toll':>7} {'Total':>7}  Status",
    ]

    for route in routes:
        cost = calculate_route_cost(route, settings, pricing_plugin)
        lines.append(
            f"{route.name:<20} "
            f"{route.miles:>6.1f} "
            f"{route.minutes:>8} "
            f"${cost['fuel_cost']:>5.2f} "
            f"${cost['toll']:>6.2f} "
            f"${cost['total']:>6.2f}  "
            f"{cost['status']}"
        )

    best_route, best_cost = find_best_value(routes, settings, pricing_plugin)
    lines.extend([
        "",
        f"Best value: {best_route.name} at ${best_cost['cost_per_mile']:.2f} per mile",
    ])
    return "\n".join(lines)

