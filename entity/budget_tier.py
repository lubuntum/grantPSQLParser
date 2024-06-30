from pony.orm import Database, PrimaryKey, Set, Optional, select, db_session
from entity.base import db

DUMMY_TIER = 0


class BudgetTier(db.Entity):
    _table_ = "budget_tier"
    id = PrimaryKey(int, auto=True)
    tier = Optional(int, unique=True)
    description = Optional(str)
    projects = Set('Project')

    @staticmethod
    def get_dummy_tier():
        with db_session:
            return select(t for t in BudgetTier if t.tier == DUMMY_TIER).first()
