from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Book-Buddy"
AUTHOR_USER_NAME = "Xaps23"
SRC_REPO = "books_recommender"
LIST_OF_REQUIREMENTS = []

setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Xaps23",  # Consider using AUTHOR_USER_NAME here
    description="A small local package for ML-Based Book Recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Xaps23/Book-Buddy",  # Dynamic URL
    author_email="sarwashree23@gmail.com",
    packages=find_packages(),
    license="MIT",
    install_requires=LIST_OF_REQUIREMENTS,
)