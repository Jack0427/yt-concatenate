from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        data = None  # 每一個步驟都是用上一個步驟加工後的東西
        for step in self.steps:
            try:
                data = step.process(data, inputs, utils)
            except StepException as e:
                print(f'Exception heppend: {e}')
                break
