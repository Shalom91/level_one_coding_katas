multiples_of_3_or_5 = []
for number in range(1000):
    if (number % 3 == 0) or (number % 5 == 0):
        multiples_of_3_or_5.append(number)
print(sum(multiples_of_3_or_5))