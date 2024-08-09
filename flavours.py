with open("flavours.txt") as f:
    flavour = input("Check flavour: ").lower()
    flavours = []
    for line in f:
        flavours.append(line.strip().lower())

    while flavour != '':
        if flavour in flavours:
            print("Done it already.")
            flavour = input("Check flavour: ").lower()
        else:
            print("Sounds good!")
            flavour = input("Check flavour: ").lower()
            flavours.append(flavour); 
