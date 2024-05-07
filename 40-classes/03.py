class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_resolution):
        self.resolution = new_resolution


my_image_1 = Image(resolution='400x800', title='title', extension='jpg')
my_image_2 = Image(resolution='400x800', title='title 2', extension='png')

print(my_image_1.__dict__)

my_image_1.resize('1080x720')

print(my_image_1.__dict__)
print(my_image_2.__dict__)
