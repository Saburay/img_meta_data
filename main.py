#Создаю небольшой скриптом на Python для получить мета-данных с изображений
#Установливаю библиотеку Pillow   pip install Pillow ffmpeg-python
import os.path
from pprint import pprint

import ffmpeg
from PIL import Image, ExifTags

def image_metadata(path_f):
    img = Image.open(path_f)
    info_dict = {
            "Имя файла": os.path.split(path_f)[1],
            "Разрешение изображения": img.size,
            "Высота изображения": img.height,
            "Ширина изображения": img.width,
            "Формат изображения": img.format,
            "Режим изображения": img.mode,
            "Анимированное изображение": getattr(img, "is_animated", False),
            "Кадров в изображении": getattr(img, "n_frames", 1)
        }
    try:
        exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}

        print(f'\n[+] Метаданные фото: {os.path.split(path_f)[1]:27}\n')
        for info in exif:
            if info == 'GPSInfo':
                print(f'{info:27}: lat {exif[info][2]} {exif[info][1]} - long {exif[info][4]} {exif[info][3]}')
            else:
                if isinstance(exif[info], bytes):
                    info_d = exif[info].decode()
                    print(f'{info:25}: {info_d}')
                else:
                    print(f'{info:25}: {exif[info]}')
    except AttributeError:
        print(f'\n[+] Информация о фото: {os.path.split(path_f)[1]:27}\n')
        for k, v in info_dict.items():
            print(f"{k:27}: {v}")
        exit(0)

if __name__ == '__main__':
    image_metadata(str(input('Введите путь к изображению без кавычек и скобок:')))
# #c = 'Image 2023-01-26.jpeg'