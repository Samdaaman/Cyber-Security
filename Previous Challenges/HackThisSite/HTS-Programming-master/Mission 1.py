import sys
import math
import itertools


def getwordlist():
    file = open("./Mission 1 Wordlist.txt", "r")
    lines = file.readlines()
    wordlist = []
    for line in lines:
        wordlist.append(line.strip("\n"))
    return wordlist


def crack():
    # get wordlist
    wordlist = getwordlist()

    # process input
    processedlines = []
    lines = sys.stdin.readlines()
    for line in lines:
        linestripped = line.strip('\n')
        processedlines.append(linestripped)
    print("\nProcessed {} words".format(len(processedlines)))

    # unscramble each word
    outputwords = []

    for i in range(len(processedlines)):
        word = processedlines[i]
        print("Unscrambling line {}, ('{}')".format(i + 1, word))

        # unscramble the word
        letters = []
        for letter in word:
            letters.append(letter)

        lengthfact = math.factorial(len(letters))
        permutations = list(itertools.permutations(letters, len(letters)))

        for j in range(lengthfact):
            canidateletters = permutations[j]
            canidateword = ""
            for letter in canidateletters:
                canidateword = canidateword + letter
            # print("Trying {}".format(canidateword))
            if canidateword in wordlist:
                print("Found {} in wordlist".format(canidateword))
                outputwords.append(canidateword)
                break

    # display cracked words
    print("\nCracked Words:\n")
    allwords = ""
    for word in outputwords:
        allwords = allwords + "," + word
    allwords = allwords.lstrip(',')
    print(allwords)


def run():
    crack()


if __name__ == '__main__':
    run()