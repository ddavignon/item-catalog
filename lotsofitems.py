from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import CatalogItem, Category, Base
 
engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



# create categories of items to track
category1 = Category(name = "Chromebook")
category2 = Category(name = "MacBook Pro")
category3 = Category(name = "Mac Mini")


session.add(category1)
session.commit()
session.add(category2)
session.commit()
session.add(category3)
session.commit()

# add item for chromebook
catelogItem1 = CatalogItem(
    name = "CMB-101",
    description = "2015 Samsung Chromebook, 4GB RAM",
    price = "$199.99",
    category = category1)

catelogItem2 = CatalogItem(
    name = "CMB-102",
    description = "2016 Acer Chromebook, 4GB RAM",
    price = "$199.99",
    category = category1)

session.add(catelogItem1)
session.commit()
session.add(catelogItem2)
session.commit()

# add item for MacBook Pro
catalogItem3 = CatalogItem(
    name = "CMB-102",
    description = "2016 MacBook Pro 13\", 16GB RAM, 256 SSD",
    price = "$1399.99",
    category = category2)

session.add(catalogItem3)
session.commit()

# add item for Mac Mini

print "added menu items!"

