def rowneqcoln(lst):
    # Check if # of rows == # of columns
    # returns True if yes, otherwise no
    n = len(lst)
    ##print "n = " + str(n)
    #
    for e in lst:  # Check length of each row == number of rows (rows == cols)
        if len(e) != n:
            ##print "e = " + str(e)
            ##print "# Rows != # Columns for this list"
            return False
    ##print "# Rows == # Columns for this list"
    return True

def is_identity_matrix(lst):
    r = 0  # Row
    c = 0  # Column
    n = len(lst)  # Number of rows/columns
    #
    if rowneqcoln(lst):
        while r < n:  # Check each rol/col combo for matching symmetry
            c = 0
            while c < n:
                ##print "Checking list element[" + str(r) + "][" + str(c) + "] (" + str(lst[r][c]) + ")"
                if (c == 0) and (r == 0):
                    if lst[r][c] != 1:
                        ##print "Check lst[0][0] == 1 failed"
                        return False
                else:
                    if (c > 0) and (r == c):
                        if lst[r][c] != 1:
                            ##print "Check lst[n][n] == 1 failed"
                            return False
                    else:
                        if lst[r][c] != 0:
                            ##print "Check lst[r][c] == 0 failed"
                            return False
                c += 1
            r += 1
        return True
    else:  # Number of rows != number of columns
        return False

