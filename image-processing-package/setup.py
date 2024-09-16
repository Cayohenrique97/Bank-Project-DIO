from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    page_description = f.read()

setup(
    name="image_processing",
    version="0.0.1",
    author="Professora DIO",
    author_email="teste@teste.com",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="meugithub",
    packages=find_packages(),
    install_requires=requirements.txt,
    python_requires=">= 3.5",
)
