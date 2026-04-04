print("Contact Book")

names = []
numbers = []

# ADD CONTACTS
for i in range(2):
    name = input("Name: ")
    number = input("Number: ")
    names.append(name)
    numbers.append(number)
    print("Saved:", name, number)

# SEARCH CONTACT
s = input("Search name: ")
for i in range(2):
    if names[i] == s:
        print("Found:", names[i], numbers[i])
        break
else:
    print("Contact not found")

# UPDATE CONTACT
u = input("Update name: ")
for i in range(2):
    if names[i] == u:
        numbers[i] = input("New number: ")
        print("Contact updated")
        break
else:
    print("Contact not found")

# DELETE CONTACT
d = input("Delete name: ")
for i in range(2):
    if names[i] == d:
        names[i] = "Deleted"
        numbers[i] = "Deleted"
        print("Contact deleted")
        break
else:
    print("Contact not found")

print("Contacts are saved")