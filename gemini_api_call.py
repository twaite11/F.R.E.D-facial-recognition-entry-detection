from google import genai
from cachetools import TTLCache

GEMINI_MODEL = "gemini-2.5-flash"
MAX_CACHE_ENTRIES = 128  # 128 entries
MAX_CACHE_TIME_S = 84600  # 1 day

cache = TTLCache(maxsize=MAX_CACHE_ENTRIES, ttl=MAX_CACHE_TIME_S)


def make_gemini_api_call(input_request: str) -> str:
    """Make API call to Gemini model.

    Args:
        input_request (str) The request to pass into the Gemini model.

    Returns:
        Gemini response.
    """
    if input_request in cache:
        return cache[input_request]

    client = genai.Client()

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=(input_request + " Make the response of this seem as though it was spoken by a human and not AI. Also please keep your response brief.")
    )

    client.close()

    cache[input_request] = response.text
    return response.text


## Upon trigger word, enter assistance:
def gemini_chat_assistant() -> None:
    """Create gemini chat assistant."""
    pass


if __name__ == "__main__":
    while (True):
        input_request = input("What can I help you with? ")
        print(make_gemini_api_call(input_request))
