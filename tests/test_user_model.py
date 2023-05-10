from unittest import TestCase

from app import app
from models import db, User, Post

#Use test database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()

class UserModelTestCase(TestCase):
    """Tests for model User."""

    def setUp(self):
        """Clear db."""
        User.query.delete()

    def tearDown(self):
        """Clean up."""

        db.session.rollback()

    def test_get_by_last_name(self):
        """Test query of user instance."""
        user = User(first_name="Dunder", last_name="Mifflin")
        db.session.add(user)
        db.session.commit()

        l_name = User.query.filter_by(last_name="Mifflin").one()
        self.assertEqual(l_name.last_name, "Mifflin") 

    def test_post_relationship(self):
        """Test relationship between User and Post models."""
        user = User(first_name="Dunder", last_name="Mifflin")
        db.session.add(user)
        db.session.commit()

        self.assertEqual(len(user.posts), 0)


