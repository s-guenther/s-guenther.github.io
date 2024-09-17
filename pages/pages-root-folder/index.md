---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: frontpage
header:
  image_fullwidth: header_unsplash_12.jpg
widget1:
  title: "Service 1"
  url: '{{ site.url }}{{ site.baseurl }}/service1/'
  image: widget-1-302x182.jpg
  text: 'This text is a short description to my first service'
widget2:
  title: "Service 2"
  url: '{{ site.url }}{{ site.baseurl }}/service1/'
  image: widget-1-302x182.jpg
  text: 'This text is a short description to my second service'
widget3:
  title: "About"
  url: '{{ site.url }}{{ site.baseurl }}/about/'
  text: 'This is a short description for my about page'
  image: widget-github-303x182.jpg
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
# callforaction:
#   url: https://tinyletter.com/feeling-responsive
#   text: Inform me about new updates and features ›
#   style: alert
permalink: /index.html
#
# This is a nasty hack to make the navigation highlight
# this page as active in the topbar navigation
#
homepage: true
---

Here starts `markdown` content.
