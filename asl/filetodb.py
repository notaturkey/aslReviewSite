from polls.models import word

with open('./aslvocab1.txt') as f:
    for line in f:
        q = word(random_word = line, url = 'https://student.truewayasl.com/?s=%' + line)
        q.save()
        