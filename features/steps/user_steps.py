from behave import given, when, then
from selenium.webdriver.common.by import By

@given('I am on the login page')
def step_impl(context):
    context.browser.get('http://localhost:8000/login/')

@given('a user exists with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    if not User.objects.filter(username=username).exists():
        User.objects.create_user(username=username, password=password)

@when('I fill in "{field_name}" with "{value}"')
def step_impl(context, field_name, value):
    field = context.browser.find_element(By.NAME, field_name)
    field.clear()
    field.send_keys(value)

@when('I press "{button_text}"')
def step_impl(context, button_text):
    button = context.browser.find_element(By.XPATH, f"//button[contains(text(), '{button_text}')]")
    button.click()

@then('I should be redirected to the home page')
def step_impl(context):
    assert context.browser.current_url.endswith('/')

@then('I should see "{text}"')
def step_impl(context, text):
    assert text in context.browser.page_source

@given('I am on the registration page')
def step_impl(context):
    context.browser.get('http://localhost:8000/register/')

@then('I should be redirected to the login page')
def step_impl(context):
    print(f"Captured Current URL: {context.browser.current_url}")  # Лог поточного URL
    expected_path = '/login/'
    assert context.browser.current_url.endswith(expected_path), (
        f"Expected to be on {expected_path}, but got {context.browser.current_url}"
    )
