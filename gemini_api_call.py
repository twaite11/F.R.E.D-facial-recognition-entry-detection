from google import genai

GEMINI_MODEL = "gemini-2.5-flash"


def make_gemini_api_call(input_request: str) -> str:
    """Make API call to Gemini model.

    Args:
        input_request (str) The request to pass into the Gemini model.

    Returns:
        Gemini response.
    """
    client = genai.Client()

    input_request += "Make the response of this seem as though it was spoken by a human and not AI. Also please keep your response brief."

    response = client.models.generate_content(
        model=GEMINI_MODEL, contents=input_request
    )

    return response.text


if __name__ == "__main__":
    input_request = input("Enter your request: ")

    print(make_gemini_api_call(input_request))
