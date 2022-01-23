# creating a class
class Animals:
   def __init__(self, nv, pv):
      # normal variable
      self._nv = nv
      # private variable(not really)
      self.__pv = pv
      self.__third = 'third private va'
      
# creating an instance of the class Animals
myPet = Animals('Normal variable', 'Private variable')
# accessing *nv*
print(myPet._nv)
# accessing *__pv** using _Animals__pv name; mangling of the class name and private var
print(myPet._Animals__pv)


# without the mangling/insertion of the class name
print(myPet._Animals__third)
#print(myPet.__third) ##this is not working