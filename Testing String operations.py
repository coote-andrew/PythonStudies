spam = 'Hello World!'
fizz = spam[0:5]
spam = 'hello guys qw er124'

john = '              there12 once was a man named fred'
print(fizz)

print(spam.upper())
print(spam.isalnum())


def findfirstword(text):
    j = 0
    for i in range(len(text)):
        if text[i].isspace():
            if i == j:
                j += 1
            else:
                print( text[j:i].rjust(15, '*'))
                break
        else:
            i += 1
            continue

        

findfirstword(spam)
findfirstword(john)


findfirstword('    Hi there, does this work?')





    
    

