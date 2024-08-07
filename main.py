from Downloadandcut import main_dandc
from join import main_join
import os

direction = os.path.dirname(os.path.abspath(__file__))

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def print_options_main():
    clear_console()
    print("Elija la opcion:")
    print("1 - Descargar video y cortar")
    print("2 - Unificar videos")
    print("3 - Terminar\n")	

def create_and_clean_folder(folder_name):
    folder_path = os.path.join(direction, folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

def main():
    direction = os.path.dirname(os.path.abspath(__file__))
    
    array_clips =  []
    
    create_and_clean_folder("Clips")
    create_and_clean_folder("Videos Enteros")
    create_and_clean_folder("Video Final")

    while True:
        print_options_main()
        option = input()

        if option == '1':
            array_clips = main_dandc(array_clips, direction)
        elif option == '2':
            clear_console()
            confirm = input("¿Estás seguro? No podrás volver atrás\n1 - Sí\n2 - No\n")
            if confirm == '1':
                main_join(array_clips, direction)
                break
        elif option == '3':
            break
        else:
            print("Elegiste una opción inválida. Vuelve a elegir")


if __name__ == "__main__":
    main()	