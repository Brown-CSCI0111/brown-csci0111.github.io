---
layout: banner-content
title: Staff
verified-icon: verified_icon.png
banner-header: Verified Employees
banner-footer: CS111 - 34 Members
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

<div class="staff-group">Professor & GTA</div>

<div class="staff-container">
  {% for staffer in Profs %}
  {{ staffer }}
  {% endfor %}
</div>

{% endif %}

<!-- HTAs -->

{% if HTAs.size != 0 %}

<div class="staff-group">HTA</div>

<div class="staff-container">
  {% for staffer in HTAs %}
  {{ staffer }}
  {% endfor %}
</div>

{% endif %}

<!-- UTAs -->

{% if UTAs.size != 0 %}

<div class="staff-group">UTA</div>

<div class="staff-container">
  {% for staffer in UTAs %}
  {{ staffer }}
  {% endfor %}
</div>

{% endif %}
