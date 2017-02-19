def add_to_index(index,keyword,url):
    # Sanity checks
    if not (keyword and url):
        print "Error:  Must pass keyword and URL to be added to index."
        return -1
    # May want to revise to check if URL already present
    for i in index:
        if i[0] == keyword:  # keyword present in index
            if url not in i[1]:  # Check if URL is new (or already present)
                i[1].append(url)  # New URL, append
            return
    index.append([keyword,[url]])  # new keyword, add list structure
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
    add_page_to_index(index,'fake.text','This is a test')
    #
    print "After add_page_to_index:\n", index

    return

