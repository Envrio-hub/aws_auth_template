from flask import Flask, request
from flask_cognito import CognitoAuth

prefix = 'project_name'

app = Flask(__name__,template_folder='templates/',
            static_folder='static/', static_url_path='/static/')

# Configuration
app.config.update({
    "COGNITO_REGION": "eu-west-1",
    "COGNITO_USERPOOL_ID": "eu-west-1_Nxnijpx3x",

    # Optional
    "COGNITO_APP_CLIENT_ID": "6sqqmlb0m56mitarbdekd6c8tr",
    'COGNITO_CHECK_TOKEN_EXPIRATION': True,
    'COGNITO_JWT_HEADER_NAME': 'Cookie',
    'COGNITO_JWT_HEADER_PREFIX': 'session_token='
})

cognito = CognitoAuth(app)