#Practica10
#Realizaun programa que simule un medidor de temperatura
#usando numeros al azar y el boton A, en el lenguaje python
#Si la temperatura<=15 muestre un sms de ,"FRIO", SINO un
#sms de "CALOR"

temperatura=0
def on_button_pressed_a():
    global temperatura
    temperatura=randint(1,40)
    basic.show_number(temperatura)
    basic.pause(1000)
    if temperatura<=15:
        basic.show_icon(IconNames.ANGRY)
        basic.show_string("FRIO")
    else:
        basic.show_icon(IconNames.HAPPY)
        basic.show_string("CALOR")
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)
