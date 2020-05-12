from core.advbase import *
from slot.a import *

def module():
    return Kleimann

class Kleimann(Adv):
    #a1 = ('fs',0.4)
    a3 = ('s',0.35)
 
    conf = {}
    conf['slots.a'] = Candy_Couriers()+The_Plaguebringer()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1
        `s2
        """
    coab = ['Ieyasu','Bow','Delphi']

    def s1_proc(self, e):
        self.afflics.poison('s1',120,0.582)

    def s2_proc(self, e):
        with KillerModifier('s2_killer', 'hit', 0.5, ['poison']):
            self.dmg_make("s2", 11.00)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
