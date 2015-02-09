

class ValorRaknare(object):
    ''' Beraknar antalet av en viss valor,
        givet ett belopp.
    '''
    def __init__(self, valor):
        self.valor = valor

    def AntalOchAterstaende(self, belopp):
        ''' Raknar antalet av en valor samt '''
        aterstaende = belopp%self.valor
        antal = belopp/self.valor
        return antal, aterstaende


class VaxelRaknare(object):
    ''' Beraknar antalet av varje valor, givet
        ett belopp. 
    '''

    def __init__(self, valorer):
        self.valorer = valorer

    def ValorAntal(self, aterstaende):
        ''' Raknar antalet av vardera valor och sparar
            resultat som dictionary.
        '''
        valorAntal = dict()
        for valor in self.valorer:
            antal, aterstaende = ValorRaknare(valor).AntalOchAterstaende(aterstaende)
            if not antal:
                continue
            valorAntal[valor] = antal
        return valorAntal, aterstaende

    def VisaAntal(self, belopp):
        valorAntal, aterstaende = self.ValorAntal(belopp)
        print 'Beloppet %.1f har foljande valorer:' % belopp
        for valor in self.valorer:
            antal = valorAntal.get(valor)
            if not antal:
                continue
            print '{0:10}{1:10}'.format(str(valor), str(antal) + " st")
        print '(Aterstaende belopp: %.1f)' % aterstaende


vaxelRaknareSEK = VaxelRaknare([1000, 500, 100, 50, 20, 10, 5, 1])

vaxelRaknareSEK.VisaAntal(1997)
vaxelRaknareSEK.VisaAntal(43)