# ZeroMQ | ZMQ | ØMQ Messaging Patterns Implementation Python using pyzmq #

## Getting Started ##

### Clone this repository ###
```
$ git clone https://github.com/ecedreamer/zmq-patterns-python.git
```
### Make a python virtual environment ###

``` 
$ python3 -m venv venv

    OR if you use virtualenv package

$ python3 -m virtualenv venv

```

### Activate your virtual environment ###
```
$ source venv/bin/activate
```

### Install Dependencies ###
```
(venv) $ pip install -r requirements.txt
```

### Running req-res pattern example, follow the stpes below ###

- Open two terminal side by side. 
- Our environment must be activated in both the terminal

- In one of the terminal, run the server
    ```
    (venv) $ python patterns/reqres/server.py
    ```
- In another terminal, run the client
    ```
    (venv) $ python patterns/reqres/client.py
    ```
- Study the code and make sure that the expected behaviour is same as output. 
