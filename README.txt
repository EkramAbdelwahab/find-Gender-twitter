#finding gender of the user of each tweet:

- getting tweets from twitter using twitter api.
- saving these tweets in a text file(all_result.txt).
- in this script: open this file
- loop on each line and extract user name.
  note that user name contains first and second name.
- splite the user name for getting the first name only.
- appending all first names in an array.
- then to determin if the gender is male. female or  
   undetermined use the link "http://api.genderize.io/"
   by making a request to check the name.
- then print the gender of each name.
/////////////

#difficults:
- getting api for finding gender from the user name.
- on creating twitter account, twitter doesn't require   gender.

# test

I used this array for testing 
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

then used tweets user name (first name) 

# results
you can see some snapshots for results.
//////////////////////////////////////////////
# on Elasticsearch
- you can also know gender from elasticsearchan in snapshots.
- on elasticsearch max_number of names that it can derermin its gender is 10 names only in one time.
//////////////////////////////////////////////
#running
- you can run this script as any python script using 
  python test_gender.py