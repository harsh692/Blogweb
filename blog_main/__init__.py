## Under blog_main/__init__.py

from flask import Flask

app=Flask(__name__)

from blog_main.core.views import core
app.register_blueprint(core)

from blog_main.error_pages.handlers import error_pages
app.register_blueprint(error_pages)