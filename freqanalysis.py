def chkinput(m):
    valid = 'abcdefghijklmnopqrstuvwxyz'
    l = len(m)
    i = 0
    #
    if l < 1:
        print "Error:  Message must contain at least one character in the set of a-z."
        return False
    while i < len(m):
        if m[i] not in valid:
            print "Error:  Invalid characters in message, only a-z supported."
            return False
        i += 1
    return True

def freq_analysis(m):
    l = len(m)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    freq_list = []
    i = 0
    #
    if chkinput(m):
        while i < len(alphabet):
            ##freq_list.append(1.0 * m.count(alphabet[i]) / l)
            freq_list += [ (1.0 * m.count(alphabet[i]) / l) ]
            i += 1
    else:  # Should get error message from chkinput
        return
    return freq_list

