from django.db import models


# import sqlalchemy
# from sqlalchemy.ext.declarative import declarative_base
#
class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()

# from sqlalchemy.orm import relationship, sessionmaker
# Base = declarative_base()
# engine = sqlalchemy.create_engine('postgresql://stepan:gKZjcUH5yD4duw2@158.160.63.83:5432/stage_skinepic', echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()
#
# conn = engine.connect()
