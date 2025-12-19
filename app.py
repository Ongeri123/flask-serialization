from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'

# initialize the SQLAlchemy instance defined in `models.py`
db.init_app(app)
# create a migration object to manage migrations
migrate = Migrate(app, db)




if __name__ == '__main__':
    app.run(debug=True)