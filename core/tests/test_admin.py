from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTest(TestCase):
    """Unit for Admin site"""
    
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(email="joe@gmail.com", password="okay01928#")
        self.user = get_user_model().objects.create_user(email="test@gmail.com", password="okay01928#", name="test1")
        self.client.force_login(self.admin_user)
        
    def test_users_listed(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        
        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.name)
        
    def test_user_change_page(self):
        url = reverse("admin:core_user_change", args=(self.user.id,))
        res = self.client.get(url)
        
        self.assertEqual(res.status_code, 200)
        
    def test_create_user_page(self):
        url = reverse("admin:core_user_add")
        res = self.client.get(url)
        
        self.assertEqual(res.status_code, 200)