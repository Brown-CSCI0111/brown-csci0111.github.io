---
layout: banner-content
title: Staff
verified-icon: verified_icon.png
banner-header: Verified Employees
banner-footer: CS111 - 32 Members
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

## Professor & GTA

<div class="staff-container">
  {% for staffer in Profs %}
  {{ staffer }}
  {% endfor %}
</div>

{% endif %}

<!-- HTAs -->

{% if HTAs.size != 0 %}

## HTA

<div class="staff-container">
  {% for staffer in HTAs %}
  {{ staffer }}
  {% endfor %}
</div>

{% endif %}

<!-- UTAs -->

{% if UTAs.size != 0 %}

## UTA

<div class="staff-container">
  {% for staffer in UTAs %}
  {{ staffer }}
  {% endfor %}
</div>

{% endif %}
