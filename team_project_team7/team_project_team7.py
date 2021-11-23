import tkinter
from functools import partial
from tkinter import *
import pandas as pd
from PIL import Image
import random as r

path_dir = './image'
window = Tk()
window.title("베라 아이스크림 추천기")
window.geometry("700x550")
window.resizable(0, 0)
image_main = PhotoImage(file=path_dir + '/쿠키런_뽑기머신.gif')

table = pd.read_csv('31_single.csv')
table_mul = pd.read_csv('31_multi.csv')

def getNumber_mul():
    return r.randrange(0, len(table_mul.index))

def getNumber_single():
    return r.randrange(0, len(table.index))

def showimg_single(recommand):
    global image
    image = PhotoImage(file=path_dir + '/' + recommand + '.png')
    label_1.place_forget()
    label_2.place_forget()
    label_3 = Label(window,text="%s 아이스크림을 추천합니다.!"%recommand,font="NanumGothic 20")
    label_4= Label(window, image=image)
    label_3.place(x=50, y=10)
    label_4.place(x=130, y=120)

def showimg_mul(recommand):
    print(recommand)
    image = Image.open(path_dir+'/%s.png'%recommand)
    image_size = image.size
    image = image.resize((int(image_size[0] * (1.5)), int(image_size[1] * (1.5))))
    image.show()
    label_1.place_forget()
    label_3 = Label(window,text="다른메뉴도 골라보세요 :)",font="NanumGothic 20")
    label_3.place(x=200, y=10)


def choose_mul(str, num):
    table_mul_ice = table_mul['%s'%str].dropna()
    num = int(num)
    recommand = []
    num_list = []
    if num <= len(table_mul_ice.index):
        for i in range(0, num):
            num = getNumber_mul()
            while num > len(table_mul_ice.index):
                num = getNumber_mul()
            while num in num_list:
                num = getNumber_mul()
            num_list.append(num)
            recommand.append(table_mul_ice[i])
            showimg_mul(recommand[i])
        return recommand
    elif num == len(table_mul_ice.index):
        for i in range(0, num):
            recommand.append(table_mul_ice[i])
            showimg_mul(recommand[i])
        return recommand

def choice_mul(str, num):
    if str not in table_mul.keys():
        print('맛을 다시 입력하세요.')
        return False
    else:
        recommand = choose_mul(str, num)
        print(recommand, '을(를) 추천합니다.')
        return False

def num_choose(str):
    btn5 = Button(window, text="종료", command=window.destroy, width=7, height=1)
    btn5.place(x=300, y=130)

    if str in ['민트중심','베이직']:
        bt1 = Button(window, text="2", command=partial(choice_mul, str, '2'), width=7, height=1)
        bt2 = Button(window, text="3", command=partial(choice_mul, str, '3'), width=7, height=1)
        bt1.place(x=500, y=50)
        bt2.place(x=370, y=50)
    elif str in ['초코덕후', '인기5', '상큼새콤']:
        bt1 = Button(window, text="2", command=partial(choice_mul, str, '2'), width=7, height=1)
        bt2 = Button(window, text="3", command=partial(choice_mul, str, '3'), width=7, height=1)
        bt3 = Button(window, text="4", command=partial(choice_mul, str, '4'), width=7, height=1)
        bt4 = Button(window, text="5", command=partial(choice_mul, str, '5'), width=7, height=1)
        bt1.place(x=500, y=50)
        bt2.place(x=370, y=50)
        bt3.place(x=240, y=50)
        bt4.place(x=100, y=50)
    elif str in ['베리시리즈', '치즈콕콕', '호불호']:
        bt1 = Button(window, text="2", command=partial(choice_mul, str, '2'), width=7, height=1)
        bt2 = Button(window, text="3", command=partial(choice_mul, str, '3'), width=7, height=1)
        bt3 = Button(window, text="4", command=partial(choice_mul, str, '4'), width=7, height=1)
        bt1.place(x=500, y=50)
        bt2.place(x=370, y=50)
        bt3.place(x=240, y=50)

def choice_ice_mul():
    btn_1.place_forget()
    btn_2.place_forget()
    btn_3.place_forget()
    btn1 = Button(window, text="민트중심", command=partial(num_choose, '민트중심'), width=7, height=1)
    btn2 = Button(window, text="초코덕후", command=partial(num_choose, '초코덕후'), width=7, height=1)
    btn3 = Button(window, text="베이직", command=partial(num_choose, '베이직'), width=7, height=1)
    btn4 = Button(window, text="베리시리즈", command=partial(num_choose, '베리시리즈'), width=7, height=1)
    btn5 = Button(window, text="치즈콕콕", command=partial(num_choose, '치즈콕콕'), width=7, height=1)
    btn6 = Button(window, text="호불호", command=partial(num_choose, '호불호'), width=7, height=1)
    btn7 = Button(window, text="상큼새콤", command=partial(num_choose, '상큼새콤'), width=7, height=1)
    btn8 = Button(window, text="인기5", command=partial(num_choose, '인기5'), width=7, height=1)
    btn9 = Button(window, text="종료", command=window.destroy, width=7, height=1)
    btn1.place(x=500, y=50)
    btn2.place(x=370, y=50)
    btn3.place(x=240, y=50)
    btn4.place(x=100, y=50)
    btn5.place(x=500, y=90)
    btn6.place(x=370, y=90)
    btn7.place(x=240, y=90)
    btn8.place(x=100, y=90)
    btn9.place(x=300, y=130)

def choose(input):
    table_one = table['%s'%input].dropna()
    num = getNumber_single()
    while num >= len(table_one.index):
        num = getNumber_single()
    recommand = table_one[num]
    return recommand

def choice_one(str):
    if str not in table.keys():
        print('맛을 다시 입력하세요.')
        return False
    else:
        recommand = choose(str)
        showimg_single(recommand)
        print(recommand, '을(를) 추천합니다.')
        return False

def choice_ice_one():
    btn_1.place_forget()
    btn_2.place_forget()
    btn_3.place_forget()
    btn1 = Button(window, text="민트", command=partial(choice_one, '민트'), width=7, height=1)
    btn2 = Button(window, text="달콤", command=partial(choice_one, '달콤'), width=7, height=1)
    btn3 = Button(window, text="치즈", command=partial(choice_one, '치즈'), width=7, height=1)
    btn4 = Button(window, text="팝핑", command=partial(choice_one, '팝핑'), width=7, height=1)
    btn5 = Button(window, text="상큼", command=partial(choice_one, '상큼'), width=7, height=1)
    btn6 = Button(window, text="종료", command=window.destroy, width=7, height=1)
    btn1.place(x=500, y=50)
    btn2.place(x=400, y=50)
    btn3.place(x=300, y=50)
    btn4.place(x=200, y=50)
    btn5.place(x=100, y=50)
    btn6.place(x=300, y=90)


btn_1 = Button(window ,text="한가지", command = choice_ice_one, width=7,height=1)
btn_2 = Button(window ,text="여러가지", command = choice_ice_mul, width=7,height=1)
btn_3 = Button(window ,text="종료", command = window.destroy, width=7,height=1)
label_1 = Label(window,text="환영합니다. 아래의 버튼 중 하나를 선택해주세요.",font="NanumGothic 20")
label_2 = Label(window, image=image_main)
label_1.place(x=50,y=10)
label_2.place(x=100,y=80)
btn_1.place(x=400,y=50)
btn_2.place(x=100,y=50)
btn_3.place(x=250, y=50)
window.mainloop()
print('이용해주셔서 감사합니다. 오늘도 좋은하루되세요 :)')