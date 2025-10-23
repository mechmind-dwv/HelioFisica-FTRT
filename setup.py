from setuptools import setup, find_packages

setup(
    name="heliofisica-ftrt",
    version="1.0.0",
    author="Benjamin Cabeza Duran / DeepSeek",
    author_email="ia.mechmind@gmail.com",
    description="Sistema de predicción de actividad solar mediante fuerzas de marea planetarias",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mechmind-dwv/HelioFisica-FTRT",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0", 
        "ephem>=4.1.3",
        "scipy>=1.7.0",
        "matplotlib>=3.5.0",
    ],
    include_package_data=True,
    package_data={
        "heliofisica_ftrt": ["data/*.csv", "data/*.json"],
    },
)
