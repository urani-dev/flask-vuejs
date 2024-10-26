import json
import os
from pathlib import Path

from flask import Blueprint

# Get environment variables.
FLASK_DEBUG = os.getenv("FLASK_DEBUG", "0")
VITE_ORIGIN = os.getenv("VITE_ORIGIN", "http://localhost:5173")

# Set application constants.
is_production = FLASK_DEBUG != "1"
project_path = Path(os.path.dirname(os.path.abspath(__file__)))

# Create assets blueprint that stores all Vite-related functionality.
assets_blueprint = Blueprint(
    "assets_blueprint",
    __name__,
    static_folder="frontend/dist/static",
    static_url_path="/static",
)

# Load manifest file in the production environment.
manifest = {}
if is_production:
    manifest_path = project_path / "frontend/dist/.vite/manifest.json"
    try:
        with open(manifest_path, "r") as content:
            manifest = json.load(content)
    except OSError as exception:
        raise OSError(
            f"Manifest file not found at {manifest_path}. Run `npm run build`."
        ) from exception


# Add `asset()` function and `is_production` to app context.
@assets_blueprint.app_context_processor
def add_context():
    def dev_asset(file_path):
        return f"{VITE_ORIGIN}/{file_path}"

    def prod_asset(file_path):
        try:
            return f"{manifest[file_path]['file']}"
        except:
            return "asset-not-found"

    def prod_css_asset(file_path):
        return manifest[file_path]['css']

    return {
        "asset": prod_asset if is_production else dev_asset,
        "asset_css": prod_css_asset,
        "is_production": is_production,
    }
