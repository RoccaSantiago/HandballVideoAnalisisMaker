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
	return strean.download()
	

def main_dandc(array_clips, direction):
	
	while(true):
		option = input()
		
		if (option == 1):
			print("Ingrese link a descargar:")
			link = input()
			main_cut(download(link), array_clips, direction)

		elif (option == 2 ):
			break
		
		else:
			print("Elegista una opcion invalida. Vuelve a elegir")



