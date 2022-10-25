it = ("kate", "james")
finance = ("jack", "jin")
sales = ("ben", "sun")
departments = (it, finance, sales)
for department in departments:
    for person in department:
        print(person)
    print("\n")
