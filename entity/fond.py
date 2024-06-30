from pony.orm import Database, PrimaryKey, Set, Optional, db_session
from entity.base import db

FONDS_TYPES = ['ПФКИ', 'ФПГ']


class Fond(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str, unique=True)
    projects = Set('Project')

    # В ПФКИ у всех кодов есть слово ПФКИ, у ФПГ - нет
    @staticmethod
    def determine_fond(request_code):
        if FONDS_TYPES[0] in request_code:
            return FONDS_TYPES[0]
        return FONDS_TYPES[1]

    @staticmethod
    def create_unique_fond(fond_type):
        with db_session:
            fond = Fond.get(name=fond_type)
            if fond is None:
                new_fond = Fond(name=fond_type)
                db.commit()
                return new_fond
            return fond
