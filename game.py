class Game(object):
    """This is the main Game class
    
    .change_scene("scene_name")
    .run()
    .current_scene = Scene

    If a temporary scene needs to draw the current scene before itself, 
    it can do so using game.current_scene.ouput(audio=False)

    """

    def __init__(self, scene_list):
        """ Initialise the Game

        scene_list is a list of Scene objects, the first of which is the initial Scene to be loaded and run

        """

        self.__scene_dict = {}

        for scene in scene_list:
            # Hold all scenes in memory, indexed by their .name
            self.__scene_dict[scene.name] = scene

            # Let each scene know about Game so they can change scene when necessary
            scene.game = self 

        self.current_scene = scene_list[0]
        self.__temp_scene = None
        self.__next_scene = None
        self.playing = True

    def change_scene(self, name):
        """ Changes the current scene to a scene with name
        
        This should be called when the current scene is to be unloaded 
        
        Use this when, for example, you are changing levels
        
        """
        if self.__scene_dict.has_key(name):
            self.__next_scene = self.__scene_dict[name]
            
    def open_temp_scene(self, name):
        """ Temporarily changes the current scene to a scene with name
        
        This should be called when the current scene is to be kept loaded and returned to
       
        Use this when, for example, you want a menu drawn over the top of the current scene
        
        """
        if self.__scene_dict.has_key(name):
            self.__temp_scene = self.__scene_dict[name]
            self.__temp_scene.load()

    def close_temp_scene(self):
        """ Exit the temporary running scene and return to running the current scene """
        if (self.__temp_scene):
            self.__temp_scene.unload()
            self.__temp_scene = None

    def run(self):
        """ Runs the game

        Calls input(), update() and output() on the current_scene

        Then, if a valid change_scene() request has been made,
        we perform a scene transition.

        """

        while (self.playing):
            # Check if there is a temporary scene
            running_scene = self.__temp_scene

            # If there is no temporary scene
            if running_scene is None:
                running_scene = self.current_scene

            running_scene.input()
            running_scene.update()
            running_scene.output()

            # Check if we need to change scenes
            if (self.__next_scene):
                self.__perform_scene_transition()

        self.__unload()

    def __unload(self):
        for scene in [self.current_scene, self.__next_scene, self.__temp_scene]:
            if scene is not None and scene.loaded:
                scene.unload()

    def __perform_scene_transition():
        self.__current_scene.unload()
        self.__current_scene = self.__next_scene
        self.__next_scene = None
        self.__current_scene.load()