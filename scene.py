

class Scene(object):
    """description of class"""


    def __init__(self):
        self.loaded = False

    def load(self):
        if not self.loaded:
            pass

    def unload(self):
        if self.loaded:
            pass

    def input(self):
        pass

    def update(self):
        pass

    def output(self, audio=True):
        pass
