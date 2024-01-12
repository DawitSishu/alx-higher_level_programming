#!/usr/bin/python3
"""
script to fetch all states using the model
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    ses = Session()

    for row in ses.query(State).order_by(State.id.asc()):
        print(row.id, end="")
        print(': ', end="")
        print(row.name)
