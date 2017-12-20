# Algoritimo para blur em fotos
# For
# image = [[7, 4, 0, 1], 
#          [5, 6, 2, 2], 
#          [6, 10, 7, 8], 
#          [1, 4, 2, 0]]
# 
# the output should be
# boxBlur(image) = [[5, 4], 
#                   [4, 4]]
# 
# There are four 3 × 3 squares in the input image, 
# so there should be four integers in the blurred output. 
# To get the first value: (7 + 4 + 0 + 5 + 6 + 2 + 6 + 10 + 7) = 47 / 9 = 5.2222 = 5. 
# The other three integers are obtained the same way, t
# hen the surrounding integers are cropped from the final result.


def boxBlur(image):
    blur = []
    for i in range(1, len(image) - 1):
        line = []
        for j in range(1, len(image[i]) - 1):
            pix = (
                image[i-1][j-1] + image[i-1][j] + image[i-1][j+1] +
                image[ i ][j-1] + image[ i ][j] + image[ i ][j+1] +
                image[i+1][j-1] + image[i+1][j] + image[i+1][j+1]
            )/9
            line.append(int(pix))
        blur.append(line)
    return blur
