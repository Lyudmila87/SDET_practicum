import os
from dataclasses import dataclass, field
from datetime import datetime
from random import choices, randint, choice

from faker import Faker

faker_ru = Faker('ru_RU')

subjects = ['Hindi', 'English', 'Maths', 'Physics', "Chemistry", "Biology", "Computer Science", "Commerce",
            "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
state_and_city = {"NCR": ["Delhi", "Gurgaon", "Noida"], "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
                  "Haryana": ["Karnal", "Panipat"], "Rajasthan": ["Jaipur", "Jaiselmer"]}
hobbies = ['Sports', 'Reading', 'Music']


@dataclass
class User:
    first_name: str = faker_ru.first_name()
    last_name: str = faker_ru.last_name()
    email: str = faker_ru.email()
    current_address: str = faker_ru.address()
    mobile: str = faker_ru.msisdn()[0:10]
    subject: set = field(default_factory=lambda: set(choices(subjects, k=randint(1, len(subjects)))))
    state: str = None
    city: str = None
    gender: str = choice(['Male', 'Female', 'Other'])
    birth_date: datetime = faker_ru.date_of_birth(minimum_age=16)
    hobbies: set = field(default_factory=lambda: set(choices(hobbies, k=len(hobbies))))
    path_to_file: str = os.path.abspath("files/cat.jpg")

    def __post_init__(self):
        self.state = choice(list(state_and_city.keys()))
        self.city = choice(state_and_city[self.state])
