from abc import ABC,abstractmethod

class Car(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Swift(Car):

    def start(self):
        print("swift starts")

    def accelerate(self):
        print("swift accelerates")

    def stop(self):
        print("swift stops") 


obj=Swift()

obj.start()
obj.accelerate()
obj.stop()