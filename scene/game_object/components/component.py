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

    def unload(self):
        if not self.loads:
            raise ComponentUnloadException

    def input(self, state):
        if not self.handles_input:
            raise ComponentInputException

    def update(self):
        pass

    def render(self):
        if not self.renders:
            raise ComponentRenderException

    def play_audio(self):
        if not self.has_audio:
            raise ComponentAudioException
        
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