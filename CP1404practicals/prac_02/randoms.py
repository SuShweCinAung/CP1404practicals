import random
dir(random)
print(random.randint(5, 20))
# in line 1, the smallest number is 5 and the largest is 19

print(random.randrange(3, 10, 2))
# in line 2, the smallest number is 3 and the largest is 9
# this line hasn't produced a 4 since it has increased by 2 based on 3

print(random.uniform(2.5, 5.5))
# in line 3, the smallest number i've seen is 2.5559517888285215 and the largest is 5.344795413569101

print(random.randint(1,101))