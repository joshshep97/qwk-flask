from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()
secret_key = os.getenv('my_secret_key')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key

    # register bp's
    from .main import bp as main_bp
    app.register_blueprint(main_bp)

    # import models
    # from .models import MODEL_NAME

    @app.route('/test')
    def test():
        return 'test complete'

    return app

