from uuid import UUID

from vellum_ee.workflows.display.nodes import BaseNodeDisplay
from vellum_ee.workflows.display.nodes.types import PortDisplayOverrides

from ...nodes.validation_router import ValidationRouter


class ValidationRouterDisplay(BaseNodeDisplay[ValidationRouter]):
    node_id = UUID("8800890e-ee8b-43ba-8a49-16b6c1eacd87")
    attribute_ids_by_name = {"validation_passed": UUID("89154e61-2afc-46e9-9b62-2e1fa7b969bf")}
    port_displays = {
        ValidationRouter.Ports.valid: PortDisplayOverrides(id=UUID("9713fd14-a3cf-417e-b9c5-396c4d7a669c")),
        ValidationRouter.Ports.invalid: PortDisplayOverrides(id=UUID("b1fefb84-e7d8-4ab9-8488-ffe3a12d98a0")),
    }
