from application import db

from entity.models import Entity
from user.models import User
from object.models import Object
from circle.models import Circle
from channel.models import Channel
from member.models import Member
from like.models import Like


objects = [
    Circle(name="Fitness", description="Keeping fit", owner_guid=4, type="circle"),
    Circle(name="Diet", description="Eating healthy", owner_guid=4, type="circle"),
    Circle(name="Diabetes", description="Manage diabetes", owner_guid=4, type="circle"),
    User(name="steve", username="steve841", email="steve@test.com", password="123", language="english", type="user"),
    User(name="hua", username="huahua", email="hua@test.com", password="123", language="english", type="user"),
    User(name="vale", username="namwan", email="vale@test.com", password="123", language="english", type="user"),
    Member(user_id=1, circle_id=1),
    Member(user_id=1, circle_id=2),
    Member(user_id=1, circle_id=3),
    Member(user_id=2, circle_id=2),
    Member(user_id=2, circle_id=3),
    Member(user_id=3, circle_id=1),
    Member(user_id=3, circle_id=3),
    Object(owner_guid=4, circle_guid=1, type="object", object_type="post", body="Hey whats up"),
    Object(owner_guid=5, circle_guid=1, type="object", object_type="post", body="All good"),
    Object(owner_guid=6, circle_guid=1, type="object", object_type="post", body="Flexing my biceps"),
    Object(owner_guid=4, circle_guid=1, type="object", object_type="post", body="Cool"),
    Object(owner_guid=5, circle_guid=1, type="object", object_type="post", body="Awesome"),
    Object(owner_guid=6, circle_guid=1, parent_id=16, type="object", object_type="reply", body="Super cool"),
    Like(user_id=5, object_id=16),
    ]

db.session.add_all(objects)
db.session.commit()
db.session.flush()

print("Success")
