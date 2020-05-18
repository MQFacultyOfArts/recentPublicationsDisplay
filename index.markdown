---
layout: default
title: index
---


<script>

{% for post in site.posts limit:1 %}
setTimeout(function() {
  window.location.href = "{{site.baseurl}}{{site.url}}{{post.url}}"
}, 300);
{% endfor %}

</script>
  
{% for post in site.posts limit:1 %}
{{site.url}}{{post.url}}
{% endfor %}
 

