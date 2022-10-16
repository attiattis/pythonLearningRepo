def main():
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
main()