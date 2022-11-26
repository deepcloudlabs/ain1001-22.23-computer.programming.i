temperatures = []
while True:
    t = input("Enter next temperature:")
    if t == "quit":
        break
    temperatures.append(int(t))

min_temp = None
max_temp = None
sum_temp = 0.0
for temperature in temperatures:
    if min_temp is None or temperature < min_temp:
        min_temp = temperature
    if max_temp is None or temperature > max_temp:
        max_temp = temperature
    sum_temp += temperature
avg_temp = sum_temp / len(temperatures)
diff_temp = max_temp - min_temp
print(f"Minimum temperature is {min_temp}.")
print(f"Maximum temperature is {max_temp}.")
print(f"Average temperature is {avg_temp}.")
print(f"Diff. between the max and min temperatures is {diff_temp}.")
