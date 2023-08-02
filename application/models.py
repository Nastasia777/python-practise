from application import db, app

app.app_context().push()

class DesperateHousewivesCast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(100), nullable=False)
    
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role
    
    def __repr__(self):
        return f"{self.name} portrayed the character of {self.role} in the series 'Desperate Housewives'."
