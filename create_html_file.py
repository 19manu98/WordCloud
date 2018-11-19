import string

# open the document with the words
try:
    speech = open("speech.txt","r")
except IOError:
    print("File does not exist")
    exit()

try:
    common = open("common stop.txt","r")
    common_word = common.read()
    common_word = common_word.split()
    # close the file
    common.close()
except IOError:
    common_word = []
    print("common does not exist")

file = speech.read()

# we don't need to keep the file open since the list already has al its content
speech.close()

# remove all the punctuation
translator=str.maketrans('','',string.punctuation)
file = file.translate(translator)

# split the string word by word
file = file.split()

# create a dict
words =dict()

# add word to the dictionary and his frequency
for word in file:
    word_ = word.lower()
    if word_ in words:
        words[word_] += 1
    else:
        words[word_] = 1

# the action fails if the user doesn't have write permission
try:
    fo = open("output.html", "w")
except IOError:
    print("You don't have the permission to write to the file")

# write the html tags
fo.write('<!DOCTYPE html>\
    <html>\
    <head lang="en">\
    <meta charset="UTF-8">\
    <title>Tag Cloud Generator</title>\
    </head>\
    <body>\
    <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')


# print the wordcloud
for word in words:
    if word in common_word:
        string = '<span style="font-size: %spx"> %s </span>' % (str(10), word)
    else:
        string = '<span style="font-size: %spx"> %s </span>' % (str(17*words[word]),word)
    fo.write(string)

# finish the file
fo.write('</div>\
    </body>\
    </html>')

# close the file
fo.close()

