from .models import Character
from werkzeug import exceptions
from flask import jsonify, request
from . import db

def index():
    try:
        characters = Character.query.all()
        print('line 9', characters)
        data = []
        for character in characters:
            data.append(character.json)
        # data = [c.json for c in characters]
        print('line 14', data)
        return jsonify({"characters": data})
    except:
        raise exceptions.InternalServerError("We are working on it")

def create():
    try:
        name, age, catch_phrase = request.json.values()
        new_character = Character(name=name, age=age, catch_phrase=catch_phrase)

        db.session.add(new_character)
        db.session.commit() 

        return jsonify({"data": new_character.json}), 201
    except:
        raise exceptions.BadRequest(f"We cannot process your request, age, name and catch_phrase are requires and you only provided")

def show(id):
    try:
        character = Character.query.filter_by(id=id).first()
        return jsonify({"data": character.json}), 200
    except:
        raise exceptions.NotFound("you get it")
        
        
def patch(id):
    character = Character.query.filter_by(id=id).first()
    data = request.json

    for attribute, value in data.items():
        if hasattr(character, attribute):
            setattr(character, attribute, value)

    db.session.commit()

    return jsonify({ "data": character.json })

def delete(id):
    character = Character.query.filter_by(id=id).first()
    db.session.delete(character)
    db.session.commit()
    return f"Character Deleted", 204