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

<!-- {% assign EdStar = "Aidan" %}
{% assign EdStarPhoto = "Aidan.jpg" %}

<div class="staff-video">
  <div class="featured-artist-container">
    <div class="featured-artist-header">
      New music from the artists you follow
    </div>
    <div class="featured-artist-card">
      <div class="featured-artist-image-container">
        <img src="../assets/images/staff/{{ EdStarPhoto}}" />
      </div>
      <div class="featured-artist-text-container">
        <h1> {{ EdStar }} </h1>
        <p> I'm the EdStar of the Week! </p>
      </div>
    </div>
  </div>

  <!-- ==== -->

   <!-- <div>
    <div class="suggested-video-header">
      Suggested for you
    </div>
    <iframe width="320" height="200" controls muted>
      <source src="https://youtu.be/Hw6bnyakAaM">
      Your browser does not support the video tag.
    </iframe>
  </div>
</div> -->

<iframe width="560" height="315" src="https://www.youtube.com/embed/Hw6bnyakAaM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen class="youtube-video"></iframe>

<!-- Assignments -->

{% assign Profs = site.staff | where: 'role', 'Professor' %}
{% assign HTAs = site.staff | where: 'role', 'HTA' %}
{% assign UTAs = site.staff | where: 'role', 'UTA' %}

<!-- Professors -->

{% if Profs.size != 0 %}

<div class="staff-group">Professor & Graduate Associate</div>

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
