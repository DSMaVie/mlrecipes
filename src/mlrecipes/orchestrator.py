from mlrecipes.models import Experiment


class Orchestrator:
    def __init__(self, experiment: Experiment) -> None:
        self.experiment = experiment

    def run(self):
        print(f"Running experiment: {self.experiment.name}")
        for step in self.experiment.steps:
            print(f"Running step: {step.name}")
            print(f"Params: {step.params}")
            print(f"Inputs: {step.inputs}")
            print(f"Artifacts: {step.artifacts}")
            print("")
