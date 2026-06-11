from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from modelo import Pais, Plataforma, Serie, Actor, Premio

# se importa información del archivo configuracion
from modelo import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


# Se crean objetos de tipo Premio
premio1 = Premio(nombre="Premio 1")
premio2 = Premio(nombre="Premio 2")
premio3 = Premio(nombre="Premio 3")
premio4 = Premio(nombre="Premio 4")
premio5 = Premio(nombre="Premio 5")
premio6 = Premio(nombre="Premio 6")
# se agrega los objetos
# a la sesión

session.add(premio1)
session.add(premio2)
session.add(premio3)
session.add(premio4)
session.add(premio5)
session.add(premio6)

# se confirma las transacciones
session.commit()
