import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json_help-kchiev215",
    version="0.0.1",
    author="Kristina Chiev",
    author_email="kchiev22",
    description="transfer json files to pandas",
    readme="README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/kchiev215/PythonFundamentals.Labs.PipModule",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
