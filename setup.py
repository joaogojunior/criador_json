from setuptools import setup

setup(
    name='criadorjson',
    version='0.1',
    packages=['criador_json'],
    author='João Guilherme de Oliveira Júnior',
    author_email='joaogojunior@gmail.com',
    description='Facilita a criação e carga de configurações.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/joaogojunior/criador_json',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
