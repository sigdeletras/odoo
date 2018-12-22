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

```
my_module
├── __init__.py
├── __manifest__.py
├── controllers
│   ├── __init__.py
│   └── controllers.py
├── demo
│   └── demo.xml
├── models
│   ├── __init__.py
│   └── models.py
├── security
│   └── ir.model.access.csv
└── views
    ├── templates.xml
    └── views.xml
```

## __init__

## Manifest

__manifest__.py, the manifest of your module, including for instance its title, description and data files to load

## Models
models/models.py, an example of model with its fields.

Business objects are declared as Python classes extending Model which integrates them into the automated persistence system.

Models can be configured by setting a number of attributes at their definition. The most important attribute is _name which is required and defines the name for the model in the Odoo system.

```python
    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    start_date = fields.Date()
    start_datetime = fields.Datetime('Start time', default=lambda self: fields.Datetime.now())
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    
    # Relational fields
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")
```

### Model inheritance


## Views

views/views.xml, a tree and a form view, with the menus opening them.

Actions and menus are regular records in database, usually declared through data files. Actions can be triggered in three ways:

- by clicking on menu items (linked to specific actions)
- by clicking on buttons in views (if these are connected to actions)
- as contextual actions on object


### Basics views

- Generic view declaration
- Tree views <tree>. List views, display records in a tabular form.
- Form views <form>. Forms are used to create and edit single records. 
- Search views <search>. Search views customize the search field associated with the list view (and other aggregated views).

Adding in:

- __manifest__.py
- views/openacademy.xml

### View inheritance

## Controllers

controllers/controllers.py, an example of controller implementing some routes,

## Demos
demo/demo.xml, demo records for the above example model

Define demonstration data. The content of the data files is only loaded when a module is installed or updated.After making some changes, do not forget to use *odoo-bin -u openacademy* to save the changes to your database.

## Security






