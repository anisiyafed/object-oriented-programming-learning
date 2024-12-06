# Example of how a class (blueprint) is created
class ClassExample:
    # this is used when we create the object
    def __init__(self, class_input):
        self.class_attribute = class_input
        print("Created object")
        print(self.class_attribute)

    def method(self):
        print("Can access attributes through 'self.'")
        print(self.class_attribute)


# multiple objects can be created based on the class (blueprint). Each with unique attributes. 
object1 = ClassExample(5)
object2 = ClassExample(123)
object1.method()
object2.method()
object1.class_attribute = 1
object1.method()
