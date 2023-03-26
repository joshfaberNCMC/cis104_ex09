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

for line in fHand:
    if line.startswith('From '):
        line = line.split()
        email = line[1]
        domain = email.split('@')[1]
        di[domain] = di.get(domain, 0) + 1
        
print(di)