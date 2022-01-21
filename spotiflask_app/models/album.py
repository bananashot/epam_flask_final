from re import match
from spotiflask_app import db
from sqlalchemy.orm import validates
from spotiflask_app.models import band
import uuid as new_uuid


class Album(db.Model):
    __tablename__ = 'Album'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    genre = db.Column(db.String(30))
    release_year = db.Column(db.Integer)

    @validates('release_year')
    def validate_start_year(self, key, year_value):
        if match('[0-9]{4}', str(year_value)):
            return year_value
        raise ValueError('Incorrect year value 4 digits are required.')

    uuid = db.Column(db.String(36), unique=True)
    band_id = db.Column(db.Integer, db.ForeignKey('Band.id'))
    songs = db.relationship('Song', back_populates='Album', lazy=True)

    def __init__(self, name, genre, release_year, uuid):
        self.name = name
        self.genre = genre
        self.release_year = release_year

        if uuid:
            self.uuid = uuid
        self.uuid = str(new_uuid.uuid4())

    def __repr__(self):
        return f'{self.name}'