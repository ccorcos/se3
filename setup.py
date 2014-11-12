from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='se3',
    version='0.2',
    description='Homogenous transforms in special euclidian 3-space.',
    long_description=readme(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Science/Research',
    ],
    keywords='euclidian special homogenous transform rotation 3d',
    url='https://github.com/ccorcos/se3',
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
