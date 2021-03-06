def create_data_structure(string_input):
    network = {}  # User Profiles Data Structure
    userconns = {}  # Temporary User Connections Dictionary
    # The strings below use a trailing space so we can search for the string,
    # and then advance len(<this_string>) to find the next data element(s)
    connstr = 'is connected to '  # String between user and his/her connections
    gamestr = 'likes to play '  # String between user and his/her games liked
    sentences = string_input.split('.')
    for sentence in sentences:
        ##print "sentence = " + str(sentence)
        if sentence:
            eouser = sentence.find(' ')  # User termined by whitespace
            if eouser == -1:
                print "Input string parsing error."
                return -1
            user = sentence[:eouser]
            ##print "found user = " + user
            # Can't use if sentence.find(...): because if find doesn't find string it returns
            # -1 which is interpreted as True.  Only 0 is interpreted as False which is actually
            # a valid value for find - means found at beginning of string.
            if sentence.find(connstr) >= 0:
                # Must accrue user connections - can't add with add_connections because
                # referred to users might not yet exist
                userconns[user] = sentence[sentence.find(connstr) + len(connstr):].split(', ')
                ##print "found connections = " + str(userconns[user])
            elif sentence.find(gamestr) >= 0:
                user_gamesliked = sentence[sentence.find(gamestr) + len(gamestr):].split(', ')
                ##print "found game's liked = " + str(user_gamesliked)
                add_new_user(network, user, user_gamesliked)
            else:
                print "Input string parsing error."
                return -1
        else:
            ##print "skipping empty input"
            pass  # No-op
    for user in userconns:
        for connuser in userconns[user]:
            add_connection(network,user,connuser)
    return network

def get_connections(network, user):
    if user not in network:
        return None
    else:
        if network[user][0]:
            return network[user][0]
        else:
            return []

def get_games_liked(network,user):
    if user not in network:
        return None
    else:
        if network[user][1]:
            return network[user][1]
        else:
            return []

def add_connection(network, user_A, user_B):
    errflag = False  # set if user_A or user_B not in network
    ##print "add_connection passed user_A = " + user_A + ", user_B = " + user_B
    if user_A in network and user_B in network:
        # Check if user_B already a connection of user_A
        if user_B in network[user_A][0]:
            print user_B + " is already a connection of " + user_A + "!  No changes made."
        else:
            network[user_A][0].append(user_B)
    else:
        if user_A not in network:
            print user_A + " not in network!"
            errflag = True
        if user_B not in network:
            print user_B + " not in network!"
            errflag = True
        print "No connections added/changed."
    if errflag:
        return False
    else:
	    return network

def add_new_user(network, user, games):
    ##print "add_new_user passed user = " + user + ", games = " + str(games)
    if user not in network:
        network[user] = [],games
    else:
        print "user " + user + " already in the network"
        print "not updating network or user game preferences"
        pass
    return network

def get_secondary_connections(network, user):
    secondconns = []  # List of secondary user connections
    if user not in network:
        return None
    else:
        if network[user][0]:
            for userconn in network[user][0]:
                ##print "(before) secondconns = " + str(secondconns)
                # For each user, retrieve his/her connections
                chkconns = get_connections(network,userconn)
                ##print "(after) secondconns = " + str(secondconns)
                ##print "chkconns = " + str(chkconns)
                for newconn in chkconns:
                    # Only add user to secondary connection list if he/she
                    # not already present
                    ##print "newconn = " + str(newconn)
                    if newconn not in secondconns:
                        secondconns.append(newconn)
            return secondconns
        else:
            return []

def connections_in_common(network, user_A, user_B):
    errflag = False  # set if user_A or user_B not in network
    count = 0  # Count of connections in common between users
    if user_A in network and user_B in network:
        useraconns = network[user_A][0]
        ##print "useraconns = " + str(useraconns)
        userbconns = network[user_B][0]
        ##print "userbconns = " + str(userbconns)
        # Iterate through user_A's connections
        # For each connection, see if user_B has same connection
        for aconn in useraconns:
            ##print "aconn = " + str(aconn)
            if aconn in userbconns:
                count += 1
    else:
        if user_A not in network:
            print user_A + " not in network!"
            errflag = True
        if user_B not in network:
            print user_B + " not in network!"
            errflag = True
    if errflag:
        return False
    else:
	    return count

def path_to_friend(network, user_A, user_B, usersevald=None):
	# your RECURSIVE solution here!
    if usersevald is None:
        usersevald = []
    ##print "entered path_to_friend with user_A = " + user_A + ", user_B = " + user_B + ", usersevald = " \
     ##   + str(usersevald)
    errflag = False  # set if user_A or user_B not in network
    connpath = None
    if user_A in network and user_B in network:
        usersevald.append(user_A)
        if user_B in network[user_A][0]:
            connpath = [user_A,user_B]
        else:
            for aconn in network[user_A][0]:
                ##print "user_A's (" + user_A + ") connections:  " + str(network[user_A][0]) + \
                 ##   ", starting with " + aconn
                if aconn not in usersevald:
                    ##print "calling path_to_friend with user_A = " + aconn + ", user_B = " + user_B + \
                     ##   ", usersevald = " + str(usersevald)
                    testconnpath = path_to_friend(network,aconn,user_B,usersevald)
                    ##print "returned, testconnpath = " + str(testconnpath)
                    if testconnpath:
                        return [user_A] + testconnpath
    else:
        if user_A not in network:
            print user_A + " not in network!"
            errflag = True
        if user_B not in network:
            print user_B + " not in network!"
            errflag = True
    if errflag:
        return None
    else:
	    return connpath

##########################################################################
## User Defined Procedures
##########################################################################
## User Defined - Add a new liked game for passed user
def add_game_liked(network, user, game):
    if user not in network:
        print user + " not in network!"
        return False
    if game not in network[user][1]:
        network[user][1].append(game)
    else:
        print game + " already in user's liked game list!  Not adding again."
    return network

## User Defined - Return a dictionary of all liked games, for each game indicate how many like it
def get_all_games_liked(network):
    games = {}
    for user in network:
        for game in network[user][1]:
            if game not in games:
                games[game] = 1
            else:
                games[game] += 1
    return games

## User Defined - Return list of all users
def get_all_users(network):
    users = []
    for user in network:
        users.append(user)
    return users

## User Defined - Return a dictionary of all users, for each user indicate how many connections to him/her
def get_all_users_conncount(network):
    users_conncount = {}
    # Don't see good way to leverage get_all_users
    for user in network:
        users_conncount[user] = 0
    for user in users_conncount:
        for conn in network[user][0]:
            users_conncount[conn] += 1
    return users_conncount

## User Defined - Return a dictionary of statistics for all aspects of data structure
def get_all_stats(network):
    stats = {}
    stats['user_count'] = len(get_all_users(network))
    stats['connection_count'] = 0
    stats['unique_connection_count'] = 0
    stats['liked_game_count'] = 0
    stats['unique_liked_game_count'] = 0
    uniqueconn = []
    uniquegame = []
    for user in network:
        for conn in network[user][0]:
            stats['connection_count'] += 1
            if conn not in uniqueconn:
                uniqueconn.append(conn)
                stats['unique_connection_count'] += 1
        for game in network[user][1]:
            stats['liked_game_count'] += 1
            if game not in uniquegame:
                uniquegame.append(game)
                stats['unique_liked_game_count'] += 1
    return stats

##########################################################################
## More ideas...
##########################################################################
# Enhance procedures so can deal with any passed variable being null
# Enhance procedures so only accept defined characters and return error for anything else


# Testing
# Data:
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."
#
# Code:
# Test create_data_structure
mynet = create_data_structure(example_input)
#
# Create some test users and test add_new_user
mynet = add_new_user(mynet,'NoConnsNoGames',[])  # Add new user with no games
print mynet
mynet = add_new_user(mynet,'TNT',['Starfleet Commander','Call of Arms','Top Secret'])  # Add new user
print mynet
mynet = add_new_user(mynet,'Dynamo',['City Comptroller','Top Secret'])  # Add new user
print mynet
mynet = add_new_user(mynet,'Robin',['City Comptroller','Top Secret'])  # Try to add existing user
print mynet
#
# Test get_connections
print get_connections(mynet,'Robin')  # Existing user with connections
print get_connections(mynet,'dne')  # User doesn't exist
print get_connections(mynet,'NoConnsNoGames')  # User with empty connections list
print path_to_friend(mynet,'TNT','NoConnsNoGames')  # Users have no connections in common
#
# Test get_games_liked
print get_games_liked(mynet,'Robin')  # Existing user with liked games
print get_games_liked(mynet,'dne')  # User doesn't exist
print get_games_liked(mynet,'NoConnsNoGames')  # User with empty liked games list
#
# Test add_connection
mynet = add_connection(mynet,'TNT','Dynamo')  # Add new connection
print mynet
mynet = add_connection(mynet,'Dynamo','Robin')  # Add new connection
print mynet
mynet = add_connection(mynet,'Robin','Ollie')  # Add existing connection
print mynet
mynet2 = add_connection(mynet,'dne','Dynamo')  # Try to add connection to non-existent user
print mynet
mynet2 = add_connection(mynet,'TNT','dne')  # Try to add non-existent connection to user
print mynet
mynet2 = add_connection(mynet,'dne','dne')  # Try to add non-existent connection to non-existent user
print mynet
#
# Test get_secondary_connections
print get_secondary_connections(mynet,'dne')  # User doesn't exist
print get_secondary_connections(mynet,'NoConnsNoGames')  # User has no connections
print get_secondary_connections(mynet,'Robin')  # Normal user with connections
print get_secondary_connections(mynet,'John')  # Normal user with connections
#
# Test connections_in_common
print connections_in_common(mynet,'NoConnsNoGames','NoConnsNoGames')  # Users have no connections
print connections_in_common(mynet,'NoConnsNoGames','dne')  # 1st user has no connections, 2nd doesn't exist
print connections_in_common(mynet,'dne','NoConnsNoGames')  # 1st user doesn't exit, 2nd user has no connections
print connections_in_common(mynet,'dne1','dne2')  # 1st user doesn't exit, 2nd user doesn't exist
print connections_in_common(mynet,'Robin','John')  # Users have no connections in common
print connections_in_common(mynet,'John','Mercedes')  # Users have connections in common
print connections_in_common(mynet,'John','Bryant')  # Users have no connections in common
#
# Test path_to_friend
print path_to_friend(mynet,'NoConnsNoGames','NoConnsNoGames')  # Users have no connections
print path_to_friend(mynet,'NoConnsNoGames','dne')  # 1st user has no connections, 2nd doesn't exist
print path_to_friend(mynet,'dne','NoConnsNoGames')  # 1st user doesn't exit, 2nd user has no connections
print path_to_friend(mynet,'dne1','dne2')  # 1st user doesn't exit, 2nd user doesn't exist
print path_to_friend(mynet,'Robin','John')  # Users have no connections in common
print path_to_friend(mynet,'John','Mercedes')  # Users have connections in common
print path_to_friend(mynet,'John','Bryant')  # Users have no connections in common
print path_to_friend(mynet,'TNT','NoConnsNoGames')  # Users have no connections in common
#
# Test add_game_liked
mynet2 = add_game_liked(mynet,'TNT','Pac Man')  # Add new game to existing user
print mynet2
mynet22 = add_game_liked(mynet,'dne','Pac Man')  # Add new game for user that doesn't exist
print mynet2
mynet22 = add_game_liked(mynet,'TNT','Pac Man')  # Add game already in user's list
print mynet2
#

