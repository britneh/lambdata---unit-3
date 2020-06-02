from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="britneh_lambadata",  # the name that you will install via pip
    version="1.0",
    author="Britne Hackett",
    author_email="brhacket@email.com",
    description="A couple of helpful functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    # license="MIT",
    url="https://github.com/britneh/lambdata---unit-3",
    # keywords="",
    packages=find_packages()  # ["my_lambdata"]
)
