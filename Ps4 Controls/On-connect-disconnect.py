from pyPS4Controller.controller import Controller


def connect():
    # any code you want to run during initial connection with the controller
    pass

def disconnect():
    # any code you want to run during loss of connection with the controller or keyboard interrupt
    pass



class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen(on_connect=connect, on_disconnect=disconnect)