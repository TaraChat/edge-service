from business.providers.google import GoogleProvider
import PIL.Image
import pytest


def testGoogle():
    img = PIL.Image.open("tests/providers/google/image.png")
    response = GoogleProvider("gemini-1.5-flash").generate_content(
        ["What is in this photo?", img]
    )
    print(response.text)
    assert type(response.text) == str
