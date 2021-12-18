from PIL import Image

# ASCII characters arranged from lightest to darkest in terms of density
ASCII_SCALE = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def get_pixel_matrix(img, height):
    """
    Returns a 2D array of pixel RGB values as tuples, where each nested list is one row of pixels per column of pixels.
    Input: Image file as Image object, rescaled to fit the terminal (this may need to be changed for individual users)
    Output: 2D array of pixel RGB values.
    """
    img.thumbnail((height, 50))
    pixels = list(img.getdata())
    return [pixels[i:i + img.width] for i in range(0, len(pixels), img.width)]


def get_brightness_matrix(pixel_matrix):
    """
    Converts the RGB tuples of pixels into single brightness numbers between 0 to 255
    Input: 2D array of pixel RGB values
    Output: 2D array of pixel brightness values
    """
    for x in range(len(pixel_matrix)):
        for y in range(len(pixel_matrix[x])):
            (R, G, B) = pixel_matrix[x][y]
            pixel_matrix[x][y] = (R + G + B) / 3
    return pixel_matrix


def round_to_base(x, base=4):
    """
    Rounds a number, x to the nearest multiple of base (defaults to 4)
    Input: Int or Float
    Output: Float, a multiple of base (defaults to 4)
    """
    return base * round(x / base)


def create_symbol_dict(pixel_values, symbols):
    """
    Creates a dictionary with pixel values corresponding to ASCII characters
    Input: Lists of strings of values and symbols
    Output: Dictionary with key:value pairs of pixel_values:symbols
    """
    symbol_dict = {}
    for k, v in zip(pixel_values, symbols):
        symbol_dict[k] = v
    return symbol_dict


def get_ascii_matrix(pixel_matrix, symbol_dict):
    """
    Assigns the pixel brightness to values to ASCII characters, using a symbol dictionary
    Input: 2D array of pixel brightness values
    Output: 2D array of ASCII character
    """
    for x in range(len(pixel_matrix)):
        for y in range(len(pixel_matrix[x])):
            pixel_matrix[x][y] = round_to_base(pixel_matrix[x][y])
            pixel_matrix[x][y] = symbol_dict[(pixel_matrix[x][y])]
    return pixel_matrix


def print_ascii_matrix(ascii_matrix):
    for row in ascii_matrix:
        line = [p+p for p in row]
        print("".join(line))
        # print("".join(row))


img = Image.open("pineapple.jpg")
print("Succesfully loaded image!")
print(f"Image size: {img.width} x {img.height}")

pixel_matrix = get_pixel_matrix(img, 1000)
pixel_matrix = get_brightness_matrix(pixel_matrix)
print(f"Rescaled image size: {img.width} x {img.height}")

# Create a list of values to round the pixel brightness values to
brightness_scale = [i for i in range(0, 260, 4)]

ascii_dictionary = create_symbol_dict(brightness_scale, ASCII_SCALE)
ascii_matrix = get_ascii_matrix(pixel_matrix, ascii_dictionary)

print_ascii_matrix(ascii_matrix)
