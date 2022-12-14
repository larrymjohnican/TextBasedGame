# Larry Johnican
# function showing the goal of the game and move commands
def show_instructions():
    # print a main menu and the commands
    print('\nWelcome to Dragonball Z Text Adventure Game!\n')
    print('Collect the 8 items to win the game, or be defeated by the vile Frieza.')
    print('Move commands: Go South, Go North, Go East, Go West')
    print("Add to Inventory: get 'item")


# A dictionary linking a room to other rooms
# and linking one item for each room except the Start room (West City) and the room containing the villain
rooms = {
    'West City': {'name': 'West City', 'South': "King Kai's Planet", 'North': "Korin's Tower", 'East': 'Spaceship',
                  'West': 'Kame House',
                  'item': 'Flying Nimbus'},
    "King Kai's Planet": {'name': "King Kai's Planet", 'North': 'West City', 'East': 'Heaven', 'item': 'Kaioken'},
    'Kame House': {'name': 'Kame House', 'West': 'West City', 'item': 'Kamehameha'},
    "Korin's Tower": {'name': "Korin's Tower", 'South': 'West City', 'item': 'Senzu Bean', 'East': 'The Lookout'},
    'The Lookout': {'name': 'The Lookout', 'West': "Korin's Tower", 'item': 'Dragon Ball'},
    'Heaven': {'name': 'Heaven', 'West': "King Kai's Planet", 'item': 'Armor'},
    'Spaceship': {'name': 'Spaceship', 'North': 'Namek', 'item': 'Super Saiyan'},
    'Namek': {'name': 'Namek', 'South': 'Spaceship', 'item': 'Frieza!'},  # villain encounter
    'Exit': {'name': 'Exit'}
}

global current_room
current_room = 'West City'  # start room
global inventory
inventory = []
show_instructions()


def player_status():
    global current_room
    global inventory
    # printing player status
    print('You are in the {}'.format(current_room))
    # print('Inventory: ' + str(inventory))
    if 'item' in rooms[current_room]:
        print('Inventory:' + rooms[current_room]['item'])


def player_status():
    global current_room
    global inventory
    # printing player status
    print('You are in the {}'.format(current_room))
    # print('Inventory: ' + str(inventory))
    if 'item' in rooms[current_room]:
        print('Inventory:' + rooms[current_room]['item'])


def main():
    global current_room
    global inventory
    player_status()
    command = ''
    while command == '':
        command = input('\nIn what direction would you like to go?').title()
    if command == 'player status':
        print(player_status())
    if command == 'Go North' or command == 'Go South' or command == 'Go East' or command == 'Go West':
        command = command[3:]
        if command not in rooms[current_room]:
            print('Invalid direction. Try again.')
        else:
            current_room = rooms[current_room][command]
    elif command[0:3].lower() == 'get':
        if command[4:] in rooms[current_room]['item']:
            inventory += [command[4:]]
            print(command[4:] + ' retrieved!')
            del rooms[current_room]['item']
        else:
            print('Can\'t get {}!'.format(command[4:]))

    # function for ending the game
    if current_room == 'Namek':
        # you lose
        print('Oh, No! You did not acquire all of the items')
        exit(0)

    if len(inventory) == 8:
        # you win
        print('Congratulations! You have collected all items to defeat the vile villain '
              'Frieza!')


while True:
    main()
