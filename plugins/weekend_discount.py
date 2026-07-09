PLUGIN_NAME = "weekend_discount"


def adjust_total(route_name, total):
    if route_name == "Mountain Detour":
        return round(total * 0.9975, 2)
    return total

