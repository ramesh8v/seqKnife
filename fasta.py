class loadFasta():
    '''
    Load fasta sequences into the memory and do processing
    '''

    def __init__(self, fastaFile:str):
        '''
        Function to load fasta sequences into memory as dict
        :param fastaFile: name of fasta file with path
        '''
        self.seqDict = {}
        seqName = ""
        with open(fastaFile, 'r') as f:
            for lines in f:
                lines = lines.strip()
                if lines.startswith(">"):
                    seqName = lines.strip(">")
                    self.seqDict[seqName] = ""
                else:
                    self.seqDict[seqName] = self.seqDict[seqName]+lines

    def describe(self):
        '''
        Describes length of the sequences
        :yield: returns size of each scaffold as tuples
        '''
        yield "Given file contains {length} sequences".format(length=len(self.seqDict))
        for keys, vals in self.seqDict.items():
            yield (keys, len(vals))

    def cutSeq(self, posList:list):
        '''
        Function to cut sequences based on user supplied position
        :param posList: position list like {{'name':'seq1', 'start':2, 'end':6}, {'name':'seq1', 'start':6, 'end':12}}
        :yield: returns tuple of sequences
        '''
        for vals in posList:
            yield ("|".join([vals['name'],str(vals['start']), str(vals['end'])]),
                self.seqDict[vals['name']][(vals['start'])-1:(vals['end'])])