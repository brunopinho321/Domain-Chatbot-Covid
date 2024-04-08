import actions.manager.Domain as Domain
import actions.manager.policy as policy

#domain  = Action.Domain()
#domain.set_actions(read_domain.get_actions_domain())
state = []
path = []

def intent_entity_to_predicate(intents = [], entidies = []):

    input = intents + entidies
    user_return = []
    for i in input:
        if i.find('not-') != -1:
            i_ = i.replace("not-","")
            user_return.append(Domain.Predicate(str(i_), False))
        elif i.find('(not') != -1:
            i_ = i.replace("(not","").replace("(","").replace(")", "")
            user_return.append(Domain.Predicate(str(i_), False))
        else:    
            user_return.append(Domain.Predicate(str(i), True))
    return user_return


def realization(action, intents = [], entidies = []):
    do = Domain.Domain()
    outcomes = action.get_outcomes()
    flag = False
    user_return = intent_entity_to_predicate(intents, entidies)
    for outcome in outcomes:
        for e in user_return:
            flag = do.contain(e, outcome)
            if(flag == False):
                break
        if(flag == True):
            return flag, outcome
    return flag, None

def outcome_determination(action_name, intent = '', entidies = []):
    do = Domain.Domain()
    action = do.get_action_by_name(action_name) 
    if(len(action.get_outcomes()) == 1):
        return action.get_outcomes()[0]
    flag, outcome = realization(action, [intent], entidies)
    if(flag == True):
        return outcome
    else:
        return None

def update(state_of_world, action_name, intent = '', entidies = []):
    outcome = outcome_determination(action_name, intent, entidies)
    if outcome == None:
        return state_of_world, None
    for predicate in outcome.get_predicates():
        if(predicate.get_value() == True):
            if(not(predicate.get_name() in state_of_world)):
                state_of_world.append(predicate.get_name())
        else:
            if(predicate.get_name() in state_of_world):
                if(predicate.get_value() == False):
                    try:
                        while True:
                            state_of_world.remove(predicate.get_name())
                    except ValueError:
                        pass
    return state_of_world, outcome

def wait_user_utter(action_name = '', intent = '', entidies = []):
    global state 
    if (intent.find('not-') != -1):
            intent = '(not('+intent.replace("not-", "")+'))'
    if state == []:
        if intent != '':
            state = entidies + [intent]
        return state, None
    state_of_world = state 
    state, outcome = update(state_of_world, action_name, intent, entidies)
    if(outcome == None):
        state, outcome = update(state_of_world, action_name, 'can-go-error-treatment', entidies = [])
    return state, outcome

#def wait(action_name, intent = '', entidies = []):
#    do = Domain.Domain()
#    action = do.get_action_by_name(action_name)
#    if len(action.get_outcomes()) == 1:
#        wait_user_utter(action_name, intent, entidies)
#        global state
#        return [action.get_name()] + wait(policy.policy(state), intent, entidies)
#    else:
#        return [policy.policy(state)]

def action_execution():
    global state
    p = policy.policy
    do = Domain.Domain()
    #  print('Policy: ', p(state))
    action = do.get_action_by_name(p(state))
    if action == None:
        return []
    elif(len(action.get_outcomes()) == 1):
        act = p(state)
        path.append(p(state))
        #print("action: ",act)
        wait_user_utter(action_name = p(state))
        return [act] + action_execution()
    else:
        path.append(p(state))
        #print("action: ",p(state))
        return [p(state)]

def get_path():
    return path

#state = ['user-initiative']
#wait_user_utter(intent='user-initiative')

#p = policy.policy

#print(p(state))
#do = Domain.Domain()

#actions = action_execution()
#print('state = ', state)
#print('actions = ',  actions)
# wait_user_utter(actions[-1], intent='can-start-online-service', entidies = [])
# print()

# actions = action_execution()
# print("state = ", state)
# print("actions = ", actions)
# wait_user_utter(actions[-1], entidies=['(not(have-patient-symptoms))'])
# #print()

# actions = action_execution()
# print("state = ", state)
# print("actions = ", actions) 
# wait_user_utter(actions[-1], entidies=['can-end-conversation'])
# print()

# actions = action_execution()
# print("state = ", state)
# print("actions = ", actions)
# wait_user_utter(actions[-1], entidies=['can-finish-service'])
# print()

# actions = action_execution()
# print("state = ", state)
# print("actions = ", actions)

# print("action: ",p(state))
# wait_user_utter(p(state))
# print("state of world: ",state)
# print()

# print("action: ",p(state))
# wait_user_utter(p(state), entidies=['can-show-info-about-covid'])
# print("state of world: ",state)
# print()


# print("action: ",p(state))
# wait_user_utter(p(state), entidies=['can-show-info-new-coronavirus'])
# print("state of world: ",state)
# print()


# print("action: ",p(state))
# wait_user_utter(p(state), entidies=['can-end-conversation'])
# print("state of world: ",state)
# print()

# print("action: ",p(state))
# wait_user_utter(p(state), entidies=['can-finish-service'])
# print("state of world: ",state)
# print()

# print("action: ", p(state))
# wait_user_utter(p(state), entidies=['can-finish-service'])
# print("state of world: ",state)
# print()

#ac = do.get_action_by_name('ask-patient-symptoms')

#ou = ac.get_outcome_by_name('Error')

#print(ou.show_info())