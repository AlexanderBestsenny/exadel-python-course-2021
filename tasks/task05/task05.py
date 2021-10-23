def create_user(firstName, lastName, age=42, **extra) -> dict:
    return {"name": firstName, "surname": lastName, "age": age, "extra": extra}


user1 = create_user("John", "Doe")
print(user1)

user2 = create_user("Bill", "Gates", age=65)
print(user2)

user3 = create_user("Marie", "Curie", age=66, occupation="physicist", won_nobel=True)
print(user3)

assert user1["age"] == 42

assert user2["age"] == 65
assert type(user2["extra"] is dict)
assert len(user2["extra"]) == 0

assert type(user3["extra"] is dict)
assert user3["extra"]["occupation"] == "physicist"
assert user3["extra"]["won_nobel"]
