from setuptools import find_packages, setup

setup(
    name='mrglib',
    packages=find_packages(include=['mrglib']),
    version='0.1.0',
    license='MIT',
    url='https://github.com/STEELISI/mrglib',
    download_url='',
    description='Library wrapping many mrg functionalities',
    author='Jelena Mirkovic, USC/ISI, mirkovic@isi.edu',
    install_requires=[],
    keywords=['mrg', 'SPHERE', 'mrglib', 'merge'],
    setup_requires=['pytest-runner', 'validators', 'json', 'socket', 'paramiko', 'urlretrieve'],
    tests_require=['pytest'],
    test_suite='tests',
    classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.10'
  ],
)

