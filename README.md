<h1 align="center">AirBnB clone - The console<h1/>
<p align="center">An AirBnB clone.</p>

---

## Description

This project involves building a command interpreter to manage AirBnB objects. The primary goal is to create a parent class (BaseModel) for initialization, serialization, and deserialization of instances. This lays the foundation for subsequent projects, including HTML/CSS templating, database storage, API, and front-end integration. This project is to implement the back-end console.

## Command Interpreter

The command interpreter is a shell-like interface that allows users to manage objects in the AirBnB project. It provides functionalities such as creating new objects, retrieving objects from files or databases, performing operations on objects, updating object attributes, and destroying objects.

## How to Start

To start the command interpreter, run the following:

```
$ ./console.py
```

## How to Use

Once in interactive mode, the following commands are available:

* `help`: Display help messages for available commands.
* `EOF`: Exit the command interpreter.
* `quit`: Exit the command interpreter.

In non-interactive mode, you can use echo or cat with a pipe to pass commands:

```
$ echo "help" | ./console.py
```

## Examples

Interactive mode:

```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) quit
$
```

Non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
```

## Authors

1. Tasha Daije
2. Salome Njenga

For a detailed list of contributors, refer to the AUTHORS file
