from flask import  render_template, request, Blueprint, redirect, make_response, url_for
from flask_cors import CORS
from flask_cognito import cognito_jwt_decode, CognitoAuth
from app import app
import requests, json

landing_page = Blueprint('landing_page_router', __name__, template_folder='templates')

CORS(landing_page)
CognitoAuth(app)

with open('cognito_credentials.json', 'r') as f:
    credentials = json.load(f)

@app.get('/landing_page/')
def get_landing_page():
    if 'code' not in request.args.keys() and not request.cookies.get('code'):
        return redirect(location = url_for("login_user"), code = 302)
    
    # Creating a session access token
    resp_json = None
    if not request.cookies.get('session_token'):
        data = {
            "grant_type": "authorization_code",
            "client_id": credentials["client_id"],
            "client_secret": credentials["client_secret"],
            "code": request.args['code'],
            'redirect_uri': credentials["redirect_uri"]
        }
        resp = requests.post("https://envrio.auth.eu-west-1.amazoncognito.com/oauth2/token", data=data, verify=True)
        resp_json = json.loads(json.dumps(resp.json(),sort_keys=True, indent=4, separators = (",",":")))
        verified_claims: dict = cognito_jwt_decode(token=resp_json['access_token'], region=credentials["region"], userpool_id=credentials["userpool_id"])
        client_id = verified_claims['username']
    else: client_id = request.cookies.get('username')

    response = make_response(render_template('landing_page.html'))

    if resp_json: response.set_cookie("session_token",resp_json['access_token'])
    if not request.cookies.get('username'): response.set_cookie('username',client_id)
    if not request.cookies.get('code'): response.set_cookie('code',request.args['code'])

    return response

