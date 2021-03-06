'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def relationship_status(from_member, to_member, social_graph):
    
    info = social_graph.get(from_member)
    follow = info['following']
        
    info2 = social_graph.get(to_member)
    follow2 = info2['following']
    
    if to_member in follow:
        status = 'follower'
    
    elif from_member in follow2:
        status = 'followed'
        
    else:
        status = 'no relationship'
        
    if (to_member in follow) and (from_member in follow2):
            status = 'friends'
    
    return status


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def tic_tac_toe(board):
    
    checker = []
    
    if len(board) == 3:
        for i in range(3):
            checker.append(board[i][0] + board[i][1] + board[i][2])
        for i in range(3):
            checker.append(board[0][i] + board[1][i] + board[2][i])
        checker.append(board[0][0] + board[1][1] + board[2][2])
        checker.append(board[0][2] + board[1][1] + board[2][0])
    
        if 'XXX' in checker:
            winner = 'X'
        elif 'OOO' in checker:
            winner = 'O'
        else:
            winner = 'NO WINNER'
    
    elif len(board) == 4:
        for i in range(4):
            checker.append(board[i][0] + board[i][1] + board[i][2] + board[i][3])
        for i in range(4):
            checker.append(board[0][i] + board[1][i] + board[2][i] + board[3][i])
        checker.append(board[0][0] + board[1][1] + board[2][2] + board[3][3])
        checker.append(board[0][3] + board[1][2] + board[2][1] + board[3][0])
        
        if 'XXXX' in checker:
            winner = 'X'
        elif 'OOOO' in checker:
            winner = 'O'
        else:
            winner = 'NO WINNER'
            
    elif len(board) == 5:
        for i in range(5):
            checker.append(board[i][0] + board[i][1] + board[i][2] + board[i][3] + board[i][4])
        for i in range(5):
            checker.append(board[0][i] + board[1][i] + board[2][i] + board[3][i] + board[4][i])
        checker.append(board[0][0] + board[1][1] + board[2][2] + board[3][3] + board[4][4])
        checker.append(board[0][4] + board[1][3] + board[2][2] + board[3][1] + board[4][0])
        
        if 'XXXXX' in checker:
            winner = 'X'
        elif 'OOOOO' in checker:
            winner = 'O'
        else:
            winner = 'NO WINNER'
    
    elif len(board) == 6:
        for i in range(6):
            checker.append(board[i][0] + board[i][1] + board[i][2] + board[i][3] + board[i][4] + board[i][5])
        for i in range(5):
            checker.append(board[0][i] + board[1][i] + board[2][i] + board[3][i] + board[4][i] + board[5][i])
        checker.append(board[0][0] + board[1][1] + board[2][2] + board[3][3] + board[4][4] + board[5][5])
        checker.append(board[0][5] + board[1][4] + board[2][3] + board[3][2] + board[4][1] + board[5][0])
        
        if 'XXXXXX' in checker:
            winner = 'X'
        elif 'OOOOOO' in checker:
            winner = 'O'
        else:
            winner = 'NO WINNER'
    
    return winner

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def eta(first_stop, to_stop, route_map):
    travel_times = [route_map[list(route_map.keys())[0]]["travel_time_mins"]]
    travel_route = [list(route_map.keys())[0][0]]
    next_stop = list(route_map.keys())[0][1]
    sample_map = route_map.copy()
    sample_map.pop(list(route_map.keys())[0])
    while len(sample_map) != 0:
        for n in sample_map.copy():
            if n[0] == next_stop:
                travel_times.append(sample_map[n]["travel_time_mins"])
                travel_route.append(n[0])
                next_stop = n[1]
                sample_map.pop(n)
    first_stop = travel_route.index(first_stop)
    to_stop = travel_route.index(to_stop)
    time = 0
    if to_stop < first_stop:
        for travel_time in travel_times[first_stop:]:
            time = time + travel_time
        for travel_time in travel_times[0:to_stop]:
            time = time + travel_time
    else:
        for travel_time in travel_times[first_stop:to_stop]:
            time = time + travel_time
    return time
