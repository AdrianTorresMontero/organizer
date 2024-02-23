import os
from shutil import move


#Route
route = './'

#List of folders to create
folders = ['Images', 'Pdfs', 'Winrars']

nani =  os.listdir(route)

#Function for moving files
def organize(file_type,folder):
  for i in nani:
    e=i[-6:]
    if file_type in e:
      move(f'./{i}', f'./{folder}/')

#Folders creation
for u in folders:
  if u not in nani:
    os.mkdir(route + u)
  else:
    print('Folders already created')
    break

print('Folders were created')

#Moving files
organize('.jpg','Images')
organize('.png','Images')
organize('.pdf','Pdfs')
organize('.zip','Winrars')




