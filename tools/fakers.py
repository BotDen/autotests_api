from faker import Faker


class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def get_first_name(self) -> str:
        return self.faker.first_name()

    def get_last_name(self) -> str:
        return self.faker.last_name()

    def get_middle_name(self) -> str:
        return self.faker.middle_name()

    def get_email(self) -> str:
        return self.faker.email()

    def get_password(self) -> str:
        return self.faker.password()

    def get_uuid(self) -> str:
        return self.faker.uuid4()

    def get_text(self) -> str:
        return self.faker.text()

    def get_sentence(self) -> str:
        return self.faker.sentence()

    def get_integer(self, start: int = 1, end: int = 100) -> int:
        return self.faker.random_int(min=start, max=end)

    def get_min_score(self, start=1, end = 49) -> int:
        return self.get_integer(start=start, end=end)

    def get_max_score(self, start=50, end = 100) -> int:
        return self.get_integer(start=start, end=end)

    def get_estimated_time(self, start: int = 1, end: int = 10) -> str:
        return f"{self.get_integer(start=start, end=end)} week"


fake = Fake(faker=Faker("ru_RU"))
