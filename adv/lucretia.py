from core.advbase import *

def module():
    return Lucretia

class Lucretia(Adv):
    a1 = ('energized_att', 0.20)
    a3 = ('bk',0.3)
    conf = {}
    conf['acl'] = """
        `dragon, s=2
        `s2, x=5
        `s1
        `s3
        """
    coab = ['Blade','Dagger','Halloween_Elisanne']

    def s1_proc(self, e):
        self.energy.add(1, team=True)

    def s2_proc(self, e):
        self.energy.add(2)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)



'''
2 1 | 2 3 1 | 2 1 | 1 3 2 | 2 1 | 3 2 1 | 2 1 | 2 3 1 | 2 1 | 2 3 1 |
2 3 | 5 0 1 | 3 4 | 5 0 2 | 4 5 | 0 2 3 | 5 0.| 2 2 3 | 5 0 | 2 2 3 |

2 1 | 2 1 3 | 2 1 | 2 1 3 |
2 3 | 5 0 0 | 2 3 | 5 0 0 |

2 1 | 2 3 1 | 2 1 | 2 3 1 |
2 3 | 5 0 1 | 3 4 | 6.0 1 |

2 1 | 2 3 1 | 2 1 | 1 3 2 | 2 1 | 3 2 1 | 1 2 | 3 2 1
2 3 | 5 0 1 | 3 4 | 5 0 2 | 4 5 | 0 2 3 | 4 6.| 0 2 3
'''