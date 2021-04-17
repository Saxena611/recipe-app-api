from django.test import TestCase , Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        # Client() allows to make get post request.
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@django.com',
            password = 'admin123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'test@django.com',
            password = 'test123',
            name = 'Full name test'
        )
    
    def test_users_listed(self):
        """
        Test that user are listed on user page
        """
        url = reverse('admin:core_user_changelist')
        # generate url for the page
        res = self.client.get(url)
        self.assertContains(res,self.user.name)
        self.assertContains(res,self.user.email)
        # assertContains django custom method
        # checks for a value in the content
        
    def test_user_change_page(self):
        """Test that user edit page work"""
        url = reverse('admin:core_user_change',args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)
        
    def test_create_user_page(self):
        """Test that user create page work"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)