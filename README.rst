===================
Django Generic File
===================

    A Generic File Model for all kind of file attachment with AJAX fileupload and drag & drop feature.
    
Installation
============

    pip install django-generic-file

Usage
=====

    Add "genericfile" to your INSTALLED_APPS.

    **Include following static files in your template**

    - <link rel="stylesheet" type="text/css" href="{% static 'genericfile/genericfile.css' %}">
    - <script src="{% static 'genericfile/genericfile.js' %}"></script>

    **At the top of your template load our template tags**

    {% load genericfiletags %}

Then to render your form
========================

1. In Add Form (where object is not yet created)

    <form action='.' method='post'>

        {% csrf_token %}

        {{ form }}

        {% get_genericfile_form %}

        <button type='submit' class="btn blue">Submit</button>

    </form>

2. In Edit Form (where object is known)

    <form action='.' method='post'>

        {% csrf_token %}

        {{ form }}

        {% get_genericfile_form host_object=form.instance %}

        <button type='submit' class="btn blue">Submit</button>

    </form>

To get the list of files in Details view
========================================

    {% get_genericfile_list host_object=object as attachments %}

    <ul>

      {% for file in attachments %}

        <li><a href="{{file.attachment.url}}" target="_blank">{{file.get_name}}</a></li>

      {% empty %}

        <li>No files found</li>

      {% endfor %}

    </ul>

Additional Requirements
=======================

    Include following in you html file

    - <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
    - <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
