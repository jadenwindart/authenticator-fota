from app import app
from .api.device import register,get_credentials,authenticate_device

@app.route('/')
def index():
    return "Hello World"

app.add_url_rule('/register','register',register,methods=['POST'])
app.add_url_rule('/credentials','credentials',get_credentials,methods=['GET'])
app.add_url_rule('/authenticate','authenticate',authenticate_device,methods=['POST'])