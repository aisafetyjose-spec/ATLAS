from vellum.workflows import BaseNode, Port
from vellum.workflows.ports import Port

from .input_validator import InputValidator


class ValidationRouter(BaseNode):
    validation_passed: bool = InputValidator.Outputs.validation_passed

    class Outputs(BaseNode.Outputs):
        pass

    class Ports(BaseNode.Ports):
        valid = Port.on_if(InputValidator.Outputs.validation_passed.equals(True))
        invalid = Port.on_else()

    class Display(BaseNode.Display):
        x = 2494
        y = 333
        z_index = 24
        icon = "vellum:icon:arrows-split-up-and-left"
        color = "stone"

    def run(self) -> Outputs:
        return self.Outputs()
