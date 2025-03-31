from setuptools import setup, find_packages

setup(
    name="simple-image2ascii",
    version="0.0.2",
    author="Aleksey Timoshin",
    author_email="timoshin_aleksey02@mail.ru",
    description="A Python library for converting images and videos into ASCII art.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AlekseyScorpi/simple-image2ascii",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "opencv-python"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)