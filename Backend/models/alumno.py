from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.db import meta, engine

alumnos = Table('alumnos', meta,
                Column('ID', Integer,
                       primary_key=True, autoincrement=True),
                Column('matricula', Integer),
                Column('nombre', String(255)),
                Column('apellidos', String(255)),
                Column('cuatrimestre', Integer),
                Column('promedio', Float))
meta.create_all(engine)
