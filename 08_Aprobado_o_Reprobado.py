#Practica8
#Realiza un programa que muestre un sms, si el estudiante
#es aprobado o reprobado, usando numeros al azar y el
#boton A, en el lenguaje Python

numero=0
def on_button_pressed_a():
    global numero
    numero=randint(1,10)
    basic.show_number(numero)
    basic.pause(1000)
    if numero>=6:
        basic.show_string("APROBADO")
    else:
        basic.show_string("REPROBADO")
    
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)
