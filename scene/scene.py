

class Scene(object):
    """A Scene is a collection of GameObjects and Scripts
    
    It handles loading, input, update and output of all GameObjects and Scripts.
    
    """

    text_output = True

    def __init__(self, game_objects, scripts):
        self.loaded = False
        self.game_objects = game_objects
        self.scripts = scripts

        self.game = None

    def load(self):
        if not self.loaded:
            for game_objects in game_objects:
                game_objects.load()
                game_object.scene = self

            self.loaded = True

    def unload(self):
        if self.loaded:
            pass

    def input(self):
        # TODO: Write this
        input_state = None

        for script in scripts:
            if script.handles_input:
                script.input(input_state)

        for game_object in game_objects:
            if game_object.handles_input:
                game_object.input(input_state)

    def update(self):
        for game_objects in self.game_objects:
            game_objects.update()

        for script in self.scripts:
            if script.updates:
                script.update()

    def output(self, audio=True):
        for game_object in self.game_objects:
            if game_object.renders:
                if not text_output:
                    game_object.render()
                else:
                    print(game_object)

            if audio and game_object.has_audio and not text_output:
                game_object.play_audio()

        for script in self.scripts:
            if script.renders:
                if not text_output:
                    script.render()
                else:
                    print(script)

            if audio and script.has_audio and not text_output:
                script.play_audio()