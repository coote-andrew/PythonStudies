#! /usr/bin/env python3

#Usage
#py.exe mcb.pyw save <keyword> - saves clipboard to keyword
#py.exe mcb.pyw <keyword> - loads keyword to clipboard
#py.exe mcb.pyw list - loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#Save clipboard content
if len(sys.argv) ==3 and sys.argv[1].lower() == 'save':
    keyword = sys.argv[2]
    #TODO
    text = pyperclip.paste()
    mcbShelf[keyword] = text
elif len(sys.argv) ==3 and sys.argv[1].lower() == 'delete':
    keyword = sys.argv[2]
    #TODO
    del mcbShelf[keyword]


#load content and list
elif len(sys.argv)==2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        keyword = sys.argv[1]
        pyperclip.copy(mcbShelf[keyword])
    
mcbShelf.close()

