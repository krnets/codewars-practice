/*namespace Kata
{
    using System.Collections.Generic;

    public class Kata
    {
        static Dictionary<string, List<string>> map = new Dictionary<string, List<string>>();

        static string[] rules =
        {
            "spock scissor", "scissor paper", "paper rock", "rock lizard", "scissor lizard",
            "lizard spock", "spock rock", "rock scissor", "lizard paper", "paper spock"
        };

        static Kata()
        {
            foreach (var pairRule in rules)
            {
                var arr = pairRule.Split();
                var first = arr[0];
                var second = arr[1];

                if (map.ContainsKey(first))
                    map[first].Add(second);
                else map[first] = new List<string> {second};
            }
        }

        public static string RPSLP(string player1, string player2)
        {
            if (string.IsNullOrEmpty(player1) || string.IsNullOrEmpty(player2))
                return "Oh, Unknown Thing";

            player1 = player1.ToLower();
            player2 = player2.ToLower();

            return !map.ContainsKey(player1) || !map.ContainsKey(player2) ? "Oh, Unknown Thing" :
                player1 == player2 ? "Draw!" :
                map[player1].Contains(player2) ? "Player 1 won!" : "Player 2 won!";
        }
    }
}*/

using System.Linq;
using static System.String;

namespace Kata
{
    using System.Collections.Generic;

    public class Kata
    {
        private static Dictionary<string, string[]> rulesMap = new Dictionary<string, string[]>()
        {
            {"spock", new[] {"scissor", "rock"}},
            {"scissor", new[] {"paper", "lizard"}},
            {"paper", new[] {"rock", "spock"}},
            {"rock", new[] {"lizard", "scissor"}},
            {"lizard", new[] {"spock", "paper"}}
        };

        public static string RPSLP(string player1, string player2)
        {
            if (IsNullOrEmpty(player1) || IsNullOrEmpty(player2) || !rulesMap.ContainsKey(player1.ToLower()) || !rulesMap.ContainsKey(player2.ToLower()))
                return "Oh, Unknown Thing";

            (player1, player2) = (player1.ToLower(), player2.ToLower());

            return player1 == player2 ? "Draw!" : rulesMap[player1].Contains(player2) ? "Player 1 won!" : "Player 2 won!";
        }
    }
}