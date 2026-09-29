#PRACTICA 2
#Realiza un programa que muestre las letras X, Y, Z
#usando el boton A=X, B=Y, AB=Z
#en el lenguaje Python para microbit

def on_button_pressed_a():
   basic.show_leds("""
   # . . . #
   . # . # .
   . . # . .
   . # . # .
   # . . . #
   """)
basic.pause(500)
basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
   basic.show_leds("""
   # . . . #
   . # . # .
   . . # . .
   . . # . .
   . . # . .
   """)
basic.pause(500)
basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
   basic.show_leds("""
   # # # # #
   . . . # .
   . . # . .
   . # . . .
   # # # # #
   """)
basic.pause(500)
basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)
