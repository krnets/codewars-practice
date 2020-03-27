# 6kyu - Basic subclasses - Adam and Eve

""" According to the creation myths of the Abrahamic religions, 
Adam and Eve were the first Humans to wander the Earth.

You have to do God's job. 
The creation method must return an array of length 2 containing objects (representing Adam and Eve). 
The first object in the array should be an instance of the class Man. 
The second should be an instance of the class Woman. 
Both objects have to be subclasses of Human. 
Your job is to implement the Human, Man and Woman classes. """

# def God():
#     Adam = Man()
#     Eve = Woman()
#     return [Adam, Eve]

# class Human:
#     pass

# class Man(Human):
#     pass

# class Woman(Human):
#     pass


def God():
    Adam = Man('Adam', 'male')
    Eve = Woman('Eve', 'female')
    return [Adam, Eve]

class Human:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

class Man(Human):
    def __init__(self, name, sex):
        super().__init__(name, sex)

class Woman(Human):
    def __init__(self, name, sex):
        super().__init__(name, sex)


paradise = God()
q = isinstance(paradise[0], Man)  # True, "First object are a man")
q
q = God()[0].name
q
q = God()[0].sex
q
q = God()[1].name
q
q = God()[1].sex
q
