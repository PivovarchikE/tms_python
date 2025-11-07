from flask import Flask

def create_app():
    app = Flask(__name__)

    from .commands.raw_commands import init_commands
    init_commands(app)

    from .views import init_views
    init_views(app)

    return app
