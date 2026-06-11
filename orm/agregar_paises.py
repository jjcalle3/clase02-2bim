from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo modelo
from modelo import Pais, Plataforma, Serie, Actor, Premio

# se importa información del archivo configuracion
from config import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


# Se crean objeto de tipo Pais
p1 = Pais(nombre="Estados Unidos", continente="América")
p2 = Pais(nombre="México", continente="América")
p3 = Pais(nombre="Brasil", continente="América")
p4 = Pais(nombre="Reino Unido", continente="Europa")
p5 = Pais(nombre="España", continente="Europa")
p6 = Pais(nombre="Francia", continente="Europa")
p7 = Pais(nombre="Alemania", continente="Europa")
p8 = Pais(nombre="Corea del Sur", continente="Asia")
p9 = Pais(nombre="Japón", continente="Asia")
p10 = Pais(nombre="India", continente="Asia")
p11 = Pais(nombre="Nigeria", continente="África")
p12 = Pais(nombre="Sudáfrica", continente="África")
p13 = Pais(nombre="Egipto", continente="África")
p14 = Pais(nombre="Australia", continente="Oceanía")
p15 = Pais(nombre="Nueva Zelanda", continente="Oceanía")



session.add(p1)
session.add(p2)
session.add(p3)
session.add(p4)
session.add(p5)
session.add(p6)
session.add(p7)
session.add(p8)
session.add(p9)
session.add(p10)
session.add(p11)
session.add(p12)
session.add(p13)
session.add(p14)
session.add(p15)

# se confirma las transacciones
session.commit()
