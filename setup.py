from setuptools import setup, find_packages

setup(
    name='FCADas',
    version='0.1',
    description='TODO',
    long_description='TODO',
    author='`Michał Kucharek, Bartłomiej Więcek',
    author_email='md.kucharek@gmail.com',
    url='https://github.com/mdkuch00/FCADas.git',
    packages=find_packages(),
    install_require=[
        'et-xmlfile==1.1.0',
        'ezdxf==1.0.3',
        'numpy==1.26.0',
        'pandas==2.1.0',
        'pyparsing==3.1.1',
        'python-dateutil==2.8.2',
        'pytz==2023.3.post1',
        'six==1.16.0',
        'typing_extensions==4.7.1',
        'tzdata==2023.3',
    ],
    classifiers=[
        'Development status :: 3 - Alpha',
        'Intendent Audience :: Developers',
        'License :: OSI Aproved :: MIT License',
        'Programing Language :: Python >3.10',
    ],
)