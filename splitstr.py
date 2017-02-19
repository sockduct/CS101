def split_string(string,separators):
    wordlist = []
    word = ''
    newword = False
    c = 0
    #
    while c < len(string):
        ##print "Looking at:  ", string[c]
        if string[c] not in separators:
            word += string[c]
            newword = True
            ##print "Adding non-separator to word which is now:  ", word
        else:  # c is a separator
            ##print "Found separator ``" + string[c] + "''"
            if newword:  # if we have a word add it to the list
                wordlist.append(word)
                ##print "Adding word (" + word + ") to wordlist (" + str(wordlist) + "), resetting newword"
                word = ''
                newword = False
        c += 1
    if newword:  # if string not terminated by separator
        wordlist.append(word)
        ##print "Adding word (" + word + ") to wordlist (" + str(wordlist) + "), resetting newword"
        word = ''
        newword = False
    return wordlist

def split_string2(string,separators):
    wordlist = []
    atsplit = True  # Hit a separator
    #
    for char in string:  # iterate through string one character at a time
        print "Looking at:  ", char
        if char in separators:
            atsplit = True
            print "Found separator ``" + char + "''"
        else:
            if atsplit:
                wordlist.append(char)  # start new list element
                atsplit = False
                print "Appending char (" + char + ") to wordlist (" + str(wordlist) + "), resetting atsplit"
            else:
                wordlist[-1] += char  # add char to last word
                print "Appending char (" + char + ") to wordlist (" + str(wordlist) + "), resetting atsplit"
    return wordlist

def test():
    print split_string('','')
    print split_string('a','')
    print split_string('','b')
    print split_string('This is a test.',' .')
    print split_string("This is a much, much more complex example.  (With nested things.)  Let's see how it deals with this!!!",', .()!')

