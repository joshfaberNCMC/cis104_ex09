def fileOpen():
    while True:
        fName = input("Enter file name, or type 'Exit Program': ")
        if fName == 'Exit Program':
            quit()
        else:
            try:
                fHand = open(fName)
                return fHand
            except:
                print('Invalid file name:', fName)

fHand = fileOpen()
di = dict()
import re

for line in fHand:
    line = re.split('[- , . ! : ; / () <> \[ \]]', line)
    for word in line:
        if word not in di:
            di[word] = 1
        else:
            di[word] = di[word] + 1    

while True:
    search = input('Enter a word, or type \'Exit Program\' (Input is case sensitive): ')
    if search == 'Exit Program':
        quit()
    elif search in di:
        print(True)
        print('File does contain:', search)
        print('Occurrences:', di[search])
    else:
        print(False)
        print('File does not contain:', search)