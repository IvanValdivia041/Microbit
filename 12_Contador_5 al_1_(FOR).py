#Practica12
#Realiza un programa que simule un contador de numero en retroceso
#del 1 al 5, usando FOR y el boton B, en el lenguaje Phyton

def on_button_pressed_b():

    for i in range(5, 0,-1):
        basic.show_number(i)
        basic.pause(300)
    #al terminar el bucle
    basic.show_icon(IconNames.YES)
    basic.show_string("FINAL")
    basic.pause(500)
    basic.clear_screen()

input.on_button_pressed(Button.B, on_button_pressed_b)

