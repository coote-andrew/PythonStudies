#Passing Reference

def eggs(someParameter):
    i = 0
    while True:
        someParameter.append('Hello')
        i += 1
        if (i>10):
            break

spam = [1,2,3]
eggs(spam)
spam.insert(1, 'Booga wooga!')
print(spam)
monty = tuple(spam)
print(monty)
