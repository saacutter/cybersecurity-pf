from app import db, login
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone
from typing import List

@login.user_loader
def load_user(id):
    return Users.query.get(id)

class Users(db.Model, UserMixin):
    id:              Mapped[int]      = mapped_column(db.Integer, primary_key=True)
    username:        Mapped[str]      = mapped_column(db.Text, unique=True, nullable=False, index=True)
    password:        Mapped[str]      = mapped_column(db.String(128), nullable=False, index=True)