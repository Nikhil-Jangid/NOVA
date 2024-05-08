import wikipedia

def search_wikipedia(topic):
    try:
        topic = topic.replace("wikipedia", "")
        results = wikipedia.summary(topic, sentences=2)
        return results
    except wikipedia.exceptions.DisambiguationError as e:
        return "Multiple options found. Please specify your search term more precisely."
    except wikipedia.exceptions.PageError as e:
        return f"No results found for '{topic}'."
