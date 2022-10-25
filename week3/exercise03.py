departments = {
    "it": ["kate", "james"],
    "finance": ["jack", "jin"],
    "sales": ["ben", "sun"]
}

for dept_name in departments.keys():
    print(dept_name)

for name in departments.values():
    print(name)

for item in departments.items():
    print(item)
