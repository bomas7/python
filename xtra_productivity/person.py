import datetime

class Activity:

    def __init__(
        self, name, description, frequency,
        start_date = datetime.date.today(),
        days_completed = None
    ):
        self.name = name
        self.description = description
        self.frequency = frequency
        self.start_date = start_date
        if days_completed:
            self.days_completed = days_completed
        else:
            self.days_completed = []

    @classmethod
    def from_input(cls):
        try:
            return cls(input('Name: '), input('Description: '), int(input('Frequency: ')))
        except ValueError:
            print('Frequency is how often you would like to perform a task (in days)')

    @classmethod
    def from_dict(cls, kwargs):
        return cls(**kwargs)

    def store(self):
        with open(self.name + '.txt', 'w') as f:
            f.write(str(vars(self)))

def main():
    tester = Activity('Daily Programming', 'Program for at least 30 minutes a day', 1)
    test2 = Activity.from_dict(tester.store())
    print(vars(test2))

if __name__ == '__main__':
    main()
