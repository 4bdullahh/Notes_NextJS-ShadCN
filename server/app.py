import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from server.model import Note

app = Flask(__name__)
CORS(app)
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/api/home", methods=["GET"])
def return_home():
    data = db.session.query(Note).all()
    return jsonify({
        'notes': data
    })
@app.route("/api/note/create", methods=["GET"])
def create_note():
    title = request.form.get("title")
    description = request.form.get("description")
    new_notes =  Note(title=title, description=description, user_id=1)

    db.session.add(new_notes)
    db.commit()



if __name__ == "__main__":
    app.run(debug=True, port=8080)
