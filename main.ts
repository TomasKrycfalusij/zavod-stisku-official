pins.touchSetMode(TouchTarget.P1, TouchTargetMode.Capacitive)
pins.touchSetMode(TouchTarget.P2, TouchTargetMode.Capacitive)
let is_pin1 = input.pinIsPressed(TouchPin.P1)
let is_pin2 = input.pinIsPressed(TouchPin.P2)
let player1 = false
let player2 = false
let playing = false
let ready = true
let clicked_early1 = false
let clicked_early2 = false
input.onPinPressed(TouchPin.P1, function player1_pressed() {
    
    let clicked_early1 = true
    player1 = true
})
input.onPinPressed(TouchPin.P2, function player2_pressed() {
    
    let clicked_early2 = true
    player2 = true
})
forever(function start() {
    while (ready == true) {
        
        basic.clearScreen()
        basic.pause(randint(1000, 3000))
        playing = true
        music.playMelody("D", 500)
        while (playing == true && player1 == false && player2 == false) {
            basic.showLeds(`
            . # # # .
            # . . . #
            # . # . #
            # . . . #
            . # # # .
            `)
        }
        basic.pause(3000)
    }
})
forever(function vyhodnocovani() {
    
    if (playing == true) {
        if (player1 == true) {
            basic.showString("1")
            restart()
        } else if (player2 == true) {
            basic.showString("2")
            restart()
        } else if (player1 == true && player2 == true) {
            basic.showString("R")
            restart()
        }
        
    } else if (playing == false) {
        if (player1 == true) {
            playing = false
            basic.showString("A")
            restart()
        } else if (player2 == true) {
            playing = false
            basic.showString("B")
            restart()
        }
        
    }
    
})
function restart() {
    
    player1 = false
    player2 = false
    ready = false
    clicked_early1 = false
    clicked_early2 = false
    playing = false
    basic.clearScreen()
    basic.pause(3000)
    ready = true
}

