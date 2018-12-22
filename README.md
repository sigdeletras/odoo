# odoo_app

Testing Odoo

## Creación estructura del módulo

```
odoo-bin scaffold openacademy addons
```

Añadiendo folder al path de addons

- Go to location: /etc/odoo/odoo-server.conf
- Add path in that file: addons_path = /opt/odoo/enterprise,/opt/odoo/addons,/opt/odoo/custom-addons

```
./odoo-bin --addons-path=enterprise/,../custom-addons/,../odoo/addons/
```

## __init__

## Manifest

## Models

Business objects are declared as Python classes extending Model which integrates them into the automated persistence system.

Models can be configured by setting a number of attributes at their definition. The most important attribute is _name which is required and defines the name for the model in the Odoo system.

```python
    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
```

## Views

Actions and menus are regular records in database, usually declared through data files. Actions can be triggered in three ways:

- by clicking on menu items (linked to specific actions)
- by clicking on buttons in views (if these are connected to actions)
- as contextual actions on object

Define new menu entries:

### Basics views

- Generic view declaration
- Tree views <tree>. List views, display records in a tabular form.
- Form views <form>. Forms are used to create and edit single records. 
- Search views <search>. Search views customize the search field associated with the list view (and other aggregated views).

- __manifest__.py
- views/openacademy.xml


## Controllers


## Demos

Define demonstration data. The content of the data files is only loaded when a module is installed or updated.After making some changes, do not forget to use *odoo-bin -u openacademy* to save the changes to your database.

## Security


