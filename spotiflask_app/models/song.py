from re import match
from spotiflask_app import db
from sqlalchemy.orm import validates
import uuid as new_uuid


class Song(db.Model):
    __tablename__ = 'Song'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)

    @validates('order_id')
    def validate_start_year(self, key, order_value):
        if match('[0-9]{1,2}', str(order_value)):
            return order_value
        raise ValueError('Incorrect year value 1 or 2 digits are required.')

    name = db.Column(db.String(128))
    uuid = db.Column(db.String(36), unique=True)
    album_id = db.Column(db.Integer, db.ForeignKey('Album.id'))
    duration = db.Column(db.String(5))

    @validates('duration')
    def validate_duration(self, key, duration_value):
        if match('[0-9]]{1,2}:[0-9]{2}', duration_value):
            return duration_value
        raise ValueError('Incorrect duration format "minutes:seconds" required.')

    __table_args__ = (db.UniqueConstraint('id', 'order_id', name='_song_order_id_uc'),)

    def __init__(self, order_id, name, country, uuid):
        self.order_id = order_id
        self.name = name
        self.country = country

        if uuid:
            self.uuid = uuid
        self.uuid = str(new_uuid.uuid4())

    def __repr__(self):
        return f'{self.name}'
