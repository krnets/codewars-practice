### Target Date

<div class="markdown prose max-w-none mb-8" id="description"><p>You have an amount of money <code>a0 &gt; 0</code> and you deposit it with an interest rate of <code>p percent divided by 360</code> <em>per day</em> on the <code>1st of January 2016</code>. You want to have an amount <code>a &gt;= a0</code>.</p>
<h4 id="task">Task:</h4>
<p>The function <code>date_nb_days</code> (or dateNbDays...) with parameters <code>a0, a, p</code> will return, as a string, the date on which you have just reached <code>a</code>.</p>
<h4 id="example">Example:</h4>
<p><code>date_nb_days(100, 101, 0.98) --&gt; "2017-01-01" (366 days)</code></p>
<p><code>date_nb_days(100, 150, 2.00) --&gt; "2035-12-26" (7299 days)</code></p>
<h4 id="notes">Notes:</h4>
<ul>
<li>The return format of the date is <code>"YYYY-MM-DD"</code></li>
<li>The deposit is always on the <code>"2016-01-01"</code></li>
<li>Don't forget to take the rate for a day to be <code>p divided by 36000</code> since banks consider that there are <code>360</code> days in a year.</li>
<li>You have: <code>a0 &gt; 0, p% &gt; 0, a &gt;= a0</code></li>
</ul>
</div>