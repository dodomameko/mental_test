from flask import Flask
import os

from flask import abort, redirect, url_for

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'flask_hamster.sqlite'),
    )
 # C:\Users\Jeridodo\Desktop\flask\flask_hamster\instance
  
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    
    else:
        app.config.from_mapping(test_config)

# ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import subscribe
    app.register_blueprint(subscribe.bp)
    
    
    #@app.route('/')
    #def index():
    #    return 'hello'

    return app