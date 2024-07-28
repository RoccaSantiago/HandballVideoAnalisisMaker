from pytube import YouTube
foom moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def print_d&c():
	print("Insete la opcion:")
	print("1 - Descargar video y cortar")
	print("2 - volver")



def download(link):
	yt = YouTube(link)
	stream = yt.streams.filter(progressive = true, file_extension = "mp4").first()
	download_path = strean.download()
	

def main_d&c():
	while(true):
		option = input()
		
		if (opcion == 1):
			print("Ingrese link a descargar:")
			link = input()
			download(link)
			main_cut()
		else:
			break


