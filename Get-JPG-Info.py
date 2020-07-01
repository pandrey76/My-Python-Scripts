import PIL.Image
img = PIL.Image.open('/home/admin1/Загрузки/PHOTO-2020-07-01-21-25-01.jpg')
exif_data = img._getexif()
print(exif_data)
