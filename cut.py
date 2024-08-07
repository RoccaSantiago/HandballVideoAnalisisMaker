from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import sys

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_cut(counter):
    clear_console()
    print("Inserte la opción:")
    print("1 - Cortar otro clip" if counter > 1 else "1 - Cortar clip")
    print("2 - Volver\n")

def cut(start_time, end_time, name, download_path, direction):
    output = os.path.join(direction, "Clips", f"{name}.mp4")
    
    # Redirigir la salida estándar y de error para suprimir los mensajes de ffmpeg
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

def main_cut(download_path, array_clips, direction):
    counter = 1
    while True:
        print_cut(counter)
        option = input()
        
        if option == '1':
            clear_console()
            print(f"Clip {counter}")
            name = input("Inserte el nombre del clip:\n\n")
            
            while name in array_clips:
                name = input("Ese nombre ya existe. Inserte otro:\n")
            
            array_clips.append(name)
            
            start_time = input("Inserte en qué minuto y segundos arranca el clip separado por un espacio (ej. 1 24): \n\n").split()
            start_time = int(start_time[0]) * 60 + int(start_time[1])

            end_time = input("Inserte en qué minuto y segundos termina el clip separado por un espacio (ej. 1 24): \n\n").split()
            end_time = int(end_time[0]) * 60 + int(end_time[1])

            cut(start_time, end_time, name, download_path, direction)
            counter += 1

        elif option == '2':
            break
        
        else:
            print("Elegiste una opción inválida. Vuelve a elegir.")
