from .bfs import BFS


class WizardRace:
    def __init__(self, labyrinth, exit_position):
        self.labyrinth = labyrinth
        self.exit_position = exit_position

    def predict_winner(self, wizards, speeds):
        times = []

        for wizard, speed in zip(wizards, speeds):
            time_to_exit = BFS.find_shortest_path(self.labyrinth, wizard, self.exit_position) / speed
            times.append((time_to_exit, wizard))

        return min(times)[1]