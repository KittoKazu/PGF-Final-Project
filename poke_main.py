import poke_menu as menu

def main():
    menu.display_menu()
    subsystem_input = menu.get_func_input()
    menu.run_subsystem(subsystem_input)

if __name__ == '__main__':
    main()
