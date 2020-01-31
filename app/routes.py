from app import app
from .api.device import register

@app.route('/')
def index():
    return "Hello World"

app.add_url_rule('/','register',register)