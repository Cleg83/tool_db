import os
from tool_db import app


if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),  # Defaults to 0.0.0.0
        port=int(os.environ.get("PORT", 5000)),  # Defaults to 5000
        debug=os.environ.get("DEBUG", False) == "TRUE"  # Convert DEBUG to bool
    )