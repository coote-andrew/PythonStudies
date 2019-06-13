#Table Printer

tableData = [['apples','oranges','cherries','banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ['another', 'one', 'onemore', 'another']
             ]


def printTable(table):
    colWidths = [0] * len(table)
    longest = 0
    for y in range(len(table)):
        colWidths[y] = len(table[y][0])
        for x in range(len(table[y])):
            if x > longest:
                longest = x
            if colWidths[y] >= len(table[y][x]):
                continue
            else:
                colWidths[y] = len(table[y][x])


    totalLength = len(table) + 3
    for y in range(len(colWidths)):
        totalLength = totalLength + colWidths[y]


        
    print(''.rjust(totalLength, '*'))
    for row in range(longest + 1):
        print('* ', end = "")
        for col in range(len(table)):
            print(table[col][row].rjust(colWidths[col]), end = " ")
        print('*')
    print(''.rjust(totalLength, '*'))
            


printTable(tableData)
