import random


num_trials = 30


number_counts = {}


for _ in range(num_trials):
    num = random.randint(1, 9)
    if num in number_counts:
        number_counts[num] += 1
    else:
        number_counts[num] = 1

most_common_number = max(number_counts, key=number_counts.get)

 
print(f"가장 많이 나온 수: {most_common_number}")
print(f"{most_common_number}단")
for i in range(1, 10):
    print(f"{most_common_number} * {i} = {most_common_number * i}")