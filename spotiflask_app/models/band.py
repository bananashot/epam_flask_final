from re import match
from spotiflask_app import db
from sqlalchemy.orm import validates
import uuid as new_uuid


class Band(db.Model):
    """
        This class represents a Band. \n
        Attributes:
        -----------
        param name: Describes name of the Band
        type name: str max_length=128
        param country: Describes country of the Band in ISO format
        type country: str max_length=2
        param release_year: Describes the year the band started
        type release_year: int
        param albums: list of albums of the band
        type albums: list[Album] or None
    """
    __tablename__ = 'Band'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    country = db.Column(db.String(2))

    @validates('country')
    def validate_country(self, key, country_value):
        if match('[A-Z]{2}', country_value):
            return country_value
        raise ValueError("Incorrect value, ISO format of 2 capital letters are required.")

    start_year = db.Column(db.Integer)

    @validates('start_year')
    def validate_start_year(self, key, year_value):
        if match('[0-9]{4}', str(year_value)):
            return year_value
        raise ValueError('Incorrect year value 4 digits are required.')

    uuid = db.Column(db.String(36), unique=True)
    albums = db.relationship('Album', back_populates='Band', lazy=True)

    # @property
    # def genres(self):
    #     return object_session(self).get(album.Album, self.genre)

    __table_args__ = (db.UniqueConstraint('name', 'country', name='_band_location_uc'),
                      )

    def __init__(self, name, country, start_year, uuid):
        self.name = name
        self.country = country
        self.start_year = start_year

        if uuid:
            self.uuid = uuid
        self.uuid = str(new_uuid.uuid4())

    def __repr__(self):
        return f'{self.name}'
