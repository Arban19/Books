import random

print("Hello, I'm your psychic. I will resolve your problem, I have the answer to what's bothering you.")
def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certainly so"
    if answerNumber == 2:
        return "It is decidedly so"
    if answerNumber == 3:
        return "Yes"
    if answerNumber == 4:
        return "Reply hazy, try again"
    if answerNumber == 5:
        return "Ask again later"
    if answerNumber == 6:
        return "Concentrate and ask again"
    if answerNumber == 7:
        return "My reply is no"
    if answerNumber == 8:
        return "Outlook not so good"
    if answerNumber == 9:
        return "Very doubtful"

print(getAnswer(random.randint(1,9)))
