from zigzag1 import Solution as Solution1

def test_zigzag():
    solution = Solution1()
    s = solution.convert('PAYPALISHIRING', 3)
    assert s == 'PAHNAPLSIIGYIR'

    s = solution.convert('A', 1)
    assert s == 'A'

    s = solution.convert('01234567890', 4)
    assert s == '06157248039'

    s = solution.convert('01', 1)
    assert s == '01'

'''
from cProfile import Profile
from pstats import Stats

profiler = Profile()
profiler.runcall(lambda : solution.convert('PAYPALISHIRING', 3))

stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
stats.print_callers()
'''
