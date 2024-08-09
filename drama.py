print("The Drama Tisers")
print("----------------")
print()
print("Select an option below")
print()

members = []

while True:
    option = input("<a>dd a new member, <p>rint members, <q>uit: ").lower()

    if option == "a":
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        full_name = first_name + " " + last_name

        acting = input("Are you interested in acting? <y>es, <n>o: ").lower()
        production = input("Are you interested in helping with the production? <y>es, <n>o: ").lower()

        if acting == "y":
            acting = True
        else:
            acting = False

        if production == "y":
            production = True
        else:
            production = False

        if not first_name or not last_name:
            print("You need to enter a first name AND a last name")
            print("Details have not been added. Please try again.")
            print()
        else:
            members.append([full_name, acting, production])

    elif option == "p":
        print()
        print("Our current list of members and preferences")
        print("-------------------------------------------")
        print()
        print("Members")
        print("------")
        for member in members:
            print(member[0])

        print()
        print("Actors")
        print("------")
        for member in members:
            if member[1]:
                print(member[0])

        print()
        print("Helpers")
        print("------")
        for member in members:
            if member[2]:
                print(member[0])
        print()

    elif option == "q":
        break

    else:
        print("Invalid option. Please try again.")
