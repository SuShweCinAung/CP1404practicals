def main():
    for i in range(0,101,10):
        print(i, end = " ")
    for i in range(20,0,-1):
        print(i, end = " ")
    stars = int(input("Number of stars: "))
    symbol = "*"
    for i in range (stars):
        print(symbol, end = " ")
    stars = int(input("Number of stars: "))
    for row in range(1, stars+1):
        for column in range(1,row+1):
            print(symbol, end = "")
        print(i)
main()