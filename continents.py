continents = [
    'Asia',
    'South America',
    'North America',
    'Africa',
    'Europe',
    'Antarctica',
    'Australia',
]


my_list = []
char = 'A'
for item in continents:
  if item[0] in char:
    my_list.append(item)
  else:
    continue
for continent in my_list:
  print('* ' + continent)