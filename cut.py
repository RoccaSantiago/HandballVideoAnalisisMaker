from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import sys

def print_cut(counter):
	print(" \n Inserte la opcion:")
	if (counter > 1):
		print("1 - Cortar otro clip")
	else:
		print("1 - Cortar clip")
	print("2 - volver")


def cut(start_time, end_time, name, download_path, direction):
    output = os.path.join(direction, "Clips", name + ".mp4")
    
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w')

    try:
        ffmpeg_extract_subclip(download_path, start_time, end_time, targetname=output)
    finally:
        sys.stdout.close()
        sys.stderr.close()
        sys.stdout = original_stdout
        sys.stderr = original_stderr

def main_cut(download_path,array_clips, direction):
	counter = 1
	while(True):
		print_cut(counter)
		option = input()
		
		if (option == '1'):
			print("Clip " + str(counter))
			print("Inserte el nombre del clip")
			
			while(True):
				name = input()
				if name in array_clips:
					print("Ese nombre ya existe. Inserte otro")
				else:
					break
			
			array_clips.append(name)
			
			print("Inserte en que minuto y segundos arranca el clip separado por un espacio (eg 1 24)")
			start_time = input().split(" ")
			start_time = int(start_time[0]) * 60 + int(start_time[1])


			print("Inserte en que minuto y segundos termina el clip separado por un espacio (eg 1 24)")
			end_time = input().split(" ")
			end_time = int(end_time[0]) * 60 + int(end_time[1])
			print(end_time)

			cut(start_time, end_time, name, download_path, direction)
			
			counter+=1
			 
		elif (option == '2'):
			break
		
		else:
			print("Elegista una opcion invalida. Vuelve a elegir")
		