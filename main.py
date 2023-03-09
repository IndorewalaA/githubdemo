def encode(password):
    encoded = ""
    for digit in range(len(password)):
        endig = int(password[digit]) + 3
        encoded += str(endig)
    return encoded

def decode(password):
    encoded = ""
    for digit in range(len(password)):
        endig = int(password[digit]) - 3
        encoded += str(endig)
    return encoded
def main():
    startDeterminer = True
    encodedPass = ""
    password = ""
    while startDeterminer:
        print("Menu", "-------------", "1. Encode", "2. Decode", "3. Quit", sep="\n")
        print()
        userChoice = int(input("Please enter an option: "))
        if userChoice == 1:
            password = input("Please enter your password to encode: ")
            encodedPass = encode(password)
            print("Your password has been encoded and stored! ")
            print()
        elif userChoice == 2:
            decodedPass = decode(password)
            print(f"The encoded password is {encodedPass}, and the original password is {decodedPass}. ")
        elif userChoice == 3:
            break

if __name__ == '__main__':
    main()

