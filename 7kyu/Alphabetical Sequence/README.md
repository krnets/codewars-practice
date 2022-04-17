### Alphabetical Sequence

<div class="markdown prose max-w-none mb-8" id="description"><p>In this kata you will be given a random string of letters and tasked with returning them as a string of comma-separated sequences sorted alphabetically, with each sequence starting with an uppercase character followed by <code>n-1</code> lowercase characters, where <code>n</code> is the letter's alphabet position <code>1-26</code>.</p>
<h2 id="example"><span style="color: #f88">Example</span></h2>
<pre><code class="language-javascript"><span class="cm-variable">alphaSeq</span>(<span class="cm-string">"ZpglnRxqenU"</span>) <span class="cm-operator">-</span><span class="cm-operator">&gt;</span> <span class="cm-string">"Eeeee,Ggggggg,Llllllllllll,Nnnnnnnnnnnnnn,Nnnnnnnnnnnnnn,Pppppppppppppppp,Qqqqqqqqqqqqqqqqq,Rrrrrrrrrrrrrrrrrr,Uuuuuuuuuuuuuuuuuuuuu,Xxxxxxxxxxxxxxxxxxxxxxxx,Zzzzzzzzzzzzzzzzzzzzzzzzzz"</span>
</code></pre>
<pre style="display: none;"><code class="language-python"><span class="cm-variable">alpha_seq</span>(<span class="cm-string">"ZpglnRxqenU"</span>) <span class="cm-operator">-</span><span class="cm-operator">&gt;</span> <span class="cm-string">"Eeeee,Ggggggg,Llllllllllll,Nnnnnnnnnnnnnn,Nnnnnnnnnnnnnn,Pppppppppppppppp,Qqqqqqqqqqqqqqqqq,Rrrrrrrrrrrrrrrrrr,Uuuuuuuuuuuuuuuuuuuuu,Xxxxxxxxxxxxxxxxxxxxxxxx,Zzzzzzzzzzzzzzzzzzzzzzzzzz"</span>
</code></pre>
<h2 id="technical-details"><span style="color: #f88">Technical Details</span></h2>
<ul>
<li>The string will include only letters.</li>
<li>The first letter of each sequence is uppercase followed by <code>n-1</code> lowercase.</li>
<li>Each sequence is separated with a comma.</li>
<li>Return value needs to be a string.</li>
</ul>
</div>
