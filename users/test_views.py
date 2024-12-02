import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_register_user(client):
    response = client.post(reverse('register'), {
        'username': 'testuser',
        'password1': '12345678@',
        'password2': '12345678@',
    })
    assert response.status_code == 302
    assert User.objects.filter(username='testuser').exists()

@pytest.mark.django_db
def test_login_user(client, django_user_model):
    user = django_user_model.objects.create_user(username='testuser', password='password123')
    response = client.post(reverse('login'), {
        'username': 'testuser',
        'password': 'password123',
    })
    assert response.status_code == 302
    assert '_auth_user_id' in client.session


from unittest.mock import patch
from django.contrib.auth.models import User

@pytest.mark.django_db
@patch('django.contrib.auth.forms.UserCreationForm.save')
def test_register_user_with_mock(mock_save, client):
    mock_save.return_value = User(username='mockuser')
    response = client.post(reverse('register'), {
        'username': 'mockuser',
        'password1': '12345678@',
        'password2': '12345678@',
    })
    assert response.status_code == 302
    assert mock_save.called