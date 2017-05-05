print 'This is a script'
name = 'Peter Voivontas'
words = name.split(' ')
for i in words:
    if i != 'Voivontas':
        print i,
    else:
        print len(i) * '*'

