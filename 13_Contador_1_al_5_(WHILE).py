#Practica13
#Realizar un programa qeu simule un contador de numeros
#del 1 al 5, usando WHILE y el boton A, en el lenguaje Phyton


def on_button_pressed_a():
    i=1
    while i<=5:
        basic.show_number(i)
        basic.pause(500)
        i=i+1
    basic.show_string("FINAL")
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)
