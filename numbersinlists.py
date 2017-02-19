def chkinput(s):
    l = len(s)
    i = 0
    valid = '123456789'
    #
    if l < 1:
        print "Error:  Must include at least one number as input."
        return False
    while i < l:
        if s[i] not in valid:
            print "Error:  Input string must only consist of numbers from 1-9."
            return False
        i += 1
    return True

def numbers_in_lists(s):
    l = len(s)
    i = 0
    maxprev = 0
    usesub = False
    lst = []
    sublst = []
    #
    if chkinput(s):
        ##print "Input (" + s + ") validated."
        while i < l:
            n = int(s[i])
            ##print "n = " + str(n)
            if (not usesub) and (n <= maxprev):
                sublst.append(n)
                usesub = True
                ##print "Case 1, lst = " + str(lst) + ", usesub = " + str(usesub) + ", sublst = " + str(sublst) + ", maxprev = " + str(maxprev)
            elif usesub and (n <= maxprev):
                sublst.append(n)
                ##print "Case 2, lst = " + str(lst) + ", usesub = " + str(usesub) + ", sublst = " + str(sublst) + ", maxprev = " + str(maxprev)
            elif usesub:
                lst.append(sublst)
                sublst = []
                usesub = False
                lst.append(n)
                maxprev = n
                ##print "Case 3, lst = " + str(lst) + ", usesub = " + str(usesub) + ", sublst = " + str(sublst) + ", maxprev = " + str(maxprev)
            else:
                lst.append(n)
                maxprev = n
                ##print "Case 4, lst = " + str(lst) + ", usesub = " + str(usesub) + ", sublst = " + str(sublst) + ", maxprev = " + str(maxprev)
            i += 1
        if sublst:
            lst.append(sublst)
    else:
        # Should have received error from chkinput
        return
    return lst

