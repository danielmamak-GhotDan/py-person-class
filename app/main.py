class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_person = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        list_person.append(new_person)
