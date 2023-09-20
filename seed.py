from application import db
from application.models import Character

db.drop_all()
print("Dropping database")
db.create_all()
print("Creating database")

print("Seeding database")
entry1 = Character(name="Phoebe", age=29, catch_phrase="Smelly cat, SMElly cat, what are they feeding you?")
entry2 = Character(name="Joey", age=26, catch_phrase="How you doin?")
entry3 = Character(name="Ross", age=26, catch_phrase="We were on a break!")
entry4 = Character(name="Chandler", age=26, catch_phrase="We were on a break!")
entry5 = Character(name="Rachel", age=25, catch_phrase="It’s like all my life everyone’s told me, ‘You’re a shoe! You’re a shoe! You’re a shoe!’")
entry6 = Character(name="Monica", age=25, catch_phrase="I knowwww!")

db.session.add_all([entry1, entry2, entry3, entry4, entry5, entry6])

db.session.commit()