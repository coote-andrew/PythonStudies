#Magic 8 ball 2
import random

messages = ['It is certain', 'It is decidely so', 'Reply hazy, try again', 'Ask again later','Concentrate and ask again','My reply is no','Outlook not so good','Very doubtful']

print(messages[random.randint(0,len(messages)-1)])
