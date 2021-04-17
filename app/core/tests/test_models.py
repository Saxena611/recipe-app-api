from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "animeshsaxena611@gmail.com"
        password = "dev_ani"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        
        self.assertEqual(user.email,email)
        # cannot check password using assertEqual
        # as passoword as encrypted
        # check_password -> django function
        # which specifically checks password
        self.assertTrue(user.check_password(password))
        

    def test_new_user_email_normalize(self):
        """Test the email for the new user is normalized"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email,'test123')
        self.assertEqual(user.email,email.lower())
        
    def test_new_user_invalid_email(self):
        """Test creating user with no email raises email error"""
        # anything below executing should raise a valueerror
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')
            
    def test_create_new_superuser(self):
        """Creating a new superuser"""
        # superuser are included as a part of permissionmixin
        user = get_user_model().objects.create_superuser(
            'devanimesh@devani.com',
            'dev_ani'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        