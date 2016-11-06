
def bwt_encode(data):
    arr = list(data)
    arr.append('|')
    matrix = []
    for i in range(len(arr)):
        matrix.append(arr)
        arr = arr[1:] + arr[:1]
    matrix.sort()
    return ''.join(row[-1] for row in matrix)


def test_encode():
    cases = (
        ('aba', 'baa'),
        ('banana', 'nnbaaa'),
        ('SIX.MIXED.PIXIES.SIFT.SIXTY.PIXIE.DUST.BOXES',
         'TEXYDST.E.IXXIIXXSSMPPS.B..E.S.UESFXDIIOIIIT'),
        ('horses are not good people', 'idgaf'),

    )
    for case, expected in cases:
        result = bwt_encode(case).replace('|', '')
        if result != expected:
            print('Nope:\n{}\n{}\n{}'.format(case, expected, result))

test_encode()
