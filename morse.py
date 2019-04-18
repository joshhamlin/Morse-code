# convert strings to morse code
def toMorse(Main):
    MorseFinAry = []
    Tarry = list(Main)
    for char in Tarry:
        if char.lower() == "a":
            MorseFinAry.append(".- ")
        elif char.lower() == "b":
            MorseFinAry.append("-... ")
        elif char.lower() == "c":
            MorseFinAry.append("-.-. ")
        elif char.lower() == 'd':
            MorseFinAry.append("-.. ")
        elif char.lower() == 'e':
            MorseFinAry.append(". ")
        elif char.lower() == 'f':
            MorseFinAry.append("..-. ")
        elif char.lower() == 'g':
            MorseFinAry.append("--. ")
        elif char.lower() == 'h':
            MorseFinAry.append(".... ")
        elif char.lower() == 'i':
            MorseFinAry.append(".. ")
        elif char.lower() == 'j':
            MorseFinAry.append(".--- ")
        elif char.lower() == 'k':
            MorseFinAry.append("-.- ")
        elif char.lower() == 'l':
            MorseFinAry.append(".-.. ")
        elif char.lower() == 'm':
            MorseFinAry.append("-- ")
        elif char.lower() == 'n':
            MorseFinAry.append("-. ")
        elif char.lower() == 'o':
            MorseFinAry.append("--- ")
        elif char.lower() == 'p':
            MorseFinAry.append(".--. ")
        elif char.lower() == 'q':
            MorseFinAry.append("--.- ")
        elif char.lower() == 'r':
            MorseFinAry.append(".-. ")
        elif char.lower() == 's':
            MorseFinAry.append("... ")
        elif char.lower() == 't':
            MorseFinAry.append("- ")
        elif char.lower() == 'u':
            MorseFinAry.append("..- ")
        elif char.lower() == 'v':
            MorseFinAry.append("...- ")
        elif char.lower() == 'w':
            MorseFinAry.append(".-- ")
        elif char.lower() == 'x':
            MorseFinAry.append("-..- ")
        elif char.lower() == 'y': #and z
            MorseFinAry.append("-.-- ")
        elif char.lower() == 'z':
            MorseFinAry.append("--.. ")
        elif char == "1":
            MorseFinAry.append(".---- ")
        elif char == "2":
            MorseFinAry.append("..--- ")
        elif char == "3":
            MorseFinAry.append("...-- ")
        elif char == '4':
            MorseFinAry.append("....- ")
        elif char == '5':
            MorseFinAry.append("..... ")
        elif char == '6':
            MorseFinAry.append("-.... ")
        elif char == '7':
            MorseFinAry.append("--... ")
        elif char == '8':
            MorseFinAry.append("---.. ")
        elif char == '9':
            MorseFinAry.append("----. ")
        elif char == '0':
            MorseFinAry.append("----- ")
        elif char == '.':
            MorseFinAry.append(".-.-.- ")
        elif char == ',':
            MorseFinAry.append("--..-- ")
        elif char == "?":
            MorseFinAry.append("..--..")
        elif char == '/':
            MorseFinAry.append("-..-.")
        elif char == '@':
            MorseFinAry.append(".--.-. ")
        elif char == " ":
            MorseFinAry.append("| ")
        else:
            print("char not valid")
    return MorseFinAry

while True:
    print("Type [help] if you are unsure how to use this\n")
    InMain = input("Type a string or morse code -->")
    if InMain == "[help]":
        print("When typing in strings just type as you normally would\n")
        print("Case will not effect the out put because mores code does not account for case\n")
        print("example --> Type a string or morse code -->I would like to read this in morse code  \n")
        print("you can use the following in your sting |a - z|, |0 - 9|, '.', ',', '?', '/' and '@' ")



    #works good converting to morse code

    Pans = toMorse(InMain)
    print(''.join(Pans))

    #works we just need to handle funny input and touch up UI
