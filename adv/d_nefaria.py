import adv.adv_test
from core.advbase import *
from slot.d import *

def module():
    return Dragonyule_Nefaria

class Dragonyule_Nefaria(Adv):
    a1 = ('s',0.25)
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s3, fsc
        `fs, seq=4
        """
    conf['slots.d'] = DJ()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

