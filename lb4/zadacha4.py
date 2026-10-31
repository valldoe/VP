phonebook = {}

for i in range(3):
    contact = input().split()
    phonebook.update({contact[0] : contact[1]})

search = input()

print(phonebook)

if phonebook.get(search) == None:
    print("contanct not found")
else:
    print(phonebook.get(search))