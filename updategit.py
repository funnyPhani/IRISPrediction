

import os


giturl=input('enter the git url :')



os.system('git init')

os.system('git add .')

os.system('git status')

os.system('git commit -m "Initial commit"')

os.system('git remote add origin '+giturl)

os.system('git push -f origin master')


print('\n  Task Completed...!')