---
layout: syllabus
title: Syllabus
header: Course Syllabus
group: navigation
---
{% include JB/setup %}

# Engineering 0: Introduction to Markdown

In this class we will achieve the following:

* First Objective
* Second Objective
* and so on...

## Instructors
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

## Grading

Grades will be assigned as follows:

* 50% homeworks
* 50% final

## Schedule

See the [schedule page]({{BASE_PATH}}/schedule.html).


