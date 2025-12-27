import os
import time
import subprocess
import urllib.request
import json
import sys
import shutil
import zipfile
import requests
from itertools import cycle
import re

def addon():
    filename = "addons/SingUtils.addon"
    url = "https://www.dropbox.com/scl/fo/4qcikzxe7qlzl5bl18wnb/ANnsGn9NBIIAoDN3iEkRewk?rlkey=iksm74uv2d7axi2od75m74lm1&st=t0vrg4mh&dl=1"
    temp_zip = "addons/temp.zip"  
    with open(filename, "r") as file:
        content = file.read()
    if "a_version 1.3" not in content:
        response = requests.get(url)
        with open(temp_zip, "wb") as file:
            file.write(response.content)
        with zipfile.ZipFile(temp_zip, "r") as zip_ref:
            zip_ref.extractall("addons") 
            extracted_files = zip_ref.namelist()
            for file_name in extracted_files:
                if file_name.endswith("SingUtils.addon"):
                    os.rename(os.path.join("addons", file_name), filename)
        os.remove(temp_zip)
        files = os.listdir('.')
        python_files = [file for file in files if file.endswith(".py")]
        for python_file in python_files:
                file_path = os.path.join('.', python_file)
                subprocess.run(['python', file_path])
addon()


def run_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘


def eldirewe():
    real_path = os.path.realpath(os.getcwd())
    while not os.path.exists(os.path.join(real_path, ".git")) and real_path != "/":
        real_path = os.path.dirname(real_path)
    if os.path.exists(os.path.join(real_path, ".git")):
        return real_path
    else:
        raise FileNotFoundError("ta ta ta")

def eldire():
    os.chdir(eldirewe())



def generate_gradient(color1, color2, steps):
    gradient = []
    for i in range(steps):
        r = int(color1[0] + (color2[0] - color1[0]) * (i / steps))
        g = int(color1[1] + (color2[1] - color1[1]) * (i / steps))
        b = int(color1[2] + (color2[2] - color1[2]) * (i / steps))
        gradient.append((r, g, b))
    return gradient

def gradient_text(text, gradient, fixed_colors=None):
    colored = []
    gradient_cycle = cycle(gradient)
    for char in text:
        if fixed_colors and char in fixed_colors:
            r, g, b = fixed_colors[char]
            colored.append(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
        elif char == ' ':
            colored.append(char)
        else:
            r, g, b = next(gradient_cycle)
            colored.append(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
    return ''.join(colored)

def printsito(text, gradient, speed=0.005, fixed_colors=None, highlight_segments=None):
    sys.stdout.write("\033[?25l")
    gradient_cycle = cycle(gradient)
    i = 0
    while i < len(text):
        matched = False
        if highlight_segments:
            for segment, color in highlight_segments.items():
                if text[i:i+len(segment)] == segment:
                    r, g, b = color
                    sys.stdout.write(f"\033[38;2;{r};{g};{b}m{segment}\033[0m")
                    sys.stdout.flush()
                    time.sleep(speed * len(segment))
                    i += len(segment)
                    matched = True
                    break
        if not matched:
            char = text[i]
            if fixed_colors and char in fixed_colors:
                r, g, b = fixed_colors[char]
                sys.stdout.write(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
            elif char == ' ':
                sys.stdout.write(char)
            else:
                r, g, b = next(gradient_cycle)
                sys.stdout.write(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
            sys.stdout.flush()
            time.sleep(speed)
            i += 1
    sys.stdout.write("\033[?25l\n")


def inputsito(prompt, gradient, speed=0.005, fixed_colors=None, highlight_segments=None):
    sys.stdout.write("\033[?25l")
    gradient_cycle = cycle(gradient)
    i = 0
    while i < len(prompt):
        matched = False
        if highlight_segments:
            for segment, color in highlight_segments.items():
                if prompt[i:i+len(segment)] == segment:
                    r, g, b = color
                    sys.stdout.write(f"\033[38;2;{r};{g};{b}m{segment}\033[0m")
                    sys.stdout.flush()
                    time.sleep(speed * len(segment))
                    i += len(segment)
                    matched = True
                    break
        if not matched:
            char = prompt[i]
            if fixed_colors and char in fixed_colors:
                r, g, b = fixed_colors[char]
                sys.stdout.write(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
            elif char == ' ':
                sys.stdout.write(char)
            else:
                r, g, b = next(gradient_cycle)
                sys.stdout.write(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
            sys.stdout.flush()
            time.sleep(speed)
            i += 1
    sys.stdout.write("\033[?25l\n")
    return input()

def inputsito_2(prompt, gradient, speed=0.005, fixed_colors=None):
    sys.stdout.write("\033[?25l")
    gradient_cycle = cycle(gradient)

    for char in prompt:
        if fixed_colors and char in fixed_colors:
            r, g, b = fixed_colors[char]
            sys.stdout.write(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
        elif char == ' ':
            sys.stdout.write(char)
        else:
            r, g, b = next(gradient_cycle)
            sys.stdout.write(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\033[?25h")
    return input()

def animacion_actualizacion(gradient, anim_symbols="◝◞◟◜", text=" ⎹ Actualizando versiones...", updated_text="✔ ⎹ Versiones actualizadas!", typing_speed=0.005, animation_speed=0.1, duration=5, fixed_colors=None):
    full_text = f"{anim_symbols[0]} {text}"
    sys.stdout.write("\033[?25l")
    for i, char in enumerate(full_text):
        if fixed_colors and char in fixed_colors:
            r, g, b = fixed_colors[char]
            sys.stdout.write(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
        elif char == ' ':
            sys.stdout.write("\033[?25l")
            sys.stdout.write(char)
            sys.stdout.write("\033[?25l")
        else:
            r, g, b = gradient[i % len(gradient)]
            sys.stdout.write(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()
        time.sleep(typing_speed)
    sys.stdout.write("\033[?25l")
    sys.stdout.write("\r")

    start_time = time.time()
    idx = 0
    while time.time() - start_time < duration:
        symbol = anim_symbols[idx % len(anim_symbols)]
        idx += 1
        animated_text = f"{symbol} {text}"
        colored_text = gradient_text(animated_text, gradient, fixed_colors=fixed_colors)
        sys.stdout.write("\033[?25l")
        sys.stdout.write(f"\r{colored_text}")
        sys.stdout.flush()
        time.sleep(animation_speed)

    sys.stdout.write("\r" + " " * len(full_text) + "\r")
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()
    updated_colored_text = gradient_text(updated_text, gradient, fixed_colors=fixed_colors)
    sys.stdout.write(f"{updated_colored_text}\n")
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def mostrar_progreso(duracion=10, longitud=15, gradient=None):
    sys.stdout.write("\033[?25l")

    if not gradient:
        c1 = (69, 255, 75)
        c2 = (69, 255, 75)
        c3 = (69, 255, 75)
        gradient_1 = generate_gradient(c1, c2, 70)
        gradient_2 = generate_gradient(c2, c3, 30)
        gradient = gradient_1 + gradient_2

    try:
        pasos = int(duracion * 10)
        for i in range(pasos + 1):
            progreso = int((i / pasos) * longitud)
            barra = '━' * progreso + '═' * (longitud - progreso)
            barra_colorida = gradient_text(barra, gradient)
            sys.stdout.write(f"\r{barra_colorida}")
            sys.stdout.flush()
            time.sleep(duracion / pasos)
        sys.stdout.write("\n")
    finally:
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

def download_file(url, dest_folder):
    current_dir = os.getcwd()
    os.chdir(current_dir)
    c1 = (5, 81, 181)
    c2 = (255, 236, 209)
    c3 = (5, 81, 181)
    ssm = 20
    sme = 10
    gradient1 = generate_gradient(c1, c2, ssm)
    gradient2 = generate_gradient(c2, c3, sme)
    full_gradient = gradient1 + gradient2
    fixed_colors = {"🡻": (255, 236, 209),}
    printsito("🡻‎⎹ Descargando archivos...", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    mostrar_progreso(duracion=5, longitud=27)
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    local_filename = os.path.join(dest_folder, url.split('/')[-1])
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def extract_zip_file(zip_path, extract_to):
    os.system('clear')
    current_dir = os.getcwd()
    os.chdir(current_dir)
    c1 = (5, 81, 181)
    c2 = (255, 236, 209)
    c3 = (5, 81, 181)
    ssm = 20
    sme = 10
    gradient1 = generate_gradient(c1, c2, ssm)
    gradient2 = generate_gradient(c2, c3, sme)
    full_gradient = gradient1 + gradient2
    fixed_colors = {"⎙": (255, 236, 209),}
    printsito("⎙ ⎹ Extrayendo modpack...", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    mostrar_progreso(duracion=5, longitud=25)
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def move_files(src_folder, dest_folder, required_folders=None):    
    os.system('clear')
    current_dir = os.getcwd()
    os.chdir(current_dir)
    c1 = (5, 81, 181)
    c2 = (255, 236, 209)
    c3 = (5, 81, 181)
    ssm = 20
    sme = 10
    gradient1 = generate_gradient(c1, c2, ssm)
    gradient2 = generate_gradient(c2, c3, sme)
    full_gradient = gradient1 + gradient2
    fixed_colors = {"⎘": (255, 236, 209),}
    printsito("⎘ ⎹ Moviendo archivos del modpack...", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    mostrar_progreso(duracion=5, longitud=36)
    if required_folders and all(os.path.exists(os.path.join(src_folder, folder)) for folder in required_folders):
        dest_folder = os.path.join(dest_folder, required_folders[0])
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

    for item in os.listdir(src_folder):
        s = os.path.join(src_folder, item)
        d = os.path.join(dest_folder, item)
        if os.path.exists(d):
            if os.path.isdir(d):
                shutil.rmtree(d)
            else:
                os.remove(d)
        if os.path.isdir(s):
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)        


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘


def download_modpack():
    os.system('clear')
    time.sleep(1)

    eldire()

    c1 = (5, 81, 181)
    c2 = (255, 236, 209)
    c3 = (5, 81, 181)

    ssm = 25
    sme = 10

    gradient1 = generate_gradient(c1, c2, ssm)
    gradient2 = generate_gradient(c2, c3, sme)
    full_gradient = gradient1 + gradient2

    highlight_color = (100, 100, 100)
    highlight_segments = {"https://www.youtube.com/watch?v=3768Yomkfow": highlight_color}
    
    fixed_colors = {
        "◰": (255, 236, 209),
        "➜": (255, 69, 69),
        "⏎": (255, 236, 209),              
    }
    printsito("◰ ⎹ Instalacion de Modpack", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    printsito("➜ ⎹ Si no sabés utilizar esta opción mirá: https://www.youtube.com/watch?v=3768Yomkfow", full_gradient, speed=0.005, fixed_colors=fixed_colors, highlight_segments=highlight_segments)
    printsito("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    inputsito("⏎ ⎹ Si ya lo miraste apretá Enter para continuar", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    os.system('clear')
    
    while True:        
        fixed_colors = {
        "☰": (255, 236, 209),
        "⚠": (250, 214, 80),
        "➥": (255, 236, 209),        
        "❱": (143, 255, 219),
        "✔": (255, 236, 209),
        "⏎": (255, 236, 209),
        "⇁": (255, 0, 0),
        "↼": (255, 0, 0),
        "❮": (255, 236, 209),
        "❰": (255, 236, 209),
        "㊀": (255, 134, 56),
        "✖": (255, 69, 69),                
        }  
        highlight_color = (255, 69, 69)
        highlight_segments = {"𝗦𝗘𝗥𝗩𝗘𝗥 𝗣𝗔𝗖𝗞": highlight_color}
        printsito("☰ ⎹ Server Pack URL", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("⚠ ⎹ Acordate que debe ser el URL del 𝗦𝗘𝗥𝗩𝗘𝗥 𝗣𝗔𝗖𝗞 del Modpack que vayas a instalar", full_gradient, speed=0.005, fixed_colors=fixed_colors, highlight_segments=highlight_segments)
        printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        url = inputsito_2("➥ ⎹ Ingresá la URL del Modpack ❱ ", full_gradient, speed=0.005, fixed_colors=fixed_colors).strip()    
        if url == '':
            printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            printsito("㊀⎹ No dejés el campo vacío, ingresá una URL.", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            time.sleep(4)
            os.system('clear')
            continue
        if not url.startswith("https://"):
            printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            printsito("✖ ⎹ Ingresá una URL válida.", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            time.sleep(4)
            os.system('clear')
            continue
        break
    
    download_folder = "descargas"
    temp_extract_folder = os.path.join(download_folder, "temp_extract")
    dest_folder = "servidor_minecraft"

    # descarga y extrae
    os.system('clear')
    zip_path = download_file(url, download_folder)
    extract_zip_file(zip_path, temp_extract_folder)

    # manejar archivos segn la estrutura de carpetas
    os.system('clear')
    if len(os.listdir(temp_extract_folder)) == 1:
        move_files(os.path.join(temp_extract_folder, os.listdir(temp_extract_folder)[0]), dest_folder)
    elif any(folder in os.listdir(temp_extract_folder) for folder in ["data", "bStats"]):
        move_files(temp_extract_folder, dest_folder, ["data", "bStats"])
    else:
        move_files(temp_extract_folder, dest_folder)

    # limpia, como toda mujer
    shutil.rmtree(temp_extract_folder)
    os.remove(zip_path)
    if os.path.isdir(download_folder):
        os.rmdir(download_folder)

    os.system('clear')
    printsito("✔ ⎹ Modpack Instalado!", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    printsito("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    highlight_color = (110, 33, 252)
    highlight_segments = {"MSX": highlight_color}
    fixed_colors = {"⏎": (255, 236, 209), "❰": (255, 236, 209), "❮": (255, 236, 209),}
    inputsito("⏎ ⎹ Apretá enter para volver al menú de MSX", full_gradient, speed=0.005, fixed_colors=fixed_colors, highlight_segments=highlight_segments)
    os.system('clear')
    highlight_color = (110, 33, 252)
    highlight_segments = {"MSX...": highlight_color}
    printsito("❰❮⎹ Saliendo al menu de MSX...", full_gradient, speed=0.005, fixed_colors=fixed_colors, highlight_segments=highlight_segments)
    time.sleep(3)

    
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘


def fabric_ver():
    os.system('clear')

    current_dir = os.getcwd()
    
    install_dir = "servidor_minecraft"
    if not os.path.exists(install_dir):
        os.makedirs(install_dir)

    c1 = (5, 81, 181)
    c2 = (255, 236, 209)
    c3 = (5, 81, 181)

    ssm = 25
    sme = 10

    gradient1 = generate_gradient(c1, c2, ssm)
    gradient2 = generate_gradient(c2, c3, sme)
    full_gradient = gradient1 + gradient2

    while True:
        fixed_colors = {
        "↹": (255, 236, 209),
        "⚠": (250, 214, 80),
        "➥": (255, 236, 209),
        "❱": (152, 227, 203),
        "↺": (255, 236, 209),
        "㊀": (255, 134, 56),
        "✖": (255, 69, 69),
        "☑": (255, 236, 209),
        "◝": (255, 236, 209),
        "◞": (255, 236, 209),
        "◟": (255, 236, 209),
        "◜": (255, 236, 209),
        "✔": (255, 236, 209),
        }
        printsito("↹ ⎹ Cambiar versión de Fabric", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        mc_version = inputsito_2("➥ ⎹ Ingresá la versión de Minecraft que querés instalar ❱ ", full_gradient, speed=0.005, fixed_colors=fixed_colors).strip()
        if mc_version == '':
            printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            printsito("㊀⎹ No dejés el campo vacío, ingresá la versión", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            time.sleep(4)
            os.system('clear')
            continue
        pattern = r'^\d+\.\d+(\.\d+)?$'
        if not re.match(pattern, mc_version):
            printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            printsito("✖ ⎹ Versión incorrecta. Solo números y puntos (ej: 1.20.1)", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            time.sleep(4)
            os.system('clear')
            continue
        fabric_version = inputsito_2("➥ ⎹ Ingresá la versión de Fabric que querés instalar ❱ ", full_gradient, speed=0.005, fixed_colors=fixed_colors).strip()
        if fabric_version == '':
            printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            printsito("㊀⎹ No dejés el campo vacío, ingresá la versión", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            time.sleep(4)
            os.system('clear')
            continue
        if not re.match(pattern, fabric_version):
            printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            printsito("✖ ⎹ Versión incorrecta. Solo números y puntos (ej: 0.16.8)", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            time.sleep(4)
            os.system('clear')
            continue
        break
    
    fabric_installer_url = f"https://meta.fabricmc.net/v2/versions/loader/{mc_version}/{fabric_version}/1.0.1/server/jar"
    fabric_installer_path = os.path.join(install_dir, "fabric-server-launch.jar")
    
    os.system('clear')
    while True:
        printsito("☑ ⎹ Confirmación", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito(f"⚠ ⎹ Ingresaste: Minecraft {mc_version} | Fabrcic {fabric_version}", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        confirm = inputsito_2("➥ ⎹ Son correctos?〔S/N〕❱ ", full_gradient, speed=0.005, fixed_colors=fixed_colors).strip().lower()
        if confirm == 's':
            break
        elif confirm == 'n':
            os.system('clear')
            printsito("↺ ⎹ Reiniciando curso...", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            time.sleep(3)
            fabric_ver()
            break
        elif confirm == '':
            printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            printsito("㊀⎹ No dejés el campo vacío, respondé con〔S/N〕", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            time.sleep(4)
            os.system('clear')
        else:
            printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            printsito("✖ ⎹ Respuesta inválida, respondé con〔S/N〕", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            time.sleep(4)
            os.system('clear')

    os.chdir('servidor_minecraft')
    if os.path.isfile('fabric-server-launch.jar'):
        os.remove('fabric-server-launch.jar')
    os.chdir(current_dir)
    
    fabric_installer_url = f"https://meta.fabricmc.net/v2/versions/loader/{mc_version}/{fabric_version}/1.0.1/server/jar"
    fabric_installer_path = os.path.join(install_dir, "fabric-server-launch.jar")    
    
    printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    animacion_actualizacion(
    gradient=full_gradient,
    anim_symbols="◝◞◟◜",
    text="⎹ Actualizando versiones...",
    updated_text="✔ ⎹ Versiones actualizadas!",
    typing_speed=0.01,
    animation_speed=0.07,
    duration=5,
    fixed_colors=fixed_colors
    )
    
    time.sleep(3)
    os.system('clear')
    urllib.request.urlretrieve(fabric_installer_url, fabric_installer_path)

    config_path = "configuracion.json"
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            config = json.load(file)
        if config.get("version_jdk") == "ninguna":
            config["version_jdk"] = "17"
        config["server_version"] = mc_version
        config["server_type"] = "fabric"
        with open(config_path, 'w') as file:
            json.dump(config, file, separators=(', ', ': '))
    eula_path = os.path.join(install_dir, "eula.txt")
    with open(eula_path, 'w') as eula_file:
        eula_file.write("eula=true\n")
    
    fixed_colors = {"🡻": (255, 236, 209),}
    printsito("🡻‎⎹ Descargando e instalando Fabric...", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    mostrar_progreso(duracion=5, longitud=27)    
    printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    time.sleep(3)
    os.system('clear')
    fixed_colors = {"✔": (255, 236, 209), "✔": (255, 236, 209), "❯": (255, 236, 209), "❱": (255, 236, 209), "⏎": (255, 236, 209), "❰": (255, 236, 209), "❮": (255, 236, 209),}
    printsito("✔ ⎹ Fabric instalado!", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    printsito(f"❯❱⎹ La versión de tu servidor es: Minecraft {mc_version} | Fabric {fabric_version}", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    printsito("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    highlight_color = (110, 33, 252)
    highlight_segments = {"MSX": highlight_color}
    fixed_colors = {"⏎": (255, 236, 209), "❰": (255, 236, 209), "❮": (255, 236, 209),}
    inputsito("⏎ ⎹ Apretá enter para volver al menú de MSX", full_gradient, speed=0.005, fixed_colors=fixed_colors, highlight_segments=highlight_segments)
    os.system('clear')
    highlight_color = (110, 33, 252)
    highlight_segments = {"MSX...": highlight_color}
    printsito("❰❮⎹ Saliendo al menu de MSX...", full_gradient, speed=0.005, fixed_colors=fixed_colors, highlight_segments=highlight_segments)
    time.sleep(3)


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘


def neo_warn():
    os.system('clear')
    time.sleep(1)

    eldire()

    c1 = (5, 81, 181)
    c2 = (255, 236, 209)
    c3 = (5, 81, 181)

    ssm = 25
    sme = 10

    gradient1 = generate_gradient(c1, c2, ssm)
    gradient2 = generate_gradient(c2, c3, sme)
    full_gradient = gradient1 + gradient2

    while True:
        fixed_colors = {
        "↹": (255, 236, 209),
        "⚠": (250, 214, 80),
        "➥": (255, 236, 209),
        "❱": (152, 227, 203),
        "🗑": (255, 236, 209),
        "❯": (255, 236, 209),
        "❙": (255, 236, 209),
        "↺": (255, 236, 209),
        "㊀": (255, 134, 56),
        "✖": (255, 69, 69),
        }
        printsito("↹ ⎹ Instalar NeoForge", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito(f"⚠ ⎹ Instalar esta version custom requiere reinstalar tu servidor...", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        respuesta = inputsito_2("➥ ⎹ ¿Deseas continuar?〔S/N〕❱ ", full_gradient, speed=0.005, fixed_colors=fixed_colors).strip().lower()
        if respuesta == 's':
            os.system('clear')
            try:
                shutil.rmtree('servidor_minecraft')
                printsito("🗑 ⎹ Servidor eliminado! ", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            except FileNotFoundError:
                printsito("❯❙⎹ Servidor no encontrado, omitiendo eliminación... ", full_gradient, speed=0.005, fixed_colors=fixed_colors)
                time.sleep(3)
            
            time.sleep(3)
            neo_ver()
            break

        elif respuesta == 'n':
            os.system('clear')
            time.sleep(1)
            highlight_color = (110, 33, 252)
            highlight_segments = {"MSX...": highlight_color}
            printsito("↺ ⎹ Saliendo al menú de MSX...", full_gradient, speed=0.005, fixed_colors=fixed_colors, highlight_segments=highlight_segments)
            time.sleep(3)
            break

        elif respuesta == '':
            printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            printsito("㊀⎹ No dejés el campo vacío, respondé con〔S/N〕", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            time.sleep(5)
            os.system('clear')

        else:
            printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            printsito("✖ ⎹ Respuesta inválida, respondé con〔S/N〕", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            time.sleep(5)
            os.system('clear')


def neo_ver():
    os.system('clear')

    current_dir = os.getcwd()
    install_dir = "servidor_minecraft"
    if not os.path.exists(install_dir):
        os.makedirs(install_dir)

    c1 = (5, 81, 181)
    c2 = (255, 236, 209)
    c3 = (5, 81, 181)
    
    ssm = 25
    sme = 10
    
    gradient1 = generate_gradient(c1, c2, ssm)
    gradient2 = generate_gradient(c2, c3, sme)
    full_gradient = gradient1 + gradient2
    
    while True:
        highlight_segments = {
        "1.20.2 - 1.21.11": (45, 45, 45),
        }
        fixed_colors = {
        "↹": (255, 236, 209),
        "➜": (250, 214, 80),
        "⚠": (255, 134, 56),
        "➥": (255, 236, 209),
        "❱": (152, 227, 203),
        "↺": (255, 236, 209),
        "㊀": (255, 134, 56),
        "✖": (255, 69, 69),
        "☑": (255, 236, 209),
        "◝": (255, 236, 209),
        "◞": (255, 236, 209),
        "◟": (255, 236, 209),
        "◜": (255, 236, 209),
        "✔": (255, 236, 209),
        }
        printsito("↹ ⎹ Instalar NeoForge", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("➜ ⎹ Versiones disponibles: 1.20.2 - 1.21.11", full_gradient, speed=0.005, highlight_segments=highlight_segments, fixed_colors=fixed_colors)
        printsito("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("⚠ ⎹ Se descargará la última version de NeoForge para la version de Minecraft que ingreses.", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        mc_version = inputsito_2("➥ ⎹ Ingresá la versión de Minecraft que querés instalar ❱ ", full_gradient, speed=0.005, fixed_colors=fixed_colors).strip()
        if mc_version == '':
            printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            printsito("㊀⎹ No dejes el campo vacío, ingresa la versión", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            time.sleep(4)
            os.system('clear')
            continue
        pattern = r'^\d+\.\d+(\.\d+)?$'
        if not re.match(pattern, mc_version):
            printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            printsito("✖ ⎹ Versión incorrecta. Solo números y puntos (ej: 1.20.6)", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            time.sleep(4)
            os.system('clear')
            continue
            # Determinar la última versión de NeoForge para la versión de Minecraft seleccionada
        nf_full_version = get_latest_neoforge(mc_version)
        if not nf_full_version:
            mc_version_color = (255, 69, 69)  # Verde, por ejemplo
            highlight_segments = {mc_version: mc_version_color}
            printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            printsito(f"✖ ⎹ No se encontró una versión de NeoForge para Minecraft {mc_version}", full_gradient, speed=0.005, fixed_colors=fixed_colors, highlight_segments=highlight_segments)
            fixed_colors = {"➜": (69, 255, 75)}
            highlight_segments = {
            "1.20.2-1.21.4": (69, 255, 75),
            }
            printsito(f"➜ ⎹ Versiones disponibles: 1.20.2-1.21.4", full_gradient, speed=0.005, fixed_colors=fixed_colors, highlight_segments=highlight_segments)
            time.sleep(5)
            os.system('clear')
            continue
        break

    jar_name = f"neoforge-{nf_full_version}-installer.jar"
    neoforge_url = f"https://maven.neoforged.net/releases/net/neoforged/neoforge/{nf_full_version}/{jar_name}"
    neoforge_path = os.path.abspath(os.path.join(install_dir, jar_name))  # Usar ruta absoluta

    os.system('clear')
    while True:
        highlight_color = (45, 45, 45)  # RGB del gris
        highlight_segments = {"(última)": highlight_color}
        fixed_colors = {
        "⚠": (250, 214, 80),
        "➥": (255, 236, 209),
        "❱": (152, 227, 203),
        "↺": (255, 236, 209),
        "✖": (255, 69, 69),
        "☑": (255, 236, 209),
        "◝": (255, 236, 209),
        "◞": (255, 236, 209),
        "◟": (255, 236, 209),
        "◜": (255, 236, 209),
        "✔": (255, 236, 209),
        }
        printsito("☑ ⎹ Confirmación", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
        printsito(f"⚠ ⎹ Ingresaste: Minecraft {mc_version} | NeoForge {nf_full_version} (última)", full_gradient, speed=0.005, fixed_colors=fixed_colors, highlight_segments=highlight_segments)
        confirm = inputsito_2("➥ ⎹ Son correctos?〔S/N〕❱ ", full_gradient, speed=0.005, fixed_colors=fixed_colors).strip().lower()
        if confirm == 's':
            break
        elif confirm == 'n':
            os.system('clear')
            printsito("↺ ⎹ Reiniciando curso...", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            time.sleep(3)
            neo_warn()
            break
        else:
            printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            printsito("✖ ⎹ Respuesta inválida, respondé con〔S/N〕", full_gradient, speed=0.005, fixed_colors=fixed_colors)
            time.sleep(4)
            os.system('clear')

    printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    animacion_actualizacion(
    gradient=full_gradient,
    anim_symbols="◝◞◟◜",
    text="⎹ Actualizando versiones...",
    updated_text="✔ ⎹ Versiones actualizadas!",
    typing_speed=0.01,
    animation_speed=0.07,
    duration=5,
    fixed_colors=fixed_colors
    )

    time.sleep(3)
    os.system('clear')
    urllib.request.urlretrieve(neoforge_url, neoforge_path)

    config_path = "configuracion.json"
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            config = json.load(file)
        if config.get("version_jdk") == "ninguna":
            config["version_jdk"] = "17"
        config["server_version"] = mc_version
        config["server_type"] = "neoforge"
        with open(config_path, 'w') as file:
            json.dump(config, file, separators=(', ', ': '))
    eula_path = os.path.join(install_dir, "eula.txt")
    with open(eula_path, 'w') as eula_file:
        eula_file.write("eula=true\n")
    
    fixed_colors = {"🡻": (255, 236, 209),}
    printsito("🡻‎⎹ Descargando e instalando NeoForge...", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    printsito("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    time.sleep(2)
    os.chdir(install_dir)
    subprocess.run(["java", "-jar", jar_name, "--installServer", "--server-jar"], check=True)
    os.rename('server.jar', 'neoforge.jar')
    os.chdir(current_dir)
    os.system('clear')
    highlight_color = (45, 45, 45)
    highlight_segments = {"(última)": highlight_color}
    fixed_colors = {"✔": (255, 236, 209), "✔": (255, 236, 209), "❯": (255, 236, 209), "❱": (255, 236, 209), "⏎": (255, 236, 209), "❰": (255, 236, 209), "❮": (255, 236, 209),}
    printsito("✔ ⎹ NeoForge instalado!", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    printsito(f"❯❱⎹ La versión de tu servidor es: Minecraft {mc_version} | NeoForge {nf_full_version} (última)", full_gradient, speed=0.005, fixed_colors=fixed_colors, highlight_segments=highlight_segments)
    printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    printsito("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    printsito("", full_gradient, speed=0.005, fixed_colors=fixed_colors)
    highlight_color = (110, 33, 252)
    highlight_segments = {"MSX": highlight_color}
    fixed_colors = {"⏎": (255, 236, 209), "❰": (255, 236, 209), "❮": (255, 236, 209),}
    inputsito("⏎ ⎹ Apretá enter para volver al menú de MSX", full_gradient, speed=0.005, fixed_colors=fixed_colors, highlight_segments=highlight_segments)
    os.system('clear')
    highlight_color = (110, 33, 252)
    highlight_segments = {"MSX...": highlight_color}
    printsito("❰❮⎹ Saliendo al menu de MSX...", full_gradient, speed=0.005, fixed_colors=fixed_colors, highlight_segments=highlight_segments)
    time.sleep(3)

def get_latest_neoforge(mc_version):
    try:
        url = "https://maven.neoforged.net/api/maven/versions/releases/net/neoforged/neoforge"
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())

        versions = data.get("versions", [])
        if not versions:
            return None

        parts = mc_version.split(".")
        if len(parts) < 2:
            return None

        mc_minor = parts[1]
        mc_patch = parts[2] if len(parts) >= 3 else "0"
        prefix = f"{mc_minor}.{mc_patch}."

        compatibles = [v for v in versions if v.startswith(prefix)]
        if not compatibles:
            return None

        def version_key(v):
            return [int(p) if p.isdigit() else p for p in v.replace("-", ".").split(".")]

        compatibles.sort(key=version_key)
        return compatibles[-1]

    except Exception:
        return None

