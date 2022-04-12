### Expressions Matter

<li><strong><em>Given</em></strong> <em>three integers</em> <code>a</code> ,<code>b</code> ,<code>c</code>, <strong><em>return</em></strong> <em>the <strong><em>largest number</em></strong> obtained after inserting the following operators and brackets</em>: <code>+</code>, <code>*</code>, <code>()</code></li>
<li>In other words , <strong><em>try every combination of a,b,c with [*+()] , and return the Maximum Obtained</em></strong><hr>
<h1 id="consider-an-example-">Consider an Example :</h1>
</li>
<p><strong><em>With the numbers are 1, 2 and 3</em></strong> , <em>here are some ways of placing signs and brackets</em>:</p>
<ul>
<li><code>1 * (2 + 3) = 5</code></li>
<li><code>1 * 2 * 3 = 6</code></li>
<li><code>1 + 2 * 3 = 7</code></li>
<li><code>(1 + 2) * 3 = 9</code></li>
</ul>
<p>So <strong><em>the maximum value</em></strong> that you can obtain is  <strong><em>9</em></strong>.</p>
<hr>
<h1 id="notes">Notes</h1>
<ul>
<li><strong><em>The numbers</em></strong> <em>are always</em> <strong><em>positive</em></strong>. </li>
<li><strong><em>The numbers</em></strong> <em>are in the range</em> <strong><em>(1  ≤  a, b, c  ≤  10)</em></strong>.</li>
<li><em>You can use the same operation</em> <strong><em>more than once</em></strong>.</li>
<li><strong>It's not necessary</strong> <em>to place all the signs and brackets</em>.</li>
<li><strong><em>Repetition</em></strong> <em>in numbers may occur</em> .</li>
<li>You <strong><em>cannot swap the operands</em></strong>. For instance, in the given example <strong><em>you cannot get expression</em></strong> <code>(1 + 3) * 2 = 8</code>.</li>
</ul>
<hr>
<h1 id="input--output-examples">Input &gt;&gt; Output Examples:</h1>
<pre><code>expressionsMatter(1,2,3)  ==&gt;  return 9
</code></pre>
<h2 id="explanation"><strong><em>Explanation</em></strong>:</h2>
<p><em>After placing signs and brackets, the <strong><em>Maximum value</em></strong> obtained from the expression</em> <code>(1+2) * 3 = 9</code>.</p>
<hr>
<pre><code>expressionsMatter(1,1,1)  ==&gt;  return 3
</code></pre>
<h2 id="explanation-1"><strong><em>Explanation</em></strong>:</h2>
<p><em>After placing signs, the <strong><em>Maximum value</em></strong> obtained from the expression is</em> <code>1 + 1 + 1 = 3</code>.</p>
<hr>
<pre><code>expressionsMatter(9,1,1)  ==&gt;  return 18
</code></pre>
<h2 id="explanation-2"><strong><em>Explanation</em></strong>:</h2>
<p><em>After placing signs and brackets, the <strong><em>Maximum value</em></strong> obtained from the expression is</em> <code>9 * (1+1) = 18</code>.</p>