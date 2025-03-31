from setuptools import setup, find_packages

setup(
    name="NN",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "jax==0.5.0",
    ],
)
