from setuptools import setup, find_packages

# Copy the contents of the README file as the description

with open("README.md", "r") as file: 
    desc = file.read()

# Setup the package

setup(
    name="Worder", 
    version="0.1", 
    package=find_packages(),
    install_required=[
        "fast-whisper>=1.2.0"
        "av>=12.0.0"
    ],
    entry_points={
        "console_scripts": [
            "worder = Worder:main",
        ],
    },
    long_description=desc, 
    long_description_content_type="text/markdown", 
)
