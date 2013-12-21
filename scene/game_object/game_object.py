from transform import Transform

class GameObject(object):
    """A GameObject is a collection of Components
    
    It handles loading, input, update and output of all Components.

    A GameObject must have a Transform (this is automatically added during creation as the 0th component).

    """

    def __init__(self, components, name = "Game Object"):
        self.components = [Transform, ] + components
        self.name = name
        
        self.handles_input = False
        self.renders = False
        self.has_audio = False
        self.loads = False

        self.scene = None

        for component in self.components:
            component.game_object = self

            if component.handles_input:
                self.handles_input = True

            if component.renders:
                self.renders = True

            if component.has_audio:
                self.has_audio = True

            if component.loads:
                self.loads = True

    def load(self):
        if not self.loads:
            raise GameObjectLoadException

        for component in self.components:
            if component.loads:
                component.load()

    def unload(self):
        if not self.loads:
            raise GameObjectUnloadException

        for component in self.components:
            if component.loads:
                component.unload()

    def input(self, state):
        if not self.handles_input:
            raise GameObjectInputException

        for component in self.components:
            if component.handles_input:
                component.input(state)

    def render(self):
        if not self.renders:
            raise GameObjectRenderException

        for component in self.components:
            if component.renders:
                component.render()

    def play_audio(self):
        if not self.has_audio:
            raise GameObjectRenderException

        for component in self.components:
            if component.has_audio:
                component.play_audio()

    def __repr__(self):
        """ Returns an object representation of the Game Object and all Components 
        Does not need to be overridden.
        
        """
        if not self.renders:
            raise GameObjectRenderException

        str = "%s:\n" % (self.name)

        for component in self.components:
            if component.renders:
                str += "\t" + repr(component) + "\n"

    class GameObjectLoadException(Exception):
        pass

    class GameObjectUnloadException(GameObjectLoadException):
        pass

    class GameObjectRenderException(Exception):
        pass

    class GameObjectAudioException(Exception):
        pass

    class GameObjectLoadException(Exception):
        pass

    class GameObjectInputException(Exception):
        pass