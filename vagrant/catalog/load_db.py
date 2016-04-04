from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CategoryItem, User

engine = create_engine('sqlite:///categories.db')
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


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Menu for UrbanBurger
category1 = Category(user_id=1,
                    name="Soccer",
                    image="https://upload.wikimedia.org/wikipedia/commons/b/b9/Football_iu_1996.jpg"
            )

session.add(category1)
session.commit()

category2 = Category(user_id=1,
                    name="Snowboarding",
                    image="https://upload.wikimedia.org/wikipedia/commons/6/61/Snowboarding1.jpg"
            )

session.add(category2)
session.commit()

category3 = Category(user_id=1,
                    name="Table Tennis",
                    image="http://tenrandomfacts.com/wp-content/uploads/2013/04/Table-Tennis1.jpg"
            )

session.add(category3)
session.commit()

category4 = Category(user_id=1,
                    name="Basketball",
                    image="http://www.abc.net.au/news/image/4168986-3x2-940x627.jpg"
            )

session.add(category4)
session.commit()

category5 = Category(user_id=1,
                    name="Baseball",
                    image="http://images.christianpost.com/full/88701/clayton-kershaw-la-dodgers.jpg"
            )

session.add(category5)
session.commit()

categoryItem1 = CategoryItem(user_id=1,
                            name="Soccer Ball",
                            description='A football, soccer ball, or association football ball is the ball used in the sport of association football. The name of the ball varies according to whether the sport is called "football", "soccer", or "association football". ',
                            category=category1,
                            image="https://upload.wikimedia.org/wikipedia/commons/1/1d/Football_Pallo_valmiina-cropped.jpg"
                )

session.add(categoryItem1)

categoryItem2 = CategoryItem(user_id=1,
                            name="Shinguards",
                            description="Play like the legend himself in guards that won't weight you down. Hard slip-in guard. Includes compression TechFit sleeves with shield pocket. 50/50 polycarbonate/injection molded EPP.",
                            category=category1,
                            image="http://www.aysostore.com/images/sc-979sa.jpg"
                )

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=1,
                            name="Goggles",
                            description="Goggles or safety glasses are forms of protective eyewear that usually enclose or protect the area surrounding the eye in order to prevent particulates, water or chemicals from striking the eyes. They are used in chemistry laboratories and in woodworking.",
                            category=category2,
                            image="http://static.dudeiwantthat.com/img/outdoors/winter/gps-hud-snow-goggles-5569.jpg"
                )

session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(user_id=1,
                            name="Table Tennis Bat",
                            description="A table tennis bat is used by table tennis players. The table tennis racket is usually made from laminated wood covered with rubber on one or two sides depending on the player's grip. Unlike a conventional 'racket', it does not include strings strung across an open frame.",
                            category=category3,
                            image="http://robbinstabletennis.com/images/graphite-racket-lg.jpg"
                )

session.add(categoryItem4)
session.commit()

categoryItem4 = CategoryItem(user_id=1,
                            name="Basketball",
                            description="Basketball is a sport played by two teams of five players on a rectangular court. The objective is to shoot a ball through a hoop 18 inches (46 cm) in diameter and 10 feet (3.048 m) high mounted to a backboard at each end.",
                            category=category4,
                            image="http://boykinsbasketball.com/wp-content/uploads/2015/10/5451a9bac173c.preview-699.jpg"
                )

session.add(categoryItem4)
session.commit()


print "new items added!"
