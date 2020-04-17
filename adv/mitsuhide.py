import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Mitsuhide

class Mitsuhide(Adv):
    a1 = ('a',0.2,'hit15')
    a3 = ('k_paralysis',0.3)

    conf = {}
    conf['slots.d'] = Daikokuten()
    conf['slots.a'] = TB()+Spirit_of_the_Season()
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=4
    """
    conf['afflict_res.paralysis'] = 0

    def init(self):
        self.s1_stance = 1

    def s1_proc(self, e):
        self.afflics.paralysis('s1',120, 0.97)
        for _ in range(11):
            self.dmg_make('s1',0.61,'s')
            self.hits += 1

    def s2_proc(self, e):
        if(self.hits >= 5):
            self.dmg_make('s2',0.4725,'s')
        if(self.hits >= 10):
            self.dmg_make('s2',0.4725,'s')
        if(self.hits >= 15):
            self.dmg_make('s2',0.945,'s')
        if(self.hits >= 20):
            self.dmg_make('s2',0.945,'s')
        if(self.hits >= 25):
            self.dmg_make('s2',0.945,'s')
        if(self.hits >= 30):
            self.dmg_make('s2',0.945,'s')

        Spdbuff('s2',0.1,10).on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)




