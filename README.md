# Site generator

# Desciption
This package enables you to generate static HTML sites from a python script. 

## Use
Create a base template.
By default this is ./templates/base.html. 
Inside the base template other (sub)templates can be referenced
For example:
```
<body>
{{ main }}
{{ footer }}
</body>
```
Make sure 'main.html' and 'footer.html' are present in the template folder. 

Then use the .render method to create a complete html file.
By default this is 'index.html'.
```
s = SiteGenerator()
s.render()
```

## Extra options
### Replacements
It is possible to use variables with the {% variable %} tag. 
For example:
```
<p>{% footertext %}</p>
```

Variables are replaced by providing a dictionary:

```
s = SiteGenerator()
s.replacements = {"footertext": "This is a footertext",
                    "secondtext": "This is secondtext"}
s.render()
```
If no match is found in the dictionary the tag will not be replaced.

### Multiple (sub)templates with the same name
All the templates with the same template tag are rendered in the static HTML file. The template tag is defined as the text in the filename before the first underscore.
The alfa-numerical order after the first underscore is used as render order.

For example if 'main_1.html' and 'main_2.html' files are present, both are rendered in the result file in the {{ main }} location.  

### Custom names and locations
```
s = SiteGenerator()
s.base_template = "custom_base.html"  
s.output_file = "custum_index.html"
s.template_folder = "./custom_templates",
s.render
```