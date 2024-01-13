#!/usr/bin/python3
"""
cities list
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    usr = sys.argv[1]
    pas = sys.argv[2]
    dname = sys.argv[3]

    url = {'drivername': 'mysql+mysqldb', 'host': 'localhost',
           'username': usr, 'password': pas, 'database': dname}

    engine = create_engine(URL(**url), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    states = session.query(State)

    for st in states:
        print("{}: {}".format(st.id, st.name))
        for city in st.cities:
            print("\t{}: {}".format(city.id, city.name))
