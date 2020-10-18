let start = 0
let elapse = 0
let score = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    start = input.runningTime()
    basic.showIcon(IconNames.Heart)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    elapse = input.runningTime() - start
    score = Math.abs(7000 - elapse)
    basic.showNumber(score)
})
