import os
import time
from openai import OpenAI, OpenAIError, RateLimitError, APIConnectionError

HF_TOKEN = os.getenv("api_key", "")
if not HF_TOKEN:
    raise RuntimeError("Missing the API KEY for ChatGPT. Set environment variable 'api_key'.")


client = OpenAI(api_key=HF_TOKEN)

def safe_text_request(prompt: str, model: str, retries: int = 3):
    '''
    A function that generate a safe text request for the chat model.
    :param prompt - str - The given prompt to the model
    :param model - str - The current model we are using to generate the text
    :param retries - str - The amount of retries it tries to do before failing
    '''
    last_err = None
    for attempt in range(1, retries + 1):
        try:
            return client.responses.create(
                model=model,
                input=prompt,
                instructions="Return ONLY valid JSON matching the schema.",
                max_output_tokens=900,
                text={"format": {"type": "json_object"}},
            )
        except RateLimitError as e:
            last_err = e
            wait = attempt * 2
            print(f"Rate limit hit, retrying in {wait}s...")
            time.sleep(wait)
        except APIConnectionError as e:
            last_err = e
            print("Connection issue, retrying...")
            time.sleep(2)
        except OpenAIError as e:
            print(f"OpenAI error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    print(f"Failed after retries. Last error: {last_err}")
    return None


def safe_image_request(prompt: str, retries: int = 3):
    last_err = None
    for attempt in range(1, retries + 1):
        try:
            return client.images.generate(
                model="dall-e-2",
                prompt=prompt,
                size="1024x1024",
                response_format="b64_json",
            )
        except RateLimitError as e:
            last_err = e
            wait = attempt * 2
            print(f"Rate limit on image gen, retrying in {wait}s...")
            time.sleep(wait)
        except APIConnectionError as e:
            last_err = e
            print("Connection issue on image gen, retrying...")
            time.sleep(2)
        except OpenAIError as e:
            print(f"OpenAI image error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected image error: {e}")
            return None

    print(f"Image gen failed after retries. Last error: {last_err}")
    return None
