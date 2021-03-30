from app import login, db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    nickname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)

    def __repr__(self, username):
        return '<User> {}'.format(self.nickname)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
