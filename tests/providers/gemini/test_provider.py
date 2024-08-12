from src.business.providers.gemini import GeminiProvider
import PIL.Image
import pytest


def testGemini():
    img = PIL.Image.open("tests/providers/gemini/image.png")
    response = GeminiProvider("gemini-1.5-flash").generate_content(
        ["What is in this photo?", img]
    )
    print(response.text)
    assert type(response.text) == str
