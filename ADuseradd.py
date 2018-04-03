
"""
Script to allow adding of users in a linux environment to
an AD via the useradd command
author: Shane Ogden
"""
import os

def main():
    path = raw_input("Enter user file path: ")
    file = open(path)

    os.system("dos2unix '" + path + "'")

    groups = []
    for line in file:
        command = 'useradd'
        line = line.replace('"', '')
        line = line.replace('\n', '')
	line = line.replace(' ', '')
	line = line.replace('\r', '')
        x = line.split(',')
        print(x)
        username = ''
	contained = False
	for y in groups:
		if y == x[4]:
			contained = True
        if contained == False:
            groups.append(x[4])
            os.system("groupadd " + x[4].lower())
        command = command + ' -g ' + x[4]
        if x[4] == 'Engineering':
            command = command + ' -s /bin/csh'
        else:
            command = command + ' -s /bin/bash'

        username = x[1][1] + x[0]
        final = command + ' -m -d ' + '/home/' + x[4] + '/' + username + ' ' + username
        final = final.lower()
	print(final)
        os.system(final)



if __name__ == '__main__':
    main()
