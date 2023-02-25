phonebook = {}
i = "0"

while i != "6":
    f = open("test.txt", "r")
    line = f.read()
    lines = line.split("\n")
    for i in lines:
        contact = i.split()
        if len(contact)>1:
            phonebook[contact[0]] = contact[1]
    f.close
    print("1. Insert New Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. View All Contact")
    print("6. Exit")
    
    i = input("Insert Input : ")
    if(i == "1"):
        nama  = input("enter contact name : ")
        if nama in phonebook:
            print("contact already exists, please go to the Update Contact menu to change the contact number")
        else:
            nomor = input("enter contact number : ")
            phonebook[nama] = nomor
            print("Successfully added contact")
    elif(i == "2"):
        nama  = input("enter contact name : ")
        if nama in phonebook:
            nomor = input("enter contact number : ")
            phonebook[nama] = nomor
            print("Successfully updated contact")
        else:
            print("contact not found, please go to the Insert New Contact menu to add a contact number")
    elif(i == "3"):
        nama  = input("enter contact name : ")
        if nama in phonebook:
            phonebook.pop(nama)
            print("Successfully deleted contact")
        else:
            print("Contact not found")
    elif(i == "4"):
        nama  = input("enter contact name : ")
        if nama in phonebook:
            print("Contact found")
            print(nama + " : " + phonebook[nama])
        else:
            print("Contact not found")
    elif(i == "5"):
        for x in phonebook:
            print(x + " : " + phonebook[x])
    elif(i == "6"):
        print("Have a nice day")
    else:
        print("Wrong Input!!")    
    f = open("test.txt", "w")
    for x in phonebook:
        f.write(x + " " + phonebook[x] + "\n")
    f.close()