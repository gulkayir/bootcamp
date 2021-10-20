import json
with open('task1.json', 'w') as mf:
    json_obj = mf.read()
    python_obj = json.dump(json_obj, mf)

with open('task1.py','w') as myfile:
    python_obj = json.load(myfile)

   
    
    
# with open ('task1.py', 'w') as file:
    
print(json_obj)
print(type(json_obj))