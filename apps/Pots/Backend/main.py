import os,uuid
import json
from flask_cors import CORS
from flask import Flask,config,render_template,request,Response,make_response
from werkzeug.datastructures import Headers
from src.Pots.user_manager import UserController
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
root_dir = os.path.join(root_dir, 'Pots/Frontend')
template_dir = os.path.join(root_dir, 'templates')
static_dir = os.path.join(root_dir, 'static')
app = Flask(__name__, template_folder=template_dir,static_folder=static_dir,root_path=os.path.dirname(__file__))
app.config.from_pyfile("config.py")

# CORS(app)
def valid_login(username,password,request):
    import uuid
    ses = app.session_interface.open_session(app,request)
    value = uuid.uuid3(uuid.NAMESPACE_DNS,password)
    return ses.get(username) == value


@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    code = 200
    print(request)
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password'],request):
            return home(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    if error != None:
        code = 401
    res=make_response(Response(render_template('login.html'),status=code,headers=Headers(defaults={"Access-Control-Allow-Origin":"*"})))     
    return res



@app.route('/user/id:<dni>', methods=['GET'])
def home(dni):
    uc = UserController(dni)
    headers = Headers(defaults={"Access-Control-Allow-Origin":"*"})
    print(uc.name) 
    if uc.name == None:
        res=make_response(Response(render_template('not_found.html'),status=200,headers=headers))
        return res
    return make_response(Response(json.dumps({"name":uc.name,"lastName":uc.last_name,"email":uc.email}),headers=headers))
    


