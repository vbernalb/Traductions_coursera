import os
from googletrans import Translator

# Los textos a traducir deben estar en una carpeta llamada vtt dentro de este directorio
path = os.path.join(os.getcwd(), "vtt")


def get_files_from_path(path_file):
    """ Obtiene la lista de archivos que hay en el path (si hay, incluye directorios) """
    files = os.listdir(path_file)
    return files


def translate(path_file, src_lang, dest_lang):
    """ Traduce el archivo en el path dado"""
    with open(path_file) as f:
        trans = translator.translate(f.read(), src=src_lang, dest=dest_lang)
    text = trans.text
    text = text.replace("->", "-->").replace(",", ".").replace(": ", ":")
    return text


def write_text(path_file, text):
    """ Sobreescribe el archivo original con el texto dado """
    with open(path_file, "w", encoding="utf-8") as f2:
        f2.write(text)


files = get_files_from_path(path)
translator = Translator()

# Para cada archivo en la carpeta vtt
for file in files:
    # se crea el path para el archivo
    path_file = os.path.join(path, file)
    # se traduce
    text = translate(path_file, "en", "es")
    # se sobreescribe
    write_text(path_file, text)