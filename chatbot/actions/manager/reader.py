file = open("actions/manager/planner-for-relevant-policies/src/human_policy.out", "r")
savefile = open("actions/manager/policy.py", "w")
savefile.close()

lines = []
for ls in file:
    ls = file.read().splitlines()

for l in ls:
    lines.append(str(l))

#for l in lines:
#    print(l)

comands = []

for i in range(len(lines)):
    line = lines[i]

    if (str(line).find('If')) == False:
        line = line[10:]
        #print(line)
        predicates = line.split("/")
        #print(len(predicates))
        logic_string = "    if ("
        
        if(str(predicates[0]).find("not(") != -1):
            logic_string += str(str(predicates[0]).replace(")","")+"' in state_of_world)").replace("()", "").replace("('", "'").replace("not(", "not('")
        
        else:
            logic_string += str("('"+predicates[0]+"' in state_of_world)").replace("()", "")

        for p in predicates[1:]:
        
            if(str(p).find("not(") != -1):
                logic_string = logic_string + " and " + str(str(p).replace(")","")+"' in state_of_world)").replace("()","").replace("('", "'").replace("not(", "not('")
        
            else:
                logic_string = logic_string + " and " + str("('"+p+"' in state_of_world)").replace("()","")
            #print(p)
        
        logic_string += "):"
        #print(logic_string)
        comands.append(logic_string)
        execute = str(lines[i+1]).replace("Execute:", "").replace("/","").replace("SC","").replace("NSC","").replace("N","").rstrip().lstrip()
        
        for r in range(100):
            st = "d="+str(r)
            execute = execute.replace(st, "").rstrip().lstrip()
        
        for r in range(100):
            st = str(r)
            execute = execute.replace(st, "").strip().lstrip()
        
        comands.append("        "+"return "+"'"+execute+"'"+"\n".rstrip())
        #print("     "+execute) 

save = open("actions/manager/policy.py", "w")

save.write("def policy(state_of_world):\n")
for c in comands:
    save.write(str(c+"\n").replace("-","-"))

save.close()