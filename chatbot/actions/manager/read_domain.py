import actions.manager.Domain as Domain

def imprimi(lines):
    for l in lines:
        print(l)

def get_actions_domain(url = 'actions/manager/planner-for-relevant-policies/src/Dom.pddl'):
    domain = open(url, 'r')
    lines = []
    domain_lines = []
    for ls in domain:
        ls = domain.read().splitlines()
    for l in ls:   
        lines.append(str(l).lstrip().rstrip())
    for l in lines:
        if l != "":
            domain_lines.append(l)

    #imprimi(domain_lines)

    actions = []
    act = ''
    for i in range(len(domain_lines)):
        d = domain_lines[i]
    
    
        if str(d).find("(:action") != -1 :
            #print(d)
            action = Domain.Action('',[])
            act_name = str(d).replace("(:action", "").lstrip().rstrip().replace("_","-")
            action.set_name(act_name)
            out = domain_lines[i+1: ]
            #outcomes = []
            for j in range(len(out)):
                o = out[j]
                if(str(o).find("(:action") != -1):
                    #print()
                    break
                if str(o).find(":effect (and") != -1:
                    #print(o)
                    break
                elif str(o).find(";outcome") != -1:
                    out_name = str(o).replace(";outcome", "").lstrip().rstrip()
                    outcome = Domain.Outcome()
                    outcome.set_name(out_name)
                    stop = "continue"
                    #print(out_name)
                    pred = out[j+1:]
                    predicates = []
                    for k in range(len(pred)):
                        p = pred[k]
                        if(str(p).find("(and") != -1) or p == ")":
                            continue
                        if str(p).find(";outcome") != -1  or str(p).find("(:action") != -1:
                            stop = ";outcome"
                            break
                        else:
                            predicate =  Domain.Predicate()
                            
                            if(p.find("(not") != -1):
                                predicate.set_value(False)
                                p = str(p).replace('not', '').replace("(", "").replace(")", "").lstrip().rstrip()
                                predicate.set_name(str(p))
                            else:
                                predicate.set_value(True)
                                p = str(p).replace("(", "").replace(")", "").lstrip().rstrip()
                                predicate.set_name(str(p).lstrip().rstrip())
                            predicates.append(predicate)
                    #print(predicates)
                    outcome.set_predicates(predicates)
                    #print("outcome: ", outcome.get_name())
                    #print()
                    action.add_outcome(outcome)
                        #action.show_info()        
        #break
            actions.append(action)
        domain.close()
    return actions           
        
        


