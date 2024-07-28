from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def print_cut(counter):
	print("Insete la opcion:")
	if (counter >= 1):
		print("1 - Cortar otro clip")
	else:
		print("1 - Cortar clip")
	print("2 - volver")

def cut(start_time, end_time,name, download_path):
	output = ".\clips\ " & name & ".mp4"
	ffmpeg_extract_subclip(download_path, start_time, end_time, targetname = output)

def main_cut(download_path,array_clips):
	counter = 0
	while(true):
		print_cut(counter)
		option = input()
		
		if (option == 1):
			print("Clip " + i)
			print("Inserte el nombre del clip")
			name = input()
			array_clips.append(name)
			
			print("Inserte en que minuto (sin segundos) arrancara el clip:")
			start_time = int(input()) * 60
			print("Inserte en que segundos arrancara el clip:)
			start_time += int(input)
			
			print("Inserte en que minuto (sin segundos) terminara el clipo")
			end_time = int(input()) * 60
			print("Inserte en que segundos terminara el clip:)
			end_time += int(input)

			cut(start_time, end_time, name, download_path)
			
			counter+=1
			 
		else:
			break