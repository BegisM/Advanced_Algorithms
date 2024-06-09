import unittest
from assignment_2_spell_checker.labyrinth.wizard_race import WizardRace

class TestLabyrinth(unittest.TestCase):
    def setUp(self):
        self.labyrinth = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': [],
            'F': ['E'],
            'E': []
        }
        self.wizards = ['A', 'B', 'C']
        self.speeds = [1, 2, 1.5]
        self.exit_position = 'E'
        self.race = WizardRace(self.labyrinth, self.exit_position)

    def test_wizard_race(self):
        winner = self.race.predict_winner(self.wizards, self.speeds)
        self.assertIn(winner, self.wizards)

if __name__ == '__main__':
    unittest.main()