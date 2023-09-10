from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\d{10}$',
    message='Phone number must be entered in the format: \'9940128262\'. Up to 10 digits allowed.'
)