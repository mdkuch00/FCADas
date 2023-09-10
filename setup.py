from setuptools import setup, find_packages

setup(
    name='FCADas',
    version='0.1',
    description='TODO',
    long_description='TODO',
    author='Michał Kucharek, Bartłomiej Więcek',
    author_email='md.kucharek@gmail.com',
    url='https://github.com/mdkuch00/FCADas.git',
    packages=find_packages(),
    install_require=[
        'et-xmlfile==1.1.0',
        'ezdxf==1.0.3',
        'openpyxl==3.1.2',
        'pyparsing==3.1.1',
        'typing_extensions==4.7.1',
    ],
    classifiers=[
        'Development status :: 3 - Alpha',
        'Intendent Audience :: Developers',
        'License :: OSI Aproved :: MIT License',
        'Programing Language :: Python >3.10',
    ],
)