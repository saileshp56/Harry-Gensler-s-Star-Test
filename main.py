def occurrenceCheck():  # only checks if letter appears >2, not < 2
    lettersCopy = letters.copy()

    for item in lettersCopy:
        temp = 0
        for element in letters:
            if (item == element and item.isupper()):
                temp += 1

        if temp > 2:
            return False
    return True


def finalOccurrenceCheck():
    lettersCopy = letters.copy()

    for item in lettersCopy:
        temp = 0
        for element in letters:
            if (item == element and item.isupper()):
                temp += 1
        if temp < 2:

            return False

    return True


def starCount():
    starsCopy = stars.copy()

    for item in starsCopy:
        temp = 0
        for element in stars:
            if (item == element and item.isupper()):
                temp += 1

        if temp > 1:
            return False
    return True


def starCountTwo():
    starsCopy = stars.copy()
    for item in letters:
        if item.isupper() and item not in starsCopy:
            return False
    return True


def conclusionCheck(splitPremise):
    global right_side
    global in_progress
    in_progress = False
    splitPremise.pop(0)
    if (splitPremise[0].islower() and len(splitPremise[0]) == 1):
        lowerConclusionCheck(splitPremise)

    if (splitPremise[0].lower() == 'no'):
        letters.append(splitPremise[1])
        letters.append(splitPremise[3])



    elif (splitPremise[0].lower() == 'all'):
        stars.append(splitPremise[3])
        letters.append(splitPremise[1])
        letters.append(splitPremise[3])

        right_side += 1

    elif (splitPremise[0].lower() == 'some' and splitPremise[3].lower() == 'not'):

        stars.append(splitPremise[1])
        letters.append(splitPremise[1])
        letters.append(splitPremise[4])
        return

    elif (splitPremise[0].lower() == 'some' and splitPremise[2].lower() == 'is' and splitPremise[
        3].lower() != 'not'):  # some A is B
        stars.append(splitPremise[1])
        stars.append(splitPremise[3])
        letters.append(splitPremise[1])
        letters.append(splitPremise[3])
        right_side += 1


def lowerConclusionCheck(splitPremise):
    global right_side
    global in_progress
    in_progress = False

    # t is not b/B
    if (splitPremise[1].lower() == 'is' and splitPremise[2].lower() == 'not'):

        letters.append(splitPremise[3])

    else:  # t is b/B

        stars.append(splitPremise[2])

        letters.append(splitPremise[2])

        right_side += 1


def lowerCheck(splitPremise):
    global right_side
    if (splitPremise[1].lower() == 'is' and splitPremise[2].lower() == 'not'):

        letters.append(splitPremise[3])
        stars.append(splitPremise[3])

        right_side += 1

    else:  # a is b/B

        letters.append(splitPremise[2])


def starCheck(premise):
    global right_side

    splitPremise = premise.split()

    if (splitPremise[0] == '*'):
        conclusionCheck(splitPremise)

    elif splitPremise[1].islower():
        lowerCheck(splitPremise)


    elif (splitPremise[0].lower() == 'no'):

        stars.append(splitPremise[1])
        stars.append(splitPremise[3])
        letters.append(splitPremise[1])
        letters.append(splitPremise[3])

        right_side += 1


    elif (splitPremise[0].lower() == 'all'):
        stars.append(splitPremise[1])
        letters.append(splitPremise[1])
        letters.append(splitPremise[3])

    elif (splitPremise[0].lower() == 'some' and splitPremise[3].lower() == 'not'):
        stars.append(splitPremise[4])
        letters.append(splitPremise[1])
        letters.append(splitPremise[4])

        right_side += 1
    else:  # some A is B
        letters.append(splitPremise[1])
        letters.append(splitPremise[3])


letters = []
stars = []
right_side = 0
in_progress = True

print(
    "Enter a premise and only capitalize the propositions (if needed). For conclusion start the sentence with * and a space. To quit at anytime, enter quit\nSample Input: some A is not B\n")

while True:
    premise = input("Enter a premise or conclusion:\n")
    if premise.upper() == "QUIT":
        print("No issues with validity thus far")
        break
    starCheck(premise)

    if (not occurrenceCheck()):
        print("Invalid because of too many occurrences of a letter(s)")
        in_progress = False
    if (right_side > 1):
        print("Invalid because of right side having: 2 stars")
        in_progress = False
    if (not starCount()):
        print("Invalid because a letter has too many stars")
        in_progress = False
    if (in_progress == False and not starCountTwo()):
        print("Invalid because a letter has too few stars")
        in_progress = False

    if (in_progress == False):
        if (not finalOccurrenceCheck()):
            print("Invalid because of too few occurrences of a letter(s)")  # MUST CHECK TO SEE IF THIS WORKS!!!
            print("---------------------------------")
        else:
            print("No problems were found. It is valid")
            print("---------------------------------")

        letters.clear()
        stars.clear()
        right_side = 0
        in_progress = True
