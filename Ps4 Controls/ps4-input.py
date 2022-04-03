from pyPS4Controller.controller import Controller


def konami_callback():
    print("Konami sequence detected!")


def my_sequences():
    return [
        {"inputs": ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'share', 'options'],
         "callback": konami_callback}
    ]


controller = Controller(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen(on_sequence=my_sequences())

#             Inputs you can use:
# x
# square
# triangle
# circle
# up
# down
# left
# right
# L1
# L2
# L3
# R1
# R2
# R3
# left_joystick
# right_joystick
# share
# options
# ps