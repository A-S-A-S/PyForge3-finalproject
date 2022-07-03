# PyForge3: Final Project

Simple containerized CLI python app to obtain and retrieve some data.


## How to use
First of all, you need docker and docker-compose installed on your machine.<br>
When all done, clone this repo and simply run from the root folder:
```
docker-compose build && docker-compose up -d
```
This will create and start two containers: "PyForgeApp" and "postgres".

__Note__: postgres passwords are stored as plain text at the moment. You should replace it before doing anything special

Now let's dive into our container:
```
docker exec -ti PyForgeApp /bin/bash
```
And run the app:
```
$ python main.py
```
If everything went well, you'll see the CUI menu:
```
Choose thing you want me to do :

        1 : Populate DB
        2 : Show me the data
        0 : Exit


Enter your choice :
```
## Tests
Call _pytest_ from the root directory of repository.

## TODO:
- Decide about entry point
