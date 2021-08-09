from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="google_drive_manager",
    version="0.0.1",
    author="Jungwoo Han",
    author_email="ajtwlswjddnv1102@gmail.com",
    description="google drive manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HanJungwoo1102/google_drive_manager",
    packages=find_packages(),
    python_requires='>=2.6',
    install_requires=requirements,
)
