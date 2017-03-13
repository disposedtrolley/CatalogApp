from flask import Flask

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'you-will-never-guess'

from CatalogApp import views

if __name__ == "__main__":
    app.run()
