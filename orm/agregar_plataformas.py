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


p1 = session.query(Pais).filter_by(nombre="Estados Unidos").first()
p2 = session.query(Pais).filter_by(nombre="España").first()
p3 = session.query(Pais).filter_by(nombre="Reino Unido").first()
p4 = session.query(Pais).filter_by(nombre="Francia").first()
p5 = session.query(Pais).filter_by(nombre="Alemania").first()
p6 = session.query(Pais).filter_by(nombre="Corea del Sur").first()
p7 = session.query(Pais).filter_by(nombre="Japón").first()
p8 = session.query(Pais).filter_by(nombre="India").first()
p9 = session.query(Pais).filter_by(nombre="Nigeria").first()
p10 = session.query(Pais).filter_by(nombre="Sudáfrica").first()
p11 = session.query(Pais).filter_by(nombre="Egipto").first()
p12 = session.query(Pais).filter_by(nombre="Australia").first()
p13 = session.query(Pais).filter_by(nombre="Nueva Zelanda").first()
p14 = session.query(Pais).filter_by(nombre="México").first()
p15 = session.query(Pais).filter_by(nombre="Brasil").first()


# Se crean objetos de tipo Plataforma

plataforma1 = Plataforma(nombre="StreamFlix", pais=p1, suscriptores_millones=154.7)
plataforma2 = Plataforma(nombre="CineMax Play", pais=p1, suscriptores_millones=9.4)
plataforma3 = Plataforma(nombre="Horizon Plus", pais=p1, suscriptores_millones=68.5)
plataforma4 = Plataforma(nombre="IberiaTV", pais=p2, suscriptores_millones=56.3)
plataforma5 = Plataforma(nombre="BritBox Global", pais=p3, suscriptores_millones=177.7)
plataforma6 = Plataforma(nombre="Lumiere Play", pais=p4, suscriptores_millones=163.5)
plataforma7 = Plataforma(nombre="Berlin Stream", pais=p5, suscriptores_millones=214.5)
plataforma8 = Plataforma(nombre="K-Drama World", pais=p6, suscriptores_millones=24.1)
plataforma9 = Plataforma(nombre="Sakura Plus", pais=p7, suscriptores_millones=103.3)
plataforma10 = Plataforma(nombre="Bollywood Now", pais=p8, suscriptores_millones=10.5)
plataforma11 = Plataforma(nombre="Nollywood Play", pais=p9, suscriptores_millones=55.2)
plataforma12 = Plataforma(nombre="CapeView", pais=p10, suscriptores_millones=123.0)
plataforma13 = Plataforma(nombre="Nile Screen", pais=p11, suscriptores_millones=9.8)
plataforma14 = Plataforma(nombre="Aussie Vision", pais=p12, suscriptores_millones=50.5)
plataforma15 = Plataforma(nombre="Kiwi Stories", pais=p13, suscriptores_millones=157.2)
plataforma16 = Plataforma(nombre="Latam Series", pais=p14, suscriptores_millones=132.4)
plataforma17 = Plataforma(nombre="Brasil Play", pais=p15, suscriptores_millones=55.6)
plataforma18 = Plataforma(nombre="Global Series Hub", pais=p1, suscriptores_millones=142.9)
plataforma19 = Plataforma(nombre="Europa Cine", pais=p4, suscriptores_millones=194.9)
plataforma20 = Plataforma(nombre="Asia Drama Plus", pais=p6, suscriptores_millones=5.0)    

# se agrega los objetos a la sesión

session.add(plataforma1)
session.add(plataforma2)
session.add(plataforma3)
session.add(plataforma4)
session.add(plataforma5)
session.add(plataforma6)
session.add(plataforma7)
session.add(plataforma8)
session.add(plataforma9)
session.add(plataforma10)
session.add(plataforma11)
session.add(plataforma12)
session.add(plataforma13)
session.add(plataforma14)
session.add(plataforma15)
session.add(plataforma16)
session.add(plataforma17)
session.add(plataforma18)
session.add(plataforma19)
session.add(plataforma20)

# se confirma las transacciones
session.commit()
