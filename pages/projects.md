---
layout: page
format: blog-index
header: no
# subheadline: "Projects Main Page"
title:  "Projects"
teaser: "Overview over past projects"
meta_teaser: "Some Additional Information"
# breadcrumb: true
image:
    title: projects_pv.jpg
permalink           : "/projects/"
---

{% for post in site.posts %}
  <div class="row">
    <div class="small-12 columns b60">
      <h3 style="margin: 0;"><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
      <p class="subheadline" style="margin: 0; color: grey;">{{ post.subheadline }}</p>
      <p>
        {% if post.image.thumb %}<a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}" title="{{ post.title | escape_once }}"><img src="{{ site.urlimg }}{{ post.image.thumb }}" class="alignleft" width="150" height="150" alt="{{ page.title escape_once }}"></a>{% endif %}

        {% if post.meta_description %}{{ post.meta_description | strip_html | escape }}{% elsif post.teaser %}{{ post.teaser | strip_html | escape }}{% endif %}

        <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}" title="{{ site.data.language.read }} {{ post.title | escape_once }}"><strong>{{ site.data.language.read_more }}</strong></a>
      </p>
    </div><!-- /.small-12.columns -->
  </div><!-- /.row -->
{% endfor %}

_This site is still under construction. Drop by occasionally and stay tuned for
updates._
