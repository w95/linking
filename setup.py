from setuptools import setup

long_description = None
with open('README.md') as f:
    long_description = f.read()

setup(
    name='linking',
    version='0.0.4',
    author='Enrike Nur',
    author_email='enrike.nur@gmail.com',
    description='Linkify plain text, convert URLs and emails',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords = ['linking', 'linkify', 'email', 'URL', 'convert'],
    url='http://github.com/w95/linking',
    license='BSD',
    py_modules=['linking'],
    install_requires=[
        'six'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Filters',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
