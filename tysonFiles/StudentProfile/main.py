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


# Helper function to get students list from database
def getStudentsList():
    # Check if file doesn't exist, then create it
    if not os.path.exists(studentsDatabaseFileName):
        open(studentsDatabaseFileName, 'w').close()

    with open(studentsDatabaseFileName, "r") as file:
        studentList = []
        
        for line in file:
            record = list(map(str, line.split(",")))
            if record[-1][-1] == "\n":
                record[-1] = record[-1][:-1]
            
            if record != "\n":
                studentList.append(record)
        return studentList

def displayMenu():
    print("--------------------------------------")
    print(" Welcome to Student Management System")
    print("---------------------------------------")
    print("1. Add new student")
    print("2. Delete students' records")
    print("3. Modify students' details")
    print("4. Recalcualte E_x_a_m score")
    print("5. Print Student list")
    print("6. Quit")

   
def addStudent():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    
    studentsRecords = getStudentsList()
    studentData = []

    for field in studentsFields:
        value = input("Enter " + field + ": ")
        studentData.append(value)
    
    for student in studentsRecords:
        if studentData[0] == student[0] and studentData[2] == student[2]:
            print("The student record is already in the database! Zero records added.")
            input("Press any key to continue")
            return
    
    # recalculate the total score of the student
    recalculateScoreOfAStudent(studentData)
    # Add to the list
    studentsRecords.append(studentData)    
    
    # Save the database with the new record
    saveStudentsToDatabase(studentsRecords)
    
def deleteStudent():
    print("-------------------------")
    print("Delete Student Information")
    print("-------------------------")
    
    # All students data
    studentsRecords = getStudentsList()
    
    # Results from users input
    results = []
    indexes = [] # indexes of the results in the database

    print("Select an option:")
    print("a. Retrieve information by ID")
    print("c. Back")
    userChoice = input("Enter your option: ").lower()
    
    while userChoice != "a" and userChoice != "b" and userChoice != "c":
        print("Please select a valid option!")
        userChoice = input("Enter your option: ").lower()

    # if user selected By ID
    if userChoice == "a":
        studentId = input("Enter student ID: ")
        for i, student in enumerate(studentsRecords):
            if student[0] == studentId:
                results.append(student)
                indexes.append(i)
    

    # if user selected to go back
    elif userChoice == "c":
        return

    # In case if no records matched the entered criteria
    if len(results) == 0:
        print("No records were found in the database with the entered criteria!")
        return pressAnyKey()

    printStudentsList(results)

    selectedStudent = input("Enter student number: ")
    
    while not selectedStudent in list(map(str, range(1, len(results)+1))):
        print("Selected number not in range!")
        selectedStudent = input("Enter student number: ")
        
    # Delete from the list
    del studentsRecords[indexes[int(selectedStudent) - 1]]

    # Save the database without the deleted record
    saveStudentsToDatabase(studentsRecords)
    
def modifyStudentDetails():
    print("-------------------------")
    print("Modify Student Information")
    print("-------------------------")
    
    # All students data
    studentsRecords = getStudentsList()
    
    # Results from users input
    results = []
    indexes = [] # indexes of the results in the database

    print("Select an option:")
    print("a. Retrieve information by ID")
    print("c. Back")
    userChoice = input("Enter your option: ")
    
    while userChoice != "a" and userChoice != "b" and userChoice != "c":
        print("Please select a valid option!")
        userChoice = input("Enter your option: ").lower()

    # if user selected By ID
    if userChoice == "a":
        studentId = input("Enter student ID: ")
        for i, student in enumerate(studentsRecords):
            if student[0] == studentId:
                results.append(student)
                indexes.append(i)
    
    
    # if user selected to go back
    elif userChoice == "c":
        return

    # In case if no records matched the entered criteria
    if len(results) == 0:
        print("No records were found in the database with the entered criteria!")
        return pressAnyKey()

    printStudentsList(results)

    selectedStudent = input("Enter student number: ")
    
    while not selectedStudent in list(map(str, range(1, len(results)+1))):
        print("Selected number not in range!")
        selectedStudent = input("Enter student number: ")

    print("What do you want to modify?")
    print("a. Absences")
    print("b. E_x_a_ms 1")
    print("c. E_x_a_ms 2")
    
    userChoice = input("Enter your option: ").lower()
    
    while userChoice != "a" and userChoice != "b" and userChoice != "c":
        print("Please select a valid option!")
        userChoice = input("Enter your option: ").lower()

    # if user selected Absences
    if userChoice == "a":
        newAbsences = input("Enter new student absences: ")
        # Update absences with the entered value
        studentsRecords[indexes[int(selectedStudent) - 1]][2] = newAbsences
        
    # if user selected E_x_a_ms 1
    elif userChoice == "b":
        newE_x_a_m1 = input("Enter new student E_x_a_ms 1 grade: ")
        # Update E_x_a_ms 1 grade with the entered value
        studentsRecords[indexes[int(selectedStudent) - 1]][3] = newE_x_a_m1
        # change the total score
        studentsRecords[indexes[int(selectedStudent) - 1]][4] = int(newE_x_a_m1) + int(studentsRecords[indexes[int(selectedStudent) - 1]][4])


    # if user selected E_x_a_ms 2
    elif userChoice == "c":
        newE_x_a_m2 = input("Enter new student E_x_a_ms 2 grade: ")
        # Update E_x_a_ms 2 grade with the entered value
        studentsRecords[indexes[int(selectedStudent) - 1]][4] = newE_x_a_m2
        # change the total score
        studentsRecords[indexes[int(selectedStudent) - 1]][5] = int(newE_x_a_m2) + int(studentsRecords[indexes[int(selectedStudent) - 1]][5])


    
    # Save the database after the update
    saveStudentsToDatabase(studentsRecords)

def recalculateScoreOfAStudent(student):
    # add the two scored and append it to the last part
    student[5] = int(student[3])+int(student[4])
    return student
def recalculateE_x_a_mScoresOfAllStudents():
    studentsRecords=[]
    for student in getStudentsList():
        studentsRecords.append(recalculateScoreOfAStudent(student))

    # Save the database after the update
    saveStudentsToDatabase(studentsRecords)
while True:
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