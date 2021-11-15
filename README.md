# my_project repo example (LINUX+PYTHON3.8+CONDA)

This repo is an empty one but with all necessary documents:
* structure DDD 
* .gitgnore already: filled with most current files
* .dockerignore: already filled with most current files
* init.sh: script to settle inital env
* setup.py: find local package
* source_code/setting/base.py: already filled with absolute path variables
* conda.yml for installing packages
* config.py: Exemple of config file to load yml & credentials
* ... many small details that will make your life easier :)

You can erase the description above for your own project

Project : description of the project

## Getting started

### Requirements

Following tools must be install to setup this project:

- `python >= 3.8`
- `conda >= 4.9.2`
- `git lfs`

### Setup environment

Following command lines could be used to setup the project.

```
By SSH
$ git clone git@github.com:VandvC/base_python_conda.git
or By https
$ git clone https://github.com/VandvC/base_python_conda.git
$ source init.sh
```

### Run script


```
$ python3.8 <path/to/main.py>
```

#### Create a conda environment

In the main repo directory

    conda env create -f <conda_yml_file> 
    conda activate <environnement_name>


## Links
Exemple of links below
*  Reference
    *  [Docs](https://github.com/VandvC)
    *  [Examples](https://github.com/VandvC)
    *  [Code](https://github.com/VandvC)
    *  [Blog](https://github.com/VandvC)
*  Ask for help
    *  [github issues](https://github.com/VandvC) for bug reports and feature requests

## Outline

0. [Overview](source_code/application/main.py) - main program to run
