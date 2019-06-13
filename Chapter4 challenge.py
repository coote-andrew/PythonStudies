spam = ['apples', 'bananas', 'tofu', 'cats']
spam *= 2
spamS = ''

for i in range(len(spam) - 2):
    spamS += str(spam[i]) + ', '

spamS += spam[len(spam) - 2] + ' and ' + spam[len(spam) -1]

print(spamS)
