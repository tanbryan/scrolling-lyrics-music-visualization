from setuptools import setup, find_packages

setup(
    name='mp4_generator',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mp4_generator = mp4_generator.__main__:main'
        ]
    }
)
