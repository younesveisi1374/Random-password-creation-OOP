# import library's
from abc import ABC, abstractmethod
import string
import random
# abstract class


class ABS_class(ABC):
    length = 20

    def __init__(self, characterList):
        self.characterList = characterList
    # abstractmethod

    @property
    @abstractmethod
    def generate_password(self):
        pass


# a simple value for inheritance
characterList = ""
# a class to create pssword with letters


class Password_letters(ABS_class):
    def __init__(self, characterList):
        super().__init__(characterList)
        super().length

    @property
    def generate_password(self):
        self.characterList += string.ascii_letters
        password = []
        for i in range(self.length):
            randomchar = random.choice(self.characterList)
            password.append(randomchar)
        return "".join(password)


generate = Password_letters(characterList)
print(generate.generate_password)

# a class to create pssword with numbers


class Password_numbers(ABS_class):
    def __init__(self, characterList):
        super().__init__(characterList)
        super().length

    @property
    def generate_password(self):
        self.characterList += string.digits
        password = []
        for i in range(self.length):
            randomchar = random.choice(self.characterList)
            password.append(randomchar)
        return "".join(password)


generate = Password_numbers(characterList)
print(generate.generate_password)

# a class to create pssword with numbers and letters


class Password_numbers_letters(ABS_class):
    def __init__(self, characterList):
        super().__init__(characterList)
        super().length

    @property
    def generate_password(self):
        self.characterList += string.ascii_letters + string.digits
        password = []
        for i in range(self.length):
            randomchar = random.choice(self.characterList)
            password.append(randomchar)
        return "".join(password)


generate = Password_numbers_letters(characterList)
print(generate.generate_password)
