""" Module to create db from models.
"""

from stream.models import Base

if __name__ == '__main__':
   engine = create_engine('mysql://root:password@127.0.0.1:3306/test', echo=True)
   Base.metadata.create_all(engine, checkfirst=True)