class DataDescriptor:
    def __get__(self, instance, owner):
        print("DataDescriptor __get__ called")
        return "VALUE FROM DATA DESCRIPTOR"

    def __set__(self, instance, value):
        print("DataDescriptor __set__ called (instance tried override)")

class NonDataDescriptor:
    def __get__(self, instance, owner):
        print("NonDataDescriptor __get__ called")
        return "VALUE FROM NON-DATA DESCRIPTOR"

class Parent:
    shared = "VALUE FROM PARENT CLASS"

class Example(Parent):
    data = DataDescriptor()
    nondata = NonDataDescriptor()
    shared = "VALUE FROM CHILD CLASS"   # should override parent
    class_attr = "VALUE FROM CLASS"

    def __init__(self):
        self.data = "INSTANCE TRIES TO OVERRIDE DATA DESCRIPTOR"
        self.nondata = "INSTANCE OVERRIDES NON-DATA DESCRIPTOR"
        self.class_attr = "INSTANCE OVERRIDES CLASS ATTRIBUTE"

    def method(self):
        return "METHOD RESULT"

    def __getattr__(self, name):
        return f"{name} FROM __getattr__"

obj = Example()

print("\n 1 Data descriptor vs instance")
print(obj.data)

print("\n 2 Instance vs non-data descriptor")
print(obj.nondata)

print("\n 3 Instance vs class attribute")
print(obj.class_attr)

print("\n 4 Child class vs parent class (MRO)")
print(obj.shared)

print("\n 5 Method binding (non-data descriptor behavior)")
print(obj.method())

print("\n 6 Missing attribute fallback")
print(obj.unknown)
