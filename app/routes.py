from app import app
from .api.device import register_device,get_credentials,authenticate_device,get_device_list
from .api.user import login,register

@app.route('/')
def index():
    return "Hello World"

app.add_url_rule('/register','register_device',register_device,methods=['POST'])
app.add_url_rule('/credentials','credentials',get_credentials,methods=['GET'])
app.add_url_rule('/authenticate','authenticate',authenticate_device,methods=['POST'])
app.add_url_rule('/list',"device_list",get_device_list,methods=['GET'])
app.add_url_rule('/user/login','login', login , methods=['POST'])
app.add_url_rule('/user/register','register',register,methods=['POST'])