import random
def main():
    number_list=[]
    turn = int(input("How many quick picks? "))
    for i in range(1, turn+1):
        for num in range(0, 6):
            num = random.randint(1,45)
            while num in number_list:
                num = random.randint(1, 45)
            number_list.append(num)
            number_list.sort()
        print("{:>2} {:>2} {:>2} {:>2} {:>2} {:>2}".format(number_list[0],number_list[1],number_list[2],number_list[3],number_list[4],number_list[5]))
main()
