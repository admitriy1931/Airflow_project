import requests as requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sys

from model.currency import Currency

sys.path.append("..")

from model.base import Base

from conf import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session_local = SessionLocal()

url = "https://api.hh.ru/vacancies"

params = {
    "text": "data enginer",
    "area": 1,  # ID региона (1 — Москва)
    "per_page": 2  # Количество вакансий на странице
}
response = requests.get(url, params=params)
records = []
if response.status_code == 200:
    data = response.json()
    print(data)
    for item in data["items"]:
        records.append(Currency(
            vacancy = item['name'],
            company = item['employer']['name'],
            web_cite = item['alternate_url']
            ))
else:
    print("Error: ", response.status_code)

for record in records:
    session_local.add(record)

session_local.commit()


