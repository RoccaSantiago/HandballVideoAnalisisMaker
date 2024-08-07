from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import sys

def get_directory():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

direction = get_directory()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def join_clips(array_clips, direction):
    clear_console()
    name = input("¿Cómo desea llamar el video final?\n\n")
    
    direction_clips = os.path.join(direction, "Clips")
    direction_video = os.path.join(direction, "Video Final")
    
    clips = []
    for video in array_clips:
        video_path = os.path.join(direction_clips, f"{video}.mp4")
        clips.append(VideoFileClip(video_path))
    
    final_video = concatenate_videoclips(clips)
    
    final_video.write_videofile(os.path.join(direction_video, f"{name}.mp4"))

def main_join(array_clips, direction):
    while True:
        clear_console()
          
        print("El video se unirá en el siguiente orden:")
        
        for i, clip in enumerate(array_clips):
            print(f"{i} - {clip}")
        
        print("\n1 - Cambiar el orden")
        print("2 - No cambiar el orden y unir clips\n")
            
        option = input()
        
        if option == '1':
            while True:
                sequence = input("Inserte una secuencia de índices separados por un espacio y sin repetidos (ej. 2 3 4 1 6 5 7)\n\n").split()
                sequence = [int(i) for i in sequence]
                
                if (max(sequence) > len(array_clips) or 
                    len(sequence) != len(array_clips) or 
                    len(set(sequence)) != len(array_clips)):
                    print("Secuencia inválida. Por favor, intente de nuevo.")
                else:
                    break
            
            array_clips = [array_clips[i] for i in sequence]

        elif option == '2':
            join_clips(array_clips, direction)
            break

        else:
            print("Opción inválida. Por favor, intente de nuevo.")
