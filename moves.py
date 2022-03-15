# lookup table for all possible move combos
_MOVES = [
        'none',                        # 0
        'jump',                        # 1
        'left',                        # 2
        'jump+left',
        'right',                       # 4
        'jump+right',
        'left+right',
        'jump+left+right',
        'up',                          # 8
        'jump+up',
        'left+up',
        'jump+left+up',
        'right+up',
        'jump+right+up',
        'left+right+up',
        'jump+left+right+up',
        'down',                        # 16
        'jump+down',
        'left+down',
        'jump+left+down',
        'right+down',
        'jump+right+down',
        'left+right+down',
        'jump+left+right+down',
        'up+down',
        'jump+up+down',
        'left+up+down',
        'jump+left+up+down',
        'right+up+down',
        'jump+right+up+down',
        'left+right+up+down',
        'jump+left+right+up+down']

_MOVES_SHORT = [
        'N',    # 0
        'J',    # 1
        'L',    # 2
        'JL',
        'R',    # 4
        'JR',
        'LR',
        'JLR',
        'U',    # 8
        'JU',
        'LU',
        'JLU',
        'RU',
        'JRU',
        'LRU',
        'JLRU',
        'D',    # 16
        'JD',
        'LD',
        'JLD',
        'RD',
        'JRD',
        'LRD',
        'JLRD',
        'UD',
        'JUD',
        'LUD',
        'JLUD',
        'RUD',
        'JRUD',
        'LRUD',
        'JLRUD']
