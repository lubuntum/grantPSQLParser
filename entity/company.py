from pony.orm import Database, PrimaryKey, Set, Optional, db_session

from entity.base import db


class Company(db.Entity):
    _table_ = "company"
    id = PrimaryKey(int, auto=True)
    location_id = Optional('Location')
    INN = Optional(str, column='INN', unique=True)
    OGRN = Optional(str, column='OGRN')
    about_org = Optional(str)
    website = Optional(str)
    contact_location = Optional(str)
    projects = Set('Project')

    @staticmethod
    def create_unique_company(location, INN, OGRN, about_org, website, contact_location):
        with db_session:
            company = Company.get(INN=INN)
            if company is None:
                company = Company(location_id=location.id, INN=INN, OGRN=OGRN, about_org=about_org
                                  , website=website, contact_location=contact_location)
                db.commit()
                return company
            return company
