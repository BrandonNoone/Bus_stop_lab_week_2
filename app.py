from person import Person
from bus import Bus

bus_1 = Bus("22", "Ocean Terminal", 0, "Brum Brum")

tammy = Person("Tammy", 25)
summer = Person("Summer", 2)

print (bus_1.num_of_passengers())

first = bus_1.pick_up("Tammy")

