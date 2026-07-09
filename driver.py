from pathlib import Path

from trip_planner.plugin_loader import load_pricing_plugin
from trip_planner.reports import build_report
from trip_planner.routes import load_routes
from trip_planner.settings import load_settings
from trip_planner.shell_format import quote_report_name
from trip_planner.versioning import supports_runtime


BASE_DIR = Path(__file__).resolve().parent


def main():
    if not supports_runtime("3.10"):
        raise RuntimeError("Legacy Trip Planner requires Python 3.10 or newer")

    settings = load_settings(BASE_DIR / "data" / "settings.ini")
    routes = load_routes(BASE_DIR / "data" / "routes.csv")
    plugin = load_pricing_plugin(BASE_DIR / "plugins" / "weekend_discount.py")

    print(build_report(routes, settings, plugin))
    print(f"Loaded plugin: {plugin.PLUGIN_NAME}")
    print(f"Quoted report name: {quote_report_name('trip_report.csv')}")


if __name__ == "__main__":
    main()

