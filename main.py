import copy

tiles = []

def i(a):
    return a.split('-')

def verifyState(game):
    for pattern in game:
        if len(pattern) < 3:
            return False
        
        complete = False
        
        if all(tile[0] == pattern[0][0] for tile in pattern) and len(set([tile[1] for tile in pattern])) == len([tile[1] for tile in pattern]):
            complete = True

        temp = [int(tile[0]) - 1 == int(pattern[idx -1][0]) for idx,tile in enumerate(pattern)]
        temp[0] = True

        if all(tile for tile in temp) and all(tile[1] == pattern[0][1] for tile in pattern):
            complete = True

        if not complete: 
            return complete
    return True

def layer(a,b,results,newTiles):
    temp = copy.deepcopy(a)
    state = copy.deepcopy(b)

    for action,tile in [['old',x] for x in temp]+ [['new',x] for x in temp]:
        if action == 'old':
            
            state[-1].append(tile)
        else:
            if len(state[-1]) < 3:
                return
            state.append([tile])
        
        temp.remove(tile)
        if len(temp): 
            if all(tile in newTiles for tile in temp) and verifyState(state):
                results.append(state)
            layer(temp,state,results,newTiles)
        elif verifyState(state):
            results.append(state)

        temp = copy.deepcopy(a)
        state = copy.deepcopy(b)

def newPossibleStates(tiles, newTiles):
    results = []
    state = [0]
    for tile in tiles:
        temp = copy.deepcopy(tiles)
        state[0] = [tile]
        temp.remove(tile)
        layer(temp,state,results, newTiles)
    return results

def solve(newTiles):
    results = newPossibleStates(tiles + newTiles, newTiles)
    def getFlatLength(result):
        length = 0
        for pattern in result:
            length += len(pattern)
        return length

    results.sort(key=getFlatLength, reverse=True)

    print(results[:5])

while True:
    command = input('set, add, check or print (s,a,c,p): ')

    if command == 's':
        data = input('enter a state (/ to cancel): ')
        if data == '/':
            continue
        tiles = data.split(",")
        print(tiles)
    elif command == 'a':
        data = input('enter new tiles (/ to cancel): ')
        if data == '/':
            continue
        tiles = tiles + data.split(",")
        print(tiles)
    elif command == 'p':
        print(tiles)
    elif command == 'c':
        data = input('enter all your tiles (/ to cancel): ')
        if data == '/':
            continue
        solve(data.split(","))

