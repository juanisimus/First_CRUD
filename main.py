import sys
clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software Engineer'
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer'
    }
]

def create_client(client):
    global clients
    if client_name not in clients:
        # clients += client_name
        # _add_coma()
        clients.append(client_name)
    else:
        print('Client already in the client\'s list')


def list_clients():
    for idx, client in enumerate(clients):
        print(f'{idx}: {client}')
    # global clients
    


def update_client(client_name, update_client_name):
    global clients
    if client_name in clients:
        # clients = clients.replace(client_name + ',', update_client_name + ',')
        index = clients.index(client_name)
        clients[index] = update_client_name
    else:
        print('Client is not in client\'s list')


def delete_client(client_name):
    global clients
    if client_name in clients:
        # clients = clients.replace(client_name + ',', '')
        clients.remove(client_name)
    else:
        print('Client is not in client\'s list')


def search_client(client_name):
    # client_list = clients.split(',')
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


# def _add_coma():
#     global clients
#     clients += ','


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?: ')
    print('[C] Create client')
    print('[U] Update client')
    print('[D] Delete client')
    print('[S] Search client')


def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name?: ')
        if client_name == 'exit':
            client_name = None
            break
    if not client_name:
        sys.exit()
    return client_name


if __name__ == "__main__":
    _print_welcome()
    command = input()
    command = command.upper()
    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
        
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()

    elif command == 'U':
        
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name?: ')
        update_client(client_name, update_client_name)
        list_clients()

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('The client is in the list')
        else:
            print(f'The client {client_name} is not in the list')

    else:
        print('Invalid command')
    
    
    
    