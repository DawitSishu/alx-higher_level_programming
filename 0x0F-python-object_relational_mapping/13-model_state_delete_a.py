#!/usr/bin/python3
""" List all state objects using sqlalchemy """

if __name__ == '__main__':

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm.session import sessionmaker, Session
    from model_state import Base, State

    nm = argv[1]
    pas = argv[2]
    dn = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(nm, password, dn))

    Session = sessionmaker(bind=engine)
    ses = Session()

    ses.query(State).filter(State.name.like('%a%')).\
        delete(synchronize_session=False)

    ses.commit()
