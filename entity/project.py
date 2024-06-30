from pony.orm import Database, PrimaryKey, Set, Optional, db_session, select

from entity.base import db


class Project(db.Entity):
    id = PrimaryKey(int, auto=True)
    company_id = Optional('Company')
    status_id = Optional('Status')
    contest_id = Optional('Contest')
    fond_id = Optional('Fond')
    budget_tier_id = Optional('BudgetTier')
    direction_id = Optional('Direction')
    title = Optional(str)
    price = Optional(float)
    fond_price = Optional(float)
    request_code = Optional(str, unique=True)
    from_date = Optional(str)
    start_date = Optional(str)
    end_date = Optional(str)
    short_desc = Optional(str)
    social = Optional(str)
    geography = Optional(str)
    target = Optional(str)
    aim = Optional(str)
    tasks = Optional(str)
    rating = Optional(float)

    @staticmethod
    def create_project(company, status, contest, fond, budget_tier, direction,
                       title, price, fond_price, request_code, from_date, start_date, end_date,
                       short_desc, social, geography, target, aim, tasks, rating):
        with db_session:
            project = Project(company_id=company.id, status_id=status.id, contest_id=contest.id,
                              fond_id=fond.id, budget_tier_id=budget_tier.id, direction_id=direction.id,
                              title=title, price=price, fond_price=fond_price, request_code=request_code,
                              from_date=from_date, start_date=start_date, end_date=end_date,
                              short_desc=short_desc, social=social, geography=geography, target=target,
                              aim=aim, tasks=tasks, rating=rating)
            db.commit()
            return project

    @staticmethod
    def is_project_exists(request_code):
        with db_session:
            return select(p for p in Project if p.request_code == request_code).exists()
