# WOF_Piab

WOF_Piab is an implementation of [WOFpy](https://pythonhosted.org/WOFpy/), which in turn is a Python package that implements
[CUAHSI's](http://his.cuahsi.org) WaterOneFlow Web service.
WaterOneFlow is a Web service with methods for querying time series of water data at point locations,
which returns data in WaterML format, providing standardized access to water quantity and quality data.

WOF_Piab reads data from an [ODM Version 1.1](https://www.researchgate.net/publication/237464319_CUAHSI_Community_Observations_Data_Model_ODM_Version_11_Design_Specifications) PostgreSQL database through a Data Access Object (DAO) and translates it into WaterML. WOFpy can be configured to read data from many different sources, such as non ODM databases and even csv files, by changing its DAO.

The original WOFpy code was modified so that it can handle series of the same variable and location, but with different methods, quality control codes or censor codes, such as those present in the Piabanha basin ODM database. 

WOFpy uses Python version 2.7.

## Getting Started

In order to avoid clashes with Python environments already installed in your system, WOF_Piab is prepared to be installed with pipenv, in a separate environment with the right version of Python and the right version of the supporting packages, obtained from PyPI.

### Prerequisites

Pipenv can be installed in different OS's, as long as the machine has Python installed, using [pipx](https://github.com/pipxproject/pipx), which can be installed via pip:

```
$ python3 -m pip install --user pipx
$ python3 -m pipx ensurepath
```
Once pipx is installed, run:

```
$ pipx install pipenv
```

to install pipenv.

### Installing

1. Checkout the project from GitHub
```
$ git clone https://github.com/flaviolyra/wof_piab
```
2. Move to the directory
```
$ cd wof_piab
```
3. Create a new pipenv project using Python 2.7
```
$ pipenv --python 2.7
```
4. install all dependencies of the project
```
$ pipenv install
```
5. Activate the project's virtualenv
```
$ pipenv shell
```


## Deployment

Once the virtual environment is activated, the Web Service can be deployed on localhost port 8081 over a uWSGI server with:
```
(wof_piab) $ uwsgi piabanha.ini
```
It can also be deployed on a different server by changing the uwsgi parameters in piabanha.ini.

## Testing

You can check that the web service is running navigating to localhost:8081 to open the service site. There you can get the URL of the service WSDL, as well as its endpoint, and navigate to a page where you can test its REST API.

The SOAP web service and its REST API version can be thoroughly tested using the open source version of [SoapUI](https://www.soapui.org/).


## Authors

Original Development was supported by the Texas Water Development Board as part of**’Water Data for Texas’** - a unified hydrological information system that shares environmental data for the state of Texas


