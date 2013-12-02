class Camera(GameObject):
    """A Camera is a specific GameObject implementation"""


    def __init__(self, listener=True):
        super(Camera, self).__init__(self)

        self.listener = listener