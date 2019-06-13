#LIst practice + 'in' and 'not' operators
myPets = ['zophie', 'pooka', 'fat-tail']


while True:
    print('Enter a pet name:')
    name = input()
    if name == '':
        print(myPets)
        break
    elif name not in myPets:
        print('I do not have a pet named ' + name)
        myPets = myPets + [name]
        print('I do now though...')
    else:
        print(name + ' is my pet.')



cat = ['fat', 'black','loud']
size, color, disposition = cat

print(size)
