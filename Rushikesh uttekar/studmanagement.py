

students={}

while True:
        print("1.Add or Update student info\n2.Display student information\n3.exit")
        choice = int(input("Enter your choice: "))
        if choice==1:
                name=input("Enter student name: ")
                age =int(input("Enter student age: "))
                marks =int(input("Enter marks out of 100: "))
                if name in students:
                        print(f"\nUpdating data for {name}\n")
                else:
                        print(f"\nAdding new student {name}\n")
                        students[name]={"age":age,"Marks":marks}
        elif choice==2:
                for name,details in students.items():
                        print(f"Name:{name},Age:{details['age']},Marks:{details['Marks']}\n")
        elif choice==3:
                break
        else:
                print("Invalid option")
