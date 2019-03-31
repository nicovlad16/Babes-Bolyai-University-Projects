class Console():
    def __init__(self, ctrl):
        self.__ctrl = ctrl


    def run(self):
        while True:
            print(self.__ctrl.get_grid())
            cmd = input(">>")
            cmd = cmd.strip()
            cmds = cmd.split(" ")
            try:
                if not cmd:
                    print("Invalid command.")
                elif cmds[0] == "exit":
                    exit(0)
                elif cmds[0] == "tick":
                    self.__ui_tick(cmds[1:])
                elif cmds[0] == "place":
                    self.__ui_place(cmds[1:])
                elif cmds[0] == "save":
                    self.__ui_save(cmds[1:])
                elif cmds[0] == "load":
                    self.__ui_load(cmds[1:])
                else:
                    print("Invalid command.")
            except Exception as e:
                print(e)


    def __ui_tick(self, params):
        if len(params) == 0:
            self.__ctrl.tick()
            print("New generation successfully created.")
        elif len(params) == 1:
            self.__ctrl.tick(params[0])
            print("New generations successfully created.")
        else:
            print("Invalid params.")


    def __ui_place(self, params):
        if len(params) != 2:
            print("Invalid params.")
            return
        else:
            self.__ctrl.place_pattern(params[0], params[1])
            print("pattern added")


    def __ui_save(self, params):
        if len(params) != 1:
            print("Invalid params.")
            return
        else:
            filename = params[0]
            self.__ctrl.save_file(filename)
            print("file saved")


    def __ui_load(self, params):
        if len(params) != 1:
            print("Invalid params.")
            return
        else:
            filename = params[0]
            self.__ctrl.load_file(filename)
            "file opened"
