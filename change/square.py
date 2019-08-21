import time
def square_area (a):
    area=a**2
    return (print('正方形的面积为'+str(area)))

print('正方形面积计算')
time.sleep(0.3)
a=float(input('请输入正方形边长：'))
square_area (a)