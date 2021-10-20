import pickle, os
import random

filename = "words.txt"

def get_contents():
    f = open(filename, 'rb')
    d = {}

    try:
        while True:
            d = pickle.load(f)
    except EOFError:
        f.close()

    return d

def write(data):
    try:
        os.remove(filename)
    except:
        pass

    f = open(filename, 'wb')
    pickle.dump(data, f)
    f.close()

    return True

def add_profile(profile_name):
    d = get_contents()
    d.update({profile_name.upper(): {}})

    return write(d)

def add_data(profile, key, value):
    d = get_contents()
    data = d[profile.upper()]

    data.update({key.upper(): value})
    d.update({profile.upper(): data})

    return write(d)

def quiz():
    d = get_contents()
    d = d["VOCABULARY"]

    done = []
    wrong = []
    score = 0

    d = {v: k for k, v in d.items()}

    while len(done) != len(d):
        key = random.choice(list(d.keys()))

        if key not in done:
            print(key)
            user = input("Give the word: ")
            print(d[key])

            if user.upper() != d[key].upper():
                wrong.append({"user": user, "answer": d[key]})
            else:
                score += 1

            done.append(key)

    return score, len(done), wrong

def expand():

    while 1:
        w = input("Word: ")
        m = input("Meaning: ")
        add_data("vocabulary", w, m)


    
