Django Generic File
===================

A Generic File Model for all kind of file attachment with AJAX fileupload and drag & drop feature.

- Attach files to any Model across your project
- Include file upload field in your django templates using our templatetags
- Retrieve back the list of files attached to your Object using our templatetags

Installation
------------
::

    pip install django-generic-file

Usage
-----

1. Add **"genericfile"** to your INSTALLED_APPS and migrate.

2. Include following static files in your template::

    <link rel="stylesheet" type="text/css" href="{% static 'genericfile/genericfile.css' %}">
    <script src="{% static 'genericfile/genericfile.js' %}"></script>

3. At the top of your template load our template tags::

    {% load genericfiletags %}

To render file field in your form use "get_genericfile_form"
------------------------------------------------------------

**example 1:** In Your Add Forms (basically where object is not yet created / unknown)::

    <form action='.' method='post'>
        {% csrf_token %}
        {{ form }}
        {% get_genericfile_form %}
        <button type='submit' class="btn blue">Submit</button>
    </form>

    # then in POST method of your view, 
    from genericfile.views import update_genericfile
    update_genericfile(self.request.POST, self.object)

**example 2:** In Your Edit Form (where object is known)::

    <form action='.' method='post'>
        {% csrf_token %}
        {{ form }}
        {% get_genericfile_form host_object=form.instance %}
        <button type='submit' class="btn blue">Submit</button>
    </form>

Options
-------

1. **maxFileCount** - to Restrict Number of files::

    {% get_genericfile_form maxFileCount=1 %}

    # Default is NoLimit

2. **allowedTypes** - to Restrict File types::

    {% get_genericfile_form allowedTypes="jpg,jpeg,png,gif,doc,pdf,zip,html,txt,docx" %}

    # Default is AnyFiles
        
To retrieve the list of files use "get_genericfile_list"
--------------------------------------------------------
::

    {% get_genericfile_list host_object=object as attachments %}
    <ul>
      {% for file in attachments %}
        <li><a href="{{file.attachment.url}}" target="_blank">{{file.get_name}}</a></li>
      {% empty %}
        <li>No files found</li>
      {% endfor %}
    </ul>

Additional Note
---------------

Include if you not have included them already in you html file
::

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
