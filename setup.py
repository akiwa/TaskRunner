import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='task_runner',
    version='0.0.1',
    description='TODO',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license_file='LICENSE',
    url='https://github.com/akiwa/TaskRunner',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',

    entry_points={
        'console_scripts': [
            'launch_task_runner=task_runner.main:main'
        ]
    },
    install_requires=[
        'flask>=1.1.2',
    ]
)
