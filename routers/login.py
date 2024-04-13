from flask import Blueprint, request, redirect, render_template, url_for
from flask_cors import CORS
from urllib.parse import urlencode, urlparse
from app import app, prefix
import json

user_router = Blueprint("user_router",__name__, template_folder='templates')
CORS(user_router)

with open('cognito_credentials.json', 'r') as f:
    credentials = json.load(f)

# # Register the function to run before each request
# @app.before_request
# def before_request():
#     if request.cookies.get('session_token'):
#         mutable_headers = request.headers.to_wsgi_list()
#         mutable_headers.append(("Authorization", f"Bearer {request.cookies.get('session_token')}"))
#         request.environ["HTTP_AUTHORIZATION"] = f"Bearer {request.cookies.get('session_token')}"

@app.get(f'/{prefix}/')
def root():
    return redirect(location = url_for("login_user"), code = 302)

@app.route('/login',methods = ['GET','POST'])
def login_user(request = request):
    if request.method == 'GET':
        return render_template('login_page.html')
    else:
        base_url = credentials['base_url']
        auth_params = {
            "client_id": credentials['client_id'],
            "response_type": "code",
            "scope": "openid",
            "redirect_uri": credentials['redirect_uri']
        }
        return redirect(base_url + ('&' if urlparse(base_url).query else '?') + urlencode(auth_params))


@app.route('/logout')
def logout():
    return redirect(location = url_for("login_user"))