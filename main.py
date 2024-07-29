from Downloadandcut import main_downloadandcut
from join import main_join
import os

def print_options_main():
	print("Elija la opcion:")
	print("1 - Descargar video y cortar")
	print("2 - Unificar videos")
	print("3 - Terminar")	

def main():
	array_clips = []

	direction = os.path.dirname(os.path.abspath(__file__))

	if not (os.path.exists("Clips")):
		os.makedirs("Clips")
	
	if not (os.path.exists("Video final")):
		os.makedirs("Video final")
	
	while(true):
		print_options_main()
		option = input()

		if(option == 1):
			array_clips = main_dandc(array_clips, direction)
		
		elif(option == 2):

			print("¿Estas seguro? No podras volver atras")
			
			optionB = input()
			
			print("1 - Si")
			print("2 - No")
			
			if(optionB == 1):
				main_join(array_clips, direction)
				break
		
		elif(option == 3):
			break
		
		else:
			print("Elegista una opcion invalida. Vuelve a elegir")

main()	
