class Car(object):

    def __init__(self, make, model, topspeed):
        self.make = make
        self.model = model
        self.speed = topspeed

    def get_make_and_model(self):
        return self.make, self.model

    def drive(self):
        print("zero to", self.speed)

f = Car("Ford", "Focus", 120)
a = Car("Nissan", "Altima", 115)

print(f.get_make_and_model())
# --> ("Ford", "Focus")
print(a.get_make_and_model())
# --> ("Nissan", "Altima")

# we can get the variables out of an object using objectname-dot-variablename
avg_speed = (f.speed + a.speed) / 2

print("average speed is", avg_speed)
# --> average speed is 117.5

f.drive()
# --> zero to 120