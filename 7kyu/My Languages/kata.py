def my_languages(results):
    return sorted(
        (language for language, score in results.items() if score >= 60),
        key=results.get,
        reverse=True,
    )
