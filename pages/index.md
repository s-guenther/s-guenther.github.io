---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: frontpage
header:
  image_fullwidth: logo_sgrse_banner.svg
widget1:
  title: "Research Software"
  url: '/research-software/'
  image: unsplash_code_303.jpg
  text: 'Custom software tools tailored to your unique challenges, integrating cutting-edge research into ready-to-deploy and production-ready solutions.'
widget2:
  title: "Scientific Computing"
  url: '/scientific-computing/'
  image: unsplash_pc_303.jpg
  text: 'Data science workflows, high-performance computing, modeling, simulation, and optimization to drive complex analyses and decision-making. '
widget3:
  title: "Hardware Prototyping"
  url: '/hardware-prototyping/'
  image: rendering_303.jpg
  text: 'Development of custom mechatronic and electromechanical prototypes, turning innovative concepts into functional hardware.'
#
# Use the call for action to show a button on the frontpage
#
# To make internal links, just use a permalink like this
# url: /getting-started/
#
# To style the button in different colors, use no value
# to use the main color or success, alert or secondary.
# To change colors see sass/_01_settings_colors.scss
#
callforaction:
  url: '/projects/'
  text: This sounds abstract? Have a look at concrete projects.
  style: info
permalink: /index.html

#
# This is a nasty hack to make the navigation highlight
# this page as active in the topbar navigation
#
homepage: true
---

##### Tailored software solutions for complex computational challenges

---

I provide customized solutions for

<p align="center">
<strong>Modeling</strong>, <strong>Simulation</strong>, <strong>Optimization</strong>, and <strong>Artificial Intelligence</strong>,
</p>

with a focus on:

<p align="center">
<strong>Renewable Energy Systems</strong>, <strong>Energy Storage</strong>, and <strong>Infrastructure & Transport</strong>.
</p>

With over 10 years of experience in research and development across
academia and industry, I combine deep technical knowledge with
state-of-the-art research software engineering to deliver custom
solutions. Interested? Don't hesitate to [contact me]({{ site.url }}/contact/)
to learn more. 

---

_This site is still under construction. Drop by occasionally and stay tuned for
updates._