# PyForge3: Final Project

_The intial task is:_

- [X] A public project on GitHub.
- [X] Using docker.
- [X] And PostgreSQL database (find image on docker hub).
- [X] Using SQLAlchemy to define the database table.
- [ ] CLI function to get data on compounds out of API ebi-ac-uk. 
Limit yourself with 1 second per request - we don't want to crush the opensource API. <br>
Sample path for the ATP compound: https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/ATP Compounds to get are: <br>
    - [ ] ADP
    - [ ] ATP
    - [ ] STI
    - [ ] ZID
    - [ ] DPM
    - [ ] XP9
    - [ ] 18W
    - [ ] 29P
 - [ ] Store the data received into the database. Columns needed are:
  - [ ] compound (ADP or ATP or...)
  - [ ] name
  - [ ] formula
  - [ ] inchi
  - [ ] inchi_key
  - [ ] smiles
  - [ ] cross_links_count - amount of objects in cross_links property
- [ ] CLI function to print the table into terminal. <br>
If any value is longer than 13 characters - limit it to 10 characters and add "...".  <br>
For example: inchi_key of 29P from "DHEOBTWDCMSDOQ-HNNXBMFYSA-N" must on print be reduced to "DHEOBTWDCM...".
Use logging with a txt handler to log function calls from task 5.
Create test folder with tests and cover cases for function from the task 5: empty input string, correct input compound name, incorrect input compound name.
- [ ] Enrich the README file with instructions on how to run your project and how to print the result.