def newurl(lst,url):
    # Sanity checks
    if not (lst and url):
        print "Error:  Must pass URL list and new URL to check for."
        return -1
    for u,c in lst:
        if u == url:
            return False
    return True

def add_to_index(index,keyword,url):
    # Sanity checks
    if not (keyword and url):
        print "Error:  Must pass keyword and URL to be added to index."
        return -1
    # May want to revise to check if URL already present
    for i in index:
        if i[0] == keyword:  # keyword present in index
            if newurl(i[1],url):  # Check if URL is new (or already present)
                i[1].append([url,0])  # New URL, append
            return
    index.append([keyword,[[url,0]]])  # new keyword, add list structure
    return

def lookup(index,keyword):
    # Sanity checks
    if not index:
        print "Error:  Must pass index with elements."
        return -1
    if not keyword:
        print "Error:  Must pass keyword to be searched for in index."
        return -1
    for k in index:
        if k[0] == keyword:
            return k[1]
    return []  # Didn't find a match for keyword, return empty list

def add_page_to_index(index,url,content):
    # Sanity checks
    if not (url and content):
        print "Error:  Must pass url and content to index."
        return -1
    words = content.split()
    # May want to revise to remove separators from words (e.g.:  ,'" \/()[]{}:...)
    for w in words:
        add_to_index(index,w,url)
    return

def record_user_click(index,word,url):
    # Sanity checks
    if not (index and word and url):
        print "Error:  Must pass index, keyword and URL to process user click."
        return -1
    for k in index:
        if k[0] == word:
            ##print "Found keyword (" + word + ") with URLs: ", str(k[1])
            for l in k[1]:
                if l[0] == url:
                    ##print "Found URL (" + url + "), incrementing count"
                    l[1] += 1
                    ##print "List:  ", str(k[1]), ", c = " + str(l[1])

def test():
    index = []
    #
    # add_to_index tests
    add_to_index(index,'','')
    add_to_index(index,'a','')
    add_to_index(index,'','b')
    add_to_index(index,'udacity','http://udacity.com')
    add_to_index(index,'computing','http://acm.org')
    add_to_index(index,'udacity','http://npr.org')
    add_to_index(index,'udacity','http://npr.org')
    #
    print "After add_to_index:\n", index
    #
    # lookup tests
    lookup([],'')
    lookup(index,'')
    print lookup(index,'udacity')
    print lookup(index,'dne')
    #
    # add_page_to_index tests
    add_page_to_index(index,'','')
    add_page_to_index(index,'a','')
    add_page_to_index(index,'','b')
    add_page_to_index(index,'url1','This is a test')
    add_page_to_index(index,'url2','Another page of text')
    #
    print "After add_page_to_index:\n", index
    #
    # record_user_click tests
    record_user_click([],'','')
    record_user_click(index,'','')
    record_user_click(index,'a','')
    record_user_click(index,'','b')
    record_user_click(index,'test','url1')
    record_user_click(index,'test','url1')
    record_user_click(index,'test','url1')
    record_user_click(index,'This','url1')
    record_user_click(index,'page','url2')
    #
    print "After record_user_click:\n", index

    return

