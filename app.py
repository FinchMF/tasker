from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from routes import Routes


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app = Routes.initRoutes(app)
db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(debug=True)