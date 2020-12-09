def main():
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers)/len(numbers)
    print("The first number is ",numbers[0])
    print("The last number is ",numbers[-1])
    print("The smallest numbers is ",minimum)
    print("The largest numbers is ",maximum)
    print("The average of the numbers is ",average)
main()