from PIL import Image
import numpy as np
from math import sqrt
import random



def matrix_transposition(lst: list):
    result = []
    for i in range(len(lst[0])):
        bufflist = []
        for j in range(len(lst)):
            bufflist.append(lst[j][i])
        result.append(bufflist)
    return result


lst1 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

lst2 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

lst3 = [[2, 3],
        [2, 3],
        [2, 3],
        [2, 3],
        [2, 3],
        [2, 3]]

# lst4 = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
#         [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
#         [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]
# lst5 = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
#         [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
#         [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]
# lst7 = [lst4, lst5]
lst8 = [1,2,3,4,5,6]

def to_vector(lst: list):
    final = []
    #print(len(lst[0]),len(lst[0][0]),len(lst[1]),len(lst[1][0]),len(lst[2]),len(lst[2][0]),len(lst[3]),len(lst[3][0]))
    for i in range(len(lst)):
        result = []
        for j in range(len(lst[i])):
            for g in range(len(lst[i][j])):
                result += lst[i][j][g]
        final.append(result)
    return final

def matrix_multiplication_W_v2(X: list, W: list):
    if len(X) != len(W):
        return 'Uncorrect size'
    result = []
    for w1 in range(len(W[0])):
        for width in range(len(W)):  # widht = height1
            res = [num * W[width][w1] for num in X]
            summ = sum(res)
        result.append(summ)
    return result



def matrix_minus(lst1: list, lst2: list):
    if len(lst1) != len(lst2):
        return "Uncorrect data!"
    result = []
    for i in range(len(lst1)):
        lst = []
        for j in range(len(lst1[0])):
            element = []
            for h in range(len(lst1[i][j])):
                el = lst1[i][j][h] - lst2[i][j][h]
                element.append(el)
            lst.append(element)
        result.append(lst)
    print(result)


def matrix_multiplication_W(lst4: list, lst3: list):
    if len(lst4[0]) != len(lst3):
        return 'Uncorrect size'
    result = []
    for height in range(len(lst4)):
        lst = []
        for w1 in range(len(lst3[0])):
            flag = True

            for width in range(len(lst4[height])):  # widht = height1
                res = [num * lst3[width][w1] for num in lst4[height][width]]
                if flag is True:
                    buff = res
                    summ = list(map(sum, zip(buff)))
                    flag = False
                else:
                    summ = list(map(sum, zip(res, summ)))
            lst.append(summ)
        result.append(lst)
    return result

def load_image(name_picture: str):
    image = Image.open(name_picture)  # Открываем изображение
    width = image.size[0]  # Определяем ширину
    height = image.size[1]  # Определяем высоту
    pix = image.load()
    lst = []
    lst2 = []
    for y in range(height):
        lst = []
        for x in range(width):
            r = pix[x, y][0]  # узнаём значение красного цвета пикселя
            g = pix[x, y][1]  # зелёного
            b = pix[x, y][2]  # синего
            lst.append([round(((2 * r / 255) - 1),4), round(((2 * g / 255) - 1),4), round(((2 * b / 255) - 1),4)])
            #lst.append([r,g,b])
        lst2.append(lst)
    return lst2

def division_into_parts(img: list, width: int):
    choose = len(img[0]) // width
    size1 = len(img[0]) // choose
    #print(size1)
    rectangles = []
    for i in range(choose):
        rectangles.append([])

    for j in range(len(img)):
        lst1 = []
        for g in range(len(img[j])):
            lst1.append(img[j][g])
            if (g+1) % size1 == 0 and len(lst1) != 0:
                rectangles[((g + 1) // size1) - 1].append(lst1)
                lst1 = []
    return rectangles

def paint_image(img: list):
    # Выходное изображение PNG
    #print(img[0])
    map_data = np.array(img)
    #print(map_data)
    map_data = np.asarray(map_data, np.uint8)
    pic = Image.fromarray(map_data)
    pic.save('result.png')
    pic.show()

def to_vector(lst: list):
    final = []
    for i in range(len(lst)):
        result = []
        for j in range(len(lst[i])):
            for g in range(len(lst[i][j])):
                result += lst[i][j][g]
        final.append(result)
    return final

def get_vector_of_rectangle(rectagles: list):
    result = []
    rectangls = to_vector(rectangles)
    for i in range(len(rectangls)):
        buff = []
        buff.append(rectangls[i])
        result.append(np.array(buff))
    return result

def back_tolist_from_numpy(neurons: list):
    result = []
    for i in range(len(neurons)):
        result.append(np.array(neurons[i]).reshape(-1,))
    return result

def image_restoration(rectangles: list, size_image: int, amount_squares):
    for rectangle in rectangles:
        #print(len(rectangle))
        for i in range(len(rectangle)):
            rectangle[i] = int((255*((rectangle[i]+1)/2)))
    result = []
    pix = []
    # Восстанавливаем пиксели в одну большую строку
    for rectangle in rectangles:
        stroka = []
        for j in range(len(rectangle)):
            pix.append(rectangle[j])
            if (j+1) % 3 == 0:
                stroka.append(pix)
                pix = []

        result.append(stroka)
    # print(len(result[0]))

    # Восстанавливаем наши прямоугольники
    weight = size_image // amount_squares
    rectangles = []
    for pixels in result:
        rectangle = []
        stroka = []
        for j in range(len(pixels)):
            stroka.append(pixels[j])
            if (j+1) % weight == 0:
                rectangle.append(stroka)
                stroka = []
        rectangles.append(rectangle)

    # Ставим пискели на свои места
    final_image = []
    yes = True
    for rectangle in rectangles:
        if yes is True:
            for i in range(len(rectangle)):
                final_image.append(rectangle[i])
            yes = False
        else:
            for i in range(len(rectangle)):
                final_image[i] = final_image[i] + rectangle[i]
    paint_image(final_image)

def get_vector_of_rectangle2(rec: list):
    result = []
    for rectangle in rec:
        vec = to_vector2(rectangle)
        for i in vec:
            buff = [i]
            result.append(np.array(buff))
    return result

        # for square in rectangle:
        #     print(to_vector(square[0]))
        #     exit

def back_to_rectangles(squares: list,amount_squares: int, YOU: int):
    result = []
    rectangle = []
    sq = []
    buff = []
    amount = amount_squares * YOU * 3
    for square in squares:
      for rgb in square[0]:
        rectangle.append(rgb)
        if len(rectangle) == amount: # надо учиться считать
            buff.append(rectangle)
            result.append(np.array(buff))
            buff = []
            rectangle = []
    return result


def to_vector2(lst: list):
    final = []
    for square in lst:
        result = []
        buff = []
        for j in range(len(square)):
            for g in range(len(square[j])):
                for rgb in range(len(square[j][g])):
                    result.append(square[j][g][rgb])
        buff.append(result)
        final.append(np.array(buff))
    return final

def division_into_parts_v2(rectangles: list, size1: int):
    result = []
    for rect in rectangles:
        buff = []
        for i in range(len(rect)):
            buff.append(rect[i])
            if (i + 1) % size1 == 0 and len(buff) != 0:
                result.append(buff)
                buff = []
    return result