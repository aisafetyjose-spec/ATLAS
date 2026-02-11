from typing import Any

from vellum.workflows import BaseNode

from .qa_check import QACheck


class FlagIssues(BaseNode):
    flagged_summary: str = QACheck.Outputs.flagged_summary
    issues: list[Any] = QACheck.Outputs.issues
    recommended_fixes: list[Any] = QACheck.Outputs.recommended_fixes

    class Outputs(BaseNode.Outputs):
        flag_banner: str

    class Display(BaseNode.Display):
        x = 4610
        y = 490.5
        z_index = 32
        icon = "vellum:icon:exclamation-triangle"
        color = "tomato"

    def run(self) -> Outputs:
        banner = f"\n╔══════════════════════════════════════════════════════════════════╗\n║  ⚠️  QA COMPLIANCE FAILED - REQUIRES CLINICIAN ATTENTION  ⚠️     ║\n╠══════════════════════════════════════════════════════════════════╣\n║  This draft was generated but has compliance issues that must    ║\n║  be addressed before signing. Review the flagged items below.    ║\n╚══════════════════════════════════════════════════════════════════╝\n\n{self.flagged_summary}\n\n══════════════════════════════════════════════════════════════════\n"
        return self.Outputs(flag_banner=banner)
