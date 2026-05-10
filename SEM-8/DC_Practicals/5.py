from collections import defaultdict

data = [
    ("2001", 30),
    ("2001", 32),
    ("2002", 25),
    ("2002", 28),
    ("2003", 35),
    ("2003", 36),
    ("2004", 20),
    ("2004", 22),
]


def mapper(data):
    return [(year, temp) for year, temp in data]


def shuffle(mapped):
    d = defaultdict(list)
    for year, temp in mapped:
        d[year].append(temp)
    return d


def reducer(shuffled):
    avg_temp = {}
    for year, temps in shuffled.items():
        avg_temp[year] = sum(temps) / len(temps)
    return avg_temp


mapped = mapper(data)
shuffled = shuffle(mapped)
reduced = reducer(shuffled)
hottest = max(reduced, key=reduced.get)
coolest = min(reduced, key=reduced.get)
print("Average:", reduced)
print("Hottest Year:", hottest)
print("Coolest Year:", coolest)
