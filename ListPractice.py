#Lists practice
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) +1) + ' (Or enter nothing to stop.):')
    name = input()
    if name =='':
        break
    catNames = catNames + [name]
print('THe cat names are:')
for name in catNames:
    print(' ' + name)
