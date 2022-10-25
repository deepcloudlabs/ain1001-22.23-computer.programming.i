accounts = [
    ("TR630006273757834768657521", 10000, "ACTIVE"),
    ("TR750006279525658613768626", 0, "CLOSED"),
    ("TR640006297648161842839121", 30000, "BLOCKED"),
]

print("{:26} {:8} {:8}".format("Account ID", "Balance", "Status"))

for account in accounts:
    accountId, balance, status = account
    print(f"{accountId:<26} {balance:<8} {status:8}")
