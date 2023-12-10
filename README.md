# 0x00. AirBnB clone - The console

Welcome to Project AirBnB clone, This is the first step towards building the AirBnB clone project attempts to clone the AirBnB application and website, including the database, storage, RESTful API, Web Framework, and Front End tools.

## Contents:

* [1 Introduction](#1-Introduction)
* [2 Installation](#2-Installation)
* [3 Testing](#3-Testing)
* [4 Command Overview](#4-Command)
* [5 Usage](#5-Usage)
* [6 Authors](#6-Authors)


Team project to build a clone of [AirBnB](https://www.airbnb.com/)

## Overview

AirBnB clone with a robust and powerful command-line interface (CLI) known as "The Console." This project aims to replicate the core functionalities of the popular accommodation platform, allowing users to manage and interact with property listings, bookings, and user profiles seamlessly through a text-based interface.

## ``2-Installation``
1.  Clone this GitHub repository to your local machine.

`git clone https://github.com/khalildahbane/AirBnB_clone.git`

2.  change directory to the project directory.

`cd AirBnB-Clone` 

3.  run the console.

`./console.py`

### Execution ``3 Testing``

shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
Non Interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## ``Command Overview ``

* `create`: Create a new instance of a specified class.
* `show`: Display the string representation of an instance.
* `destroy`: Delete an instance based on the class name and ID.
* `all`: Print all string representations of instances, filtered by class name.
* `update`: Update an instance based on the class name and ID.
* `count`: Retrieve the number of instances of a specified class.
* `quit or EOF`: Exit the program.

## ``4-Usage``

* Start the console in interactive mode:

```bash
$ ./console.py
(hbnb)
```

* Use help to see the available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

* Quit the console:

```bash
(hbnb) quit
$
```

* create:

> *Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.*

```bash
(hbnb) create BaseModel
57262839-51d7-4a9a-93e2-35ed8e91d823
$
```

* show:

> *Deletes an instance of a given class with a given ID.*
> *Update the file.json*

```bash
(hbnb) show BaseModel 57262839-51d7-4a9a-93e2-35ed8e91d823
[BaseModel] (57262839-51d7-4a9a-93e2-35ed8e91d823) {'id': '57262839-51d7-4a9a-93e2-35ed8e91d823', 'created_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412265), 'updated_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412357)}
(hbnb)
(hbhb)
```

* all:

> *Prints all string representation of all instances of a given class.*
> *If no class is passed, all classes are printed.*

```bash
(hbnb) all
[BaseModel] (57262839-51d7-4a9a-93e2-35ed8e91d823) {'id': '57262839-51d7-4a9a-93e2-35ed8e91d823', 'created_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412265), 'updated_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412357)}
(hbnb) all BaseModel
[BaseModel] (57262839-51d7-4a9a-93e2-35ed8e91d823) {'id': '57262839-51d7-4a9a-93e2-35ed8e91d823', 'created_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412265), 'updated_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412357)}
```
* destroy:

>*Deletes an instance of a given class with a given ID.*
>*Update the file.json*

```bash
(hbnb) destroy
** class name missing **
(hbnb) destroy BaseModel
** instance id missing **
(hbnb) destroy BaseModel 57262839-51d7-4a9a-93e2-35ed8e91d823
(hbnb) all
[]
```

* count:

> *Prints the number of instances of a given class.*

```bash
(hbnb) create User
ce5f7ac5-4b2e-4c90-933d-6c78e69ab1c7
(hbnb) create User
dd697519-4ac9-42e0-80e2-fa7b3ac61193
(hbnb) create User
52c4036b-f018-49d0-8d93-d7a2d56bcdad
(hbnb) count User
3
```

## ``6-Authors`

-  [khalildahbane](https://github.com/khalildahbane)
-  [Cha1mae](https://github.com/Cha1mae)
