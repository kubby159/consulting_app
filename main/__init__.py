from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def page_not_found(error):
    return render_template('404.html', error = error), 404


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    #orm
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # bluprint
    from .views import main_views, question_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)

    # 오류페이지
    app.register_error_handler(404, page_not_found)


    return app