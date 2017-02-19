def binstr(n):
    b = bin(n)[2:]  # Convert n to binary string and strip leading '0b'
    b = '0'*(8 - len(b)) + b  # Make b 8 digits long by prepending 'missing' 0's
    return b

def mkrules(p):
    d = { 1:['...','.'], 2:['..x','.'], 4:['.x.','.'], 8:['.xx','.'], \
          16:['x..','.'], 32:['x.x','.'], 64:['xx.','.'], 128:['xxx','.'] }
    b = binstr(p)
    rules = {}
    pos = 7
    for i in [1,2,4,8,16,32,64,128]:
        ##print "\ni = " + str(i)
        if b[pos] == '1':
            d[i][1] = 'x'
        rules[d[i][0]] = d[i][1]
        ##print "d = " + str(d)
        ##print "rules = " + str(rules)
        pos -= 1
    ##print "end: d = " + str(d)
    ##print "end: rules = " + str(rules)
    return rules

def celltrans(s,rules):
    news = ''
    ##print "s = " + s
    if len(s) == 1:
        ##print "sequence = " + s*3
        news = rules[s*3]
    else:
        for i in range(0,len(s)):
            ##print "i = " + str(i) + ", news = " + news
            if i == 0:
                ##print "sequence = " + s[-1]+s[0:2]
                news += rules[s[-1]+s[0:2]]
            elif i == (len(s) - 1):
                ##print "sequence = " + s[-2:]+s[0:1]
                news += rules[s[-2:]+s[0:1]]
            else:
                ##print "sequence = " + s[i-1:i+2]
                news += rules[s[i-1:i+2]]
    ##print "returning news = " + news
    return news

def cellular_automaton(s,p,g):
    ##print "Passed s = " + s + ", p = " + str(p) + ", g = " + str(g)
    rules = mkrules(p)
    ##print "rules = " + str(rules)
    for i in range(1,g+1):
        ##print "main: i = " + str(i) + ", s = " + s
        news = celltrans(s,rules)
        s = news
    return s

