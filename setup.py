from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mmget",
    version="0.0.1",
    author="Ben Lau",
    author_email="xbenlau@gmail.com",
    description="Multi Model Get - A library to download files from various sources including Hugging Face and Civitai",  # noqa
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/benlau/mmget",
    packages=find_packages(exclude=("demo",)),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.1",
    ],
)