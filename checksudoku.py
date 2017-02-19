def valid_elements(sqlst,vset):
    for i in sqlst:
        for j in i:
            if not j in vset:
                ##print "j (", str(j), ") is not in value range"
                return False
            ##else:
                ##print "j (", str(j), ") is in value range"
    return True

def uniq_relements(sqlst,vset):
    for i in sqlst:
        elchk = [] + vset  # Want to be separate from vset
        for j in i:
            if j in elchk:
                ##print "j (", str(j), ") is in value range"
                elchk[elchk.index(j)] = 0
                ##print "Removing j (", str(j), ") from element list:  ", elchk
            else:
                ##print "j (", str(j), ") is not in value range"
                return False
    return True

def uniq_celements(sqlst,vset):
    c = len(sqlst) - 1

    while c >= 0:
        elchk = [] + vset  # Want to be separate from vset
        r = len(sqlst) - 1
        while r >= 0:
            if sqlst[r][c] in elchk:
                ##print "sqlst[r][c] (", str(sqlst[r][c]), ") is in value range"
                elchk[elchk.index(sqlst[r][c])] = 0
                ##print "Removing j (", str(sqlst[r][c]), ") from element list:  ", elchk
                r -= 1
            else:
                return False
        c -= 1
    return True

def check_sudoku(sqlst):
    l = len(sqlst)
    count = 1
    vset = []
    status = False

    while count <= l:
        vset.append(count)
        count += 1
    status = valid_elements(sqlst,vset)
    status = uniq_relements(sqlst,vset)
    status = uniq_celements(sqlst,vset)

    return status

