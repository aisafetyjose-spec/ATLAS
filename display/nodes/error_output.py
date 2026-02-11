from uuid import UUID

from vellum_ee.workflows.display.editor import NodeDisplayComment, NodeDisplayData
from vellum_ee.workflows.display.nodes import BaseErrorNodeDisplay

from ...nodes.error_output import ErrorOutput


class ErrorOutputDisplay(BaseErrorNodeDisplay[ErrorOutput]):
    node_id = UUID("a2859443-8690-46f0-8508-78697cbdd611")
    target_handle_id = UUID("b0462864-8057-4454-bc93-41419d9da535")
    node_input_ids_by_name = {"error_source_input_id": UUID("2722dd08-2ad8-474e-9d52-1a06cdcf3ca8")}
    display_data = NodeDisplayData(
        comment=NodeDisplayComment(
            expanded=True,
            value="Stops workflow when input validation fails.\n\nProvides clear error message with guidance on how to fix.\n",
        )
    )
