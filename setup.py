from setuptools import setup, find_packages

setup(
    name='docker-repo',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'docker_repo=docker_repo.cli:cli',
        ],
    }
)
