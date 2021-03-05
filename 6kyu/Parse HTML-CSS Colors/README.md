### Parse HTML/CSS Colors

In this kata you parse RGB colors represented by strings. The formats are primarily used in HTML and CSS. 

Your task is to implement a function which takes a color as a string and returns the parsed color as a map (see Examples).

Input:

The input string represents one of the following:

6-digit hexadecimal - "#RRGGBB"
e.g. "#012345", "#789abc", "#FFA077"
Each pair of digits represents a value of the channel in hexadecimal: 00 to FF

3-digit hexadecimal - "#RGB"
e.g. "#012", "#aaa", "#F5A"
Each digit represents a value 0 to F which translates to 2-digit hexadecimal: 0->00, 1->11, 2->22, and so on.

Preset color name
e.g. "red", "BLUE", "LimeGreen"
You have to use the predefined map presetColors. 

The keys are the names of preset colors in lower-case and the values are the corresponding colors in 6-digit hexadecimal (same as 1. "#RRGGBB").

Examples:
```c
Parse("#80FFA0")   === new RGB(128, 255, 160))
Parse("#3B7")      === new RGB( 51, 187, 119))
Parse("LimeGreen") === new RGB( 50, 205,  50))

// RGB struct is defined as follows:
struct RGB
{
    public byte r, g, b;
    public RGB(byte r, byte g, byte b);
}


