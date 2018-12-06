from werkzeug.security import generate_password_hash, check_password_hash
from . import login, db
from flask_login import UserMixin, AnonymousUserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    username = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(15), index=True, unique=True)

    # def __init__(self, nickname=None, username=None, password=None):
    #     nickname = self.nickname
    #     username = self.username
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

def validate_on_submit(self):
    pass
