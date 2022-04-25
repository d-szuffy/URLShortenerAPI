from random import choice
from string import ascii_letters


def create_shortened_url(model_instance):
    random_code = "http://localhost:8000/" + ''.join(choice(ascii_letters) for x in range(10))

    if model_instance.objects.filter(slug=random_code).exists():
        # Run the function again
        return create_shortened_url(model_instance)

    return random_code
