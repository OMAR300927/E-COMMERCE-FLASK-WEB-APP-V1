from flask import Flask, redirect, url_for
import stripe


def create_app():
    
    app = Flask(__name__)
    app.config.from_object("myapp.config.Config")

    stripe.api_key = app.config["STRIPE_SECRET_KEY"]

    from .extension import db, migrate, jwt
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from .modules import jwt_callbacks

    from .modules import model

    from .Admin.routes import admin_bp
    app.register_blueprint(admin_bp)
    from .Users.routes import users_bp
    app.register_blueprint(users_bp)

    @app.route('/')
    def index():
        return redirect(url_for('users_bp.home'))
    

    return app