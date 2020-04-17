import adv.adv_test
from core.advbase import *
from slot.a import *

def module():
    return Alfonse

class Alfonse(Adv):
    a1 = ('lo',0.50*10.0/15.0)
    a3 = ('sp',0.08)

    conf = {}
    conf['slots.a'] = TSO()+BN()
    conf['acl'] = """
        `s1
        `s2,fsc
        `s3,fsc
        `fs, seq=3
        """
    def d_slots(self):
        if self.slots.c.has_ex('bow'):
            self.conf.slot.a = TSO()+JotS()

    def s1_before(self, e):
        Selfbuff('s1buff',0.15,10).on()


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

