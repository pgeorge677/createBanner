#!/usr/bin/env python

import os
import argparse
from PIL import Image


def convert_to_webp(filename, path):
    # extension = filename.split('.')[-1]
    file_name = filename.split('.')[0]
    image = Image.open(os.path.join(path, filename))
    image.save(os.path.join(path, file_name + '.webp'), "webp", quality=85)

    rgb_im = Image.new("RGB", image.size, (255, 255, 255))
    rgb_im.paste(image, image)
    rgb_im.save(os.path.join(path, file_name + '.jpg'), optimize=True, quality=85)


def convert_all(path):
    sub_folders = next(os.walk(path))[1]  # Obtener todas las subcarpetas
    for folder in sub_folders:
        folder_path = os.path.join(path, folder)
        if not os.path.isdir(folder_path):
            continue  # Ignorar si no es una carpeta
        subfiles = os.listdir(folder_path)
        png_files = [file for file in subfiles if file.endswith(".png")]
        if png_files:
            for imageFile in png_files:
                convert_to_webp(imageFile, folder_path)

    root_files = os.listdir(path)  # Obtener archivos de la carpeta raíz
    root_png_files = [file for file in root_files if file.endswith(".png")]
    if root_png_files:
        for imageFile in root_png_files:
            convert_to_webp(imageFile, path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Debes de tener los archivo .png en la carpeta indicada, puedes tener subcarpetas con mas archivos .png',
        usage='"python %(prog)s path"')
    parser.add_argument("path", type=str,
                        help="Ruta del directorio que contiene las imágenes banner.png y banner-center.png o subcarpetas con las imagenes")
    args = parser.parse_args()
    convert_all(args.path)
