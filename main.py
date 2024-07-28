def print_options_main():
	print("Elija la opcion:")
	print("1 - Descargar video y cortar")
	print("2 - Unificar videos")
	print("3 - Terminar")	

def main():
	array_clips = []
	while(true):
		print_options_main()
		option = input()

		if(option == 1):
			array_clips = main_download&cut(array_clips)
		elif(option == 2):
			main_join(array_clips)
			break
		elif:(option == 3):
			break
		else:
			print("Elegista una opcion invalidad. Vuelve a elegir")

	
