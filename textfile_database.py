# from student import Student


def viewAllRecords():
    with open("student_records.txt", "r") as f:
        lines = f.readlines()

        if len(lines) == 0 :
            print("Student records currently empty ...")
        else :
            print('====================================\n')
            print('\tStudent Records\n')

            for line in lines:
                data = line.rsplit(",")
                name = data[0].rsplit("=")[1]
                course = data[1].rsplit("=")[1]
                year = data[2].rsplit("=")[1]
                address = data[3].rsplit("=")[1]

                print(f"Name: {name} Course: {course} Year: {year} Address: {address}")

            print('====================================\n')

def createRecord(newRecord):
    appendToFile(newRecord)
    

def searchRecord(name):
    with open("student_records.txt", "r") as f:
        lines = f.readlines()
        if len(lines) == 0 :
            print("Student records currently empty ...")
        else :
            names = getStudentNames()
            index = names.index(name)
            data = lines[index].rsplit(",")
            name = data[0].rsplit("=")[1]
            course = data[1].rsplit("=")[1]
            year = data[2].rsplit("=")[1]
            address = data[3].rsplit("=")[1]
            print(f"Name: {name} Course: {course} Year: {year} Address: {address}")

def appendToFile(newRecord):
    with open("student_records.txt", "a+") as f:
        f.write(f'name={newRecord.studentName},course={newRecord.studentCourse},year={newRecord.studentYear},address={newRecord.studentAddress}\n')

def writeToFile(lines):
    with open("student_records.txt", "w") as f:
        f.writelines(lines)
    

def deleteStudentRecord(name):
    with open("student_records.txt", "r") as f:
        lines = f.readlines()
        names = getStudentNames()
        index = names.index(name)
        lines[index] = ""
        writeToFile(lines)

def getStudentNames():
    names = []
    with open("student_records.txt", "r") as f:
        lines = f.readlines()
        if len(lines) == 0 :
            print("Student records currently empty ...")
        else :
            for line in lines:
                data = line.rsplit(",")
                name = data[0].rsplit("=")[1]
                names.append(name)
    return names

# def main():
    # viewAllRecords()
    # searchRecord("janrelle lubiano")
    # newRecord = Student("mark", "BSCS", 3, "ampayon butuan city")
    # appendToFile(newRecord)
    # deleteStudentRecord("edwin")


