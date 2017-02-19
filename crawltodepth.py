# 
# This question explores a different way (from the previous question)
# to limit the pages that it can crawl.
#
#######

# THREE GOLD STARS #
# Yes, we really mean it!  This is really tough (but doable) unless 
# you have some previous experience before this course.


# Modify the crawl_web procedure to take a second parameter,
# max_depth, that limits the depth of the search.  We can 
# define the depth of a page as the number of links that must
# be followed to reach that page starting from the seed page,
# that is, the length of the shortest path from the seed to
# the page.  No pages whose depth exceeds max_depth should be
# included in the crawl.  
# 
# For example, if max_depth is 0, the only page that should
# be crawled is the seed page. If max_depth is 1, the pages
# that should be crawled are the seed page and every page that 
# it links to directly. If max_depth is 2, the crawl should 
# also include all pages that are linked to by these pages.
#
# Note that the pages in the crawl may be in any order.
#
# The following definition of get_page provides an interface
# to the website found at http://www.udacity.com/cs101x/index.html

# The function output order does not affect grading.

def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
            '<p> It is a good idea to '
            '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
            'crawl</a> before you try to  '
            '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
            'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
            '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
            'am quite good at '
            '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
            '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
            '</body> </html>')
        elif url == "http://top.contributors/velak.html":
            return ('<a href="http://top.contributors/jesyspa.html">'
        '<a href="http://top.contributors/forbiddenvoid.html">')
        elif url == "http://top.contributors/jesyspa.html":
            return  ('<a href="http://top.contributors/elssar.html">'
        '<a href="http://top.contributors/kilaws.html">')
        elif url == "http://top.contributors/forbiddenvoid.html":
            return ('<a href="http://top.contributors/charlzz.html">'
        '<a href="http://top.contributors/johang.html">'
        '<a href="http://top.contributors/graemeblake.html">')
        elif url == "http://top.contributors/kilaws.html":
            return ('<a href="http://top.contributors/tomvandenbosch.html">'
        '<a href="http://top.contributors/mathprof.html">')
        elif url == "http://top.contributors/graemeblake.html":
            return ('<a href="http://top.contributors/dreyescat.html">'
        '<a href="http://top.contributors/angel.html">')
        elif url == "A1":
            return  '<a href="B1"> <a href="C1">  '
        elif url == "B1":
            return  '<a href="E1">'
        elif url == "C1":
            return '<a href="D1">'
        elif url == "D1":
            return '<a href="E1"> '
        elif url == "E1":
            return '<a href="F1"> '
    except:
        return ""
    return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

# My new code

def posintree(tree2,epos,element):
    count = 0
    while count < len(tree2):
        if tree2[count][epos] == element:
            return count
        count += 1
    # We didn't find element in depth
    return -1

def lposintree(tree2,epos,element):
    count = len(tree2) - 1
    while count >= 0:
        if tree2[count][epos] == element:
            return count
        count -= 1
    # We didn't find element in depth
    return -1

def find_depth2(tree2,depth2,dpos):
    tlen = len(tree2) - 1
    ndepth = 0
    nextel = depth2[dpos][0]
    dexist = False
    cdepth = 0
    root = False
    #
    ##print "Entered find_depth2 - tlen ", str(tlen), ", nextel ", nextel
    ##print "Tree:  ", tree2
    ##print "Depth:  ", depth2, ", dpos:  ", dpos
    # Check if not the first element (root) and depth count exists:
    if (dpos > 0) and (depth2[dpos][1] > 0):
        dexist = True
        cdepth = depth2[dpos][1]
        ##print "Element already has depth of ", str(cdepth)
    # Sanity check, if nextel == seed then abort (loop)
    if nextel == tree2[0][1]:
        ndepth = -1  # Loop, set depth to -1
        root = True
    # Looking for depth2 element in tree as child from the end backwards
    while not root:
        ##print "Entered while loop, looking for ", nextel
        tpos = lposintree(tree2,1,nextel)
        assert tpos >= 0
        nextel = tree2[tpos][0]
        if nextel != 'root':
            ##print "Incrementing depth"
            ndepth += 1
        else:
            root = True
    if dexist:
        if ndepth < cdepth:
            ##print "Depth of ", depth2[dpos][0], " before:  ", str(depth2[dpos][1])
            depth2[dpos][1] = ndepth
            ##print "New depth of ", depth2[dpos][0], " after:  ", str(depth2[dpos][1])
            ##print "New depth assigned:  ", ndepth
            # Update Children
            count = 0
            for i,j in tree2:
                if i == depth2[dpos][0]:
                    ##print "Calling find_depth recursively with index of ", posindepth(depth2,j), "(", j, ")"
                    find_depth2(tree2,depth2,posindepth(depth2,j))
                count += 1
        ##else:
            ##print "Depth unchanged, Original:  ", cdepth, ", Rehash:  ", ndepth
    else:
        ##print "Depth of ", depth2[dpos][0], " before:  ", str(depth2[dpos][1])
        depth2[dpos][1] = ndepth
        ##print "New depth of ", depth2[dpos][0], " after:  ", str(depth2[dpos][1])
    return

# Recursive procedure - abandoning:
# Problem is that there can be more than one path to the root and this
# approach doesn't seem well suited to that
def find_depth(tree2,depth2,tlen2,dlen2,seed2):
    cont = True
    print "Entered find_depth"
    print "Tree:  ", tree2
    print "Depth:  ", depth2
    print "Tlen:  ", tlen2, ";  Dlen:  ", dlen2, ";  Seed:  ", seed2
    if tree2[tlen2][0] == 'root':
        print "Found root"
        return False
    else:
        print "depth2[" + str(dlen2) + "][1]:  ", str(depth2[dlen2][1])
        depth2[dlen2][1] += 1
        print "Incrementing depth2[" + str(dlen2) + "][1] to " + str(depth2[dlen2][1])
        target = tree2[tlen2][0]
        print "Target is ", tree2[tlen2][0]
        pos = 0
        for parent,child in tree2:
            print "Processing ", parent, child
            if child == target:
                cont = find_depth(tree2,depth2,pos,dlen2,seed2)
            if not cont:
                break
            pos += 1
        return

def indepth(depth2,element):
    ##print "Entered indepth"
    for i,j in depth2:
        ##print "Comparing i (" + i + ") to element (" + element + ")"
        if i == element:
            return True
    # element not present in depth2
    return False

def posindepth(depth2,element):
    count = 0
    for i,j in depth2:
        if i == element:
            return count
        count += 1
    # We didn't find element in depth
    return -1

def lposindepth(depth2,element):
    count = len(depth2) - 1
    while count >= 0:
        if depth2[count][0] == element:
            return count
        count -= 1
    # We didn't find element in depth
    return -1

# End my new code

def crawl_web(seed,max_depth):
    tocrawl = [seed]
    crawled = []
    tryagain = []
    tree = [ ['root', seed] ]
    depth = [ [seed, 0] ]
    duniq = True
    #
    ##print "Seed:  ", seed
    while tocrawl:
        page = tocrawl.pop()
        ##print "\nPage Selected:  ", page
        assert posindepth(depth,page) >= 0
        if (page not in crawled) and (depth[posindepth(depth,page)][1] <= max_depth):
            newlinks = get_all_links(get_page(page))
            ##print "Links on " + page + ":  ", newlinks
            for url in newlinks:
                if [page, url] not in tree:
                    # Sanity check - if URL in crawled, don't add to tree
                    if url != seed:
                        tree.append([page,url])
                        ##print "New Tree element:  ", page, url
                        # Sanity check - is element already in depth?
                        if indepth(depth,url):
                            duniq = False
                        # Find regardless
                        if duniq:  # New element
                            depth.append([url,0])
                            find_depth2(tree,depth,len(depth) - 1)
                        else:
                        # Still call find_depth if not new element
                        # Could be different (lesser) depth with alternate path from root
                            #assert lposindepth(depth,url) >= 0
                            #find_depth2(tree,depth,lposindepth(depth,url))
                            assert posindepth(depth,url) >= 0
                            find_depth2(tree,depth,posindepth(depth,url))
                        assert posindepth(depth,page) >= 0
                        ##print "Depth element:  ", url, " with a depth of ", str(depth[posindepth(depth,url)][1])
                        duniq = True  # Reset
                    else:
                        assert posindepth(depth,url) >= 0
                        find_depth2(tree,depth,posindepth(depth,url))
                        assert posindepth(depth,page) >= 0
                        ##print "Depth element:  ", url, " with a depth of ", str(depth[posindepth(depth,url)][1])
            union(tocrawl, newlinks)
            crawled.append(page)
        else:
            if page not in crawled:  # We skipped page because of depth, save for later
                if posindepth(tryagain,page) == -1:
                    ##print "Tryagain with ", page
                    tryagain.append([page,0])
                    tocrawl = [page] + tocrawl
                else:
                    tryagain[posindepth(tryagain,page)][1] += 1
                    if tryagain[posindepth(tryagain,page)][1] < 3:
                        ##print "Try #", tryagain[posindepth(tryagain,page)][1], " with ", page
                        tocrawl = [page] + tocrawl
    ##print "\n\nTree:  ", tree
    ##print "Depth:  ", depth
    ##print "\n Crawled:  "
    return crawled

#print crawl_web("http://www.udacity.com/cs101x/index.html",0)
#>>> ['http://www.udacity.com/cs101x/index.html']

#print crawl_web("http://www.udacity.com/cs101x/index.html",1)
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html',
#>>> 'http://www.udacity.com/cs101x/crawling.html']

#print crawl_web("http://www.udacity.com/cs101x/index.html",50)
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html',
#>>> 'http://www.udacity.com/cs101x/crawling.html',
#>>> 'http://www.udacity.com/cs101x/kicking.html']

#print crawl_web("http://top.contributors/forbiddenvoid.html",2)
#>>> ['http://top.contributors/forbiddenvoid.html',
#>>> 'http://top.contributors/graemeblake.html',
#>>> 'http://top.contributors/angel.html',
#>>> 'http://top.contributors/dreyescat.html',
#>>> 'http://top.contributors/johang.html',
#>>> 'http://top.contributors/charlzz.html']

#print crawl_web("A1",3)
#>>> ['A1', 'C1', 'B1', 'E1', 'D1', 'F1']
# (May be in any order)

