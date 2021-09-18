try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()


setup(
    name="junkfile",
    version="1.0.0-dev",
    description="Directory organizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ivan José Frezza Júnior",
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="python organize project",
    include_package_data=True,
    packages=find_packages(exclude=".venv"),
    install_requires=required,
    python_requires="~=3.8",
)
