from menu import Menu
from choose_menu import Choose_menu
from levels_menu import Levels_menu
from arcade import Arcade

def main():
    menu = Menu()
    menu.create_menu(Choose_menu())
    menu.run()


if __name__ == '__main__':
    main()