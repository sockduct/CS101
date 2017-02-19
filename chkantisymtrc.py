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

def antisymmetric(lst):
    i = 0  # Index
    rc = 0  # row/column count
    n = len(lst)  # Number of rows/columns
    #
    if rowneqcoln(lst):
        while rc < n:  # Check each rol/col combo for matching symmetry
            i = 0
            while i < n:
                ##print "Comparing list element[" + str(rc) + "][" + str(i) + "] (" + str(lst[rc][i]) + ") with list element[" + str(i) + "][" + str(rc) + "] (" + str(lst[i][rc]) + ")"
                if lst[rc][i] != -lst[i][rc]:
                    return False
                i += 1
            rc += 1
        return True
    else:  # Number of rows != number of columns
        return False

