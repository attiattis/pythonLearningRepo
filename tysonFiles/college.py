# Information about college
campuses = ('Bengaluru Central Campus', 'Bengaluru Bannerghatta Road Campus', 'Bengaluru Kengeri Campus', 'Delhi NCR Off Campus', 'Pune Lavasa Off Campus')
diploma = ('Diploma in English', 'Diploma in English and Arts')
ug_courses = ('B.A. Communication and Media, English and Psychology', 'B.A. Journalism, English and Psychology', 'B.A. Psychology, Sociology and English', 'B.A. Performing Arts, English and Psychology', 'B.A. Theatre Studies, English and Psychology', 'B.A. English Honours')
cert_courses = ('Certification Course in English', 'Certification Course in Arts')
output = []

def validateAge(age):
    '''This method is to validate the age'''
    if age < 17:
        print("Sorry. You are not eligible to enroll for a course.")
        return False
    else:
        return True


# collecting data
def main():
    name = input("Enter your name: ")
    try:
        age  = int(input("Enter your age: "))
    except:
        print("Invalid age")
        return
    if validateAge(age):
        # age is valid. So read remaining part
        # Course details
        while True:      
            print("Following courses are available : ")
            print("1. Bachelor's degree")
            print("2. Diploma")
            print("3. Certification")
            print("4. To exit")
            option = int(input("Enter your choice (1/2/3/4) : "))
            if option >= 1 and option <= 4:
                break
            else:
                print("Invalid option.Please enter again.")
        
        # Selecting the course user wants
        print("The following courses are available : ")
        if option == 1:
            for i in range(len(ug_courses)):
                print(i+1,"." , ug_courses[i])
            select = int(input("Enter your option : ")) 
            output.append(ug_courses[select-1])
        elif option == 2:
            for i in range(len(diploma)):
                print(i+1,"." , diploma[i])
            dip = int(input("Enter your option : ")) 
            output.append(diploma[dip-1])
        elif option == 3:
            for i in range(len(cert_courses)):
                print(i+1,"." , cert_courses[i])
            cert = int(input("Enter your option : ")) 
            output.append(cert_courses[cert-1])
        elif option == 4:
            return
        # selecting the campus
        print("Available campuses are : ")
        for i in range(len(campuses)):
            print(i+1,"." , campuses[i])
        campusOption = int(input("Enter your option : ")) 
        output.append(campuses[campusOption-1])

        # Display the details
        print(f"Name    :  {name} \nAge     :  {age} \nCourse  : {output[0]} \nCampus  : {output[1]}") 
        print("You are selected for this course")
    else:
        return False

# calling the main function   
main()











    
      

        
    
    
