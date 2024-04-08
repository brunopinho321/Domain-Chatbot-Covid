import actions.manager.read_domain as read_domain
class SuperClass:
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

class Predicate(SuperClass):
    def __init__(self, name = "", value = False):
        super().__init__(name)
        self._value = value

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def show_info(self):
        print("predicate: ",self._name, ", value: ", self._value)


class Outcome(SuperClass):
    def __init__(self,name='0', predicates  = []):
        super().__init__(name)

        self._predicates = predicates
    
    def get_predicates(self):
        return self._predicates
    
    def set_predicates(self, predicates):
        self._predicates = predicates
    
    def add_predicate(self, predicate):
        self._predicates.append(predicate)
    
    def show_info(self):
        print('outcome: ',self._name)
        for p in self._predicates:
            p.show_info()


class Action(SuperClass):
    def __init__(self, name = '', outcomes = []):
        super().__init__(name)
        self._outcomes = outcomes

    def add_outcome(self, outcome):
        self._outcomes.append(outcome)
    
    def get_outcomes(self):
        return self._outcomes
    
    def get_outcome_by_name(self, name):
        for out in self._outcomes:
            if out.get_name() == name:
                return out
    def set_outcomes(self, outcomes):
        self.outcomes = outcomes
   
    def show_info(self):
        print("action: ", self._name)
        for out in self._outcomes:
            out.show_info()
            print()

class Domain:
    def __init__(self):
        self._actions = read_domain.get_actions_domain()

    def set_actions(self, actions):
        self._actions = actions
    
    def get_actions(self):
        return self._actions
    
    def get_action_by_name(self, name):
        for action in self._actions:
            if action.get_name() == name:
                return action
        return None
    
    def compare(self, entide, predicate):
        if (entide.get_name() == predicate.get_name()):
            if(entide.get_value() == predicate.get_value()):
                return True
            else: 
                return False
    def contain(self, entide, outcome):
        flag = False
        for pred in outcome.get_predicates():
            flag = self.compare(entide, pred)
            if(flag == True):
                break
        return flag

    def find_in_list(self, entidies, action):
        flag = False
        outcome = None
        for out in action.get_outcomes():
            outcome = out 
            for e in entidies:
                if(self.contain(e, out)):
                    flag = True
                else:
                    flag = False
                    outcome = None
            if(flag == True):
                break
        return flag, outcome

    

