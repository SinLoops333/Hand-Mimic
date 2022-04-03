from pyPS4Controller.controller import Controller

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_up_arrow_press(self):
        print("going up")

    def on_up_down_arrow_release(self):
        print("not going up anymore")

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen(timeout=60)
#use all buttons