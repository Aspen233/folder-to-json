from setuptools import setup, find_packages

setup(
    name='folder-to-json',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'folder2json=scripts.main:main',
        ],
    },
    install_requires=[],
    description='A tool to convert folder structures and file content into JSON format.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Aspen233',
    url='https://github.com/Aspen233/folder-to-json',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
