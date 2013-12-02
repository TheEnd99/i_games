"""
############################################################
Caverna - Principal
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2013/11/04
:Status: This is a "work in progress"
:Revision: 0.1.3
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.

Caverna é um jogo de aventuras em uma caverna.
"""
CAVEX = "https://dl.dropboxusercontent.com/u/1751704/labase/caverna/img/cavernax.jpg"
CAVEZ = "http://1.bp.blogspot.com/_P5lPT2FbdDU/TJnykGs1NsI/AAAAAAAAAQ0/U-qpDfPEb0s/s1600/cenario+02+copy.JPG"

class Caverna:
    """Uma caverna com cameras tuneis e habitantes. :ref:`caverna`
    """
    def __init__(self, gui):
        """Initializes builder and gui. """
        self.doc = gui.DOC
        self.html = gui.HTML
        self.camera = {}
        self.tunel = {}
        self.heroi = None
        self.main = self.doc['main']

    def cria_caverna(self):
        """Cria a caverna e suas partes."""
        self.camara = Camara(self.html,"Camara0",self).cria_caverna()
        # criando um tunel
        tunel1 = Tunel(self.html,"Tunel0", self).cria_caverna()
        tunel2 = Tunel(self.html,"Tunel1", self).cria_caverna()
        tunel3 = Tunel(self.html,"Tunel2", self).cria_caverna()
        #self.main <= self.camara.div
        return self


class Camara:
    """Uma camara de caverna com tuneis e habitantes, :ref:`camara`
    """
    def __init__(self, html, nome, lugar):
        """Inicia a camara. """
        self.html = self.nome, self.html, nome, lugar
        self.passagem = self.div = None
        self.tunel = {}
        self.lugar.main <= self.div

    def cria_camara(self):
        """Cria a caverna e suas partes."""
        self.div = self.html.DIV()
        self.passagem = self.html.DIV()
        self.div <= self.html.DIV
        self.div.style.backgroundSize = 'cover'
        self.div.style.backgroundImage = 'url(%s)' % CAVEX
        self.div.style.width = 1000
        self.div.style.height = 800
        self.div.text = "LoL"
        self.div <= self.passagem
        self.lugar.main <= self.div
        return self


 class Tunel:
    """Uma tunel de caverna com tuneis e habitantes, :ref:`camara`"""
     def __init__(self, html, nome, lugar):
        """Inicia a camara. """
        self.html = self.nome, self.html, nome, lugar
        self.passagem = self.div = None
        self.Camara = {}

     def cria_tunel(self):
        """Cria a caverna e suas partes."""
        self.div = self.html.DIV()
        self.div.style.backgroundSize = 'cover'
        self.div.style.backgroundImage = 'url(%s)' % CAVEZ
        self.div.style.width = 1000
        self.div.style.height = 800
        self.div.text = "caverna do dragão"
        return self


def main(gui):
    print('Caverna 0.1.0')
    caverna = Caverna(gui).cria_caverna()
ZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZ