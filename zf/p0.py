import json
import os

# Get current working directory
patha = os.getcwd()
files=os.listdir(patha)#create a list of the contnt of the folder with that path
print(files)
""" # Create a folder path
pathf = os.path.join(patha, "zf")
exist=os.path.exists(pathf)#check if the file exists or not
if (not exist):
    os.mkdir(pathf)#create the folder
# Create an absolute path to the JSON file
pathjson = os.path.join(pathf, "data.json")

# Dictionary to be written as JSON
data = {
    "language": "python",
    "score": 10,
    "chapters":"read"
}
#dump convert the dict to str the opposite of loads
# Write the dictionary to the JSON file
with open(pathjson, "w") as jsonfile:
    content = json.dumps(data)
    jsonfile.write(content)
with open(pathjson,'r') as jsonfile:
    content=jsonfile.read()
    data=json.loads(content)
    print(data)
 """