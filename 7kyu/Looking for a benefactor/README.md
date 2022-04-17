### Looking for a benefactor

<div class="markdown prose max-w-none mb-8" id="description"><p>The accounts of the "Fat to Fit Club (FFC)" association are supervised by John as a volunteered accountant.
The association is funded through financial donations from generous benefactors. John has a list of
the first <code>n</code> donations: <code>[14, 30, 5, 7, 9, 11, 15]</code>
He wants to know how much the next benefactor should give to the association so that the 
average of the first <code>n + 1</code> donations should reach an average of <code>30</code>.
After doing the math he found <code>149</code>. He thinks that he could have made a mistake.</p>
<p>if <code>dons = [14, 30, 5, 7, 9, 11, 15]</code> then <code>new_avg(dons, 30) --&gt; 149</code></p>
<p>Could you help him?</p>
<h2 id="task">Task</h2>
<p>The function <code>new_avg(arr, navg)</code> should return the expected donation
(rounded up to the next integer) that will permit to reach the average <code>navg</code>. </p>
<p>Should the last donation be a non positive number <code>(&lt;= 0)</code> John wants us: </p>
<ul>
<li><p>to return:</p>
<ul>
<li>Nothing in Haskell, Elm</li>
<li>None in F#, Ocaml, Rust, Scala</li>
<li><code>-1</code> in C, D, Fortran,  Nim, PowerShell, Go, Pascal, Prolog, Lua, Perl</li>
</ul>
</li>
<li><p>or to throw an error (some <strong>examples</strong> for such a case):</p>
<ul>
<li>IllegalArgumentException() in Clojure, Java</li>
<li>ArgumentException() in C#</li>
<li>echo <code>ERROR</code> in Shell</li>
<li>argument-error in Racket</li>
<li>std::invalid_argument in C++</li>
<li>ValueError in Python</li>
</ul>
</li>
</ul>
<p>So, he will clearly see that his expectations are not great enough. 
<em>In "Sample Tests" you can see what to return.</em></p>
<h3 id="notes">Notes:</h3>
<ul>
<li>all donations and <code>navg</code> are numbers (integers or floats), <code>arr</code> can be empty.</li>
<li>See examples below and "Sample Tests" to see which return is to be done.</li>
</ul>
<pre><code>new_avg([14, 30, 5, 7, 9, 11, 15], 92) should return 645
new_avg([14, 30, 5, 7, 9, 11, 15], 2) 
should raise an error (ValueError or invalid_argument or argument-error or DomainError or ... ) 
or return `-1` or ERROR or Nothing or None depending on the language.
</code></pre>
</div>