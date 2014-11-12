from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='se3',
    version='0.1',
    description='Some useful function for homogenous transforms in special euclidian 3-space.',
    long_description=readme(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Science/Research',
    ],
    keywords='keyword1 keyword2',
    url='http://github.com/user/repo',
    author='Chet Corcos',
    author_email='ccorcos@gmail',
    license='MIT',
    packages=['se3'],
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    include_package_data=True,
    zip_safe=False
)
