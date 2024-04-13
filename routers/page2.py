from flask import  render_template, Blueprint, request
from flask_cors import CORS
from flask_cognito import  CognitoAuth, cognito_auth_required
from app import app

page2 = Blueprint('page2_router', __name__, template_folder='templates')

CORS(page2)
cognito = CognitoAuth(app)

@app.get('/page2/')
@cognito_auth_required
def get_page2():
    return render_template('page2.html')

