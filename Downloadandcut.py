from pytubefix import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from cut import main_cut
import sys


def print_dandc():
	print("Insete la opcion:")
	print("1 - Descargar video y cortar")
	print("2 - volver")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    sys.stdout.write(f"\rDescargando... {percentage_of_completion:.2f}%")
    sys.stdout.flush()

def download(link, direction):
	yt = YouTube(link,on_progress_callback= on_progress)
	stream =  yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
	return stream.download(output_path= (direction + "\Videos enteros"))
	

def main_dandc(array_clips, direction):
	
	while(True):
		print_dandc()
		option = input()
		
		if (option == '1'):
			print("Ingrese link a descargar:")
			link = input()
			main_cut(download(link,direction), array_clips, direction)

		elif (option == '2' ):
			break
		
		else:
			print("Elegista una opcion invalida. Vuelve a elegir")

	return array_clips