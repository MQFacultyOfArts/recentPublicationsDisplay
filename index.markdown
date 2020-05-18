---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

---
<html>
  <head>
    <meta charset="utf-8">
    <title>{{ page.title }}</title>
    <style>
    	#qrcode { position:fixed;
    		bottom:10px;
    		right:10px;
    		z-index:100 }
 		iframe {position:fixed; 
 			top:0; 
 			left:0; 
 			bottom:0; 
 			right:0; 
 			width:100%; 
 			height:100%; 
 			border:none; 
 			margin:0; padding:0; overflow:hidden; z-index:-999999}
	</style>
	<script>
    {% for post in site.posts limit:1 %}
setTimeout(function() {
  window.location.href = "{{post.url | absolute_url}}"
}, 300);
    
    {% endfor %}
</script>
  </head>
  <body style="margin:0">
{% for post in site.posts limit:1 %}
{{post.url | absolute_url}}
{% endfor %}
  </body>
</html>