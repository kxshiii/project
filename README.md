Contact Book CLI with ORM

Features

Add contacts with name, email, and auto-generated secure passwords.

Assign contacts to user-defined groups (like "Friends", "Work").

Store multiple passwords per contact with timestamps for history.

View all contacts, grouped or ungrouped.

Search for a contact by name.

Delete contacts or individual passwords.

All data is stored persistently in a local SQLite database.

How It Works

Launching the App:

Run the app using python main.py inside your Pipenv shell.

Main Menu:

A CLI menu guides you through actions like adding, viewing, searching, and deleting contacts.

Adding a Contact:

You'll be prompted for a name and email.

You can choose to assign the contact to a group.

The app will ask if you want to auto-generate a strong password.

Storing and Viewing:

The contact and password are saved in a database.

You can view all contacts, their group assignments, and associated passwords.

Deleting and Searching:

You can search for a contact by name to view or delete.

You can also delete old passwords or entire contacts.

Getting Started

Clone the repository:

git clone https://github.com/yourusername/contact_book_orm.git
cd contact_book_orm

Set up the environment:

pipenv install
pipenv shell

Run the app:

python main.py

Requirements

Python 3.8+

Pipenv

SQLAlchemy
