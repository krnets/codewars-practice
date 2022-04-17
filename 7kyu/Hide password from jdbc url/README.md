### Hide password from jdbc url

<div class="markdown prose max-w-none mb-8" id="description"><p>We have to create a function that receives a connection string with password included and you have to mask the password i.e. change password by asterisks.</p>
<p>Preconditions:</p>
<ul>
<li>non empty valid url</li>
<li>password always next to string section <code>password=</code></li>
<li>assume password will not contain ampersand sign for sake of simplicity</li>
<li>to make it more real it has non ASCII characters</li>
<li>"password=" and "user" will occur only once</li>
</ul>
<blockquote>
<p>empty passwords are not validated but best solutions take empty passwords into account</p>
</blockquote>
<p>Example:</p>
<hr>
<h2 id="input">input</h2>
<blockquote>
<p><code>jdbc:mysql://sdasdasdasd:szdasdasd:dfsdfsdfsdf/sdfsdfsdf?user=root&amp;password=12345</code></p>
</blockquote>
<h2 id="output">output</h2>
<blockquote>
<p><code>jdbc:mysql://sdasdasdasd:szdasdasd:dfsdfsdfsdf/sdfsdfsdf?user=root&amp;password=*****</code></p>
</blockquote>
<p>Extra readings:</p>
<p><a href="https://alvinalexander.com/java/jdbc-connection-string-mysql-postgresql-sqlserver" target="_blank">https://alvinalexander.com/java/jdbc-connection-string-mysql-postgresql-sqlserver</a></p>
</div>