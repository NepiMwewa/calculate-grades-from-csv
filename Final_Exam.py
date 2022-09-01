#
#  Program  :   Final Exam Program
#  Author   :   Alexander Harmon
#  Date     :   5/5/2021
#  Purpose  :   Grabs student data from a csv file, reads and calculates their
#               grade. Then prints their grades in a formatted manner
#

#import the csv reader to read the csv file.
from csv import reader

#main function
def main():
    #open the contents of the csv file to read, and skip the first header line
    infile = open("FinalExamData.csv", "r")
    csvReader = reader(infile)
    next(csvReader)
    
    #Call the print header function to print the headings for the print output
    printHeader()
    
    #step through the csv file and grab the data from each row
    for row in csvReader :
        #call calcPointTotal to calculate the total number of points earned
        points = calcPointTotal(row)
        #call calcPercentOfGrade with "points" to find the grade percent the
        #student earned in the class
        percentage = calcPercentOfGrade(points)
        #finally, use the percentage to call calcLetterGrade to get the final 
        #grade letter of the student
        letter = calcLetterGrade(percentage)
        
        #Call printStudentReport to print to the user all of the student's
        #names, grades for each assignments and exam, grade percentage and  
        #the grade letter.
        printStudentReport((row[0] + " " + row[1]), row[2], row[3], row[4], row[5], percentage, letter)
        
    #close the csv file
    infile.close()

#calculates the total amount of points the student earned and returns the
#total amount of points
def calcPointTotal(student):
    return (int(student[2]) + int(student[3]) + int(student[4]) + 
            int(student[5]))

#calculates the total percentate of points the student earned in the class and
#returns the percentage
def calcPercentOfGrade(pointTotal):
    return (pointTotal / 250) * 100

#calculates the letter the student recieved. return the letter
def calcLetterGrade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

#formats and prints the header for the print output
def printHeader():
    header = ["Name","Assign 1","Assign 2","Assign 3","Exam","Percent","Letter"]
    print("%-20s" % header[0] + "%-10s" % header[1] + "%-10s" % header[2] + "%-10s" % 
          header[3] + "%-6s" % header[4] + "%-10s" % header[5] + header[6])

#formates and prints the output of the student's names, scores percentage
# and letter
def printStudentReport(name, assign1, assign2, assign3, exam, percentage,
                       letter):
    print("%-20s" % name + "%8s" % assign1 + "%10s" % assign2 + "%10s" % assign3
          + "%6s" % exam + "%8.0f%%" % percentage + "%9s" % letter)

#call main
main()