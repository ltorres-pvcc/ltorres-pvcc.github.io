#Name: Leo Torres
#Program Purpose: This program reads a comma-delinited data file into a LIST of smaller lists.
#   The data for each student is appended to a list with six data fields:
#   Position 0 is the last name, 1 is the first name, 2 is HW, 3 is midterm exam, & 4 is the final exam
#   The group of student lists in the larger "outer" list
#   The resulting report is sent to an output file 

import datetime
stu = []
student_file = "students.csv"
out_file = "stu_report.txt"

def main(): 
    read_data_file()
    calculate_grades()
    create_report_file()

def read_data_file():
    datafile = open(student_file,"r") #The "r" indicates this is a READ File
    lines = datafile.readlines() #Read the entire file into a variable called lines
    for i in lines:
        stu.append (i.split(",")) #Split the data by commas and add each section to the list
    datafile.close()

def calculate_grades():
    global average, totA, totB, totC, totD, totF
    totA = totB = totC = totD = totF = 0
    gradestotal = 0

    for i in range(len(stu)):
        hw = int(stu[i][2]) #Last name in pos. 0, first name in pos. 1, so hw is pos. 2
        midex =  int(stu[i][3]) #Midterm exam is in position 3
        (stu[i][4]) = (stu[i][4])[:-1] #Remove the \n from the final exam string (end of the input line)
        finex = int(stu[i][4]) #Final exam is in position 4
        sum_grades = hw + midex + finex
        finalgr = sum_grades/3
        gradestotal += finalgr #Add the grade to the total for calculation the average
        stu[i].append(finalgr)
        if finalgr >= 90:
            lettergrade = 'A'
            totA += 1
        elif finalgr >= 80:
            lettergrade = 'B'
            totB += 1
        elif finalgr >= 70:
            lettergrade = 'C'
            totC += 1
        elif finalgr >= 60:
            lettergrade = 'D'
            totD += 1
        else:
            lettergrade = 'F'
            totF += 1
        stu[i].append(lettergrade)
    average = gradestotal/len(stu)

def create_report_file():
    line = "\n*******************************************"
    repfile = open(out_file,"w")
    repfile.write("\n************CSC 230 Grade Report***********")
    repfile.write("\nReport Date/Time        : " + str(datetime.datetime.now()))
    repfile.write("\nTotal number of students: " + str(len(stu)))
    repfile.write("\nAverage student grade   : " + format(average, '5,.2f'))
    repfile.write("\nTotal number of A grades: " + str(totA))
    repfile.write("\nTotal number of B grades: " + str(totB))
    repfile.write("\nTotal number of C grades: " + str(totC))
    repfile.write("\nTotal number of D grades: " + str(totD))
    repfile.write("\nTotal number of F grades: " + str(totF))
    repfile.write(line)
    repfile.write("\nNAME                HW\tMID\tFIN\tFINAL GRADE")
    for i in range(len(stu)):
        sname = '{0:<18}'.format(stu[i][0]+', '+stu[i][1])
        hw = str(stu[i][2])
        midex = str(stu[i][3])
        finex = str(stu[i][4])
        fingrade = format(stu[i][5],'6,.2f')
        repfile.write("\n"+ sname + "\t" + hw + "\t" + midex + "\t" + finex + "\t" + " " + " " + " " + stu[i][6])
    repfile.write(line)
    repfile.close()
    print("open this file to view the Grades Report: " + out_file)

main()