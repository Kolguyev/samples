

class VaxelBeraknare(object):
    ''' Ansvarar for att berakna vaxel pa ett
        belopp. Tar sa stora valorer som mojligt.
    '''
    valorer = [1000, 500, 100, 50, 20, 10, 5, 1]

    @classmethod
    def Valorer(cls, belopp):
        aterstaende = belopp
        vaxelDict = dict()
        for valor in cls.valorer:
            if aterstaende >= valor:
                antal = aterstaende/valor
                vaxelDict[valor] = antal
                aterstaende -= antal*valor
        return vaxelDict

    @classmethod
    def SkrivUtValorer(cls, belopp):
        vaxelDict = cls.Valorer(belopp)
        print 'Vaxel pa %.0f SEK:' % belopp
        for valor in cls.valorer:
            antal = vaxelDict.get(valor)
            if not antal:
                continue
            print '%.0f: %d st' % (valor, antal)
        
# Exempel
belopp = 1849
VaxelBeraknare.SkrivUtValorer(belopp)
