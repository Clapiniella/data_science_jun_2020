from src.config import PORT
from src.app import app

app.run("0.0.0.0", PORT, debug=True)