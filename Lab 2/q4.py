Name=input("Enter the Name of the student :")
Roll_no=int(input("Enter the Roll no of the student :"))
marks=int(input("Enter the marks of the student :"))

if(marks>=90):
    print("Grade point is : ",10)
    print("Outstanding")
elif(marks>=80 and marks<90):
    print("Grade point is : ",9)
    print("Very Good")
elif(marks>=70 and marks<80):
    print("Grade point is : ",8)
    print("Good")
elif(marks>=60 and marks<70):
    print("Grade point is : ",7)
    print("Average")
elif(marks>=50 and marks<60):
    print("Grade point is : ",6)
    print("Pass")
elif(marks<50):
    print("Grade point is : ",0)
    print("Fail")