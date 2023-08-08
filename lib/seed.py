from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Audition, Role
from faker import Faker
import random

engine = create_engine("sqlite:///theater.db")
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()


def delete_records():
    session.query(Audition).delete()
    session.query(Role).delete()
    session.commit()


def create_auditions():
    roles = create_roles()
    auditions = []
    for i in range(10):
        audition = Audition(
            actor=fake.name(),
            location=fake.city(),
            phone=fake.phone_number(),
            hired=int(random.choice([True, False])),
            role=random.choice(roles),
        )
        session.add(audition)
        auditions.append(audition)
    session.commit()
    return auditions


def create_roles():
    roles = [Role(character_name=fake.name()) for _ in range(5)]
    session.add_all(roles)
    session.commit()
    return roles


if __name__ == "__main__":
    delete_records()
    create_auditions()
    create_roles()
