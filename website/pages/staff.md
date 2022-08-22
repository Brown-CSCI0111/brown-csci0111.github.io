---
layout: default
title: Staff
icon: staff_icon.png
banner: staff_banner.png
permalink: /staff
---

<!-- Assignments -->

{% assign Profs = site.staff | where: 'role', 'Professor' %}
{% assign HTAs = site.staff | where: 'role', 'HTA' %}
{% assign UTAs = site.staff | where: 'role', 'UTA' %}

<!-- Professors -->

{% if Profs.size != 0 %}

## Professors

<div>
  {% for staffer in Profs %}
  {{ staffer }}
  {% endfor %}
</div>

{% endif %}

<!-- HTAs -->

{% if HTAs.size != 0 %}

## HTA

<div>
  {% for staffer in HTAs %}
  {{ staffer }}
  {% endfor %}
</div>

{% endif %}

<!-- UTAs -->

{% if UTAs.size != 0 %}

## UTA

<div>
  {% for staffer in UTAs %}
  {{ staffer }}
  {% endfor %}
</div>

{% endif %}
