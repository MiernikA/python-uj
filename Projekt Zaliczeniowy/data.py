class Data:
    def __init__(self):
        self.patterns = {
            "Glider": [
                [0, 1, 0],
                [0, 0, 1],
                [1, 1, 1]
            ],
            "Blinker": [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 1, 1, 1]
            ],
            "Toad": [
                [0, 0, 0, 0],
                [0, 1, 1, 1],
                [1, 1, 1, 0],
                [0, 0, 0, 0]
            ],
            "Beacon": [
                [1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 1, 1]
            ],
            "Pulsar": [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            ],
            "Spaceship": [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [1, 1, 0, 1, 1],
                [1, 1, 1, 1, 0],
                [0, 1, 1, 0, 0]
            ],
            "Pentadecathlon": [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            ],

        }
        self.rules = {
            "Conway's 23/3": [
                [2, 3],
                [3]
            ],
            "34/34": [
                [3, 4],
                [3, 4]
            ],
            "Seeds /2": [
                [],
                [2]
            ],
            "Growth 1/1": [
                [1],
                [1]
            ],
            "Coral 45678/3": [
                [4, 5, 6, 7, 8],
                [3]
            ],
            "Maze 12345/3": [
                [1, 2, 3, 4, 5],
                [3]
            ],
            "Wolfram 0<->8/1": [
                [0, 1, 2, 3, 4, 5, 6, 7, 8],
                [3]
            ],
            "Long Life 5/345": [
                [5],
                [3, 4, 5]
            ]

        }
