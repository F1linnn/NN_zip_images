from PIL import Image
import numpy as np
from math import sqrt
import random
from matrix_actions import *


def generate_W(size: tuple, neurons: int):
    height = size[1]
    lenght = neurons
    W = np.ones((height, lenght))
    return W

def generate_W1_new(W1, Alpha, X, E, W2):
    Xt = X.T
    W2t = W2.T
    #print(Xt.shape, E.shape)
    buff = np.dot(Xt,E)
    buff = np.dot(buff,W2t)
    buff = buff * Alpha
    result = W1 - buff
    return result

def generate_W2_new(W2, X1, Alpha, E):
    X1t = X1.T
    buff = np.dot(X1t, E)
    buff = buff * Alpha
    result = W2 - buff
    return result

def rationing(W):
    size = W.shape
    sum = 0
    buff = []
    for n in range(size[1]):
        for j in range(size[0]):
            sum += pow(W[j,n],2)
        sum = sqrt(sum)
        buff.append(sum)
    for n in range(size[1]):
        for j in range(size[0]):
            W[j, n] = W[j,n] / buff[n]
    return W

def sum_error(E):
    sum = np.sum(E**2)
    return sum



# ---------------------------------------------------------

def generate_W_v2(size: int, neurons: int):
    W = []
    for h in range(size):
        lst = []
        for weight in range(neurons):
            lst.append(random.uniform(-1,1))
        W.append(lst)
    return np.array(W)

def get_number(matrix):
    return matrix[0][0]

# # -----------------------------------------------------------------------
def NN_start():
    choose = int(input("Select operating mode 1 - teaching, 2 - zip the picture, 3 - unzip the picture: "))
    name_pic = str(input('Enter name of picture: '))
    img = load_image(name_pic)
    print("Succes!")
    square_h = int(input("Enter heigth square(usually 2 or 4): "))
    square_w = int(input("Enter weigth square(usually 2 or 4):  "))
    amount_neurons = int(input("Enter amount neurons on second: "))
    h = len(img)
    w = len(img[0])
    rectangles = division_into_parts(img,square_h)
    res = division_into_parts_v2(rectangles,square_w)
    squares = to_vector2(res)
    if choose == 1:
        erorrmin = int(input("Enter the minimum error: "))
        ratio = float(input("Enter learning rate(For correct work best choise is min > 0  max = 0.01): "))  # 0.0001
        W1 = generate_W_v2(squares[0].shape[1], 6)
        W2 = W1.T
        print('Кэф' ,ratio)
        error_list = [20001.]
        i = 0
        while sum(error_list) > erorrmin:
            i+=1
            error_list = []
            for X in squares:
                X1 = np.dot(X, W1)
                X2 = np.dot(X1, W2)
                E = X2 - X
                # ratio = 1/sum_error(X1)
                error_list.append(sum_error(E))
                W2 = generate_W2_new(W2, X1, ratio, E)
                W1 = generate_W1_new(W1,ratio,X,E,W2)
                # print(W1)

            print(sum(error_list), i)

        result = []
        for square in squares:
            X1 = np.dot(square, W1)
            X2 = np.dot(X1, W2)
            result.append(X2)
        print(len(result[0]))
        buffw = w/square_w
        squares = back_to_rectangles(result, h, square_w)
        squares = back_tolist_from_numpy(squares)
        # result = back_tolist_from_numpy(squares)
        save_or_not = int(input("Do you wanna save scales(1 - yes, 0 - no)? "))
        if save_or_not == 1:
            name = str(square_w) + 'x' + str(square_h)
            name_w1 = 'W1_' + name + '_' + str(amount_neurons)
            name_w2 = 'W2_' + name + '_' + str(amount_neurons)
            np.save(name_w1, W1)
            np.save(name_w2, W2)

        image_restoration(squares, w, buffw)  # w это размер изначальной картинки, buff это кол-во блоков на которое разбивалась картинка

    elif choose == 2:
        W1 = np.load(f'W1_{square_w}x{square_h}_{amount_neurons}.npy')
        result = []
        for square in squares:
            X1 = np.dot(square, W1)
            result.append(X1)
        np.save(name_pic + '_zip', result)
    elif choose == 3:
        W2 = np.load(f'W2_{square_w}x{square_h}_{amount_neurons}.npy')
        pic_zip = np.load(f'{name_pic}_zip.npy')
        result = []
        for square in pic_zip:
            X1 = np.dot(square, W2)
            result.append(X1)
        buffw = w / square_w
        squares = back_to_rectangles(result, h, square_w)
        squares = back_tolist_from_numpy(squares)
        image_restoration(squares, w, buffw)

NN_start()