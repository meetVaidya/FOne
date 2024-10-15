from setuptools import setup, find_packages

setup(
    name="fone",
    version="0.1",
    package_dir={"": "fone"},
    packages=find_packages(where="src"),
    install_requires=["requests"],
    author="ninet33n",
    author_email="slipstreamvroom@gmail.com",
    long_description=open("README.md").read(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)