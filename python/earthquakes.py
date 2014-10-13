#!/usr/bin/python

quakefile=open("all_hour.csv", 'r')

line_list=[]

for line in quakefile.readlines():
#    print line
    line_list.append((line).strip().split(','))

#Print all list
#print line_list

#Print length of list
print ("Number of lines in file: %s " % str(len(line_list)))

#Print second line
#print line_list[2]

#If state is Alaska print quakes

for row in line_list:
    if "Alaska" in row[14]:
       print ("Time of occurrence: %s" % row[0])
       print ("Latitude: %s" % row[1])
       print ("Longitude: %s" % row[2])
       # or all in one line like this
       print ("An earthquake has occurred in Alaska at %s at Latitude: %s and Longitude: %s" % (row[0],row[1],row[2]))

