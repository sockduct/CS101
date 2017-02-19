###########################################################################
#
# Testing for finalproject
#
###########################################################################
#
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
mynet = add_new_user(mynet,'Robin',['City Comptroller','Top Secret'],True)  # Try to add existing user
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
mynet2 = add_connection(mynet,'dne','Dynamo',True)  # Try to add connection to non-existent user
print mynet
mynet2 = add_connection(mynet,'TNT','dne',True)  # Try to add non-existent connection to user
print mynet
mynet2 = add_connection(mynet,'dne','dne',True)  # Try to add non-existent connection to non-existent user
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
print connections_in_common(mynet,'NoConnsNoGames','dne',True)  # 1st user has no connections, 2nd doesn't exist
print connections_in_common(mynet,'dne','NoConnsNoGames',True)  # 1st user doesn't exit, 2nd user has no connections
print connections_in_common(mynet,'dne1','dne2',True)  # 1st user doesn't exit, 2nd user doesn't exist
print connections_in_common(mynet,'Robin','John')  # Users have no connections in common
print connections_in_common(mynet,'John','Mercedes')  # Users have connections in common
print connections_in_common(mynet,'John','Bryant')  # Users have no connections in common
#
# Test path_to_friend
print path_to_friend(mynet,'NoConnsNoGames','NoConnsNoGames')  # Users have no connections
print path_to_friend(mynet,'NoConnsNoGames','dne',True)  # 1st user has no connections, 2nd doesn't exist
print path_to_friend(mynet,'dne','NoConnsNoGames',True)  # 1st user doesn't exit, 2nd user has no connections
print path_to_friend(mynet,'dne1','dne2',True)  # 1st user doesn't exit, 2nd user doesn't exist
print path_to_friend(mynet,'Robin','John')  # Users have no connections in common
print path_to_friend(mynet,'John','Mercedes')  # Users have connections in common
print path_to_friend(mynet,'John','Bryant')  # Users have no connections in common
print path_to_friend(mynet,'TNT','NoConnsNoGames')  # Users have no connections in common
#
#
# Test user defined procedures
#
# Test add_game_liked
mynet2 = add_game_liked(mynet,'TNT','Pac Man')  # Add new game to existing user
mynet2 = add_game_liked(mynet,'TNT','',True)  # Add new game to existing user
print mynet2
mynet22 = add_game_liked(mynet,'dne','Pac Man',True)  # Add new game for user that doesn't exist
print mynet2
mynet22 = add_game_liked(mynet,'TNT','Pac Man',True)  # Add game already in user's list
print mynet2
#
# More procedures
print get_all_games_liked(mynet)
#
chart_all_games_liked(mynet)
#
print get_all_users(mynet)
#
print get_all_users_conncount(mynet)
#
chart_all_users_conncount(mynet)
#
print get_all_stats(mynet)

