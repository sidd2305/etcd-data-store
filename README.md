# Etcd Key-Value Store Project

This project implements a key-value store using etcd as the backend storage and a Flask application to interact with it.

## Requirements

- [etcd](https://etcd.io/)
- [Python](https://www.python.org/)
- [pip](https://pypi.org/project/pip/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [python-etcd3](https://python-etcd3.readthedocs.io/en/latest/readme.html)

## Installation

### Install etcd

You can install etcd on macOS using Homebrew:

```bash
brew install etcd
```
### Install python-etcd3 package

```python
pip install etcd3
```

## Running the Project

### Starting etcd Server

You can go to your terminal and type this:

```bash
etcd
```

### Running Flask App

Go to your project directory (the directory where `app.py` is stored) in terminal and type:

```bash
python app.py
```
## Functionalities Implemented


### Key-Value Pair Addition: 

You can add key-value pairs to the etcd database using the "Put Key-Value Pair" functionality. This feature is handled by the `put()` function in `app.py`, located at line 16. Users can input a key and its corresponding value, and upon submission, the key-value pair is stored in the etcd database. This functionality utilizes the `put()` API provided by the etcd package to insert the key-value pair into the database.

### Retrieving Values by Key: 

Users can retrieve the value associated with a specific key from the etcd database using the "Get Value by Key" functionality. This feature is managed by the `get()` function in `app.py`, found at line 22. Users input a key, and upon submission, the corresponding value is fetched from the etcd database and displayed to the user. This functionality utilizes the `get()` API provided by the etcd package to retrieve the value associated with the specified key.

### Deleting Keys: 

The "Delete Key" functionality allows users to remove a key and its associated value from the etcd database. This feature is controlled by the `delete()` function in `app.py`, located at line 29. Users input a key, and upon submission, the key-value pair is deleted from the etcd database if it exists. This functionality utilizes the `delete()` API provided by the etcd package to delete the specified key-value pair.

### Listing All Keys: 

Users can view a list of all keys stored in the etcd database using the "List All Keys" functionality. This feature is handled by the `list_keys()` function in `app.py`, present at line 39. Upon accessing this functionality, all keys present in the etcd database are fetched and displayed to the user. This functionality utilizes the `get_all()` API provided by the etcd package to retrieve all keys stored in the database.


### Integration of Frontend and Backend: 

The Flask framework is used to seamlessly integrate frontend HTML templates with backend Python code. The HTML templates, such as `index.html` and `list.html`, are rendered dynamically by Flask, allowing for the presentation of data retrieved from the etcd database and the handling of user interactions through form submissions. This integration is facilitated by defining routes in app.py that correspond to the various frontend actions, such as adding, retrieving, and deleting key-value pairs.

### Usage of CSS Styling: 

The HTML templates utilize Cascading Style Sheets (CSS) to enhance the visual presentation of the web application. CSS rules are applied to elements within the HTML templates to control aspects such as layout, colors, fonts, and animations. By embedding CSS styles directly within the HTML files or linking external CSS files, the appearance of the web pages can be customized to create a visually appealing and user-friendly interface. The CSS styling enhances the overall user experience by improving readability, organization, and aesthetic appeal of the web application.

### Contributors:

- Shyam Krishna Sateesh - PES1UG21CS935
- Shriansh Mohanty - PES1UG21CS584	
- Siddhanth Sridhar - PES1UG21CS593	
- Siddharth Hegde - PES2UG21CS522	


