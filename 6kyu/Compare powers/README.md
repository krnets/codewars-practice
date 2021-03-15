### Compare powers

You certainly can tell which is the larger number between 2<sup>10</sup> and 2<sup>15</sup>.

But what about, say, 2<sup>10</sup> and 3<sup>10</sup>? You know this one too.

Things tend to get a bit more complicated with both different bases and exponents: which is larger between 3<sup>9</sup> and 5<sup>6</sup>?

Well, by now you have surely guessed that you have to build a function to compare powers, returning -1 if the first member is larger, 0 if they are equal, 1 otherwise. 

Powers to compare will be provided in the [base, exponent] format:
```c
compare_powers([2,10],[2,15])==1
compare_powers([2,10],[3,10])==1
compare_powers([2,10],[2,10])==0
compare_powers([3,9],[5,6])==-1
compare_powers([7,7],[5,8])==-1
```
Only positive integers will be tested, incluing big numbers, so be diligent try to implement an efficient solution.
