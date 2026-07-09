import imp


def load_pricing_plugin(path):
    return imp.load_source("trip_pricing_plugin", str(path))

