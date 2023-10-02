import re

from django.core.exceptions import ValidationError


def validator_color(value):
    pattern = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
    if not re.match(pattern, value):
        raise ValidationError(
            'Цвет должен быть в формате Hex.'
        )
