#Guitar Tab Reader
import sys, re
print('add the tab here, then press control + d')
contents = sys.stdin.readlines()

notes = ["A","Bb","B","C","C#","D","Eb","E","F","F#","G","G#"]

TabSearch = re.compile(r'[0-9]')

def cleanUp(text):
    for i in range(len(text)):
        text[i] = text[i].rstrip()

def findNotes(text):
    cleanUp(text)
    newText =[]
    for i in range(len(text)):
        baseNote = text[i][0]
        Text = list(text[i])
        newText.append(baseNote)
        for j in range(len(Text)):
            startPoint = notes.index(baseNote.upper())
            if j == 0:
                continue
            else:
                if TabSearch.search(Text[j]):
                    try:
                        Text[j] = notes[12%(int(startPoint)+int(Text[j]))]
                    except Exception:
                        Text[j] = notes[0]
                newText.append(Text[j])
            if j ==len(Text)-1:
                newText.append('\n')
    textToReturn = ''.join(newText)
    print(textToReturn)

        
        

findNotes(contents)


