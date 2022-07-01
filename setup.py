from setuptools import setup, Command
import subprocess


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        errno = subprocess.call(['py.test'], shell=True)
        raise SystemExit(errno)

name = 'ngrammatcher'
version = '1.0'

cmdclass = {'test': PyTest}

setup(
    name=name,
    version=version,
    url='http://github.com/jwnz/ngrammatcher',
    author='Teryn Jones',
    author_email='tkjones93@gmail.com',
    description='Matches pre-defined ngrams from a given list of words/tokens.',
    long_description=open('README.rst').read(),
    packages=['ngrammatcher'],
    install_requires=[],
    platforms='any',
    cmdclass=cmdclass,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ]
)