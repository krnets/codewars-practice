### Convert a string to an integer with any specified base

In C#, the only language built-in to convert a string to an integer with a specified base is Convert.ToInt32(string value, int fromBase). 

However, this only allows conversions from base 2, 8, 10, and 16. 

What if you wanted to convert a string to an integer from any arbitrary base within `2 <= fromBase <= 36`?

Task Overview

Write a method `StringExtensions.Parse(this string value, int fromBase)` which will convert the string representation of a number with a base where the base is within the range of 2 to 36, inclusive, into an Int32.

#### Documentation:

StringExtensions.Parse Method (String, Int32)

Returns an Int32 which represents the string. The string's base is specified by the second argument.

Syntax
```csharp
public static int Parse( this string value, int fromBase )
```
Parameters

*value*

	Type: System.String
	A string which can consist of numbers or letters, and represents a number in an arbitrary base.

*fromBase*

	Type: System.Int32
	The base that value is in.

Return Value

	Type: System.Int32
	The parsed value.

#### Exceptions

|Exception      |Condition 
|--------------*|
|ArgumentNullException| 	value is null.
|ArgumentException| 	value is String.Empty or fromBase is not within the range of 2 to 36, inclusive.
|FormatException| 	value contains a character that is not a valid digit in the base specified by fromBase.
|OverflowException| 	value represents a number that is less than Int32.MinValue or greater than Int32.MaxValue.

Constraints

* The behavior for Parse is only defined for 2 <= fromBase <= 36. If fromBase is out of that range, throw an ArgumentException.
* The string passed into Parse will not contain a negative sign, '-', but the return value may still be negative. For example, if "FFFFFFFF.Parse(16)" is called, the resulting value would be -1 (this is the same behavior as Convert.ToInt32("FFFFFFFF", 16)).
* The string passed into Parse can only contain numbers, lowercase letters, and uppercase letters. An uppercase variant of a letter has the same value as its lowercase variant, e.g. "a".Parse(11) == "A".Parse(11).


