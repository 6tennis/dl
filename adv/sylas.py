from core.advbase import *
from slot.a import *

def module():
    return Sylas

class Sylas(Adv):
    a3 = ('a',0.13,'hp70')

    comment = 'not consider skill haste for team'
    conf = {}
    conf['slots.a'] = Resounding_Rendition()+The_Fires_of_Hate()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s1
        `s2
        `fs, seq=5
        """
    coab = ['Eleonora','Dragonyule_Xainfried','Lin_You']
    conf['afflict_res.poison'] = 0

    def d_coabs(self):
        if self.duration <= 60:
            self.coab = ['Blade','Dragonyule_Xainfried','Lin_You']

    def s1_proc(self, e):
        self.afflics.poison('s1',120,0.582)
        with KillerModifier('s1_killer', 'hit', 0.5, ['poison']):
            self.dmg_make('s1', 11.04)

    def s2_proc(self, e):
        Selfbuff('s2_shaste',0.30,15,'sp','buff').on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
