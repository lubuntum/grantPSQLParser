from pony.orm import Database, PrimaryKey, Set, Optional, db_session
from entity.base import db


class Contest(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str, unique=True)
    projects = Set('Project')

    @staticmethod
    def create_unique_contest(name):
        with db_session:
            contest = Contest.get(name=name)
            if contest is None:
                new_contest = Contest(name=name)
                db.commit()
                return new_contest
            return contest
