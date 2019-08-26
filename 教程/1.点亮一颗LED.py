# main.py -- put your code here!
led = pyb.LED(2)     #创建对象
while True:          #true
    led.toggle()     #循环
    pyb.delay(1000)  #等待1秒（单位为毫秒）
#此代码是无限循环的