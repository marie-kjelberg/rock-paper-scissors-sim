import numpy as np
import time 
import random
import multiprocessing
import matplotlib.pyplot as plt
from collections import Counter
TIMES = 10_000_000
FPS = 60
dt = 1/FPS
win_map = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}
object_dimensions = (32, 32)
(width, height) = (720, 600)
amounts = 5
spawn_range = 100
speed = 50*10
class Object:
    def __init__(self, type, x, y, v, angle):
        self.type = type
        self.x = x
        self.y = y
        self.v = v
        self.angle = angle

    def update_type(self, new_type): 
       self.type = new_type

    def update_pos(self, dt):
        if self.x <= 0 or self.x + object_dimensions[0] >= width: 
            self.angle = 2*np.pi - self.angle
            self.v = -self.v

        if self.y <= 0 or self.y + object_dimensions[1] >= height:
            self.angle = 2*np.pi - self.angle

        self.x += self.v * np.cos(self.angle) * dt
        self.y += self.v * np.sin(self.angle) * dt

def collision_check(x1, y1, x2, y2):
    ''' assumes both objects are sized normally '''
    return (
        x1 < x2 + object_dimensions[0] and
        x1 + object_dimensions[0] > x2 and
        y1 < y2 + object_dimensions[1] and
        y1 + object_dimensions[1] > y2
    ) 

#winners = []
start = time.time()
def run_sim(e):
    all_elements = []
    elements = ["rock", "paper", "scissors"]
    for i, element in enumerate(elements):
        for k in range(amounts):
            x = random.randrange(0, width-object_dimensions[0])
            y = random.randrange(0, height-object_dimensions[1])
            angle = random.randrange(-180, 180)
            angle = np.radians(angle)
            all_elements.append(Object(element, x, y, speed, angle))
    counts = {
    "rock": amounts,
    "scissors": amounts,
    "paper": amounts
    }
    final_winner = ""

    running = True
    while running:
        #start = time.time()

        for i, element in enumerate(all_elements):
            for j, element2 in enumerate(all_elements):
                if i == j: continue
                # check collision
                # i chose rect collision cuz I can't be bothered with anything else
                if not collision_check(element.x, element.y, element2.x, element2.y): continue

                if element.type == element2.type: continue

                if win_map[element.type] == element2.type:
                    winner = element.type
                    loser = element2.type
                    element2.update_type(element.type)
                else:
                    winner = element2.type
                    loser = element.type
                    element.update_type(element2.type)
                counts[winner] += 1
                counts[loser] -= 1
                final_winner = winner
            element.update_pos(dt)

        if counts["rock"] == 3* amounts or counts["paper"] == 3*amounts or counts["scissors"] == 3*amounts:
            #print(f"{final_winner} won.")
            #winners.append(final_winner)
            running = False 
    return final_winner

if __name__ == "__main__":
    with multiprocessing.Pool(processes=multiprocessing.cpu_count() - 1) as pool:
        results = pool.map(run_sim, range(TIMES))
        print(results)
        dur = time.time() - start
        print(dur)
        with open(f"output{TIMES}.txt", "w") as file:
            file.write(f"{dur}\n")
            for result in results:
                file.write(str(result) + "\n")

        counts = Counter(results)
        labels = list(counts.keys())
        values = list(counts.values())
        colour_map = {
            "rock": "gray",
            "paper": "blue",
            "scissors": "red"
        }
        colours = [colour_map[label] for label in labels]
        
        plt.bar(labels, values, color=colours)
        plt.title(f"Abundance of Rock, Paper, Scissors: {dur}s")
        plt.xlabel("Winners")
        plt.ylabel("Count")
        plt.savefig(f"./{TIMES}.png")
        plt.show()
