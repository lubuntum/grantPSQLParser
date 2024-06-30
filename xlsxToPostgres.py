import pandas as pd

from pony.orm import *

from entity.base import db
from entity.project import Project
from entity.status import Status
from entity.location import Location
from entity.fond import Fond
from entity.direction import Direction
from entity.contest import Contest
from entity.company import Company
from entity.budget_tier import BudgetTier
from xlsx.copyToOneFile import get_current_folder, get_xlsx_from_folder


def test_conn():
    with db_session:
        projects = select(p for p in Project)[:]
        for project in projects:
            print(project)


def test_insert():
    with db_session:
        status = Status(name="status_test_name")


if __name__ == '__main__':
    db.generate_mapping(create_tables=False)
    path = './data'
    xlsx_docs = get_xlsx_from_folder(path)
    # Заглушка, пока тиры не считаем
    dummy_budget_tier = BudgetTier.get_dummy_tier()
    for xlsx in xlsx_docs:
        df = pd.read_excel(xlsx)
        for index, row in df.iterrows():
            if Project.is_project_exists(row['requestCode']):
                print(f'{row["requestCode"]} already in database')
                continue
            status = Status.create_unique_status(name=row['status'])
            direction = Direction.create_unique_direction(name=row['direction'])
            contest = Contest.create_unique_contest(name=row['contest'])
            fond = Fond.create_unique_fond(Fond.determine_fond(request_code=row['requestCode']))
            location = Location.create_unique_location(name=row['location'])
            company = Company.create_unique_company(location=location, INN=str(row['INN']), OGRN=str(row['OGRN']),
                                                    about_org=row['aboutOrganization'], website=row['webSite'],
                                                    contact_location=row['contactLocation'], )
            project = Project.create_project(company, status, contest, fond, dummy_budget_tier, direction,
                                             row['title'], row['price'], row['fondPrice'], row['requestCode'],
                                             row['fromDate'], row['RealizeStartDate'], row['RealizeEndDate'],
                                             row['short_desc'], row['social'], row['geography'], row['winnerTarget'],
                                             row['aims'], row['tasks'], float(str(row['rating']).replace(',', '.')))
            # Создать project
            print(f'test -> {company.INN}, {company.about_org}')
        print("Конец файла", end='\n')
    # Создать dataframe для каждого xlsx дока
# TODO Ошибка с форматом дат, изменить их в psql на text
