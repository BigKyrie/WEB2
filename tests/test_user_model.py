import unittest
import time
from app import create_app, db
from app.models import User,AnonymousUser, Role, Permission


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()



    def tearDown(self):
        db.session.remove()



    def test_no_password_getter(self):
        u = User(password='111')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='aaa')
        self.assertTrue(u.verify_password('aaa'))
        self.assertFalse(u.verify_password('bbb'))

    def test_password_salts_are_random(self):
        u = User(password='aaaa')
        u2 = User(password='aaaa')
        self.assertTrue(u.password_hash != u2.password_hash)

    def test_valid_confirmation_token(self):
        u = User(password='aaa')
        db.session.add(u)
        db.session.commit()
        token = u.generate_confirmation_token()
        self.assertTrue(u.confirm(token))

    def test_invalid_confirmation_token(self):
        u1 = User(password='aaa')
        u2 = User(password='bbb')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        token = u1.generate_confirmation_token()
        self.assertFalse(u2.confirm(token))

    def test_expired_confirmation_token(self):
        u = User(password='aaa')
        db.session.add(u)
        db.session.commit()
        token = u.generate_confirmation_token(1)
        time.sleep(2)
        self.assertFalse(u.confirm(token))

    def test_valid_reset_token(self):
        u = User(password='aaa')
        db.session.add(u)
        db.session.commit()
        token = u.generate_reset_token()
        self.assertTrue(User.reset_password(token, 'bbb'))
        self.assertTrue(u.verify_password('bbb'))

    def test_invalid_reset_token(self):
        u = User(password='aaa')
        db.session.add(u)
        db.session.commit()
        token = u.generate_reset_token()
        self.assertFalse(User.reset_password(token + 'a', 'horse'))
        self.assertTrue(u.verify_password('aaa'))

    def test_valid_email_change_token(self):
        u = User(email='bigkyrie@example.com', password='aaa')
        db.session.add(u)
        db.session.commit()
        token = u.generate_email_change_token('weiyuheng@example.com')
        self.assertTrue(u.change_email(token))
        self.assertTrue(u.email == 'weiyuheng@example.com')

    def test_invalid_email_change_token(self):
        u1 = User(email='bigkyrie@example.com', password='aaa')
        u2 = User(email='weiyuheng@qq.com', password='bbb')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        token = u1.generate_email_change_token('lllll@example.com')
        self.assertFalse(u2.change_email(token))
        self.assertTrue(u2.email == 'weiyuheng@qq.com')

    def test_duplicate_email_change_token(self):
        u1 = User(email='kkk@example.com', password='aaa')
        u2 = User(email='weiyuheng@qq.com', password='bbb')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        token = u2.generate_email_change_token('kkk@example.com')
        self.assertFalse(u2.change_email(token))
        self.assertTrue(u2.email == 'weiyuheng@qq.com')

    def test_user_role(self):
        u = User(email='kkk@example.com', password='cat')
        self.assertFalse(u.can(Permission.ADMIN))


    def test_administrator_role(self):
        r = Role.query.filter_by(name='Administrator').first()
        u = User(email='978633302@qq.com', password='cat', role=r)
        self.assertTrue(u.is_administrator())

    def test_anonymous_user(self):
        u = AnonymousUser()
        self.assertFalse(u.can(Permission.ADMIN))

    def test_name(self):
        u = User(name='wei')
        self.assertTrue(u.name == 'wei')
