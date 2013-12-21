from component import Component

class Transform(Component):
    """A Transform includes position, rotation and scale data for a GameObject"""

    def __init__(self, position = (0,0), rotation = 0.0, scale = 1.0):
        super(Transform, self).__init__()
        self.position = position
        self.rotation = rotation
        self.scale = scale

    def __repr__(self):
        """ Returns an object representation of the Component 
        Should be overridden with relevant details
        
        """
        return "%s - Position: %s, Rotation: %s, Scale: %s" % (self.__class__.__name__, self.position, self.rotation, self.scale)