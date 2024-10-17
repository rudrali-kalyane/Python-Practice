
student_data = {"Rudrali":{"age":18,"marks":90},
                "Anushka":{"age":19,"marks":90},
                "Tanishka":{"age":17,"marks":80},
                "Raksha":{"age":16,"marks":70}}
c=0
while c!=4:
    print("Menu:")
    print("choice 1 :Update existing student data")
    print("choice 2 :Add new student data")
    print("choice 3 :Display student data")
    print("choice 4 :Exit")
    print("\n\n")

    c = int(input("Enter your choice : "))

    if c == 1 :
        key = (input("Enter the name of student to upadate data :"))
        key = key.capitalize()
        age = int(input("Enter new age : "))
        marks = int(input("Enter new marks : "))

        student_data[key]["age"]=age
        student_data[key]["marks"]=marks
        print("\n\n")
        # print(student_data)

    elif c == 2:
        key = (input("Enter the name of student :"))
        key = key.capitalize()
        age = int(input("Enter age : "))
        marks = int(input("Enter  marks : "))

        student_data.update({key:{"age":age,"marks":marks}})
        print("\n\n")

        # print(student_data)

    elif c == 3 :
        for i,j in student_data.items():
            print(i,j)

        print("\n\n")

    


