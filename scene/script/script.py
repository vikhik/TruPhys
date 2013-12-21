class Script(object):
    """A Script is a global affector to the game state.
    
    For example: it may be an input handler, a ui element or a global game effect (such as gravity). 

    This is a prototype class and should be overriden.
    
    """

    def __init__(self):
        self.handles_input = False
        self.renders = False
        self.has_audio = False
        self.loads = False
        self.updates = False

    def load(self):
        if not self.loads:
            raise ScriptLoadException
        else:
            raise NotImplementedError

    def unload(self):
        if not self.loads:
            raise ScriptUnloadException
        else:
            raise NotImplementedError

    def input(self):
        if not self.handles_input:
            raise ScriptInputException
        else:
            raise NotImplementedError

    def render(self):
        if not self.renders:
            raise ScriptRenderException
        else:
            raise NotImplementedError

    def play_sound(self):
        if not self.has_audio:
            raise ScriptAudioException
        else:
            raise NotImplementedError

    def update(self):
        if not self.updates:
            raise ScriptUpdateException
        else:
            raise NotImplementedError
        
    def __repr__(self):
        """ Returns an object representation of the Script 
        Should be overridden with relevant details
        
        """
        return "%s - No Details" % (self.__class__.__name__)

    class ScriptInputException(Exception):
        pass

    class ScriptLoadException(Exception):
        pass

    class ScriptUnloadException(ScriptLoadException):
        pass

    class ScriptRenderException(Exception):
        pass

    class ScriptAudioException(Exception):
        pass

    class ScriptUpdateException(Exception):
        pass