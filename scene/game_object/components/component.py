class Component(object):
    """A Component is the building block of all GameObjects
    
    For Example: Transform, RigidBody, InputHandler, AI, Sprite, AudioSource, etc.

    This is a prototype class and should be overriden.

    """
    
    def __init__(self):
        self.renders = False
        self.has_audio = False
        self.handles_input = False
        self.loads = False

        self.game_object = None

    def load(self):
        if not self.loads:
            raise ComponentLoadException
        else:
            raise NotImplementedError

    def unload(self):
        if not self.loads:
            raise ComponentUnloadException
        else:
            raise NotImplementedError

    def input(self, state):
        if not self.handles_input:
            raise ComponentInputException
        else:
            raise NotImplementedError

    def update(self):
        pass

    def render(self):
        if not self.renders:
            raise ComponentRenderException
        else:
            raise NotImplementedError

    def play_audio(self):
        if not self.has_audio:
            raise ComponentAudioException
        else:
            raise NotImplementedError

    def __repr__(self):
        """ Returns an object representation of the Component 
        Should be overridden with relevant details
        
        """
        return "%s - No Details" % (self.__class__.__name__)
        
    class ComponentRenderException(Exception):
        pass

    class ComponentAudioException(Exception):
        pass

    class ComponentLoadException(Exception):
        pass

    class ComponentUnloadException(ComponentLoadException):
        pass

    class ComponentInputException(Exception):
        pass