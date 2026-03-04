import random
from faker import Faker


def generate_random_name(sex=None):
    fake = Faker()
    if sex == "male":
        return fake.name_male()
    elif sex == "female":
        return fake.name_female()
    elif sex == "non-binary":
        return fake.name_nonbinary()
    else:
        return fake.name()
