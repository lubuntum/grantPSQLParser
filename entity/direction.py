from pony.orm import Database, PrimaryKey, Set, Optional, db_session
from entity.base import db


class Direction(db.Entity):
    id = PrimaryKey(int, auto=True)
    direction = Optional(str, unique=True)
    projects = Set('Project')

    @staticmethod
    def create_unique_direction(name):
        with db_session:
            direction = Direction.get(direction=name)
            if direction is None:
                new_direction = Direction(direction=name)
                db.commit()
                return new_direction
            return direction
