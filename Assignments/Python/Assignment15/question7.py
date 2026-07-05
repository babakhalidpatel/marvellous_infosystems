#write a lambda function using filter() which accepts a list of strings and return list of strings having length greater thean 5


lengthOfString = lambda length: len(length) > 5


def main():
    if __name__ == "__main__":
        array = ["abc","abcdefg", "jijklmn","pql","stuvwxyz"]
        res = list(filter(lengthOfString, array))
        print("Greater than 5 length list is :",res)
main()