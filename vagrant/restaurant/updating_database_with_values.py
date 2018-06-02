
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()
session.query(Restaurant).all()

cheezePizza = MenuItem(name = 'Cheeze Pizza', description = 'Made with all natural ingredients', course = 'Entree', price = '$8.99', restaurant = myFirstRestaurant)
session.add(cheezePizza)
session.commit()
session.query(MenuItem).all()

firstResult = session.query(Restaurant).first()
firstResult.name

items = session.query(MenuItem).all()
for item in items:
	print(item.name)

veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')