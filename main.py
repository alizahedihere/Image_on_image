from  PIL import Image

orange = Image.open("orange.jpg")
moon = Image.open("moon.jpg")

box=(240,79,465,360)
orange = orange.crop(box)

orange = orange.resize((111, 106), Image.BICUBIC)

orange_red, orange_green, orange_blue = orange.split()
list_orange_red = list(orange_red.getdata())
list_orange_green = list(orange_green.getdata())
list_orange_blue = list(orange_blue.getdata())

list_orange_red = list(map(lambda x: x - 150, list_orange_red))
list_orange_green = list(map(lambda x: x - 150, list_orange_green))
list_orange_blue = list(map(lambda x: x - 150, list_orange_blue))

orange_red.putdata(list_orange_red)
orange_green.putdata(list_orange_green)
orange_blue.putdata(list_orange_blue)

new_orange = Image.merge("RGB",(orange_red,orange_green,orange_blue))

moon_crop = moon.crop((173, 59, 173 + 111, 59 + 106))

orange_red, orange_green, orange_blue = new_orange.split()
moon_red, moon_green, moon_blue = moon_crop.split()

list_orange_red = list(orange_red.getdata())
list_orange_green = list(orange_green.getdata())
list_orange_blue = list(orange_blue.getdata())
list_moon_red = list(moon_red.getdata())
list_moon_green = list(moon_green.getdata())
list_moon_blue = list(moon_blue.getdata())

list_avg_red = [(a + b) // 2 for a, b in zip(list_orange_red, list_moon_red)]
list_avg_green = [(a + b) // 2 for a, b in zip(list_orange_green, list_moon_green)]
list_avg_blue = [(a + b) // 2 for a, b in zip(list_orange_blue, list_moon_blue)]

avg_red = Image.new("L", (111, 106))
avg_green = Image.new("L", (111, 106))
avg_blue = Image.new("L", (111, 106))

avg_red.putdata(list_avg_red)
avg_green.putdata(list_avg_green)
avg_blue.putdata(list_avg_blue)

avg_image = Image.merge("RGB", (avg_red, avg_green, avg_blue))

moon.paste(avg_image, (173, 59))
moon.show()
moon.save("test_on_moon.jpg")
