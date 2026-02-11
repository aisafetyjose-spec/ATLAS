from vellum.workflows.nodes.displayable import ErrorNode

from .input_validator import InputValidator


class ErrorOutput(ErrorNode):
    """Stops workflow when input validation fails.

    Provides clear error message with guidance on how to fix.
    """

    error = InputValidator.Outputs.error_message

    class Display(ErrorNode.Display):
        x = 3068
        z_index = 25
        icon = "vellum:icon:ban"
        color = "tomato"
