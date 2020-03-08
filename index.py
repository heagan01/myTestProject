import pickle

pickle_in = open('data.p', 'rb')
f = pickle.load(pickle_in)
numberOfWheatForData = f['numberOfWheat']
numberOfCornForData = f['numberOfCorn']
dataOut = open('data.p', 'wb')
dataIn = open('data.p', 'rb')

data = {
    'numberOfWheat': numberOfWheatForData,
    'numberOfCorn': numberOfCornForData
}

def options():
    global dataOut
    global data
    global numberOfWheatForData
    global numberOfCornForData
    
    print('Options for the game')
    print('\n')
    print('1) Plant Wheat')
    print('2) Plant Corn')
    print('\n')
    
    command = input('Enter in your input: ')
    
    if command == '1':
        numberOfWheatForData += 1
    elif command == '2':
        numberOfCornForData += 1
        
    pickle.dump(data, dataOut)
    
    command = input('Press enter to exit: ')
    
options()