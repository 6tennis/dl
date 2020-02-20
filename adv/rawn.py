import adv.adv_test
from core.advbase import *

def module():
    return Rawn

class Rawn(Adv):
    conf = {}
    conf['acl'] = """
        `s1, cancel
        `s2, cancel
        `s3, cancel
        `fs, x=4
    """

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
