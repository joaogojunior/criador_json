from setuptools import setup, find_packages

setup(
    name='json_config',
    version='0.1',
    packages=find_packages(),
    author='João Guilherme de Oliveira Júnior',
    author_email='joaogojunior@gmail.com',
    description='Facilita a criação e carga de configurações.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/joaogojunior/json_config',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
