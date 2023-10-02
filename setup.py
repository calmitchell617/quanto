from setuptools import find_packages, setup

setup(
    name="quanto",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author_email="david@huggingface.co",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)