from setuptools import setup, find_packages

setup(
    name="app",
    version="0.1",
    packages=find_packages(),
    package_data={"app": ["data.json"]},
    include_package_data=True,
)