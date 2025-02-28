import sys

# Define the game world
rooms = {
    'living_room': {
        'description': 'You are in the living room. There is a door to the north and a door to the east.',
        'exits': {'north': 'kitchen', 'east': 'library'},
        'objects': ['sofa', 'tv'],
        'item': 'key'
    },
    'kitchen': {
        'description': 'You are in the kitchen. There is a door to the south and a door to the north.',
        'exits': {'south': 'living_room', 'north': 'pantry'},
        'objects': ['fridge', 'oven'],
        'item': 'knife'
    },
    'library': {
        'description': 'You are in the library. There is a door to the west and a door to the north.',
        'exits': {'west': 'living_room', 'north': 'study'},
        'objects': ['bookshelf', 'desk'],
        'item': 'book'
    },
    'pantry': {
        'description': 'You are in the pantry. There is a door to the south.',
        'exits': {'south': 'kitchen'},
        'objects': ['cans', 'boxes'],
        'item': 'gear'
    },
    'study': {
        'description': 'You are in the study. There is a door to the south and a door to the east.',
        'exits': {'south': 'library', 'east': 'bedroom'},
        'objects': ['computer', 'chair'],
        'item': 'code'
    },
    'bedroom': {
        'description': 'You are in the bedroom. There is a door to the west and a door to the east.',
        'exits': {'west': 'study', 'east': 'bathroom'},
        'objects': ['bed', 'wardrobe'],
        'item': 'gear'
    },
    'bathroom': {
        'description': 'You are in the bathroom. There is a door to the west.',
        'exits': {'west': 'bedroom'},
        'objects': ['shower', 'toilet'],
        'item': 'gear'
    },
    'garden': {
        'description': 'You are in the garden. There is a door to the east and a path to the north.',
        'exits': {'east': 'greenhouse', 'north': 'shed'},
        'objects': ['flowers', 'bench'],
        'item': 'shovel'
    },
    'greenhouse': {
        'description': 'You are in the greenhouse. There is a door to the west.',
        'exits': {'west': 'garden'},
        'objects': ['plants', 'watering can'],
        'item': 'gear'
    },
    'shed': {
        'description': 'You are in the shed. There is a path to the south and a door to the east.',
        'exits': {'south': 'garden', 'east': 'garage'},
        'objects': ['tools', 'lawnmower'],
        'item': 'hammer'
    },
    'garage': {
        'description': 'You are in the garage. There is a door to the west.',
        'exits': {'west': 'shed'},
        'objects': ['car', 'bicycle'],
        'item': 'screwdriver'
    },
    'basement': {
        'description': 'You are in the basement. There is a staircase leading up.',
        'exits': {'up': 'living_room'},
        'objects': ['boxes', 'old furniture'],
        'item': 'crowbar'
    },
    'attic': {
        'description': 'You are in the attic. There is a ladder leading down.',
        'exits': {'down': 'bedroom'},
        'objects': ['old toys', 'dust'],
        'item': 'rope'
    },
    'dining_room': {
        'description': 'You are in the dining room. There is a door to the west and a door to the east.',
        'exits': {'west': 'kitchen', 'east': 'living_room'},
        'objects': ['table', 'chairs'],
        'item': 'plate'
    },
    'hallway': {
        'description': 'You are in the hallway. There is a door to the south and a door to the north.',
        'exits': {'south': 'living_room', 'north': 'guest_room'},
        'objects': ['coat rack', 'mirror'],
        'item': 'hat'
    },
    'guest_room': {
        'description': 'You are in the guest room. There is a door to the south.',
        'exits': {'south': 'hallway'},
        'objects': ['bed', 'nightstand'],
        'item': 'pillow'
    },
    'office': {
        'description': 'You are in the office. There is a door to the east.',
        'exits': {'east': 'living_room'},
        'objects': ['desk', 'computer'],
        'item': 'pen'
    },
    'laundry_room': {
        'description': 'You are in the laundry room. There is a door to the west.',
        'exits': {'west': 'kitchen'},
        'objects': ['washing machine', 'dryer'],
        'item': 'detergent'
    },
    'conservatory': {
        'description': 'You are in the conservatory. There is a door to the north.',
        'exits': {'north': 'garden'},
        'objects': ['plants', 'chair'],
        'item': 'watering can'
    },
    'workshop': {
        'description': 'You are in the workshop. There is a door to the south.',
        'exits': {'south': 'garage'},
        'objects': ['tools', 'workbench'],
        'item': 'tape'
    }
}

# Define the initial state
current_room = 'living_room'
inventory = []
handle_installed = False

def show_room(room):
    print(rooms[room]['description'])
    if 'objects' in rooms[room]:
        print('You see:', ', '.join(rooms[room]['objects']))
    if rooms[room]['item']:
        print(f"You found a {rooms[room]['item']}.")

def get_command():
    command = input('> ')
    return command.lower().strip()

def main():
    global current_room, handle_installed

    print('Welcome to the Escape Game!')
    print('Type "quit" to exit the game.')
    show_room(current_room)

    while True:
        command = get_command()
        
        if command == 'quit':
            print('Thanks for playing!')
            sys.exit()
        
        if command in rooms[current_room]['exits']:
            current_room = rooms[current_room]['exits'][command]
            show_room(current_room)
            if rooms[current_room]['item']:
                inventory.append(rooms[current_room]['item'])
                rooms[current_room]['item'] = None
        elif command == 'inventory':
            print('You have:', ', '.join(inventory))
        elif command == 'install handle' and 'hammer' in inventory and inventory.count('gear') >= 4:
            handle_installed = True
            inventory.remove('hammer')
            for _ in range(4):
                inventory.remove('gear')
            print('You installed the handle on the door.')
        elif command == 'use code' and 'code' in inventory and current_room == 'living_room':
            print('You used the code on the door.')
            inventory.remove('code')
        elif command == 'use key' and 'key' in inventory and current_room == 'living_room':
            print('You used the key to unlock the door.')
            inventory.remove('key')
        elif command == 'open door' and handle_installed and 'key' not in inventory and 'code' not in inventory:
            print('You opened the door and escaped the house! Congratulations!')
            sys.exit()
        else:
            print('You can\'t go that way or perform this action.')

if __name__ == '__main__':
    main()
