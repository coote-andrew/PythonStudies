import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'LOL'
    elif answerNumber == 4:
        return 'reply hazy, ask again later'

answer = 'yes'

while answer == 'yes':
    print('what would you like answering?')
    response = input()
    print('Ah, I can tell you want to know about ' + response)
    print('my answer is...')
    r = random.randint(1,4)
    fortune = getAnswer(r)
    print(fortune)
    print('would you like to ask another question')
    answer = input().lower()
    
