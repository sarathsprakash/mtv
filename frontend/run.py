import os
from frontend import app

if __name__ == "__main__":
    app.run(debug=os.getenv('DEBUG', False))
