class ForceUser:
    """
    Basic outline for a character
    has name, level, stats based off of specialty
    level goes up over time, stats go up based on level
    """
    def __init__(self, name, specialty=None):
        self.name = name
        self.specialty = specialty
        self.level = 1
        self.stats = {i: self.level * 5 for i in ['force', 'lightsaber', 'wisdom']}
        self.stats[specialty] += 10

menny = ForceUser("Menny Wung", 'lightsaber')
print(menny.name, menny.stats)
