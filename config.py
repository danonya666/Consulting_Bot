greetings = ['Hi!', 'Hello', 'My greetings', 'Howdy, parner!']

access_token = "558652107:AAGhJ5b3IqOsIIuf0d43ejeDZgWZdTqY3zc"

count = 0

command_list = ["/consult", "/site", "/help"]

command_length = len(command_list)

command_description = [" - Создай ресторан своей мечты!", " - Если хочешь перейти на наш сайт", " - Если запутался и нужна помощь"]

fcountries = open('countries.txt', 'r')

flogs = open('flogs.txt', 'a')

def get_countries(fcountries):
        countries = []
        for country in fcountries:
            countries.append(country.strip('\n').strip('\t'))

        return countries

countries = get_countries(fcountries)

friendly_phrases = ["Ты крутой", "Люблю тебя", "Я тебя люблю", "Давай дружить"]

friendly_stickers = ["CAADBQADGAcAAszG4gK5TgnCYv-AgQI", "CAADAgADDQcAAnlc4gmBs9-4TM8CwAI", "CAADAgADPgADyIsGAAEuCrQ7AXgedwI"]
