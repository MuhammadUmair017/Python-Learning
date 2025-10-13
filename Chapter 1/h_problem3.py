# using os modules we can see the file directories of the given path

import os 

directory_path = '/work'

contents = os.listdir(directory_path)

for item in contents:
    print(item) 

    
