#write a program which accepts one character and checks whether it is vowel or consonant.

def IsitVowel(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print("It is Vowel")
    else:
        print("It is Consonant")

def main():
    if __name__ == "__main__":
        IsitVowel(str(input("Enter a character :")))

main()