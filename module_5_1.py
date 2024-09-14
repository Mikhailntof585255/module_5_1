class House:
    def __init__(self,name,number_of_floors):
        self.name=name
        self.number_of_floors=number_of_floors
    def go_to(self,new_floor):
        if new_floor>self.number_of_floors:
            print("Такого зтажа не существует")
            return
        else:
            cuont_floore=0
            while cuont_floore<new_floor:
                cuont_floore+=1
                print(cuont_floore)
            return

h1=House("ЖК Горский",18)
h2=House("Домик в деревне",2)

print(h1.go_to(5),h1.name)
print(h2.go_to(10),h2.name)