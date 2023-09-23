class Planet:
    shape='round'  #class attribute(not for one instances but for all)
    #in instance and class
    def __init__(self,name,radius,gravity,system):
        pass
        self.name=name #These are instance attributes
        self.radius=radius
        self.gravity=gravity
        self.system=system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod #class methods
    def commons(cls):
        return f'All planets are {cls.shape} cause of gravity'

    @staticmethod #has no access to class or instance method/attribute
    def spin(speed='2000 miles per hour'): #only acesses the par defined in it
        return f'The planet spins and spins at {speed}'


# hoth=Planet('Hoth',200000,5.5, 'HothSystem') #hoth is a variable
# print(f'Name: {hoth.name}') #attaching atributes to the variable
# print(f'Radius: {hoth.radius}')
# print(f'The gravity is: {hoth.gravity}')
# print(hoth.orbit())

# naboo=Planet('Naboo',300000,8,'Naboo system')
# print(f'Name: {naboo.name}')
# print(f'Radius: {naboo.radius}')
# print(f'The gravity is: {naboo.gravity}')
# print(naboo.orbit())
# print(naboo.commons()) #or print(Planet.commons())
