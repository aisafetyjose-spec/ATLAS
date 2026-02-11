from uuid import UUID

from vellum_ee.workflows.display.nodes import BaseNodeDisplay
from vellum_ee.workflows.display.nodes.types import PortDisplayOverrides

from ...nodes.compliance_router import ComplianceRouter


class ComplianceRouterDisplay(BaseNodeDisplay[ComplianceRouter]):
    node_id = UUID("fb75e6f5-ab34-48b6-a25c-434518a5bca2")
    attribute_ids_by_name = {"compliance_ok": UUID("d4646fb2-6abf-4dde-a6de-5ad337ce0588")}
    port_displays = {
        ComplianceRouter.Ports.passed: PortDisplayOverrides(id=UUID("0c1f0be3-f881-49ee-a2a5-fa684121ddb4")),
        ComplianceRouter.Ports.failed: PortDisplayOverrides(id=UUID("1b544e15-48d7-4826-869b-da92f7b359d9")),
    }
