from uuid import UUID

from vellum_ee.workflows.display.nodes import BaseNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.flag_issues import FlagIssues


class FlagIssuesDisplay(BaseNodeDisplay[FlagIssues]):
    node_id = UUID("9ea0832f-ef8b-44cf-a80c-89d75bc49e7f")
    attribute_ids_by_name = {
        "flagged_summary": UUID("53770863-4cd8-43b3-82e4-239724ec1680"),
        "issues": UUID("25111144-2d98-4a56-bde4-06aa3f6f5154"),
        "recommended_fixes": UUID("d59fc0fc-f372-474a-8f0e-55f404f64474"),
    }
    output_display = {
        FlagIssues.Outputs.flag_banner: NodeOutputDisplay(
            id=UUID("936b5b66-9bd3-41f8-a3d6-bfbd0bac7b8a"), name="flag_banner"
        )
    }
    port_displays = {FlagIssues.Ports.default: PortDisplayOverrides(id=UUID("81418d7d-86b6-44cf-b4b6-34f6bcf50a82"))}
