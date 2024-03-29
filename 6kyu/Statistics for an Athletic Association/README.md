### Statistics for an Athletic Association

<div class="markdown prose max-w-none mb-8" id="description"><p>You are the "computer expert" of a local Athletic Association (C.A.A.).
Many teams of runners come to compete. Each time you get a string of 
all race results of every team who has run.
For example here is a string showing the individual results of a team of 5 runners:</p>
<p><code>"01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"</code></p>
<p>Each part of the string is of the form: <code>h|m|s</code>
where h, m, s (h for hour, m for minutes, s for seconds) are positive or null integer (represented as strings) with one or two digits. Substrings in the input string are separated by <code>, </code> or <code>,</code>.</p>
<p>To compare the results of the teams you are asked for giving
three statistics; <strong>range, average and median</strong>.</p>
<ul>
<li><p><code>Range</code> : difference between the lowest and highest values. 
In {4, 6, 9, 3, 7} the lowest value is 3, and the highest is 9, 
so the range is 9 − 3 = 6.</p>
</li>
<li><p><code>Mean or Average</code> : To calculate mean, add together all of the numbers 
in a set and then divide the sum by the total count of numbers.</p>
</li>
<li><p><code>Median</code> : In statistics, the median is the number separating the higher half 
of a data sample from the lower half. 
The median of a finite list of numbers can be found by arranging all 
the observations from lowest value to highest value and picking the middle one 
(e.g., the median of {3, 3, 5, 9, 11} is 5) when there is an odd number of observations. 
If there is an even number of observations, then there is no single middle value; 
the median is then defined to be the mean of the two middle values
(the median of {3, 5, 6, 9} is (5 + 6) / 2 = 5.5).</p>
</li>
</ul>
<p>Your task is to return a string giving these 3 values.  For the example given above,
the string result will be</p>
<p><code>"Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"</code></p>
<p>of the form:
 "Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"`</p>
<p>where hh, mm, ss are integers (represented by strings) with <em>each 2 digits</em>.</p>
<h4 id="remarks"><em>Remarks</em>:</h4>
<ol>
<li>if a result in seconds is ab.xy... it will be given <strong>truncated</strong> as ab.</li>
<li>if the given string is "" you will return ""</li>
</ol>
</div>