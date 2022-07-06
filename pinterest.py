from py3pin.Pinterest import Pinterest
from random import randint
import time
import os
MAX_PHOTOS = 250
file1, file2, file3, file4 =  open('titles.txt'), open('description.txt'), open('links.txt'), open('hashtags.txt')
Titles = [x for x in file1]
Descriptions = [x for x in file2]
Links = [x for x in file3]
Hashtags = [x for x in file4]
file1.close(), file2.close(), file3.close(), file4.close()

lTitles, lDescription, lLinks = len(Titles), len(Descriptions), len(Links)
file = open('logpass.txt')
email, password, username = file.readline().split()
file.close()

pinterest = Pinterest(email = email, password = password, username = username, cred_root='cred_root')
pinterest.login()

'''
#print all boards
boards = []
board_batch = pinterest.boards()
while len(board_batch) > 0:
    boards += board_batch
    board_batch = pinterest.boards()

for b in boards:
    print(b)
'''

print('Auto Posting Pinterest: ')
count = 1

while True:
    try:
        Title = Titles[randint(0, lTitles - 1)]
        Description = Descriptions[randint(0, lDescription - 1)]
        Link = Links[randint(0, lLinks - 1)]
        photo_name = str(randint(1, MAX_PHOTOS))
        pngjpg_randomizer = randint(0, 1)
        file_path = 'photos/photo' + photo_name + ['.png', '.jpg'][pngjpg_randomizer]

        pinterest.upload_pin(board_id = '1128433319072266302', image_file = file_path, description = Description + ' ' + ' '.join(Hashtags), title = Title, link = Link)

        print(str(count)+'. Posted photo: ' + photo_name + '.')
        os.remove(file_path)
    except:
        continue
    count += 1
    time.sleep(randint(2400, 3600))
