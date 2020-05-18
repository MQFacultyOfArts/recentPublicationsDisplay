---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

---

<!DOCTYPE html>
<html>
<head>
	<title>Index</title>
</head>
<body>


<script>
    {% for post in site.posts limit:1 %}
setTimeout(function() {
  window.location.href = "{{post.url | absolute_url}}"
}, 300);
    
    {% endfor %}
</script>
  
{% for post in site.posts limit:1 %}
{{post.url | absolute_url}}
{% endfor %}
 



</body>
</html>
