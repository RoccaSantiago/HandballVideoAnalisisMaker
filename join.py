from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

def swap(a,b):
	temp = a
	a = b
	b = temp

def change_order(clipA, clipB, array_clips):
		swap(array_clips[clipA],array_clips[clipB])
		return array_clips

def join_clips(array_clips, direction):
	print("Como desea llamar el video final?")
	name = input()
	clips = [VideoFileClip(video + ".mp4") for video in array_clips]
	final_video = concatenate_videoclips(clips)
	final_video.write_videofile(direction + "Video final/" + name + ".mp4")

def main_join(array_clips,direction):
	
	while(True):
		print("\n==========================================")
		print("El video se unira en el siguiente orden:")
	
		for i in range(0,len(array_clips)):
			print(f"{i} - {array_clips[i]}")
		
		print()
		print("1 - Desea cambiar el orden entre 2 clips?")
		print("2 - Desea cambiar el orden de todos los clips")
		print("3 - No cambiar el orden y unir clips")
			
		option = input()
		
		if (option == '1' ):
			print("Indique el indice del primer clip:")
			clipA = int(input()) - 1 
			print("Indique el indice del segundo clip:")
			clipB = int(input()) - 1
			
			array_clips = change_order(clipA, clipB, array_clips)
		
		if (option == '2'):
			print("Inserte una secuencia de indices separados por un espacio y sin repetidos (eg 2 3 4 1 6 5 7)")

			while(True):
				secuencia = input().split(" ")

				if max(secuencia > len(array_clips)) or len(secuencia) != len(array_clips) or len(secuencia) != len(set(array_clips)):
					print("Dio una secuencia invalida. Vuelva a escribir la secuencia")
			
				else:
					break
			
			for i in range(0,len(secuencia)):
				array_clips[i] = array_clips[secuencia[i]]

		if (option == '3'):
			join_clips(array_clips,direction)
			break
		
 
