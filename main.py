pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
pins.touch_set_mode(TouchTarget.P2, TouchTargetMode.CAPACITIVE)

is_pin1 = input.pin_is_pressed(TouchPin.P1)
is_pin2 = input.pin_is_pressed(TouchPin.P2)

player1 = False
player2 = False
playing = False
ready = True
clicked_early1 = False
clicked_early2 = False

input.on_pin_pressed(TouchPin.P1, player1_pressed)
input.on_pin_pressed(TouchPin.P2, player2_pressed)

def player1_pressed():
    global player1
    clicked_early1 = True
    player1 = True

def player2_pressed():
    global player2
    clicked_early2 = True
    player2 = True


def start():
    while ready == True:
        global ready, playing
        basic.clear_screen()
        basic.pause(randint(1000, 3000))
        playing = True
        music.play_melody("D", 500)

        while playing == True and player1 == False and player2 == False:
            basic.show_leds("""
            . # # # .
            # . . . #
            # . # . #
            # . . . #
            . # # # .
            """)
        basic.pause(3000)

forever(start)


def vyhodnocovani():
    global playing, player1, player2
    if playing == True:
        if player1 == True:
            basic.show_string("1")
            restart()
        elif player2 == True:
            basic.show_string("2")
            restart()
        elif player1 == True and player2 == True:
            basic.show_string("R")
            restart()
    elif playing == False:
        if player1 == True:
            playing = False
            basic.show_string("A")
            restart()
        elif player2 == True:
            playing = False
            basic.show_string("B")
            restart()
forever(vyhodnocovani)


def restart():
    global player1, player2, playing, ready, clicked_early1, clicked_early2
    player1 = False
    player2 = False
    ready = False
    clicked_early1 = False
    clicked_early2 = False
    playing = False
    basic.clear_screen()
    basic.pause(3000)
    ready = True