### Easy wallpaper

<div class="markdown prose max-w-none mb-8" id="description"><p>John wants to decorate the walls of a room with wallpaper.
He wants a fool-proof method for getting it right.</p>
<p>John knows that the rectangular room has a length of <code>l</code> meters, a width of <code>w</code> meters, a height of <code>h</code> meters.
The standard width of the rolls he wants to buy is <code>52</code> centimeters. The 
length of a roll is <code>10</code> meters.
He bears in mind however, that it’s best to have an extra length of wallpaper handy in case of mistakes or miscalculations so he wants to buy a length <code>15%</code> greater than the one he needs.</p>
<p>Last time he did these calculations he got a headache, so could you help John? </p>
<h4 id="task">Task</h4>
<p>Your function <code>wallpaper(l, w, h)</code> should return as a plain English word
in lower case the number of rolls he must buy.</p>
<h4 id="example">Example:</h4>
<p><code>wallpaper(4.0, 3.5, 3.0) should return "ten"</code></p>
<p><code>wallpaper(0.0, 3.5, 3.0) should return "zero"</code></p>
<h4 id="notes">Notes:</h4>
<ul>
<li><p>all rolls (even with incomplete width) are put edge to edge </p>
</li>
<li><p>0 &lt;= l, w, h (floating numbers); it can happens that <code>w * h * l</code> is zero</p>
</li>
<li><p>the integer <code>r</code> (number of rolls) will always be less or equal to 20</p>
</li>
<li><p>FORTH: the number of rolls will be a <em>positive or null integer</em> (not a plain English word; this number can be greater than 20)</p>
</li>
<li><p>In Javascript English numbers are preloaded and can be accessed as:</p>
<pre><code>numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve","thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
</code></pre>
</li>
<li><p>For other languages it is not preloaded but you can use the above one if you need it.</p>
</li>
</ul>
</div>