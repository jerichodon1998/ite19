from student import Student
from textfile_database import createRecord, getStudentNames, deleteStudentRecord, searchRecord, viewAllRecords

def create():
    viewAllRecords()

    names = getStudentNames()
    name = ""
    course = ""
    year = int
    address = ""
    loop = True
    while(loop):
        inputValue = input("Enter Student Name: ")
        if inputValue in names:
            print("Name already exist")
        else:
            name = inputValue
            loop = False
            
    print('====================================\n')
    course = input("Enter Student Course: ")
    print('====================================\n')
    year = input("Enter Student Year: ")
    print('====================================\n')
    address = input("Enter Student Address: ")
    print('====================================\n')

    newRecord = Student(name, course, year, address)
    createRecord(newRecord)

def search():
    names = getStudentNames()

    loop = True
    while(loop):
        name = input("Enter Student Name to be Searched: ")
        print('====================================\n')

        if name in names:
            searchRecord(name)
            print('====================================\n')
            loop = False
        else:
            print(f"{name} does not exist")
            print('====================================\n')

    

def display():
    viewAllRecords()

def delete():
    viewAllRecords()
    names = getStudentNames()

    loop = True
    while(loop):
        name = input("Enter Student Name to be Deleted: ")
        print('====================================\n')

        if name in names:
            deleteStudentRecord(name)
            print("Student Deleted")
            print('====================================\n')
            loop = False
        else:
            print(f"{name} does not exist")
            print('====================================\n')


def main():
    loop = True
    while(loop):
        print("Enter 'A' to create")
        print("Enter 'B' to search")
        print("Enter 'C' to display")
        print("Enter 'D' to delete")
        print("Enter 'E' to exit")

        choice = input().upper()

        if choice == "A":
            create()
        elif choice == "B":
            search()
        elif choice == "C":
            display()
        elif choice == "D":
            delete()
        elif choice == "E":
            loop = False

if __name__ == '__main__':
    main()
