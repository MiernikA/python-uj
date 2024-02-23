import tkinter as tk
import random
import copy
from data import Data

data_container = Data()

# Globals
BT_WIDTH = 8
BT_HEIGHT = 1
GRID_SIZE = 20
CELL_SIZE = 30
CELL_BORDER_WIDTH = 1
UPDATE_DELAY = 200
LIVING_RULE = [2, 3]
RESPAWN_RULE = [3]

grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
prev_grids = []
is_running = False
running_id = None

def initialize_grid():
    return [[0] * GRID_SIZE for _ in range(GRID_SIZE)]


def update_grid():
    prev_grids.append(copy.deepcopy(grid))
    new_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            live_neighbors = 0

            # checking for neighbors
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    if 0 <= row + dr < GRID_SIZE and 0 <= col + dc < GRID_SIZE:
                        live_neighbors += grid[row + dr][col + dc]

            # creating next gen
            if grid[row][col] == 1:
                if live_neighbors not in LIVING_RULE:
                    new_grid[row][col] = 0
                else:
                    new_grid[row][col] = 1
            else:
                if live_neighbors in RESPAWN_RULE:
                    new_grid[row][col] = 1
    return new_grid


def step():
    global grid
    grid = update_grid()
    draw_grid()
    if is_running:
        global running_id
        running_id = root.after(UPDATE_DELAY, step)


def step_back():
    if prev_grids:
        global grid
        grid = prev_grids.pop()
        draw_grid()


def draw_grid():
    # draw array on ui
    canvas.delete("cell")
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == 1:
                cell_color = "black"
            else:
                cell_color = "white"
            canvas.create_rectangle(
                col * CELL_SIZE,
                row * CELL_SIZE,
                (col + 1) * CELL_SIZE,
                (row + 1) * CELL_SIZE,
                fill=cell_color,
                outline="grey",
                width=0.4,
                tags="cell",
            )


def toggle_running():
    global is_running
    is_running = not is_running
    if is_running:
        start_button.config(text="Stop")
        step()
    else:
        start_button.config(text="Start")
        if running_id is not None:
            root.after_cancel(running_id)


def go_one_step():
    if not is_running:
        step()


def clear_grid():
    global is_running
    if is_running:
        is_running = False
        start_button.config(text="Start")

    global grid
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    draw_grid()


def redraw_grid():
    global grid
    grid = []
    for i in range(GRID_SIZE):
        array = []
        for j in range(GRID_SIZE):
            if random.randrange(2) == 0:
                array.append(0)
            else:
                array.append(1)
        grid.append(array)
    draw_grid()


def toggle_cell(row, col):
    grid[row][col] = 1 if grid[row][col] == 0 else 0
    draw_grid()


def select_pattern(pattern_name):
    selected_pattern.set(pattern_name)


def apply_pattern(pattern):
    clear_grid()
    global grid
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            grid[i][j] = pattern[i][j]
    draw_grid()


def apply_selected_pattern():
    selected = selected_pattern.get()
    if selected is not None and selected in data_container.patterns:
        pattern = data_container.patterns[selected]
        apply_pattern(pattern)


def select_rule(rule_name):
    selected_rule.set(rule_name)
    rule_label.config(text=f"Rule: {rule_name}")
    apply_selected_rule()


def apply_selected_rule():
    global is_running
    if is_running:
        is_running = False
        start_button.config(text="Start")
    global LIVING_RULE, RESPAWN_RULE
    selected = selected_rule.get()
    if selected is not None and selected in data_container.rules:
        LIVING_RULE = data_container.rules[selected][0]
        RESPAWN_RULE = data_container.rules[selected][1]

        # holder
        current_rule_label.config(text=f"Rule: {selected}")


# SETUP

root = tk.Tk()
root.title("Game of Life")

canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
canvas.pack()

grid_map = initialize_grid()
draw_grid()

button_frame = tk.Frame(root)
button_frame.pack(side="bottom", pady=10)

top_button_frame = tk.Frame(root)
top_button_frame.pack(side="top", pady=10)

start_button = tk.Button(top_button_frame, text="Start", command=toggle_running, width=BT_WIDTH, height=BT_HEIGHT, bd=4,
                         font="Verdana")
start_button.pack(side="left", padx=10, pady=10)

random_button = tk.Button(top_button_frame, text="Random", command=redraw_grid, width=BT_WIDTH, height=BT_HEIGHT, bd=4,
                          font="Verdana")
random_button.pack(side="left", padx=10)

clear_button = tk.Button(top_button_frame, text="Clear", command=clear_grid, width=BT_WIDTH, height=BT_HEIGHT, bd=4,
                         font="Verdana")
clear_button.pack(side="left", padx=10)

step_back_button = tk.Button(top_button_frame, text="Step Back", command=step_back, width=BT_WIDTH, height=BT_HEIGHT,
                             bd=4, font="Verdana")
step_back_button.pack(side="left", padx=10)

step_button = tk.Button(top_button_frame, text="Step", command=go_one_step, width=BT_WIDTH, height=BT_HEIGHT, bd=4,
                        font="Verdana")
step_button.pack(side="left", padx=10)

# ------------
middle_button_frame = tk.Frame(root)
middle_button_frame.pack(side="top", pady=10)

pattern_label = tk.Label(middle_button_frame, text="Select Pattern:", font="Verdana")
pattern_label.pack(side="left", padx=10)

pattern_options = list(data_container.patterns.keys())
selected_pattern = tk.StringVar(root)
selected_pattern.set(pattern_options[0])

pattern_menu = tk.OptionMenu(middle_button_frame, selected_pattern, *pattern_options)
pattern_menu.config(width=BT_WIDTH * 2, height=BT_HEIGHT, bd=4, font="Verdana")
pattern_menu.pack(side="left", padx=10)

apply_pattern_button = tk.Button(middle_button_frame, text="Apply Pattern", command=apply_selected_pattern,
                                 width=BT_WIDTH * 2, height=BT_HEIGHT, bd=4, font="Verdana")
apply_pattern_button.pack(side="left", padx=10)

# ------------
bottom_button_frame = tk.Frame(root)
bottom_button_frame.pack(side="top", pady=10)

rule_label = tk.Label(bottom_button_frame, text="    Select Rule:", font="Verdana")
rule_label.pack(side="left", padx=10)
rule_options = list(data_container.rules.keys())
selected_rule = tk.StringVar(root)
selected_rule.set(rule_options[0])

rule_menu = tk.OptionMenu(bottom_button_frame, selected_rule, *rule_options)
rule_menu.config(width=BT_WIDTH * 2, height=BT_HEIGHT, bd=4, font="Verdana")
rule_menu.pack(side="left", padx=10)

apply_rule_button = tk.Button(bottom_button_frame, text="Apply Rule", command=apply_selected_rule, width=BT_WIDTH * 2,
                              height=BT_HEIGHT, bd=4, font="Verdana")
apply_rule_button.pack(side="left", padx=10, )

current_rule_label = tk.Label(root, text="Current Rule: Default 23/3", font="Verdana")
current_rule_label.pack(side="bottom", padx=10, pady=10)

canvas.bind("<Button-1>", lambda event: toggle_cell(event.y // CELL_SIZE, event.x // CELL_SIZE))

root.mainloop()
