from abc import abstractclassmethod, ABC


class Step(ABC):
    def __init__(self):
        pass

    @abstractclassmethod
    def process(self, data, inputs, utils):
        pass


class StepException(Exception):
    pass
