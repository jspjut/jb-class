---
layout: page
title: New Class
tagline: Learning how to learn
---
{% include JB/setup %}

This is based on Jekyll Bootstrap but customized for use as a class
web page.

Read [Jekyll Quick Start](http://jekyllbootstrap.com/usage/jekyll-quick-start.html)

Complete usage and documentation available at: [Jekyll Bootstrap](http://jekyllbootstrap.com)

## jb-class updates

This has been updated to Bootstrap 3.

## Update Author Attributes

In `_config.yml` remember to specify your own data:
    
    title : My Blog =)
    
    author :
      name : Name Lastname
      email : blah@email.test
      github : username
      twitter : username

The theme should reference these variables whenever needed.

## Sample Instructor Information
{% for profid in site.profs %}
{% assign prof = site.instructors[profid] %}
<h3>{{ prof.name }}</h3>
<ul class="list-inline">
  {% if prof.email %}
    <li>Email: <a href="mailto:{{ prof.email }}">{{ prof.email }}</a></li>
  {% endif %}
  {% if prof.room %}
    <li>Room: {{ prof.room }}</li>
  {% endif %}
  {% if prof.hours %}
    <li>Hours: {{ prof.hours }}</li>
  {% endif %}
  {% if prof.web %}
    <li><a href="{{ prof.web }}">Website</a></li>
  {% endif %}
</ul>
{% endfor %}
    
## Sample Posts

This blog contains sample posts which help stage pages and blog data.
When you don't need the samples anymore just delete the `_posts/core-samples` folder.

    $ rm -rf _posts/core-samples

Here's a sample "posts list".

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

## To-Do

* Improve syllabus/schedule templates

