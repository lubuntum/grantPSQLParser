from pony.orm import Database, PrimaryKey, Set, Optional, db_session
from entity.base import db


class Status(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str, unique=True)
    projects = Set('Project')

    @staticmethod
    def create_unique_status(name):
        with db_session:
            status = Status.get(name=name)
            if status is None:
                new_status = Status(name=name)
                db.commit()
                return new_status
            return status
