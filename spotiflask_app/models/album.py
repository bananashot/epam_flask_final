from re import match
from spotiflask_app import db
from sqlalchemy.orm import validates
import uuid as new_uuid


class Album(db.Model):
    """
        This class represents an Album. \n
        Attributes:
        -----------
        param name: Describes name of the album
        type name: str max_length=128
        param genre: Describes genre of the album
        type genre: str max_length=30
        param release_year: Describes release year of the album
        type release_year: int
        param songs: list of songs from the album
        type songs: list[Song] or None
    """
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
