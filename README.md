# Odoo Basic

Tutorial https://www.odoo.com/documentation/11.0/howtos/backend.html

## VCode plugins

- Python
- XML Tools

## Scaffolding

```bash
$ odoo-bin scaffold openacademy addons
```

Add custon addons path

- Go to location: /etc/odoo/odoo-server.conf
- Add path in that file: addons_path = /opt/odoo/enterprise,/opt/odoo/addons,/opt/odoo/custom-addons

```bash
$ ./odoo-bin --addons-path=enterprise/,../custom-addons/,../odoo/addons/
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

## Manifest

__manifest__.py 

The manifest ofthe module, including for instance its title, description and data files to load.

![Module](/img/01_module_manifest.png)

![Module](/img/01_module_technical_data.png)

![Module](/img/01_module_installed_features.png)

## Models

models/models.py

Business objects are declared as Python classes extending Model which integrates them into the automated persistence system. Models can be configured by setting a number of attributes at their definition.


```python
    # Strings
    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    # Date
    start_date = fields.Date()
    start_datetime = fields.Datetime('Start time', default=lambda self: fields.Datetime.now())
    
    # Numbers
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True) # Boolena

    # Relational fields
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")
```

When a new fields are adding is necessary to restart Odoo and upgrading the module.

```bash
$ service odoo restart
```

## Views

views/views.xml

Tree and a form views, with the menus opening them. Actions and menus are regular records in database, usually declared through data files. Actions can be triggered in three ways:

- by clicking on menu items (linked to specific actions)
- by clicking on buttons in views (if these are connected to actions)
- as contextual actions on object


**Basics views*

- Tree views <tree>. List views, display records in a tabular form.
- Form views <form>. Forms are used to create and edit single records. 
- Search views <search>. Search views customize the search field associated with the list view (and other aggregated views).

Adding in __manifest__.py

```xml
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'reports.xml',

    ],
```
## Menus and actions 

```xml
<record model="ir.actions.act_window" id="course_list_action">
        <field name="name">Cursos</field>
        <field name="res_model">openacademy.course</field>
        <field name="view_type">form</field>
        <field name="view_mode">tree,form</field>
        <!-- Personalización de Búsquedas -->
        <field name="context" eval="{'search_default_my_courses': 1}"/>
        <field name="help" type="html">
            <p class="oe_view_nocontent_create">Crea el primer curso
            </p>
        </field>
    </record>

    <!-- top level menu: no parent -->
    <menuitem id="main_openacademy_menu" name="Open Academy"/>
    <!-- A first level in the left side menu is needed before using action= attribute -->
    <menuitem id="openacademy_menu" name="Open Academy" parent="main_openacademy_menu"/>
    <!-- the following menuitem should appear *after* its parent openacademy_menu and *after* its
             action course_list_action -->
    <menuitem id="courses_menu" name="Courses" parent="openacademy_menu" action="course_list_action"/>
    <!-- Full id location: action="openacademy.course_list_action"  It is not required when it is the same module -->

```

![Module](/img/02_menus.png)

## Tree views

```xml
    <record model="ir.ui.view" id="course_tree_view">
        <field name="name">course.tree</field>
        <field name="model">openacademy.course</field>
        <field name="arch" type="xml">
            <tree string="Course Tree">
                <field name="name"/>
                <field name="responsible_id"/>
            </tree>
        </field>
    </record>
```

![Module](/img/03_tree.png)

![Module](/img/03_tree2.png)

## Form views

```xml
    <!-- Sesión Formulario -->
    <record model="ir.ui.view" id="session_form_view">
        <field name="name">session.form</field>
        <field name="model">openacademy.session</field>
        <field name="arch" type="xml">
            <form string="Session Form">
                <sheet>
                    <group>
                        <group string="General">
                            <field name="course_id"/>
                            <field name="name"/>
                            <field name="instructor_id"/>
                            <field name="active"/>
                        </group>
                        <group string="Schedule">
                            <field name="start_date"/>
                            <field name="duration"/>
                            <field name="seats"/>
                            <!-- Computed fields -->
                            <field name="taken_seats" widget="progressbar"/>
                        </group>
                    </group>
                    <label for="attendee_ids"/>
                    <field name="attendee_ids"/>
                </sheet>
            </form>
        </field>
    </record>
```

![Module](/img/04_form02.png)

## Search views
```xml
    <record model="ir.ui.view" id="course_search_view">
        <field name="name">course.search</field>
        <field name="model">openacademy.course</field>
        <field name="arch" type="xml">
            <search>
                <field name="name"/>
                <field name="description"/>
                <!-- Advanced search-->
                <filter name="my_courses" string="My Courses" domain="[('responsible_id', '=', uid)]"/>
                <group string="Group By">
                    <filter name="by_responsible" string="Responsible" context="{'group_by': 'responsible_id'}"/>
                </group>

            </search>
        </field>
    </record>
```

![Module](/img/05_search.png)

![Module](/img/05_search_personalizado.png)

## Calendar

![Module](/img/06_calendar.png)

## Graph

![Module](/img/07_graph.png)

## Report

```xml
<odoo>

    <report
        id="report_session"
        model="openacademy.session"
        string="Session Report"
        name="openacademy.report_session_view"
        file="openacademy.report_session"
        report_type="qweb-pdf" />

    <template id="report_session_view">
        <t t-call="web.html_container">
            <t t-foreach="docs" t-as="doc">
                <t t-call="web.external_layout">
                    <div class="page">
                        <h2 t-field="doc.name"/>
                        <p>From <span t-field="doc.start_date"/> to <span t-field="doc.end_date"/></p>
                        <h3>Attendees:</h3>
                        <ul>
                            <t t-foreach="doc.attendee_ids" t-as="attendee">
                                <li><span t-field="attendee.name"/></li>
                            </t>
                        </ul>
                    </div>
                </t>
            </t>
        </t>
    </template>

</odoo>
```

![Module](/img/08_report02.png)

## Controllers

controllers/controllers.py

## Demos
demo/demo.xml, demo records for the above example model

Define demonstration data. The content of the data files is only loaded when a module is installed or updated.After making some changes, do not forget to use *odoo-bin -u openacademy* to save the changes to your database.

## Security






