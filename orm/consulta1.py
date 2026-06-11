from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and
from sqlalchemy import func # se importa la función func para realizar operaciones de agregación

# se importa la clase(s) del 
# archivo modelo.py
from modelo import Actor, Serie

# se importa información del archivo config.py
from config import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# los titulos de las series
titulos = session.query(
    Serie.titulo,
    func.avg(Actor.edad)
).join(Actor).group_by(Serie.id).all()

for t, pr in titulos:
    print("Título de la Serie: %s" % (t))
    print("Edades promedio: %s" % (pr))
    print("---------")

