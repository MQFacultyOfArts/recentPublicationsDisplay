---
layout: default
title: index
---


<script>

{% for post in site.posts limit:1 %}
setTimeout(function() {
  window.location.href = "{{post.url | absolute_url}}"
}, 300);
{% endfor %}

</script>
  
{% for post in site.posts limit:1 %}
<a href="{{post.url | absolute_url}}">First post</a>
{% endfor %}
 

