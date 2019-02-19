text = open("text.txt", 'r')

sentence = ''
for line in text:
    sentence = sentence+' '+line.replace('\n', ' ').replace('  ', ' ').replace('-', '').replace(',', '').replace(';', '').replace('\'', ' ').replace('?', '').replace('.', '')
sentence = sentence.replace('  ', ' ')
sentence = sentence.lstrip()

words = sentence.split(' ')
freq = {}
for word in words:
    if word.lower() in freq:
        freq[word.lower()] += 1/len(words)
    else:
        freq[word.lower()] = 1/len(words)

text.close()

text = open("textnew.txt", 'w')

for word in freq:
    text.write(word+' '*(15-len(word)))
    a = str(freq[word])
    text.write('Частота: '+str("%.5f" % freq[word])+' '*5)
    text.write('IPM: '+str(int(freq[word]*1000000))+'\n')

text.close()

kolvoing = 0
for word in freq:
    if (word[len(word)-1] == 'g')and(word[len(word)-2] == 'n')and(word[len(word)-3] == 'i'):
        kolvoing = kolvoing+1
unkolvo = 0
for word in freq:
    if (word[0] == 'u')and(word[1] == 'n'):
        unkolvo = unkolvo+1
print('В тексте '+str(kolvoing)+' слов оканчивается на -ing и '+str(unkolvo)+' слов начинается на -un')