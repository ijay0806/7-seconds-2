start = 0
elapse = 0
score = 0

def on_button_pressed_a():
    global start
    start = input.running_time()
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global elapse, score
    elapse = input.running_time() - start
    score = abs(7000 - elapse)
    basic.show_number(score)
input.on_button_pressed(Button.B, on_button_pressed_b)
