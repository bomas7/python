import webbrowser
import json


class Photo:

    def __init__(self, name, url, description):
        self.name = name
        self.url = url
        self.description = description
        self.rating = None

    @classmethod
    def from_str(cls, str):
        name, url, description = str.split(' - ')
        return cls(name, url, description)

    def show_image(self):
        path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(path).open(self.url)

    def print_description(self):
        print('Picture - {}: \n\t Description - {}'.format(self.name, self.description))

    def get_rating(self):
        try:
            user_rating = input('Enter your rating for this picture: ')
            if 0 < int(user_rating) < 11:
                return int(user_rating)
        except ValueError:
            pass
        print('\nRemember to enter a number between 1 and 10\n')
        return self.get_rating()

    def store_rating(self, rating):
        f_name = 'ratings.txt'
        with open(f_name, 'r') as f:
            ratings = json.loads(f.read().strip())
            if ratings.get(self.name):
                ratings[self.name].append(rating)
            else:
                ratings[self.name] = [rating]
        with open(f_name, 'w') as f:
            f.write(json.dumps(ratings))
        self.rating = sum(ratings[self.name]) / len(ratings[self.name])



# test = Photo('http://google.com', 'test', 'this is a test photo')
# test.show_image()
# test.print_description()
##https://stackoverflow.com/questions/22445217/python-webbrowser-open-to-open-chrome-browser?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
##https://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
