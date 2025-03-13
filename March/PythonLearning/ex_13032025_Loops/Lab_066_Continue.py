#Continue:

for number in range(10):
    if number % 2 == 0:
        continue
    else:
        print(number)

#  |i| |Condition| |o/p|
# 0 |0%2 == 0|True |o/p ->No Output
# 1 |1%2 == 0|False |o/p -> Prints number
# 0 |2%2 == 0|True |o/p ->No output
#3 |3%2 == 0|False |o/p -> Prints number