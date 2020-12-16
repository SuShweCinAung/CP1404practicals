def get_name(email):
    name = email.split("@")[0]
    parts = name.split(".")
    name = " ".join(parts).title()
    return name

def main():
    email_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        username = input("Is your name {}? (Y/n) ".format(name)).upper()
        if username.upper() == "N" or username.upper() != "Y":
            name = input("Enter your name: ")
        email = input("Email: ")
        email_name[email] = name
    for email, name in email_name.items():
        print("{} ({})".format(name, email))
main()