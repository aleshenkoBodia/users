import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_register_user(client):
    response = client.post(reverse('register'), {
        'username': 'testuser',
        'password1': '12345678@',
        'password2': '12345678@'
    })
    assert response.status_code == 302, f"Response content: {response.content.decode()}"

@pytest.mark.django_db
def test_login_user(client):
    user = User.objects.create_user(username='testuser2', password='12345678@')
    response = client.post(reverse('login'), {
        'username': 'testuser2',
        'password': '12345678@'
    })
    assert response.status_code == 302  # Redirects after successful login


@pytest.mark.django_db
def test_register_user_invalid_passwords(client):
    # Спробуємо надіслати неправильні паролі
    response = client.post(reverse('register'), {
        'username': 'testuser3',
        'password1': 'password123',
        'password2': 'wrongpassword'
    })

    # Перевіряємо, що статус-код не 302 (не відбулося перенаправлення)
    assert response.status_code == 200

