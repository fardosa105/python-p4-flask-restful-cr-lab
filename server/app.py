from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Plant(db.Model, SerializerMixin):
    __tablename__ = "plants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=True)
    image = db.Column(db.String(), nullable=True)
    price = db.Column(db.Float(), nullable=True)

# Route to get all plants
@app.route('/plants', methods=['GET'])
def get_plants():
    plants = Plant.query.all()
    return jsonify([plant.to_dict() for plant in plants]), 200

# Route to get a plant by ID
@app.route('/plants/<int:id>', methods=['GET'])
def get_plant(id):
    plant = Plant.query.get(id)
    if plant:
        return jsonify(plant.to_dict()), 200
    else:
        return jsonify({"error": "Plant not found"}), 404

# Route to create a new plant
@app.route('/plants', methods=['POST'])
def create_plant():
    data = request.get_json()

    new_plant = Plant(
        name=data.get('name'),
        image=data.get('image'),
        price=data.get('price')
    )

    db.session.add(new_plant)
    db.session.commit()

    return jsonify(new_plant.to_dict()), 201

# Ensure the tables are created
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

