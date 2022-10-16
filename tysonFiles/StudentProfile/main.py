import os

studentsFields = ['ID', 'Name', 'Absences', 'E_x_a_ms 1 Grade', 'E_x_a_ms 2 Grade', 'Total Marks']
studentsDatabaseFileName = 'student.info'
# Helper function to show 'Press any key to continue'
def pressAnyKey():
    input("Press any key to continue")
    return

# Helper function to print students list
def printStudentsList(studentList):
    print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format('', *studentsFields))

    index = 1
    for student in studentList:
        print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format((str(index)+"."), *student))
        index += 1

    return

# Helper function to save students list to database
def saveStudentsToDatabase(studentList):
    with open(studentsDatabaseFileName, "w+") as file:        
        for student in studentList:
            file.write(','.join(map(str, student)) + '\n')

    print("Student data saved successfully!")
    return pressAnyKey()

# define the menu methods
def main():
    while True:
        # TODO : need to define these methods
        displayMenu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            addStudent()
        elif choice == '2':
            deleteStudent()
        elif choice == '3':
            modifyStudentDetails()
        elif choice == '4':
            recalculateE_x_a_mScoresOfAllStudents()
        elif choice == '5':
            printStudentsList(getStudentsList())
        elif choice == '6':
            break
        else:
            print("Not valid choice!")
main()