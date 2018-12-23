# Module

![Module](/img/01_module.png)

__manifest__.py

![Module](/img/01_module_manifest.png)

![Module](/img/01_module_technical_data.png)

01_module_installed_features.png



## Model fields




## Actions and Menus
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

![Module](/img/03_tree.png)

![Module](/img/03_tree2.png)

## Form views

![Module](/img/04_form01.png)

![Module](/img/04_form02.png)

## Search views

![Module](/img/05_search.png)


![Module](/img/05_search_personalizado.png)

## Calendar


## Graph

