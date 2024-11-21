from dog import dog
with open("dogs.txt") as file:
    dogs = []
    for line in file:
        name,trick,breed,hungry = line.split()
        new = dog(name,trick,breed, hungry)
        dogs.append(new)
        print(new)

    print(dogs[0].get_name())
    print(dogs[0].get_breed())
    print(dogs[0].get_trick())
    print(dogs[0].isHungry())
    dogs[0].speak()
    dogs[0].feed()
    dogs[0].change_trick("fetch")
    print(dogs[0].get_name())
    print(dogs[0].get_breed())
    print(dogs[0].get_trick())
    print(dogs[0].isHungry())
