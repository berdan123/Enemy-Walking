class enemy():
  def __init__(self,name,health,damage,speed):
    self.name=name
    self.health=health
    self.damage=damage
    self.speed=speed
  #methods
  def walk(self):
    print(self.name,"is walking")