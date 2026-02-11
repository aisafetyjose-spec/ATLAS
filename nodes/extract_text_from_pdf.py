from vellum import ChatMessagePromptBlock, JinjaPromptBlock, PromptParameters, VariablePromptBlock
from vellum.workflows.nodes.displayable import InlinePromptNode

from ..inputs import Inputs


class ExtractTextFromPDF(InlinePromptNode):
    """Extrae texto de un documento PDF usando un LLM con visión.

    Si se proporciona clinical_dictation directamente, lo usa sin procesar.
    Si se proporciona clinical_document (PDF), extrae el texto del documento.
    """

    ml_model = "claude-sonnet-4-5-20250929"
    blocks = [
        ChatMessagePromptBlock(
            chat_role="SYSTEM",
            blocks=[
                JinjaPromptBlock(
                    template="""\
You are a medical document text extractor. Your task is to extract ALL text content from the provided clinical document exactly as written.

RULES:
1. Extract ALL text from the document, preserving the original structure
2. Maintain headers, sections, and formatting as much as possible
3. Do NOT summarize, interpret, or modify the content
4. Do NOT add any commentary or explanations
5. If the document contains tables, preserve the data in a readable format
6. Extract text in the original language of the document

Output ONLY the extracted text, nothing else.\
"""
                )
            ],
        ),
        ChatMessagePromptBlock(
            chat_role="USER",
            blocks=[
                JinjaPromptBlock(template="""Extract all text from this clinical document:"""),
                VariablePromptBlock(input_variable="document"),
            ],
        ),
    ]
    prompt_inputs = {
        "document": Inputs.clinical_document,
    }
    parameters = PromptParameters(
        stop=[],
        temperature=None,
        max_tokens=64000,
        top_p=None,
        top_k=None,
        frequency_penalty=None,
        presence_penalty=None,
        logit_bias=None,
        custom_parameters=None,
    )

    class Display(InlinePromptNode.Display):
        x = 994
        y = 375.5
        z_index = 22
        icon = "vellum:icon:file-lines"
        color = "cyan"
