from unittest import TestCase

from app import app
from models import db, User, Post

#Use test database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class PostModelTestCase(TestCase):
    """Test for model Post."""

    def setUp(self):
        """Clear db."""
        Post.query.delete()

    def tearDown(self):
        """Clean up."""

        db.session.rollback()

    def test_get_by_title(self):
        """Test query of post instance."""
        user = User(first_name="Blunder", last_name="Shiffrin")
        post = Post(title="Test Post", content="It is written.", user=user)
        db.session.add(user)
        db.session.commit()

        db.session.add(post)
        db.session.commit()

        p1 = Post.query.filter_by(title="Test Post").one()
        self.assertEqual(p1.content, "It is written.")
        self.assertEqual(p1.user_id, user.id)

    def test_user_relationship(self):
        """Test relationship between User and Post models."""
        user = User(first_name="Sunder", last_name="Ripkin")
        post = Post(title="Sunder Test", content="Does this work?", user=user)
        db.session.add(user)
        db.session.commit()

        db.session.add(post)
        db.session.commit()

        p2 = Post.query.filter_by(title="Sunder Test").one()
        self.assertEqual(p2.user_id, user.id)