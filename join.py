def change_order(cllpA, clipB, array_clips):
		swap(array_clips[clipA],array_clips[clipB])
		return array_clips

def join_clips(array_clips):
	# joinear los videos y devolverlo en una carpeta resultados

def main_join(array_clips):
	
	while(true):

		print("El video se unira en el siguiente orden:")
	
		for i in range(0,len(array_clips)):
			print(f"{i} - {array_clips[i]}")
		
	
		print("Desea cambiar el orden (entre 2 clips)?")
		print("1 - Si")
		print("2 - No")
			
		option = input()
		
		if (option == 1 ):
			print("Indique el indice del primer clip:")
			clipA = int(input()) - 1 
			print("Indique el indice del segundo clip:")
			clipB = int(input()) - 1
			
			array_clips = change_order(clipA, clipB, array_clips)
		else:
			join_clips(array_clips) 
