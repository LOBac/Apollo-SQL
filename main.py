import core.ui
import core.config
import core.utils
import mysql.connector

CONNECTION = 0
CURSOR = 0


def connect_to_server():
    connection_settings = core.config.get_config()['connection']

    conn = mysql.connector.connect(
        user=connection_settings['user'],
        password=connection_settings['password'],
        host=connection_settings['host'],
        port=connection_settings['port'],
        database=connection_settings['database'])

    # Autocommit after change
    conn.autocommit = True

    print('[i] Connected successfully.')
    input('\nPress ENTER to continue.')

    global CONNECTION
    CONNECTION = conn
    CURSOR = CONNECTION.cursor()
    return CURSOR


if __name__ == "__main__":
    settings = core.config.get_config()
    connected_to = ''

    core.ui.print_banner()
    while True:
        try:
            switch = core.ui.print_menu(connected_to)
        except:
            print('\n(!) Please, check your selection.')
            input('\nPress ENTER to continue.')
            continue

        # [1] Connect/disconnect option
        if switch == 1:
            if not connected_to:
                try:
                    print('\n[*] Connecting...')
                    CURSOR = connect_to_server()
                    host = settings['connection']['host']
                    port = settings['connection']['port']
                    user = settings['connection']['user']
                    database = settings['connection']['database']
                    connected_to = f'\n [i] Connected to {host}:{port}.`{database}` as {user}'
                except:
                    print('\n[!] Connection failed.')
                    input('\nPress ENTER to continue.')
            else:
                try:
                    CURSOR.close()
                    connected_to = ''
                    print('\n[i] Disconnected successfully.')
                    input('\nPress ENTER to continue.')
                except:
                    pass

        # [2] Query data function
        elif switch == 2:
            if connected_to == '':
                print('\n[!] Error, no connection was detected.')
                input('\nPress ENTER to continue.')
                continue
            core.utils.show_queries(CURSOR)

        # [3] Insert data function
        elif switch == 3:
            if connected_to == '':
                print('\n[!] Error, no connection was detected.')
                input('\nPress ENTER to continue.')
                continue
            core.utils.insert(CURSOR)

        # [4] Settings option
        elif switch == 4:
            option = 1
            while option != 0:
                option = core.ui.print_settings()
                if option == 0:
                    pass
                elif option != 0 and option < 6:
                    core.config.modify_config(option)
                    # Refresh settings
                    settings = core.config.get_config()
                else:
                    print(f'\n(!) Error, option {option} doesn\'t exist.')
                    input('\nPress ENTER to continue.')

        # [0] Exit execution
        elif switch == 0:
            # Close cursor before exit
            try:
                CURSOR.close()
            except:
                pass
            print('\n[i] Good bye.\n')
            break

        else:
            print(f'\n(!) Error, option {switch} doesn\'t exist.')
            input('\nPress ENTER to continue.')
