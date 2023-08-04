from setuptools import setup

setup(
    name='sunnyday',
    packages=['sunnyday'],
    version='1.0.0',
    license='MIT',
    description='A package to get the weather forecast for a given city or latitude and longitude.',
    author='Javier',
    author_email='your.email@example.com',
    url='https://example.com',
    keywords=['weather', 'forecast', 'sunnyday'],
    install_requires=[
    'requests',
    ],
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    ],
)