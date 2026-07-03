#write a program which accepts one number and prints multiplication table of that number
def MultiplicationTable(no):
    table = ""
    tableMultValues = [1,2,3,4,5,6,7,8,9,10]
    for i in tableMultValues:
        table = table + str(i*no) + " "
    print("Table of",no,"is -",table)

def main():
    if __name__ == "__main__":
        no = int(input("Enter a number :"))
        MultiplicationTable(no)

main()
