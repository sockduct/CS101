def prt_abacus_row(n):
    abacusrow = "00000*****"
    abacusspc = "   "
    abacuscol = '|'
    col = 0
    pos = 10
    #
    ##print "prt_abacus_row entered with argument of ", n # Debugging
    if n == 0:
        abacuscol = abacuscol + abacusrow + abacusspc + '|'
        return abacuscol
    else:
        while col < 10:
            ##print "While loop, col = ", col # Debugging
            if n == pos:
                ##print "Appending to abacuscol which = ", abacuscol # Debugging
                abacuscol = abacuscol + abacusspc
            abacuscol = abacuscol + abacusrow[col]
            col = col + 1
            pos = pos - 1
            ##print "pos = ", pos # Debugging
    abacuscol = abacuscol + '|'
    return abacuscol

def print_abacus(n):
    row = 10
    nstr = str(n)
    nlen = len(nstr)
    sindex = 0
    ##print "print_abacus entered" # Debugging
    # Sanity checks
    ##print "sanity check start" # Debugging
    if n < 0:
        print "Number must be >= 0!"
        return
    else:
        if n == 0:
            nlen = 0
        else:
            if nlen > 10:
                print "Number must < 9,999,999,999!"
                return
    # End sanity checks
    ##print "sanity check end" # Debugging
    while row > 0:
        ##print "While loop, row = ", row # Debugging
        if nlen == row:
            ##print "Calling prt_abacus_row, sindex = ", sindex # Debugging
            print prt_abacus_row(int(nstr[sindex]))
            sindex = sindex + 1
            nlen = nlen - 1
        else:
            ##print "Calling prt_abacus_row with 0" # Debugging
            print prt_abacus_row(0)
        ##print "Incrementing row" # Debugging
        row = row - 1
    return

