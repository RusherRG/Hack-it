<div align='center'>
  

# Hack-it

</div>

A coding challenge platform for Hack-it, 2nd round of crackathon event held during abhiyantriki 2019. The participants are given a problem statement and a wrong solution associated to that problem. The task of the participants is to input a specific test case under the input constraints for which the given solution would fail. A flask application was made including basic-authentication and UI for the platform.

## Working

* `./templates/` folder consists of the problem statement HTML files, wrong and correct solutions.
* `./app.py` script for the routing of the flask server
* A input is given to `/check` endpoint which runs both the wrong and corrent scripts and compares whether the output matches. If the output does not match, then it was a successful hack.

------------------------------------------

## Testing

``` 
Username: admin#
Password: password#

# -> integer from 0 to 99
```

## Installation and Deployment

Using Docker

``` sh
docker build . -t hackit
docker run -p 5000:5000 hackit
```

Using Python

``` python
python3 app.py
```

------------------------------------------

### Contributing

 We're are open to `enhancements` & `bug-fixes` :smile: Also do have a look [here](./CONTRIBUTING.md)

------------------------------------------

### Contributors

Members of [@kjsce-codecell](https://github.com/kjsce-codecell)
