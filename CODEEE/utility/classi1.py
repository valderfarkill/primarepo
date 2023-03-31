class Persona:
  def __init__(self,a,b): #ATTRIBUTI
    self.nome = a
    self.eta = b

  def double(self,x): #METHOD
    '''moltiplica l'input x2 volte'''
    return x*2

  def triple(self,x): #METHOD
    '''moltiplica l'input x3 volte'''
    return x*3
  
  def quadratoanni(self): #METHOD
    '''RESTITUISCE IL QUADRATO DEGLI ANNI'''
    return self.eta**2
  
emanuele = Persona('Emanuele', 33)


class Cubo:
  def __init__(self, a:float):
    self.lato = a

  def superficie(self):
    '''restituisce la superficie del cubo'''
    superficie = self.lato**2*6
    return superficie

  def volume(self):
    '''restituisce il volume del cubo'''
    volume = self.lato**3
    return volume

