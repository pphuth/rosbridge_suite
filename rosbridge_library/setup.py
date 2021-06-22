#!/usr/bin/env python

from setuptools import setup

package_name = 'rosbridge_library'

setup(
    name=package_name,
    version='1.0.2',
    packages=[
        package_name,
        package_name + '.internal',
        package_name + '.capabilities',
        package_name + '.util'
    ],
    package_dir={'' : 'src'},
    data_files=[
        ('',['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=False,
    author='Jonathan Mace',
    author_email='Jonathan Mace <jonathan.c.mace@gmail.com>',
    maintainer='Russell Toris, Jihoon Lee',
    maintainer_email='Russell Toris <rctoris@wpi.edu>, Jihoon Lee <jihoonlee.in@gmail.com>',
    description=(
        'The core rosbridge package, repsonsible for interpreting JSON and performing'
        'the appropriate ROS action, like subscribe, publish, call service, and'
        'interact with params.'
    ),
    license='BSD',
    tests_require=['pytest']
)

