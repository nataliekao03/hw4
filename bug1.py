class Base:
  def __init__(self, x, y):
        self.x = x
        self.y = y

  def shape(self):
        return "This is a " + self

class Circle(Base):
    def __init__(x, size):
        super().__init__(x, y, size)

    def draw(self):
        return f"""
({self.x}, {self.y})\n{self.size}
         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '
               """
