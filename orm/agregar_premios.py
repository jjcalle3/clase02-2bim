from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo modelo
from modelo import Pais, Plataforma, Serie, Actor, Premio

# se importa información del archivo configuracion
from config import cadena_base_datos
# se genera enlace al gestor de base de
# datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

session.query(Serie).all()



# Se crean objetos de tipo Premio
premio1 = Premio(nombre="Mejor Serie", categoria="Serie", anio=2020, serie_id=1)
premio2 = Premio(nombre="Mejor Actor", categoria="Actor", anio=2020, serie_id=2)
premio3 = Premio(nombre="Mejor Serie", categoria="Serie", anio=2021, serie_id=3)
premio4 = Premio(nombre="Mejor Actor", categoria="Actor", anio=2021, serie_id=4)
premio5 = Premio(nombre="Mejor Serie", categoria="Serie", anio=2021, serie_id=5)
premio6 = Premio(nombre="Mejor Actor", categoria="Actor", anio=2021, serie_id=6)
premio7 = Premio(nombre="Mejor Serie", categoria="Serie", anio=2022, serie_id=7)
premio8 = Premio(nombre="Mejor Actor", categoria="Actor", anio=2022, serie_id=8)
premio9 = Premio(nombre="Mejor Serie", categoria="Serie", anio=2022, serie_id=9)
premio10 = Premio(nombre="Mejor Actor", categoria="Actor", anio=2022, serie_id=10)
premio11 = Premio(nombre="Mejor Serie", categoria="Serie", anio=2023, serie_id=11)
premio12 = Premio(nombre="Mejor Actor", categoria="Actor", anio=2023, serie_id=12)
premio13 = Premio(nombre="Mejor Serie", categoria="Serie", anio=2023, serie_id=13)
premio14 = Premio(nombre="Mejor Actor", categoria="Actor", anio=2023, serie_id=14)
premio15 = Premio(nombre="Mejor Serie", categoria="Serie", anio=2024, serie_id=15)
premio16 = Premio(nombre="Mejor Actor", categoria="Actor", anio=2024, serie_id=16)
premio17 = Premio(nombre="Mejor Serie", categoria="Serie", anio=2024, serie_id=17)
premio18 = Premio(nombre="Mejor Actor", categoria="Actor", anio=2024, serie_id=18)
premio19 = Premio(nombre="Mejor Serie", categoria="Serie", anio=2024, serie_id=19)
premio20 = Premio(nombre="Mejor Actor", categoria="Actor", anio=2024, serie_id=20) 
# se agrega los objetos
# a la sesión

session.add(premio1)
session.add(premio2)
session.add(premio3)
session.add(premio4)
session.add(premio5)
session.add(premio6)
session.add(premio7)
session.add(premio8)
session.add(premio9)
session.add(premio10)
session.add(premio11)
session.add(premio12)
session.add(premio13)
session.add(premio14)
session.add(premio15)
session.add(premio16)
session.add(premio17)
session.add(premio18)
session.add(premio19)
session.add(premio20)
# se confirma las transacciones
session.commit()
