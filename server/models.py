from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# Initialize the app
app = Flask(__name__)

# Configure the database (example with SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

class Plant(db.Model, SerializerMixin):
    __tablename__ = "plants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=True)
    image = db.Column(db.String(), nullable=True)
    price = db.Column(db.Float(), nullable=True)

# Create the tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
