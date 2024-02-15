from Animals import Bird, Dog, Fish

class FabricAnimal:
    __Animals = {'dog': Dog, 'bird': Bird, 'fish': Fish}

    @staticmethod
    def create_animal(class_animal, *args, **kwargs):
        return FabricAnimal.__Animals[class_animal.lower()](*args, **kwargs)
    
if __name__ == '__main__':
    dog = FabricAnimal.create_animal('dog', 'Лада', 5, 23, 'немецкая овчарка',['сидеть', 'голос'])
    print(dog)