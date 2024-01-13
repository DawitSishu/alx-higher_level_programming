#!/usr/bin/python3
"""
insert to the db
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

    new_state = State(name="Louisiana")

    ses.add(new_state)
    ses.commit()

    print(new_state.id)
