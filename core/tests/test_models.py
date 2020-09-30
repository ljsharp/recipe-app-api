from django.test import TestCase
from django.contrib.auth import get_user_model


class  ModelTest(TestCase):
    
    def test_create_user_with_email(self):
        
        email = "test@gmail.com"
        password = "fmak2!5590"
        
        user = get_user_model().objects.create_user(email=email, password=password)
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        
    
    def test_create_user_with_email(self):
        
        email = "test@FMAIO.com"
        password = "fmak2!dfvvs"
        
        user = get_user_model().objects.create_user(email=email, password=password)
        
        self.assertEqual(user.email, email.lower())
    
    def test_new_user_with_email(self):
        
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password="ss@dfj55")
            
    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(email="joe@gmail.com", password="joe1984@")
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)