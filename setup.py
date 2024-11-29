from setuptools import setup, find_packages

setup(
    name="fastapi_wrapper",  # Name of your library
    version="1.0.0",    # Version
    packages=find_packages(),  # Automatically find packages
    install_requires=[],  # Dependencies if any
    description="A reusable CRUD Interface for FastAPI",
    author="Thomas Baumkircher",
    url="https://github.com/Thomas/my_library",  # Optional
    author_email="thomasbaumkircher@gmail.com",
)
