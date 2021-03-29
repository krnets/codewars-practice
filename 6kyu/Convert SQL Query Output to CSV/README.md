### Convert SQL Query Output to CSV

When you execute a SQL query using Microsoft SQL Server's osql utility, set the delimiter to a comma (,), and output to file, the resulting file looks similar to this:
```
MemberId   ,Surname   ,FirstName ,DateOfBirth,MembershipStartDate,NumberOfDependents,MonthlyPremiumRands\r\n
-----------,----------,----------,-----------,-------------------,------------------,---------------------------------------\r\n
1          ,Downs     ,Graham    ,1980-12-14 ,1998-01-01         ,1                 ,5120\r\n
2          ,Blogs     ,Joe       ,1978-03-20 ,2012-06-01         ,0                 ,2965\r\n
3          ,Smith     ,Jenny     ,1994-01-01 ,2005-12-01         ,11                ,31658\r\n
\r\n
(3 row(s) affected)\r\n
```
A client would like this file converted into a CSV format, suitable for viewing in their favourite spreadsheet program. The resulting file should look like this:
```
MemberId,Surname,FirstName,DateOfBirth,MembershipStartDate,NumberOfDependents,MonthlyPremiumRands\r\n
1,Downs,Graham,1980-12-14,1998-01-01,1,5120\r\n
2,Blogs,Joe,1978-03-20,2012-06-01,0,2965\r\n
3,Smith,Jenny,1994-01-01,2005-12-01,11,31658\r\n
```
Write a function that will accept an array of strings (the lines read from a SQL output file), and returns a string containing those lines converted to CSV format. In practice, the application calling your code will then write that return value to a text file.

You may assume that there will be no commas in the data. Some values, however, might be NULL. If a value is NULL, write the field as an empty string to the CSV output.

Note: If the input array is empty, return an empty string.

