from polls.models import word

with open('./aslvocab1.txt') as f:
    for line in f:
        q = word(random_word = line, url = 'https://student.truewayasl.com/?s=%' + line)
        q.save()
        
from unit.models import word

with open('./aslvocab2.txt') as f:
    for line in f:
        q = word2(random_word = line, url = 'https://student.truewayasl.com/?s=%' + line)
        q.save()