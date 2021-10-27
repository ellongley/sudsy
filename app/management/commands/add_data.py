import pandas as pd
from django.core.management.base import BaseCommand
from app.models import Claims
from sqlalchemy import create_engine
from django.conf import settings

class Command(BaseCommand):
    help = "A command to add data from a .csv file to the database."

    def handle(self, *args, **options):

        claims = 'claims.csv'
        df = pd.read_csv(claims)

        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']


        database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(user=user,password=password,database_name=database_name)

        #engine = create_engine('sqlite:///db.sqlite3')
        engine = create_engine(database_url, echo=False)

        # other if_exists options: append

        df.to_sql(Claims._meta.db_table, if_exists='replace',con=engine, index=False)
