def main():
    items = int(input("Number of items: "))
    while items < 0 :
        items = int(input("Number of items: "))
    total = 0
    for i in range (items):
        price = int(input("Price of item: "))
        total += price
    print("Total price for", items,"item(s) is $", total)
main()