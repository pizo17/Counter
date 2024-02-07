class Config:
    def __init__(self, filename, description, key_count_up, key_count_down, key_reset, key_refresh, key_help, key_return, key_quit):
        self.filename = filename
        self.description = description
        self.key_count_up = key_count_up
        self.key_count_down = key_count_down
        self.key_reset = key_reset
        self.key_refresh = key_refresh
        self.key_help = key_help
        self.key_return = key_return
        self.key_quit = key_quit


# loads config from cfg.csv
def load_cfg():
    with open("cfg.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()

        # splitting read lines at ";" separators
        line0 = lines[0].strip().split(";")
        line1 = lines[1].strip().split(";")
        line2 = lines[2].strip().split(";")
        line3 = lines[3].strip().split(";")
        line4 = lines[4].strip().split(";")
        line5 = lines[5].strip().split(";")
        line6 = lines[6].strip().split(";")
        line7 = lines[7].strip().split(";")
        line8 = lines[8].strip().split(";")

        # saving actual config content to constructor
        filename = line0[0]
        description = line1[0]
        key_count_up = line2[0]
        key_count_down = line3[0]
        key_reset = line4[0]
        key_refresh = line5[0]
        key_help = line6[0]
        key_return = line7[0]
        key_quit = line8[0]

        return Config(filename, description, key_count_up, key_count_down, key_reset, key_refresh, key_help, key_return, key_quit)


