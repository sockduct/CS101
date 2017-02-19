def create_data_structure(string_input):
    network = {}  # User Profiles Data Structure
    userconns = {}  # Temporary User Connections Dictionary
    # The strings below use a trailing space so we can search for the string,
    # and then advance len(<this_string>) to find the next data element(s)
    connstr = 'is connected to '  # String between user and his/her connections
    gamestr = 'likes to play '  # String between user and his/her games liked
    sentences = string_input.split('.')
    for sentence in sentences:
        if sentence:
            eouser = sentence.find(' ')  # User termined by whitespace
            if eouser == -1:
                print "Input string parsing error."
                return -1
            user = sentence[:eouser]
            # Can't use if sentence.find(...): because if find doesn't find string it returns
            # -1 which is interpreted as True.  Only 0 is interpreted as False which is actually
            # a valid value for find - means found at beginning of string.
            if sentence.find(connstr) >= 0:
                # Must accrue user connections - can't add with add_connections because
                # referred to users might not yet exist
                userconns[user] = sentence[sentence.find(connstr) + len(connstr):].split(', ')
            elif sentence.find(gamestr) >= 0:
                user_gamesliked = sentence[sentence.find(gamestr) + len(gamestr):].split(', ')
                add_new_user(network, user, user_gamesliked)
            else:
                print "Input string parsing error."
                return -1
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
    if user_A in network and user_B in network:
        # Check if user_B already a connection of user_A
        if user_B in network[user_A][0]:
            # Procedure specifications don't ask for warning so commented out
            #print user_B + " is already a connection of " + user_A + "!  No changes made."
            pass
        else:
            network[user_A][0].append(user_B)
    else:
        if user_A not in network:
            # Procedure specifications don't ask for warning so commented out
            #print user_A + " not in network!"
            errflag = True
        if user_B not in network:
            # Procedure specifications don't ask for warning so commented out
            #print user_B + " not in network!"
            errflag = True
        # Procedure specifications don't ask for warning so commented out
        #print "No connections added/changed."
    if errflag:
        return False
    else:
	    return network

def add_new_user(network, user, games):
    if user not in network:
        network[user] = [],games
    else:
        # Procedure specifications don't ask for warning so commented out
        #print "user " + user + " already in the network"
        #print "not updating network or user game preferences"
        pass
    return network

def get_secondary_connections(network, user):
    secondconns = []  # List of secondary user connections
    if user not in network:
        return None
    else:
        if network[user][0]:
            for userconn in network[user][0]:
                # For each user, retrieve his/her connections
                chkconns = get_connections(network,userconn)
                for newconn in chkconns:
                    # Only add user to secondary connection list if he/she
                    # not already present
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
        userbconns = network[user_B][0]
        # Iterate through user_A's connections
        # For each connection, see if user_B has same connection
        for aconn in useraconns:
            if aconn in userbconns:
                count += 1
    else:
        if user_A not in network:
            # Procedure specifications don't ask for warning so commented out
            #print user_A + " not in network!"
            errflag = True
        if user_B not in network:
            # Procedure specifications don't ask for warning so commented out
            #print user_B + " not in network!"
            errflag = True
    if errflag:
        return False
    else:
	    return count

def path_to_friend(network, user_A, user_B, usersevald=None):
    if usersevald is None:
        usersevald = []
    errflag = False  # set if user_A or user_B not in network
    connpath = None
    if user_A in network and user_B in network:
        usersevald.append(user_A)
        if user_B in network[user_A][0]:
            connpath = [user_A,user_B]
        else:
            for aconn in network[user_A][0]:
                if aconn not in usersevald:
                    testconnpath = path_to_friend(network,aconn,user_B,usersevald)
                    if testconnpath:
                        return [user_A] + testconnpath
    else:
        if user_A not in network:
            # Procedure specifications don't ask for warning so commented out
            #print user_A + " not in network!"
            errflag = True
        if user_B not in network:
            # Procedure specifications don't ask for warning so commented out
            #print user_B + " not in network!"
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

## User Defined - Return a dictionary of all liked games, for each game indicate
## how many like it
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

## User Defined - Return a dictionary of all users, for each user indicate how
## many connections to him/her
def get_all_users_conncount(network):
    users_conncount = {}
    # Don't see good way to leverage get_all_users
    for user in network:
        users_conncount[user] = 0
    for user in users_conncount:
        for conn in network[user][0]:
            users_conncount[conn] += 1
    return users_conncount

## User Defined - Return a dictionary of statistics for all aspects of data
## structure
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

