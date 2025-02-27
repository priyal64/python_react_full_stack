from abc import ABC, abstractmethod

# Abstract class
class Father(ABC):
    @abstractmethod
    def profession(self):
        pass

    def introduce(self):
        print(f"I am a {self.profession()}.")

# Engineer class
class Engineer(Father):
    def profession(self):
        return "Engineer"

# Doctor class
class Doctor(Father):
    def profession(self):
        return "Doctor"

# Instantiate and demonstrate calling introduce
engineer = Engineer()
doctor = Doctor()

engineer.introduce()  # Output: I am an Engineer.
doctor.introduce()    # Output: I am a Doctor.
