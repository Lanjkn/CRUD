

CONTACTLIST = {}


def showContacts():
    if(CONTACTLIST):
        for contact in CONTACTLIST:
            searchContacts(contact)
    else:
        print("Empty contact list.")


def searchContacts(contact):
        try:
            print(contact, ":\n Cellphone:", CONTACTLIST[contact]['cellphone'], "\n Email:", CONTACTLIST[contact]['email'], "\n Address:", CONTACTLIST[contact]['address'])
        except KeyError as e:
            print("Contact {} not found!".format(e))
        except Exception as e:
            print("Error: {}".format(e))



def newContact(contact, cellphone, email, address):
    try:
        CONTACTLIST[contact] = {
        "cellphone":cellphone,
        "email":email,
        "address":address,
        }
        print("Contact {} successfully added.".format(contact))
    except Exception as e:
        print("Error: {}".format(e))
    saveDB()    


def editContact(contact):
    try:
        CONTACTLIST[contact]
    except KeyError:
        print("contact {} not found".format(contact))
        return
    print("What do you wnat to edit?: ")
    print("1 - Cellphone")
    print("2 - Email")
    print("3 - Address")
    print("4 - All")
        
    choice = input()
    if(choice == "1"):
        cellphone = input("Input the new Cellphone: ")
        CONTACTLIST[contact]['cellphone'] = cellphone
    elif(choice == "2"):
        email = input("Input the new Email: ")
        CONTACTLIST[contact]['email'] = email
    elif(choice == "3"):
        address = input("Input the new Address: ")
        CONTACTLIST[contact]['address'] = address
    elif(choice == "4"):
        cellphone = input("Input the new Cellphone: ")
        email = input("Input the new Email: ")
        address = input("Input the new Address: ")   
        CONTACTLIST[contact]['cellphone'] = cellphone
        CONTACTLIST[contact]['email'] = email
        CONTACTLIST[contact]['address'] = address
    else:
        print("Non-existent choice.")
    saveDB()    


def eraseContact(contact):
    try:
        CONTACTLIST.pop(contact)
        print("Contact {} successfully erased.".format(contact))
    except KeyError as e:
        print("Contact {} doesn't exist.".format(e))
    saveDB()

        
def menu():
    print("Choose an option: ")
    print("1 - Add a new contact")
    print("2 - Erase a contact")
    print("3 - Edit contact data")
    print("4 - Search for contact")
    print("5 - Print contact list")
    print("6 - Export contacts to CSV file")
    print("7 - Import contacts from CSV file")
    print("0 - Exit")


def importContacts(fileName):
    try:
        with open(fileName + ".csv", 'r') as file:
            lines = file.readlines()
            for line in lines:
                contact = line.strip().split(",")
                if(contact[0] != "name"):
                    newContact(contact[0], contact[1], contact[2], contact[3])
    except IOError :
        print("File not Found.")    
    except Exception as E:
        print("Error: {}".format(E))   


def exportContacts(fileName):
    try:
        with open(fileName + ".csv", 'w') as file:
            file.write("name,cellphone,email,address\n")
            for contact in CONTACTLIST:
                file.write("{},{},{},{}\n".format(contact, CONTACTLIST[contact]['cellphone'],CONTACTLIST[contact]['email'],CONTACTLIST[contact]['address']))
    except Exception as E:
        print("Error: {}".format(E))

def saveDB():
    exportContacts("database")


def importDB():
    print("READING DATABASE")
    importContacts("database")
    print("READING FINISHED")
    print("{} contacts added.".format(len(CONTACTLIST)))
    print("-----------------------------")

# START SYSTEM
importDB()
while True: 
    menu()
    choice = input("Choose an option: ")
    if(choice == "1"):
        contact = input("Input the contact name: ")
        newCellphone = input("Input the contact cellphone: ")
        newEmail = input("Input the contact email: ")
        newAddress = input("Input the contact address: ")
        try:
            newContact(contact, newCellphone, newEmail, newAddress)
        except Exception as E:
            print(E)
    elif(choice == "2"):
        erasedContact = input("Which contact do you want to erase?: ") 
        eraseContact(erasedContact)
        
    elif(choice == "3"):
        editedContact = input("Which contact do you want to edit?: ")
        editContact(editedContact)
    elif(choice == "4"):
        searchedContact = input("Please input the contact name: ")
        searchContacts(searchedContact)
    elif(choice == "5"):
        showContacts()
    elif(choice == "6"):
        fileName = input("Input the file name to export:")
        exportContacts(fileName)
    elif(choice == "7"):
        fileName = input("Input the file name to import: ")
        importContacts(fileName)
    elif(choice == "0"):
        break
    else:
        print("Invalid Option.")
