import os


old_modules = []

# split the command output in lines:
list_modules = os.popen("pip list --outdated").read().split("\n")
#print(list_modules)


for line in list_modules:
    old_modules.append(line)
    
#print(old_modules)


old_modules.pop(0)
old_modules.pop(0)
old_modules.pop()
print(old_modules)

modules_to_update = []

# take the first word(module name) of each line:
for word in old_modules:
    modules_to_update.append(word.split()[0])
    

print(modules_to_update)


for word in modules_to_update:
    os.system(f"pip install --upgrade {word}")
