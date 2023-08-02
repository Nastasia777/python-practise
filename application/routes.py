from application import app, db
from flask import request, jsonify, render_template, redirect
from application.models import DesperateHousewivesCast
from application.forms import AddCharacterForm

def format_character(cast):
    return {
        "name": cast.name,
        "age": cast.age,
        "role": cast.role
    }

@app.route("/")
def greeting():
    return "<p>Welcome, fans of the hit TV series Desperate Housewives!</p>"

# POST 
@app.route("/cast", methods=["POST", "GET"])
def characters():
    form = AddCharacterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            character = DesperateHousewivesCast(form.name.data, form.age.data, form.role.data)
            db.session.add(character)
            db.session.commit()
            return redirect('/')

    elif request.method == "GET":
        characters = DesperateHousewivesCast.query.all()
        character_list = [format_character(character) for character in characters]

        return render_template('characters.html', characters=character_list, title="All cast", form=form)

# @app.route("/cast", methods=["POST"])
# def create_character():
#     data = request.json
#     cast = DesperateHousewivesCast(data['name'], data['age'], data['role'])
#     db.session.add(cast)
#     db.session.commit()
#     return jsonify(id=cast.id, name=cast.name, age=cast.age, role=cast.role)

# @app.route("/cast", methods=['GET'])
# def get_characters():
#     characters = DesperateHousewivesCast.query.all()
#     character_list = []
#     for character in characters:
#         character_list.append(format_character(character))
#     return character_list

# GET /:id
@app.route('/cast/<id>')
def get_character(id):
    character = DesperateHousewivesCast.query.filter_by(id=id).first()
    return render_template("character.html", character=character)

# DELETE /:id
@app.route("/cast/<id>", methods=['DELETE'])
def delete_character(id):
    character = DesperateHousewivesCast.query.filter_by(id=id).first()
    db.session.delete(character)
    db.session.commit()
    return f"Character deleted {id}"

# PATCH /:id
@app.route("/cast/<id>", methods=["PATCH"])
def update_character(id):
    character = DesperateHousewivesCast.query.filter_by(id=id)
    data = request.json
    character.update(dict(name=data["name"], age=data["age"], role=data["role"]))
    db.session.commit()
    updatedCharacter = character.first()
    return jsonify(id=updatedCharacter.id, name=updatedCharacter.name, age=updatedCharacter.age, role=updatedCharacter.role)
