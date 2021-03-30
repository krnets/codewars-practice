### Clean-up List<T> by most often used item.Category

You have simple class AmazonItem:
```csharp
public class AmazonItem
{
    public string Name;
    public string Category;
}
```
You need to write method to check all items in the List and leave only items related to most often used category.

As example:
```
{Category = "Main Category", Name = "Camera 1"}
{Category = "Main Category", Name = "Camera 2"}
{Category = "Main Category", Name = "Camera 3"}
{Category = "Main Category", Name = "Camera 4"}
{Category = "Main Category", Name = "Camera Stick"}
{Category = "Garbage", Name = "battery"}
{Category = "Garbage", Name = "bottle"}
{Category = "Notebooks", Name = "Asus Model#1"}

after clean-up must to leave only

{Category = "Main Category", Name = "Camera 1"}
{Category = "Main Category", Name = "Camera 2"}
{Category = "Main Category", Name = "Camera 3"}
{Category = "Main Category", Name = "Camera 4"}
{Category = "Main Category", Name = "Camera Stick"}
```
ADDITIONAL INFO WARNING!!!!

My tests is pretty havy. 

List used for tests will have random size up to (99999 * 2 - 1) items. 

So you need to write good enough code that working fast.

If you write the correct code and you get error similar to:
```
Process was terminated. It took longer than 6000ms to complete

13 Passed
```
This means that your code IS CORRECT, but you have too slow altorithm and you need to make it faster.

My code result for this 50 tests is 950ms and its never failing. 

(So long because of written test must to generate and shuffle the list).
