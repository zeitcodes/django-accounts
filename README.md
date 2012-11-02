Django Accounts
===============

Django Accounts re-implements several views from Django contrib auth to use the messageing framework instead stand-alone pages for simple messages. It also includes a email authentication backend.

Installation
------------

Run `pip install django-accounts-cbv`

Add `accounts` to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = (
    ...
    'accounts',
)
```

To your sites `url.py` add:

```python
urlpatterns = patterns('',
    ...
    url(r'^accounts/', include('accounts.urls')),
)
```

Authentication Backends
----------------------------

###EmailBackend
The email authentication backend will allow users to login with the email address and password.

To enable it add `'accounts.auth_backends.EmailBackend'` to your `AUTHENTICATION_BACKENDS` setting:

```python
AUTHENTICATION_BACKENDS = (
    'accounts.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)
```

Views
-----

###Login
Login inherits from FormView for easy extensibility.

###Logout
Logout inhertis from RedirectView for easy extensibility. It also displays a logout message.

###PasswordReset
PasswordReset inherits from FormView for easy extensibility. It displays a message once a reset request is submited.

###PasswordResetConfirm
PasswordResetConfirm inherits from FormView for easy extensibility. It displays a message once the user has changed their password.

###UserUpdate
UserUpdate inherits from UpdateView for easy extensibility. It allows a user change their account information.

Forms
-----

###UserForm
A form for changing an existing user's username and/or password. The password is optional and the form will only attempt to update the password if text is in the password input and it matches the confimation input.
