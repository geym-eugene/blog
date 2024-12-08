from rest_framework.exceptions import ValidationError


class TitleValidator:
    def __init__(self, forbidden_words=None):
        if forbidden_words is None:
            forbidden_words = ["ерунда", "глупость", "чепуха"]
        self.forbidden_words = forbidden_words

    def __call__(self, value):
        value_lower = value.lower()

        for word in self.forbidden_words:
            if word in value_lower:
                raise ValidationError(f"Заголовок не должен содержать слово: {word}.")