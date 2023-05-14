"""Seed file to make sample data for DB."""

from models import User, Post, Tag, PostTag, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

scott = User(first_name="Scott", last_name="Waller", image_url="https://media.cnn.com/api/v1/images/stellar/prod/210417160032-jaleel-white-purple-urkel-cannabis-trnd-restricted.jpg?q=w_933,h_1400,x_333,y_0,c_crop")
peter = User(first_name="Peter", last_name="Waller", image_url="https://be.arizona.edu/sites/abe.arizona.edu/files/styles/medium/public/images/people/Waller%20Headshot.jpg?itok=XaBWwdWa")
mark = User(first_name="Mark", last_name="Waller", image_url="https://media.licdn.com/dms/image/C5603AQHXNy7H-_NMzw/profile-displayphoto-shrink_800_800/0/1517470123356?e=1689206400&v=beta&t=3S016LN8k8-IbBxTNLSK6sUG-Vy5X5p3aglRz_9Zy-A")
hannah = User(first_name="Hannah", last_name="Burgett", image_url="https://do2ufdrk7dzyk.cloudfront.net/images/2018/10/12/Waller_Hannah.jpg?width=300")

s1 = Post(title="First Post", content="This is how you post.", user_id="1")
p1 = Post(title="First Post", content="This is how you post.", user_id="2")
m1 = Post(title="First Post", content="This is how you post.", user_id="3")
h1 = Post(title="First Post", content="This is how you post.", user_id="4")

t1 = Tag(name="goofy")
t2 = Tag(name="serious")
t3 = Tag(name="funny")
t4 = Tag(name="coding")
t5 = Tag(name="wtf")




db.session.add_all([scott, peter, mark, hannah])
db.session.commit()

db.session.add_all([s1, p1, m1, h1])
db.session.commit()

db.session.add_all([t1, t2, t3, t4, t5])
db.session.commit()

