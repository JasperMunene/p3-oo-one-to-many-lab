class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type: {pet_type}. Valid types are: {', '.join(Pet.PET_TYPES)}")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner if owner is not None else "unknown"

        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name


    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        pet.owner = self

    def get_sorted_pets(self):

        return sorted(self.pets(), key=lambda pet: pet.name)