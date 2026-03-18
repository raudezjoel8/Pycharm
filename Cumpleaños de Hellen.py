import turtle
import random

# Configuración de pantalla
pantalla = turtle.Screen()
pantalla.bgcolor("black")
pantalla.title("Feliz Cumpleaños")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Función para escribir texto bonito
def escribir(texto, x, y, tamaño, color):
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.write(texto, align="center", font=("Aptos", tamaño, "bold"))

# Función para dibujar estrellas (destellos)
def estrella(x, y, tamaño, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(tamaño)
        t.right(144)
    t.end_fill()

# Dibujar múltiples destellos
for _ in range(50):
    x = random.randint(-300, 300)
    y = random.randint(-250, 250)
    tamaño = random.randint(5, 15)
    color = random.choice(["pink", "white", "gold", "green"])
    estrella(x, y, tamaño, color)

# Texto principal
escribir("🎉 Feliz Cumpleaños 🎉", 0, 80, 28, "pink")
escribir("Hellen", 0, 40, 36, "white")

# Mensaje final
escribir("Te quiere mucho,", 0, -60, 16, "white")
escribir("Tu hermanito Bryan 💙", 0, -100, 16, "White")

# Animación simple de brillo
for _ in range(10):
    x = random.randint(-300, 300)
    y = random.randint(-250, 250)
    estrella(x, y, 10, "white")

turtle.done()