from vellum.workflows import BaseNode, Port
from vellum.workflows.ports import Port

from .qa_check import QACheck


class ComplianceRouter(BaseNode):
    compliance_ok: bool = QACheck.Outputs.compliance_ok

    class Outputs(BaseNode.Outputs):
        pass

    class Ports(BaseNode.Ports):
        passed = Port.on_if(QACheck.Outputs.compliance_ok.equals(True))
        failed = Port.on_else()

    class Display(BaseNode.Display):
        x = 4052
        y = 440
        z_index = 30
        icon = "vellum:icon:arrows-split-up-and-left"
        color = "stone"

    def run(self) -> Outputs:
        return self.Outputs()
