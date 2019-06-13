#Actually might do something useful
#not needed anymore

import os
import shutil
import re
for folderName, subfolders, filenames in os.walk('../../../../Documents/monopoly'):
        print('The current folder is ' + folderName)
        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            if filename.endswith('.png'):
                #Get Real name
                searchTerms = re.compile(r'[A-Za-z0-9-]*')
                newName = searchTerms.search(filename)                
                shutil.move(os.path.join(folderName, filename), os.path.split(os.path.join(folderName, filename))[0] + '/' +newName.group() + '1.png')
            print('FILE INSIDE ' + folderName + ': ' + filename)
        print('')
    
