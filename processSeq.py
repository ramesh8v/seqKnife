def reverseSeq(seq:str):
    '''
    reverses DNA sequences
    :param seq: input sequence as string
    :return: returns reverse sequence
    '''
    return seq[::-1]

def complementSeq(seq:str):
    '''
    returns complementary sequences
    :param seq: input sequence as string
    :return: returns complementary sequences
    '''
    _seq = seq.upper().replace('A', '1').replace('T', '2').replace('G', '3').replace('C', '4')
    return _seq.replace('1', 'T').replace('2', 'A').replace('3', 'C').replace('4', 'G')

def reverseComplementarySeq(seq:str):
    '''
    returns reverse complementary sequences
    :param seq: input sequence as string
    :return: returns reverse complementary sequences
    '''
    return reverseSeq(complementSeq(seq))