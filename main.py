import json
import time
from dotenv import dotenv_values
from src.chatgpt_api import ChatGPTRequest
from openai import RateLimitError
from json import JSONDecodeError
from src.json_processor import JsonProcessor

# -------------------------------------------------------Constants------------------------------------------------
API_KEY_DICT = dotenv_values("config/.env")
SEPARATOR = "-----------------------------------------------------------------"

# Todo: More transactions can be added here.
# Todo: Alternatively an external file can be used
transactions = [
    'https://polygonscan.com/tx/0x10f2c28f5d6cd8d7b56210b4d5e0cece27e45a30808cd3d3443c05d4275bb008',
    'https://polygonscan.com/tx/0x8bfe32956f2bf6701819a06370dba35c908b37ab047c37efd9d328d48067387a',
    'https://polygonscan.com/tx/0x9d2fe2510b86537ba7c90c3a69b553c2768e20711a8ef8c7e8053f677fea7a3c'
]

GPT_PROMPT = """
Analyze the following URL Link:
{url}
What security related values can you extract from here.
Please provide me the results in a JSON structured format.
"""


# -------------------------------------------------------Constants------------------------------------------------


def main():
    transaction_index = 0
    json_processor = JsonProcessor()
    while transaction_index < len(transactions):
        try:
            chat_gpt_request = ChatGPTRequest(list(), str(API_KEY_DICT["OPEN_AI_KEY"]))
            gpt_response = chat_gpt_request.get_single_completion(
                GPT_PROMPT.format(url=transactions[transaction_index]))
            json_processor.update_json_db(json.loads(gpt_response))
            transaction_index += 1

        except JSONDecodeError as e:
            print(e)
            print(f"Log with index {transaction_index} has a json syntax error, skipped.")
            transaction_index += 1
            continue

        except RateLimitError as e:
            print(e)
            print(f"Transaction Number Failed:{transactions[transaction_index]}")
            time.sleep(60)
            continue

    json_processor.create_json_file()
    print("Done".center(100, "-"))


if __name__ == "__main__":
    main()
