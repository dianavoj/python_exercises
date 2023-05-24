#program that finds numbers that are divisible by 7 and not multiple of 5 between 2000 and 3200 included. Output should be in a single line separated by comma
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end = ",")
