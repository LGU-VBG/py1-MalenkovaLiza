class Image:
    def __init__(self, resolution, title, extension ):
        self.resolution = resolution   # разрешение
        self.title = title
        self.extension = extension     # расширение
        
    def resize(self, new_resolution):
        self.resolution = new_resolution
        
    def print(self):
        print (f"{self.resolution}, {self.title}, {self.extension}")
        

# Создание 3-х экземпляров
first_image= Image(10, 'work', '.jpg' )
second_image= Image(23, 'history', '.jpg')
third_image= Image(15, 'icon', '.jpg')

first_image.print()
second_image.print()
third_image.print()

# Изменение разрешения
first_image.resize(20)
second_image.resize(11)
third_image.resize(60)

print ()

first_image.print()
second_image.print()
third_image.print()