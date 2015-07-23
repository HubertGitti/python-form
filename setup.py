from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='python-form',
    version='0.1.0',
    description='A package for communicating with FORM',
    long_description=readme(),
    author='Takahiro Ueda',
    author_email='tueda@nikhef.nl',
    url='https://github.com/tueda/python-form',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='form, computer algebra',
    packages=find_packages(),
    package_data={
        'form': ['init.frm'],
    },
    test_suite='nose.collector',
    tests_require=['nose'],
)
