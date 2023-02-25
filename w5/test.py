phonebook = {}
f = open("kontak.txt", "r")
line = f.read()
print(line)
lines = line.split("\n")
for i in lines:
    contact = i.split()
    if len(contact)>1:
        phonebook[contact[0]] = contact[1]
f.close
print(phonebook)
f = open("test.txt", "w")
for i in phonebook:
    f.write(i+" "+phonebook[i]+"\n")
f.close()
if "faris"  in phonebook:
    print("anjay")
