from abc import *
class TV(metaclass=ABCMeta):

    @abstractmethod
    def power_on(self):
        pass

class LGTV(TV):
    def power_on(self):
        print('power ON...')


tv = LGTV()
tv.power_on()