trains = [
    {'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
    {'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
    {'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
    {'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
    {'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
    {'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
    {'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
    {'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]
next(train for train in trains if train["train"] == "111")

next(train for train in trains if train["train"] == "111")

trains_north = []
for num in range(0, len(trains)):
    if trains[num]['direction'] == 'north':
        trains_north.append(trains[num]['train'])

trains_east = []
for num in range(0, len(trains)):
    if trains[num]['direction'] == 'east':
        trains_east.append(trains[num]['train'])

trains_by_frequency = {}

for train in trains:
    name = train['train']
    freq = train['frequency_in_minutes']

    if freq in trains_by_frequency:
        trains_by_frequency[freq].append(name)
    else:
        trains_by_frequency[freq] = [name]


print(trains_by_frequency)
