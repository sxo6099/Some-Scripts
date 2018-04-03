"""
File that creates an access log readable by management based
on accesses to your webserver.
author: Shane Ogden
"""
import os
import string

def main():
    path = raw_input("Enter file path: ")
    file = open(path)

    start = ''
    end = ''
    counter = 0

    for line in file:
        counter += 1
        x = line.split()
        if start == '':
            start = string.lstrip(x[3], '[')
        elif (end != string.lstrip(x[3], '[')):
            end = string.lstrip(x[3], '[')

    f = open("managereport.txt", "w+")
    f.write("REPORT FOR LOCALHOST APACHE WEBSERVER by S. OGDEN\n")
    f.write("=================================================\n")
    f.write("During the period from " + start + " to " + end + " there were " + str(counter) + " hits!")



if __name__ == '__main__':
    main()
