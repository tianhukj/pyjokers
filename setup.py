from setuptools import setup, find_packages

setup(
    name='pyjokers',
    version='0.1.1',
    packages=find_packages(),
    description='A simple joke generator',
    long_description=open('README.md').read(),
    author='tianhukj',
    author_email='tianhukj@outlook.com',
    url='https://github.com/tianhukj/pyjokers',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # 当前没有依赖项
    ],
)
