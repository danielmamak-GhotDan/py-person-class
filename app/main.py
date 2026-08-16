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

    for person in people:
        new_obj = Person.people[person["name"]]

        if "wife" in person and person["wife"] is not None:
            new_wife = person["wife"]
            new_obj.wife = Person.people[new_wife]

        if "husband" in person and person["husband"] is not None:
            new_husband = person["husband"]
            new_obj.husband = Person.people[new_husband]

    return list_person
