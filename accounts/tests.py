from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

class AccountsTest(TestCase):

    client = Client()

    def setUp(self):
        self.user = User.objects.create_user('mely', 'foo@bar.com', '123')

    def test_login_view(self):
        url = reverse('auth_login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200) # 200 OK

    def test_login_post(self):
        url = reverse('auth_login')
        data = {
            'username': 'mely',
            'password': '123',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302) # 302 Found

    def test_logout_view(self):
        url = reverse('auth_logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_password_reset_view(self):
        url = reverse('auth_password_reset')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_password_reset_confirm(self):
        generator = PasswordResetTokenGenerator()
        token = generator.make_token(self.user)
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        url = reverse('auth_password_reset_confirm', args=[uid, token])
        data = {
            'new_password1': '123',
            'new_password2': '123',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_accounts_profile_logged_out(self):
        url = reverse('accounts_profile')
        response = self.client.get(url)
        # Redirects to login page because client was not logged in.
        self.assertEqual(response.status_code, 302)

    def test_accounts_profile_logged_in(self):
        profile_client = Client()
        profile_client.login(username='mely', password='123')
        url = reverse('accounts_profile')
        response = profile_client.get(url)
        # Should stay on same page because client is logged in.
        self.assertEqual(response.status_code, 200)
