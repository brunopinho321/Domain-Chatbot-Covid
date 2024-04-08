import os

def _shell():
    os.system("./actions/manager/planner-for-relevant-policies/src/prp actions/manager/planner-for-relevant-policies/src/Dom.pddl actions/manager/planner-for-relevant-policies/src/pfile1.pddl --dump-policy 2")

    os.system("python ./actions/manager/planner-for-relevant-policies/prp-scripts/translate_policy.py > actions/manager/planner-for-relevant-policies/src/human_policy.out")

def _generete_policy():
    import actions.manager.reader as reader
    reader


def build_policy():
    
    _shell()
    
    _generete_policy()