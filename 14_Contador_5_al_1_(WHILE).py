#Practica14
#Realizar un programa qeu simule un retroceso de numeros
#desde el 5 hazta el 1, usando WHILE y el boton A, en el lenguaje Phyton


def on_button_pressed_a():
    i=5
    while i>=1:
        basic.show_number(i)
        basic.pause(500)
        i=i-1 
    basic.show_string("FINAL")
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

