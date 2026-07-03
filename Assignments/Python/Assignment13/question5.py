#write a program which accept marks and display grade.

def DisplayGrade(marks):
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First class")
    elif marks >= 50:
        print("Second class")
    elif marks < 50:
        print("Fail")

def main():
    if __name__ == "__main__":
        DisplayGrade(int(input("Enter marks :")))

main()