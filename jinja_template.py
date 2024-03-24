'''

{% ... %} --> conditonal and loop statements
{{ ... }} --> expressions to print template output
{# ... #} --> comments
# ... ##  --> line statements

For using jinja2 templates, you have to make folder naming 'templates' and make all your html file under this folder.

Template variables: These are defined by the context dictionary passed to the template. To access the attributes use . or [''].
For example: -
    variable_name.attribute_name
    variable_name['attribute_name']
How it works: -
For variable_name.attribute_name: -
    (i) check for specified attribute.
    (ii) if there is not, check for specified item.
    (iii) if there is not, return an undefined object.
For variable_name['attribute_name']: -
    (i) check for specified item.
    (ii) if there is not, check for specified object.
    (iii) if there is not, return an undefined object.

Conditional Statement: -
---------------------
{% if condition %}
<!-- statement -->
{% elif condition %}
<!-- statement -->
{% else %}
<!-- statement -->
{% endif %}


For loop statement: -
------------------
{% for variable in iterator %}
<!-- statement -->
{% endfor %}

Linking CSS and JS external file: -
    (i) Make a 'static' folder.
    (ii) Make CSS file under 'static/css' folder and JS file under 'static/js' folder.
    (iii) To add CSS file add this statement into that HTML file: <link rel="stylesheet" href="{{ url_for('static',filename='css/[file name].css') }}">
          To add JS file add this statement into that HTML file: <script src="{{ url_for('static',filename='js/[file name].css') }}">
'''
