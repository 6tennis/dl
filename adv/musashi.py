from core.advbase import *
from slot.a import *

def module():
    return Musashi

class Musashi(Adv):
    a1 = ('lo',0.40)
    a3 = ('od',0.08)
    conf = {}
    conf['slot.a'] = Resounding_Rendition()+The_Fires_of_Hate()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s2, seq=5
        `s1
        `s3, s
        """
    coab = ['Eleonora','Dragonyule_Xainfried','Lin_You']
    conf['afflict_res.poison'] = 0

    def s1_proc(self, e):
        self.afflics.poison('s1',110,0.53)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)