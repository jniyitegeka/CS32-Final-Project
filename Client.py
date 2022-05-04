'''Know Your Zodiac Sign___Client'''

from Socket import create_new_socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server



def main():
    

    with create_new_socket() as s:
        s.connect(HOST, PORT)

        while True:
            
            # Grab a guess from the player
            while True:
                try:
                    
                    print('## Know Your Zodiac Sign ##')
                    
                    birthday = input('Input your birthday (e.g: january,01): ').lower()
                    
                    break
                except ValueError:
                    print(' Please try again...input should be january, 01.')

            s.sendall(str(birthday))
            
            zodiac_character= s.recv()
            print(zodiac_character)

            #if response == 'Exactly! You win!':
            # break

if __name__ == '__main__':
    main()
