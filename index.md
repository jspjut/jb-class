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

In addition, I've added a `profs` and `instructors` field that can be
used as shown in the next section. The sample instructor info is as
follows:

```
profs : prof1
instructors :
  prof1 :
    name : Some Guy
    email : sguy@myu.edu
    room : 1234
    hours : MW 8-10
    web : http://sguy.github.io
```

The `profs` field should be a comma separated list of the instructors
if there are more than one for the course.

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

## Custom Navbars

I've included a few custom navbar color styles in
`assets/themes/twitter/css/custom-nav.css`
that you can select in `_includes/themes/twitter/default.html`.
Search for the following line:

```html
    <header class="navbar navbar-inverse teal-nav" role="banner">
```

and replace `teal-nav` with another color in the `custom-nav.css`
file. If you want to use the bootstrap 3 default color for instance,
you can switch it to say `purple-nav`.

## Deploy to custom web space
In `_config.yml` you should set `BASE_PATH` to the path to the root
directory where you intend to deploy your site.
For example, the setting might be:

```
  BASE_PATH : /~sguy/jb-class
```

When you want to build to deploy, run `jekyll build --safe` and then
copy the contents of the `_site` directory to the web server at the
location shown by `BASE_PATH`.
If you want to test locally, you can run `jekyll serve -w` like
normal, and the BASE_PATH will function as if it were set to `/`.
    
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

If you want to remove the blog features and pages from the navbar,
it's as simple as deleting the following lines from
`_includes/themes/twitter/default.html`:

```
  <ul class="nav navbar-nav navbar-right">
    <li class="dropdown">
      <a href="#" class="dropdown-toggle" data-toggle="dropdown">Misc<b class="caret"></b></a>
      <ul class="dropdown-menu">
        {{ "{% assign pages_list = site.pages " }}%}
        {{ "{% assign group = 'misc' " }}%}
        {{ "{% include JB/pages_list " }}%}
      </ul>
    </li>
  </ul>
```

## To-Do

* Improve syllabus/schedule templates

