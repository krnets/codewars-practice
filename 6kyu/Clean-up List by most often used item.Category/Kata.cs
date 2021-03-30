/*using System.Collections.Generic;
using System.Linq;

namespace CleanUp
{
    public class AmazonItem
    {
        public string Name;
        public string Category;
    }

    public static class AmazonWorker
    {
        public static List<AmazonItem> LeaveOnlyMainCategoryItems(List<AmazonItem> items)
        {
            var groupBy = items.GroupBy(x => x.Category)
                .ToDictionary(g => g.Key, g => g.Count());

            int max = groupBy.Values.Max();
            string largestCategory = "";

            foreach (var (key, value) in groupBy)
                if (value == max)
                {
                    largestCategory = key;
                    break;
                }

            return items.Where(x => x.Category.Equals(largestCategory)).ToList();
        }
    }
}*/

/*using System.Collections.Generic;
using System.Linq;

namespace CleanUp
{
    public class AmazonItem
    {
        public string Name;
        public string Category;
    }

    public static class AmazonWorker
    {
        public static List<AmazonItem> LeaveOnlyMainCategoryItems(List<AmazonItem> items)
        {
            var largestCategory = items.GroupBy(x => x.Category).OrderByDescending(g => g.Count()).First().Key;

            return items.Where(x => x.Category.Equals(largestCategory)).ToList();
        }
    }
}*/

using System.Collections.Generic;
using System.Linq;

namespace CleanUp
{
    public class AmazonItem
    {
        public string Name;
        public string Category;
    }

    public static class AmazonWorker
    {
        public static List<AmazonItem> LeaveOnlyMainCategoryItems(List<AmazonItem> items)
        {
            return items.GroupBy(x => x.Category).OrderBy(g => g.Count()).Last().ToList();
        }
    }
}