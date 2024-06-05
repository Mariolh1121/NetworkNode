from setuptools import setup, find_packages

setup(
    name='my_network_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'numpy',
    ],
    author='Mario Alberto Limón Hernández, Ángel Román Zamora López',
    description='Un paquete para analizar y visualizar redes',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',

    ],
    python_requires='>=3.6',
)