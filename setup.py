import setuptools

setuptools.setup(
    name="upam_client_firmware",
    version="1.0.0",
    author="Fatih Mehmet ARSLAN",
    author_email="fatiharslan@tarsolution.com",
    description="UPAM client software.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    platforms="all",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Topic :: System"
        "Topic :: System :: Hardware",
        "Topic :: System :: Hardware :: Hardware Drivers",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Intended Audience :: Developers",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    install_requires=['psutil'],
    python_requires=">3.6.*, <4",
    packages=['upam_client_firmware'],
    scripts=['bin/upam_client']
)