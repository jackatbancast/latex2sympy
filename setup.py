from setuptools import setup

try:
    with open('README.md') as f:
        long_description = f.read()
except:
    long_description = ''

setup(
    name='latex2sympy3',
    version='0.1.1',
    description='Sympy generator from LaTeX expressions.',
    long_description=long_description,
    maintainer='jack',
    maintainer_email='jack@bancast.net',
    url='https://github.com/jackatbancast/latex2sympy',
    packages=['latex2sympy'],
    license='MIT',
    install_requires=['antlr4-python3-runtime==4.5.3', 'sympy']
)
