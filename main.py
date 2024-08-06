from Downloadandcut import main_dandc
from join import main_join
import os

direction = os.path.dirname(os.path.abspath(__file__))

def print_options_main():
	print("Elija la opcion:")
	print("1 - Descargar video y cortar")
	print("2 - Unificar videos")
	print("3 - Terminar")	

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
	array_clips = []

	create_and_clean_folder("Clips")
	create_and_clean_folder("Video Final")
	create_and_clean_folder("Videos Enteros")
					
	while(True):
		print_options_main()
		option =input()

		if(option == '1'):
			array_clips = main_dandc(array_clips, direction)
		
		elif(option == '2'):

			print("¿Estas seguro? No podras volver atras")
			print("1 - Si")
			print("2 - No")

			optionB = input()
			
	
			if(optionB == '1'):
				main_join(array_clips, direction)
				break
		
		elif(option == '3'):
			break
		
		else:
			print("Elegista una opcion invalida. Vuelve a elegir")

main()	
