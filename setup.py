from setuptools import setup, find_packages

setup(
    name="my_rsa",
    version="0.1",
    packages=find_packages(),
    author="Your Name",
    author_email="your_email@example.com",
    description="A simple RSA encryption library without using built-in RSA libraries.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_rsa_lib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
