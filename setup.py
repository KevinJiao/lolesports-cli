from setuptools import setup, find_packages


setuptools.setup(
    name='riftviewer',
    version='0.0.0',
    author='Kevin Jiao, Roycce Chen',
    author_email='kevin.jiao.usa@gmail.com',
    description='A terminal viewer for LOL esports games',
    url='https://github.com/kevinjiao/riftviewer',
    packages=['riftviewer'],
    entry_points={
        'console_scripts': ['riftviewer = riftviewer.app:main']
    },
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
