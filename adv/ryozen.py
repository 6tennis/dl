import adv.adv_test
from core.advbase import *

def module():
    return Ryozen

class Ryozen(Adv):
    a3 = ('od',0.08)
    conf = {}
    conf['acl'] = """
        `s2
        `s3
        `fs, seq=5
        """
    
    def s1_proc(this, e):
        Teambuff('s1', 0.25, 15, 'defense').on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

