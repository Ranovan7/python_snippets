import json

'''
I read somewhere that using 'with' is better implementation cause it will
automatically close the file after it done, but the person saying it aren't really
sure so i'm gonna back at it after i found better explanation
'''

# loading existing json data first style
data = json.load(open("data/example.json"))

# loading existing json data second style
with open("data/example.json") as openfile:
    data = json.load(openfile)

# adding more data example into the existing data
for i in range(5):
    data.append({
        'id': i,
        'text': f"Some Data {i}"
    })

# using trycatch to prevent corrupting the file during saving attemp
try:
    json.dump(data, open("data/example.json", 'w'), indent=4)
except BaseException:
    print("An Error Occured during the attemp to save the data")
