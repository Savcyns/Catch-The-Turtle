import turtle
import  time
import random
oyun_screen = turtle.Screen()
oyun_screen.bgcolor("light blue")
oyun_screen.title("Kaplumbağayı Yakala")
oyun_screen.setup(600,600)
oyun_screen.delay()





def puan (x,y) :
    nesne.goto(random.randint(-300,300),random.randint(-300,300))
    global p
    nesne.clear()
    p=p+1



nesne = turtle.Turtle()
nesne.speed(0)
nesne.shape("turtle")
nesne.color("green")
nesne.speed(0)
nesne.penup()
nesne.goto(random.randint(-300,300),random.randint(-300,300))



skor = turtle.Turtle()
skor.speed(0)
skor.shape("square")
skor.penup()
skor.goto(0,260)
skor.hideturtle()
skor.write("Başla",align="center",font=("Bold",24,"normal"))


p=0


sure = 15



while True :
    sure_1 = time.time()
    while (time.time()-sure_1) < sure :
         nesne.onclick(puan)
else:
    skor.write("Puan :".format(p), align="center", font=("Bold", 24, "normal"))
    time.sleep(2)
    p=0
    skor.clear()
    skor.write("Başla",align="center",font=("Bold",24,"normal"))
