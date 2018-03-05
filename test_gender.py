import requests
import json
"""
names = [
'John',
'Jane',
'ekram',
'hanaa',
'samah',
'sara',
'romany',
'beshoy',
'mai',
'eman'
];

"""
names = []
tweet_file_Name = 'all_result.txt'
tweets_file = open(tweet_file_Name, "r")
#//////////////////////////////////////////////
for line in tweets_file:
    try:
        tweet = json.loads(line.strip())
        if 'text' in tweet:
            str = tweet['user']['name']
            str = str.split( )
            first_name = str[0]
            names.append(first_name)

    except:
        continue

#//////////////////////////////////////////

female = 0
male = 0
cant_tell = 0
undetermined_names = []

for name in names:
    request_string = "http://api.genderize.io/?name=" + name
    r = requests.get(request_string)
    result = json.loads(r.content)
    if result['gender']=='female':
        #female = female+1
         print name +"=> " + "gender : " + result['gender']
    elif result['gender']=='male':
        #male =male+1
        print name +"=> " + "gender : " + result['gender']
    else:
        #cant_tell=cant_tell+1
        undetermined_names.append(name)
        print name +"=> " + "gender : unknown"

