from pprint import pprint

def rotate(image):
    transposedImage = transpose(image)
    rotatedImage = reflect(transposedImage)
    return image

def transpose(image):
    for i in range(len(image)):
        for j in range(i):
            temp = image[i][j]
            image[i][j] = image[j][i]
            image[j][i] = temp
    return image

def reflect(image):
    for i in range(len(image)):
        for j in range(len(image) / 2):
            temp = image[i][j]
            image[i][j] = image[i][len(image) - (j + 1)]
            image[i][len(image) - (j + 1)] = temp
    return image

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("1-9 in matrix form rotated is: ") 
pprint(rotate(matrix))
