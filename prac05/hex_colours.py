HEX_COLOURS = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "beige": "#f5f5dc", "black": "#000000",
               "blanchedalmond": "#ffebcd", "blueviolet": "#8a2be2", "brown": "#a52a2a", "burlywood": "#deb887",
               "cadetblue": "#5f9ea0", "chocolate": "#d2691e"}

colour = input("Enter a colour")
while colour != "":
    if colour in HEX_COLOURS:
        print(HEX_COLOURS[colour])
    else:
        print("Invalid colour")
    colour = input("Enter a colour")