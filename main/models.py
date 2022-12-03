from flask_login import UserMixin
from datetime import datetime

from main import db
from main import login_manager

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(255))
	name = db.Column(db.String(500))
	surname = db.Column(db.String(500))
	patronomic = db.Column(db.String(500))
	position = db.Column(db.String(500))
	password = db.Column(db.String(80))
	avatar = db.Column(db.String)

	def to_json(self):
		return {
			"id": self.id,
			"username": self.username,
			"name": self.name,
			"surname": self.surname,
			"patronomic": self.patronomic,
			"position": self.position,
			"password": self.password,
		}
