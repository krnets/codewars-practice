fun outed(meet: Map<String, Int>, boss: String): String =
    ((meet.values.sum() + meet[boss]!!) / meet.size)
        .let { happinessRating ->
            if (happinessRating > 5) "Nice Work Champ!"
            else "Get Out Now!"
        }
