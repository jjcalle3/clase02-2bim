from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from modelo import Actor, Serie
from config import cadena_base_datos

# Configuración del motor y la sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta: Se selecciona el título y el promedio de edad

titulos = session.query(
    Serie.titulo,
    func.avg(Actor.edad)
).join(Actor, Serie.id == Actor.serie).group_by(Serie.id).all()

# Iteración de los titulos y promedios obtenidos para imprimirlos
for titulo, promedio_edad in titulos:
    print("Título de la Serie: %s" % titulo)
    # Redondeamos el promedio a 2 decimales para que se vea más limpio
    print("Edades promedio: %.2f" % promedio_edad)
    print("---------")

