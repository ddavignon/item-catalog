# Item Catalog

> Dustin D'Avignon

## About

This is the fourth project for the Udacity Full Stack Nanodegree. The Item Catalog project consists of developing an application that provides a list of items within a variety of categories, as well as provide a user registration and authentication system. 

This program uses third-party auth with Google or Facebook. Some of the technologies used to build this application include Flask, Bootsrap, Jinja2, and SQLite.

## JSON Endpoints

`/api/v1/catalog.json` - Returns JSON of all items in catalog

`/api/v1/categories/<int:category_id>/item/<int:catalog_item_id>/JSON` - Returns JSON of selected item in catalog

`/api/v1/categories/JSON` - Returns JSON of all categories in catalog

## Endpoints

#### --------------------------------------
#### CRUD for categories
#### --------------------------------------

`/` or `/categories` - Returns catalog page with all categories and recently added items

`/categories/new` - Allows user to create new category

`/categories/<int:category_id>/edit/` - Allows user to edit an existing category

`/categories/<int:category_id>/delete/` - Allows user to delete an existing category

#### --------------------------------------
#### CRUD for category items
#### --------------------------------------

`/categories/<int:category_id>/` or `/categories/<int:category_id>/items/` - returns items in category

`/categories/<int:category_id>/item/<int:catalog_item_id>/` - returns category item

`/categories/item/new` - return "This page will be for making a new catalog item

`/categories/<int:category_id>/item/<int:catalog_item_id>/edit` - return "This page will be for making a updating catalog item"

`/categories/<int:category_id>/item/<int:catalog_item_id>/delete` - return "This page will be for deleting a catalog item"

## Getting Started

make sure to have sqlite installed. https://www.sqlite.org/download.html

`git clone` the repository and run `pip install -r requirements.txt` if you are not using the vagrant virtual machine
