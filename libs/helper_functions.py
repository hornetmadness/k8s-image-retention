
from sqlalchemy import desc, asc, func
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

def unique_list(list1): 
    # insert the list to the set 
    list_set = set(list1) 
    # convert the set to the list 
    return (list(list_set)) 

def db_upsert(images):
    from libs.models import connect_db, Images

    db = connect_db()  # establish connection
    Session = sessionmaker(bind=db)
    session = Session()

    for image in images:
        exists = session.query(Images).filter(
            Images.uri == image
        ).first()

        if exists:
            print(f"Updating {image}")
            exists.last_seen = func.now()
            session.commit()
        else:
            print(f"Adding {image}")
            addrow = Images( uri = image )
            session.add(addrow)
            session.commit()


def db_find_expired(max_age):
    from libs.models import connect_db, Images
    
    db = connect_db()  # establish connection
    Session = sessionmaker(bind=db)
    session = Session()

    ago = datetime.now() - timedelta(seconds=max_age)
    return session.query(Images).filter(
        Images.last_seen <= ago
    ).all()
