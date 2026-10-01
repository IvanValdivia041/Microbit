#Practica10
#Realizaun programa que simule un medidor de temperatura
#usando numeros al azar y el boton A, en el lenguaje python
#Si la temperatura>=70 muestre un sms de ,"RAPIDO", SINO un
#sms de "LENTO"

velocidad=0
def on_button_pressed_b():
    global velocidad
    temperatura=randint(1,100)
    basic.show_number(velocidad)
    basic.pause(1000)
    if velocidad>=70:
        basic.show_icon(IconNames.HAPPY)
        basic.show_string("RAPIDO")
    else:
        basic.show_icon(IconNames.ANGRY)
        basic.show_string("LENTO")
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)
