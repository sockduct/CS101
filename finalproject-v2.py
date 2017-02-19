###########################################################################
# 
# Author:       James R. Small (js646y@att.com)
# Version:      1.1
# Since:        2015-06-20
# Last Update:  2015-06-24
#
# Description:  Intro to CS 101 Final Project, SocialNetwork
#
###########################################################################
#
# Libraries used by user defined procedures
import numpy as np
import matplotlib.pyplot as plt
#
#
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
            endofuser = sentence.find(' ')  # User termined by whitespace
            if endofuser == -1:
                print "Input string parsing error."
                return -1
            user = sentence[:endofuser]
            ##print "found user = " + user
            # Can't use if sentence.find(...): because if find doesn't find
            # string it returns -1 which is interpreted as True.  Only 0 is
            # interpreted as False which is actually # a valid value for
            # find - means found at beginning of string.
            if sentence.find(connstr) >= 0:
                # Must accrue user connections - can't add with add_connections
                # because referred to users might not yet exist
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
    # Iterate through all users in userconns list
    for user in userconns:
        # For each user, iterate through their connections and add them to
        # the network
        for connuser in userconns[user]:
            add_connection(network,user,connuser)
    return network

def get_connections(network, user):
    if user not in network:
        return None
    else:
        if network[user]['connections']:
            return network[user]['connections']
        else:
            return []

def get_games_liked(network,user):
    if user not in network:
        return None
    else:
        if network[user]['games']:
            return network[user]['games']
        else:
            return []

def add_connection(network, user_A, user_B, verbose=False):
    ##print "add_connection passed user_A = " + user_A + ", user_B = " + user_B
    if user_A in network and user_B in network:
        # Check if user_B already a connection of user_A
        if user_B in get_connections(network,user_A):
            if verbose:
                print user_B + " is already a connection of " + user_A + "!  No changes made."
        else:
            network[user_A]['connections'].append(user_B)
        return network
    else:
        if user_A not in network:
            if verbose:
                print user_A + " not in network!"
        if user_B not in network:
            if verbose:
                print user_B + " not in network!"
        if verbose:
            print "No connections added/changed."
        return False

def add_new_user(network, user, games, verbose=False):
    ##print "add_new_user passed user = " + user + ", games = " + str(games)
    if user not in network:
        network[user] = {'connections':[],'games':games}
    else:
        if verbose:
            print "user " + user + " already in the network, not updating" \
                + " network or user game preferences"
    return network

def get_secondary_connections(network, user):
    secondconns = []  # List of secondary user connections
    if user not in network:
        return None
    else:
        userconns = get_connections(network,user)
        if userconns:
            # Iterate through all user's conections
            for userconn in userconns:
                ##print "(before) secondconns = " + str(secondconns)
                # For each user, retrieve his/her secondary connections
                newsecondconns = get_connections(network,userconn)
                ##print "(after) secondconns = " + str(secondconns)
                ##print "newsecondconns = " + str(newsecondconns)
                # Iterate through each secondary connection
                for chksecondconn in newsecondconns:
                    # Only add user to secondary connection list if he/she
                    # not already present
                    ##print "chksecondconn = " + str(chksecondconn)
                    if chksecondconn not in secondconns:
                        secondconns.append(chksecondconn)
            return secondconns
        else:
            return []

def connections_in_common(network, user_A, user_B, verbose=False):
    count = 0  # Count of connections in common between users
    if user_A in network and user_B in network:
        useraconns = get_connections(network,user_A)
        ##print "useraconns = " + str(useraconns)
        userbconns = get_connections(network,user_B)
        ##print "userbconns = " + str(userbconns)
        # Iterate through user_A's connections
        # For each connection, see if user_B has same connection
        for useraconn in useraconns:
            ##print "aconn = " + str(aconn)
            if useraconn in userbconns:
                count += 1
        return count
    else:
        if user_A not in network:
            if verbose:
                print user_A + " not in network!"
        if user_B not in network:
            if verbose:
                print user_B + " not in network!"
        return False

def path_to_friend(network, user_A, user_B, verbose=False, usersevald=None):
	# RECURSIVE solution
    # Keep track of evaluated users to prevent recursion loops
    if usersevald is None:
        usersevald = []
    ##print "entered path_to_friend with user_A = " + user_A + ", user_B = " + user_B + ", usersevald = " \
     ##   + str(usersevald)
    userconnpath = None  # Connection path from user_A to user_B
    if user_A in network and user_B in network:
        usersevald.append(user_A)
        useraconns = get_connections(network,user_A)
        # Did we find the target (user_B) in user_A's connection list?
        if user_B in useraconns:
            # Yes!
            userconnpath = [user_A,user_B]
        # Not yet...
        else:
            # Iterate through user_A's connections
            for useraconn in useraconns:
                ##print "user_A's (" + user_A + ") connections:  " + str(useraconns) + \
                 ##   ", starting with " + useraconn
                # Make sure we only recurse with a connection (useraconn) if it hasn't
                # yet been evaluated (not in usersevald)
                if useraconn not in usersevald:
                    ##print "calling path_to_friend with user_A = " + useraconn + ", user_B = " + user_B + \
                     ##   ", usersevald = " + str(usersevald)
                    testuserconnpath = path_to_friend(network,useraconn,user_B,usersevald)
                    ##print "returned, testuserconnpath = " + str(testuserconnpath)
                    if testuserconnpath:
                        return [user_A] + testuserconnpath
        return userconnpath
    else:
        if user_A not in network:
            if verbose:
                print user_A + " not in network!"
        if user_B not in network:
            if verbose:
                print user_B + " not in network!"
        return None

##########################################################################
## User Defined Procedures
##########################################################################
#
##########################################################################
# Standard documentation header for each procedure
##########################################################################
#
# Short one line description.
#
# Longer description. If there were any, it would be
# here.
#
# @param <variable-name> type and description of parameter
# @return type and description of returned results
# @see Provides a link to other documentation (reference)
#
##########################################################################
#
##########################################################################
#
# Add a new liked game for passed user (User Defined Procedure)
#
# @param network User profile's data structure (dictionary)
# @param user User (string) to add liked game to
# @param game Liked Game (string) to add to user's liked game list
# @param verbose Diagnostic output verbosity (default is False/off)
# @return Updated network if valid input else False
#
def add_game_liked(network, user, game, verbose=False):
    if user not in network:
        if verbose:
            print user + " not in network!"
        return False
    if not game:
        if verbose:
            print "Invalid game.  No changes made to user's liked game list!"
    elif game not in get_games_liked(network,user):
        network[user]['games'].append(game)
    else:
        if verbose:
            print game + " already in user's liked game list!  Not adding again."
    return network

##########################################################################
#
# Return all liked games, for each game indicate how many like it
# (User Defined Procedure)
#
# @param network User profile's data structure (dictionary)
# @return games (dictionary) as described above
#
def get_all_games_liked(network):
    games = {}
    # Iterate through all users in the network
    for user in network:
        # For each user, iterate through their list of games liked
        for game in get_games_liked(network,user):
            # If it's a new game start the liked count at 1
            if game not in games:
                games[game] = 1
            # If the game is already in the list, increment the liked
            # count
            else:
                games[game] += 1
    return games

##########################################################################
#
# Chart all liked games by popularity from most to least
# (User Defined Procedure)
#
# @param network User profile's data structure (dictionary)
# @return games (dictionary) as described above
#
def chart_all_games_liked(network):
    gameslist = []
    gameslistlikes = []
    games = get_all_games_liked(network)
    for key,value in sorted(games.items()):
        gameslist.append(key)
        gameslistlikes.append(value)
    y_pos = np.arange(len(gameslist))
    #
    plt.barh(y_pos, gameslistlikes, align='center', alpha=0.4)
    plt.yticks(y_pos, gameslist)
    plt.xlabel('Number of members who like it')
    plt.title('Popularity of games liked by members')
    #
    plt.show()
	
##########################################################################
#
# Return list of all users (User Defined Procedure)
#
# @param network User profile's data structure (dictionary)
# @return users (list) as described above
#
def get_all_users(network):
    users = []
    for user in network:
        users.append(user)
    return users

##########################################################################
#
# Return all users, for each user indicate how many connections to him/her
# (User Defined Procedure)
#
# @param network User profile's data structure (dictionary)
# @return users_conncount (dictionary) as described above
#
def get_all_users_conncount(network):
    users_conncount = {}
    # Don't see good way to leverage get_all_users
    for user in network:
        users_conncount[user] = 0
    # Iterate through all users in network
    for user in users_conncount:
        # For each user, iterate through all their connections
        for conn in get_connections(network,user):
            # For each connection entry, increment user's connection count
            users_conncount[conn] += 1
    return users_conncount

##########################################################################
#
# Return statistics for all aspects of data structure
# (User Defined Procedure)
#
# @param network User profile's data structure (dictionary)
# @return stats (dictionary) as described above
#
def get_all_stats(network):
    stats = {}
    stats['user_count'] = len(get_all_users(network))
    stats['connection_count'] = 0
    stats['unique_connection_count'] = 0
    stats['liked_game_count'] = 0
    stats['unique_liked_game_count'] = 0
    uniqueconn = []
    uniquegame = []
    # Iterate through all users in network
    for user in network:
        # For each user, iterate through all their connections
        for conn in get_connections(network,user):
            stats['connection_count'] += 1
            if conn not in uniqueconn:
                uniqueconn.append(conn)
                stats['unique_connection_count'] += 1
        # For each user, iterate through all their liked games
        for game in get_games_liked(network,user):
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


