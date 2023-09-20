from application import db, app

app.app_context().push()

class Character(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    catch_phrase = db.Column(db.String(100), nullable=False)
    
    def __init__(self, name, age, catch_phrase):
        self.name = name
        self.age = age
        self.catch_phrase = catch_phrase
    
    def __repr__(self):
        return f"Hi! I'm {self.name} and my catch phrase is {self.catch_phrase}"
        
    @property
    def json(self):
        return {"id": self.id, "name": self.name, "age": self.age, "catch_phrase": self.catch_phrase}