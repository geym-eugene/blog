import re
from rest_framework.serializers import ValidationError


class PasswordValidator:

    def __init__(self):
        pass

    def __call__(self, value):
        if len(value) < 8:
            raise ValidationError("Пароль должен быть не менее 8 символов.")
        if not re.search(r'\d', value):
            raise ValidationError("Пароль должен содержать хотя бы одну цифру.")


class EmailDomainValidator:
    def __init__(self):
        self.allowed_domains = ['mail.ru', 'yandex.ru']

    def __call__(self, value):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, value):
            raise ValidationError("Неверный формат email адреса.")

        domain = value.split('@')[-1]
        if domain not in self.allowed_domains:
            raise ValidationError(f"Невалидный домен. Разрешены только домены: {', '.join(self.allowed_domains)}.")
