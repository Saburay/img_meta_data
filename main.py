#Создаю небольшой скриптом на Python для получить мета-данных с изображений
from func import  *

if __name__ == "__main__":
    path_file = input('[~] Введите путь к файлу: ')
    if not os.path.exists(path_file):
        print('[-] Файла не существует')
    else:
        if path_file.endswith(".jpg"):
            image_metadata(path_file)
        elif path_file.endswith(".jpeg"):
            image_metadata(path_file)



# if __name__ == '__main__':
#     main()

# #c = 'Image 2023-01-26.jpeg'