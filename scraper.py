import mysql.connector as my
import pandas as pd
import re
from sqlalchemy import create_engine

class Scraper:

    def __init__(self, usr, pwd, url, db):
        self.engine = create_engine('mysql+mysqlconnector://{}:{}@{}/{}'.format(usr, pwd, url, db))
        self.connection = self.engine.connect()

    def add_course_codes(self):
        courses = pd.read_sql('course', self.connection)
        print(courses.head())

    def test(self):
        print(self.engine)
        print(self.connection)

    def __del__(self):
        self.connection.close()


if __name__ == '__main__':

    usr = 'dsn_editor'
    pwd = 'RYvOipXX7mfQBaeE'
    url = 'datascience.shanti.virginia.edu'
    db = 'dsn'
    scr = Scraper(usr, pwd, url, db)
    scr.test()

