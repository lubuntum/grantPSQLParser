from pony.orm import Database, PrimaryKey, Set, Optional, db_session
from entity.base import db


class Location(db.Entity):
    id = PrimaryKey(int, auto=True)
    location = Optional(str, unique=True)
    companies = Set('Company')

    @staticmethod
    def create_unique_location(name):
        with db_session:
            location = Location.get(location=name)
            if location is None:
                new_location = Location(location=name)
                db.commit()
                return new_location
            return location
