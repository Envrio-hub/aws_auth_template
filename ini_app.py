from app import app
from routers.login import user_router
from routers.landing_page import landing_page
from routers.page2 import page2
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

def exception_handler(e):
    return str(e), 500

app.register_blueprint(user_router)
app.register_blueprint(landing_page)
app.register_blueprint(page2)
app.register_error_handler(Exception,exception_handler)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)

CORS(app)

if __name__ == '__main__':
    app.run("127.0.0.1",port = 8024, debug = True)