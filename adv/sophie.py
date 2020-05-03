from core.advbase import *
from slot.a.all import *
from slot.d.wind import *

def module():
    return Sophie

class Sophie(Adv):
    comment = 'no s1'

    conf = {}
    conf['slots.d'] = Garland()
    conf['slots.a'] = Primal_Crisis()+The_Fires_of_Hate()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s2, x=5
    """
    conf['afflict_res.poison'] = 0
    coab = ['Blade', 'Tiki', 'Lin_You']

    def s2_proc(self, e):
        self.afflics.poison('s2', 120, 0.582)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)