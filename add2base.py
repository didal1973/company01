import datetime
from data import db_session
from data.countries import Country
from data.offices import Office
from data.users import User

import csv

db_session.global_init("db/Company.db")

# Таблица Countries
session = db_session.create_session()
f = open("countries", 'r', encoding="utf8")
for text in f.readlines():
    name = text.strip().split('VALUES')[1].split()
    contry = Country()
    contry.id = name[0][1:len(name[0]) - 1]
    contry.name = name[1].replace("N'", "").replace("')", "")
    session.add(contry)
f.close()

#Таблица Offices
with open('offices.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for index, row in enumerate(reader):
        office = Office()
        office.id = int(row[0])
        office.countryid = int(row[1])
        office.title = row[2]
        office.phone = row[3]
        office.contact = row[4]
        session.add(office)

offices = {office.title: office.id for office in session.query(Office)}

#Таблица Users
k = 1
with open('UserData.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for index, row in enumerate(reader):
        user = User()
        user.id = k
        k += 1
        user.officeid = offices[row[5]]
        user.roleid = {'Administrator': 1, 'User': 2}[row[0]]
        user.email = row[1]
        user.password = row[2]
        user.firstname = row[3]
        user.lastname = row[4]
        s = row[6].split('/')
        user.birthdate = datetime.date(int(s[2]), int(s[0]), int(s[1]))
        user.active = bool(row[7])
        session.add(user)

session.commit()
