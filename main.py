from  PIL import Image

imam = Image.open("test.jpg")
moon = Image.open("moon.jpg")

box=(240,79,465,360)
imam = imam.crop(box)

imam = imam.resize((111, 106), Image.BICUBIC)

imam_red, imam_green, imam_blue = imam.split()
list_imam_red = list(imam_red.getdata())
list_imam_green = list(imam_green.getdata())
list_imam_blue = list(imam_blue.getdata())

list_imam_red = list(map(lambda x: x - 150, list_imam_red))
list_imam_green = list(map(lambda x: x - 150, list_imam_green))
list_imam_blue = list(map(lambda x: x - 150, list_imam_blue))

imam_red.putdata(list_imam_red)
imam_green.putdata(list_imam_green)
imam_blue.putdata(list_imam_blue)

new_imam = Image.merge("RGB",(imam_red,imam_green,imam_blue))

moon_crop = moon.crop((173, 59, 173 + 111, 59 + 106))

imam_red, imam_green, imam_blue = new_imam.split()
moon_red, moon_green, moon_blue = moon_crop.split()

list_imam_red = list(imam_red.getdata())
list_imam_green = list(imam_green.getdata())
list_imam_blue = list(imam_blue.getdata())
list_moon_red = list(moon_red.getdata())
list_moon_green = list(moon_green.getdata())
list_moon_blue = list(moon_blue.getdata())

list_avg_red = [(a + b) // 2 for a, b in zip(list_imam_red, list_moon_red)]
list_avg_green = [(a + b) // 2 for a, b in zip(list_imam_green, list_moon_green)]
list_avg_blue = [(a + b) // 2 for a, b in zip(list_imam_blue, list_moon_blue)]

avg_red = Image.new("L", (111, 106))
avg_green = Image.new("L", (111, 106))
avg_blue = Image.new("L", (111, 106))

avg_red.putdata(list_avg_red)
avg_green.putdata(list_avg_green)
avg_blue.putdata(list_avg_blue)

avg_image = Image.merge("RGB", (avg_red, avg_green, avg_blue))

moon.paste(avg_image, (173, 59))
moon.show()
moon.save("imam_on_moon.jpg")
