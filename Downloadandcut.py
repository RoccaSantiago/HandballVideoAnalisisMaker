from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from cut import main_cut

def print_dandc():
	print("Insete la opcion:")
	print("1 - Descargar video y cortar")
	print("2 - volver")



def download(link):
	yt = YouTube(link)
	stream = yt.streams.filter(progressive = true, file_extension = "mp4").first()
	download_path = strean.download()
	

def main_dandc():
	
	while(true):
		option = input()
		
		if (opcion == 1):
			print("Ingrese link a descargar:")
			link = input()
			download(link)
			main_cut()
		else:
			break


