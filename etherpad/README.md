# Rice software carpentry workshop
To grab the workshop data:
```bash
$ cd ~/Desktop
$ mkdir workshop
$ cd workshop
$ git clone https://github.com/wrightaprilm/rice.git
```

You can follow along on your laptop, or, if you have a preference for CLEAR, ssh to ssh.clear.rice.edu and do the work there (you can create the workshop directory in your home directory instead of your Desktop if you prefer.)

## Shell basics:
* whoami
* pwd
* cd
* ls
* ls -F    or  -a    or -Fa   (directory)
* mkdir
* nano filename
* rm
* mv
* cp

## Python Intro
Useful functions
* type
* print
* str
* int

http://www.codeacademy.com/en/tracks/python

### Operator Precedence:
http://www.mathcs.emory.edu/~valerie/courses/fall10/155/resources/op_precedence.html


### What is #! at the beginning of the file?
Location to where python is located
Find it using "which" command
```
$ which python
/usr/bin/python
```
and put this location in your PATH
```
$echo whoami
$export $PATH=$PATH:/usr/bin
```

A useful way to look at quotes and strings in python is to avoid having to 'escape' quotes.
i.e. These are equivalent:
```python
string='Don\'t forget to escape the apostrophe here.'
string="Don't forget to escape the apostrophe here."
```
but one is easier to read.
This also works:
```python
string="""You can use 'any' "old" quotes here."""
```

### Condition Flow Challenge

Download the "All Earthquakes"  CSV from http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php

Write a short python code to read this file and print lines from this file using "for" statement. Assign the rows in this file to a list variable. 

Can you improve this code?

```python
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
```
    

### Importing modules in python
Modules are add-on libraries that enhance the functionality of the basic Python offerings
The most basic way to bring in the functions of a module is to use import module_name


## Pandas:
(Start python from the data-crunching directory of the git repo)
import pandas
species = pandas.import_csv('species.csv')

Tip: Use the python "dir" command to 'look around' a module or any other object that has methods (functions) built-in... 
For example:
```python
dir(pandas) # list all methods you can call from pandas (like pandas.read_csv)
```
or
```python
dir(species) #  list all the methods that belong to a 'core.frame.DataFrame' object from pandas
```
Even better, use the "help" function to read the online help for a specific data object or module

### Handling Excel data in pandas:
```python
import pandas

surveyfile = pandas.ExcelFile("surveys.xlsx")
surveyfile.sheet_names  # to list sheet names, so you may parse the right sheet
[u'Sheet1']
surveys=surveyfile.parse("Sheet1")
```
And now surveys is a data frame of sheet1 from surveys.xlsx


