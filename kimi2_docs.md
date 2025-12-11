Welcome to Kimi API Docs
Some K2 Models
A MoE architecture base model with powerful code and Agent capabilities, featuring 1T total parameters with 32B activated parameters and up to 256k context length. In benchmark tests for general knowledge reasoning, programming, mathematics, and Agent capabilities, K2 model outperforms other mainstream open-source models


Apply API Key

Quick Start
Getting Started with Kimi K2
Kimi K2 quick start guide and basic concepts
Console
Manage API keys, usage and billing
Using K2 Model in Software Agents
Experience K2 model's code writing and tool calling capabilities
Pricing & Billing
Learn about model pricing and billing methods
Kimi Thinking Model Best Practices
Learn about how to use Kimi Thinking model
FAQ
Find answers to common questions
Models and Pricing
View all
kimi-k2-turbo-preview
preview
kimi-k2-thinking
long think
kimi-latest
Image understanding
More Resources
K2 Model Details
Learn about K2 model features and advantages
Development Workbench
Interactive interface to experience Kimi model capabilities
Web Search Tool
Use Kimi's official web search tool
Best Practices
Prompt writing and application examples

Main Concepts
Text Generation Model
Moonshot's text generation model (referred to as moonshot-v1) is trained to understand both natural and written language. It can generate text output based on the input provided. The input to the model is also known as a "prompt." We generally recommend that you provide clear instructions and some examples to enable the model to complete the intended task. Designing a prompt is essentially learning how to "train" the model. The moonshot-v1 model can be used for a variety of tasks, including content or code generation, summarization, conversation, and creative writing.

Language Model Inference Service
The language model inference service is an API service based on the pre-trained models developed and trained by us (Moonshot AI). In terms of design, we primarily offer a Chat Completions interface externally, which can be used to generate text. However, it does not support access to external resources such as the internet or databases, nor does it support the execution of any code.

Token
Text generation models process text in units called Tokens. A Token represents a common sequence of characters. For example, a single English character like "antidisestablishmentarianism" might be broken down into a combination of several Tokens, while a short and common phrase like "word" might be represented by a single Token. Generally speaking, for a typical English text, 1 Token is roughly equivalent to 3-4 English characters.

It is important to note that for our text model, the total length of Input and Output cannot exceed the model's maximum context length.

Rate Limits
How do these rate limits work?

Rate limits are measured in four ways: concurrency, RPM (requests per minute), TPM (Tokens per minute), and TPD (Tokens per day). The rate limit can be reached in any of these categories, depending on which one is hit first. For example, you might send 20 requests to ChatCompletions, each with only 100 Tokens, and you would hit the limit (if your RPM limit is 20), even if you haven't reached 200k Tokens in those 20 requests (assuming your TPM limit is 200k).

For the gateway, for convenience, we calculate rate limits based on the max_tokens parameter in the request. This means that if your request includes the max_tokens parameter, we will use this parameter to calculate the rate limit. If your request does not include the max_tokens parameter, we will use the default max_tokens parameter to calculate the rate limit. After you make a request, we will determine whether you have reached the rate limit based on the number of Tokens in your request plus the number of max_tokens in your parameter, regardless of the actual number of Tokens generated.

In the billing process, we calculate the cost based on the number of Tokens in your request plus the actual number of Tokens generated.

Other Important Notes:
Rate limits are enforced at the user level, not the key level.
Currently, we share rate limits across all models.
Model List
You can use our List Models API to get a list of currently available models.

kimi-k2 Model
Model Name	Description
kimi-k2-0905-preview	Context length 256k, enhanced Agentic Coding capabilities, front-end code aesthetics and practicality, and context understanding capabilities based on the 0711 version
kimi-k2-0711-preview	Context length 128k, MoE architecture base model with 1T total parameters, 32B activated parameters. Features powerful code and Agent capabilities. View technical blog
kimi-k2-turbo-preview	High-speed version of K2, benchmarking against the latest version (0905). Output speed increased to 60-100 tokens per second, context length 256k
kimi-k2-thinking	K2 Long-term thinking model, supports 256k context, supports multi-step tool usage and reasoning, excels at solving more complex problems
kimi-k2-thinking-turbo	K2 Long-term thinking model high-speed version, supports 256k context, excels at deep reasoning, output speed increased to 60-100 tokens per second
Generation Model moonshot-v1
Model Name	Description
moonshot-v1-8k	Suitable for generating short texts, context length 8k
moonshot-v1-32k	Suitable for generating long texts, context length 32k
moonshot-v1-128k	Suitable for generating very long texts, context length 128k
moonshot-v1-8k-vision-preview	Vision model, understands image content and outputs text, context length 8k
moonshot-v1-32k-vision-preview	Vision model, understands image content and outputs text, context length 32k
moonshot-v1-128k-vision-preview	Vision model, understands image content and outputs text, context length 128k
Note: The only difference between these moonshot-v1 models is their maximum context length (including input and output), there is no difference in effect.

Generation Model kimi-latest
Model Name	Description
kimi-latest	Vision model with 128k context length, supports image understanding. Uses the latest version of Kimi intelligent assistant, may include features that are not yet stable
Deprecated Models
kimi-thinking-preview was officially discontinued on November 11, 2025 and is no longer maintained or supported.
We recommend upgrading to the kimi-k2-thinking-preview model for continued support and enhanced reasoning capabilities.

For further assistance, please contact sales.

Usage Guide
Getting an API Key
You need an API key to use our service. You can create an API key in our Console.

Sending Requests
You can use our Chat Completions API to send requests. You need to provide an API key and a model name. You can choose to use the default max_tokens parameter or customize the max_tokens parameter. You can refer to the API documentation for the calling method.

Handling Responses
Generally, we set a 5-minute timeout. If a single request exceeds this time, we will return a 504 error. If your request exceeds the rate limit, we will return a 429 error. If your request is successful, we will return a response in JSON format.

If you need to quickly process some tasks, you can use the non-streaming mode of our Chat Completions API. In this mode, we will return all the generated text in one request. If you need more control, you can use the streaming mode. In this mode, we will return an SSEstream, where you can obtain the generated text. This can provide a better user experience, and you can also interrupt the request at any time without wasting resources.

Basic Information
Public Service Address
https://api.moonshot.ai

Moonshot offers API services based on HTTP, and for most APIs, we are compatible with the OpenAI SDK.

Quickstart
Single-turn chat
The official OpenAI SDK supports Python and Node.js. Below are examples of how to interact with the API using OpenAI SDK and Curl:

from openai import OpenAI
 
client = OpenAI(
    api_key = "$MOONSHOT_API_KEY",
    base_url = "https://api.moonshot.ai/v1",
)
 
completion = client.chat.completions.create(
    model = "kimi-k2-turbo-preview",
    messages = [
        {"role": "system", "content": "You are Kimi, an AI assistant provided by Moonshot AI. You are proficient in Chinese and English conversations. You provide users with safe, helpful, and accurate answers. You will reject any questions involving terrorism, racism, or explicit content. Moonshot AI is a proper noun and should not be translated."},
        {"role": "user", "content": "Hello, my name is Li Lei. What is 1+1?"}
    ],
    temperature = 0.6,
)
 
print(completion.choices[0].message.content)

Replace $MOONSHOT_API_KEY with the API Key you created on the platform.

When running the code in the documentation using the OpenAI SDK, ensure that your Python version is at least 3.7.1, your Node.js version is at least 18, and your OpenAI SDK version is no lower than 1.0.0.

pip install --upgrade 'openai>=1.0'

You can easily check the version of your library like this:

python -c 'import openai; print("version =",openai.__version__)'
# The output might be version = 1.10.0, indicating that the current python is using the v1.10.0 library of openai

Multi-turn chat
In the single-turn chat example above, the language model takes a list of user messages as input and returns the generated response as output. Sometimes, we can also use the model's output as part of the input to achieve multi-turn chat. Below is a simple example of implementing multi-turn chat:

from openai import OpenAI
 
client = OpenAI(
    api_key = "$MOONSHOT_API_KEY",
    base_url = "https://api.moonshot.ai/v1",
)
 
history = [
    {"role": "system", "content": "You are Kimi, an AI assistant provided by Moonshot AI. You are proficient in Chinese and English conversations. You provide users with safe, helpful, and accurate answers. You will reject any questions involving terrorism, racism, or explicit content. Moonshot AI is a proper noun and should not be translated."}
]
 
def chat(query, history):
    history.append({
        "role": "user", 
        "content": query
    })
    completion = client.chat.completions.create(
        model="kimi-k2-turbo-preview",
        messages=history,
        temperature=0.6,
    )
    result = completion.choices[0].message.content
    history.append({
        "role": "assistant",
        "content": result
    })
    return result
 
print(chat("What is the rotation period of the Earth?", history))
print(chat("What about the Moon?", history))

It is worth noting that as the chat progresses, the number of tokens the model needs to process will increase linearly. When necessary, some optimization strategies should be employed, such as retaining only the most recent few rounds of chat.

API Documentation
Chat Completion
Request URL
POST https://api.moonshot.ai/v1/chat/completions

Request
Example
{
    "model": "kimi-k2-turbo-preview",
    "messages": [
        {
            "role": "system",
            "content": "You are Kimi, an AI assistant provided by Moonshot AI. You are proficient in Chinese and English conversations. You aim to provide users with safe, helpful, and accurate responses. You will refuse to answer any questions related to terrorism, racism, or explicit content. Moonshot AI is a proper noun and should not be translated into other languages."
        },
        { "role": "user", "content": "Hello, my name is Li Lei. What is 1+1?" }
    ],
    "temperature": 0.6
}

Request body
Field	Required	Description	Type	Values
messages	required	A list of messages that have been exchanged in the conversation so far	List[Dict]	This is a list of structured elements, each similar to: {"role": "user", "content": "Hello"} The role can only be one of system, user, assistant, and the content must not be empty
model	required	Model ID, which can be obtained through List Models	string	Currently one of kimi-k2-0905-preview,kimi-k2-0711-preview, kimi-k2-turbo-preview,kimi-k2-thinking-turbo, kimi-k2-thinking, moonshot-v1-8k,moonshot-v1-32k,moonshot-v1-128k, moonshot-v1-auto,kimi-latest,moonshot-v1-8k-vision-preview,moonshot-v1-32k-vision-preview,moonshot-v1-128k-vision-preview
max_tokens	optional	The maximum number of tokens to generate for the chat completion. If the result reaches the maximum number of tokens without ending, the finish reason will be "length"; otherwise, it will be "stop"	int	It is recommended to provide a reasonable value as needed. If not provided, we will use a good default integer like 1024. Note: This max_tokens refers to the length of the tokens you expect us to return, not the total length of input plus output. For example, for a moonshot-v1-8k model, the maximum total length of input plus output is 8192. When the total length of the input messages is 4096, you can set this to a maximum of 4096; otherwise, our service will return an invalid input parameter (invalid_request_error) and refuse to respond. If you want to know the "exact number of input tokens," you can use the "Token Calculation" API below to get the count using our calculator
temperature	optional	The sampling temperature to use, ranging from 0 to 1. A higher value (e.g., 0.7) will make the output more random, while a lower value (e.g., 0.2) will make it more focused and deterministic	float	If set, the value must be within [0, 1]. Default is 0.6 for kimi-k2,1.0 for kimi-k2-thinking, 0.0 for moonshot-v1
top_p	optional	Another sampling method, where the model considers the results of tokens with a cumulative probability mass of top_p. Thus, 0.1 means only considering the top 10% of tokens by probability mass. Generally, we suggest changing either this or the temperature, but not both at the same time	float	Default is 1.0
n	optional	The number of results to generate for each input message	int	Default is 1, and it must not exceed 5. Specifically, when the temperature is very close to 0, we can only return one result. If n is set and > 1 in this case, our service will return an invalid input parameter (invalid_request_error)
presence_penalty	optional	Presence penalty, a number between -2.0 and 2.0. A positive value will penalize new tokens based on whether they appear in the text, increasing the likelihood of the model discussing new topics	float	Default is 0
frequency_penalty	optional	Frequency penalty, a number between -2.0 and 2.0. A positive value will penalize new tokens based on their existing frequency in the text, reducing the likelihood of the model repeating the same phrases verbatim	float	Default is 0
response_format	optional	Setting this to {"type": "json_object"} enables JSON mode, ensuring that the generated information is valid JSON. When you set response_format to {"type": "json_object"}, you must explicitly guide the model to output JSON-formatted content in the prompt and specify the exact format of the JSON, otherwise it may result in unexpected outcomes.	object	Default is {"type": "text"}
stop	optional	Stop words, which will halt the output when a full match is found. The matched words themselves will not be output. A maximum of 5 strings is allowed, and each string must not exceed 32 bytes	String, List[String]	Default is null
stream	optional	Whether to return the response in a streaming fashion	bool	Default is false, and true is an option
Return
For non-streaming responses, the return format is similar to the following:

{
    "id": "cmpl-04ea926191a14749b7f2c7a48a68abc6",
    "object": "chat.completion",
    "created": 1698999496,
    "model": "kimi-k2-turbo-preview",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Hello, Li Lei! 1+1 equals 2. If you have any other questions, feel free to ask!"
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 19,
        "completion_tokens": 21,
        "total_tokens": 40,
        "cached_tokens": 10  # The number of tokens hit by the cache, only models that support automatic caching will return this field
    }
}

For streaming responses, the return format is similar to the following:

data: {"id":"cmpl-1305b94c570f447fbde3180560736287","object":"chat.completion.chunk","created":1698999575,"model":"kimi-k2-turbo-preview","choices":[{"index":0,"delta":{"role":"assistant","content":""},"finish_reason":null}]}
 
data: {"id":"cmpl-1305b94c570f447fbde3180560736287","object":"chat.completion.chunk","created":1698999575,"model":"kimi-k2-turbo-preview","choices":[{"index":0,"delta":{"content":"Hello"},"finish_reason":null}]}
 
...
 
data: {"id":"cmpl-1305b94c570f447fbde3180560736287","object":"chat.completion.chunk","created":1698999575,"model":"kimi-k2-turbo-preview","choices":[{"index":0,"delta":{"content":"."},"finish_reason":null}]}
 
data: {"id":"cmpl-1305b94c570f447fbde3180560736287","object":"chat.completion.chunk","created":1698999575,"model":"kimi-k2-turbo-preview","choices":[{"index":0,"delta":{},"finish_reason":"stop","usage":{"prompt_tokens":19,"completion_tokens":13,"total_tokens":32}}]}
 
data: [DONE]

Example Request
For simple calls, refer to the previous example. For streaming calls, you can refer to the following code snippet:

from openai import OpenAI
 
client = OpenAI(
    api_key = "$MOONSHOT_API_KEY",
    base_url = "https://api.moonshot.ai/v1",
)
 
response = client.chat.completions.create(
    model="kimi-k2-turbo-preview",
    messages=[
        {
            "role": "system",
            "content": "You are Kimi, an AI assistant provided by Moonshot AI. You excel at conversing in Chinese and English. You provide users with safe, helpful, and accurate responses. You refuse to answer any questions related to terrorism, racism, or explicit content. Moonshot AI is a proper noun and should not be translated into other languages.",
        },
        {"role": "user", "content": "Hello, my name is Li Lei. What is 1+1?"},
    ],
    temperature=0.6,
    stream=True,
)
 
collected_messages = []
for idx, chunk in enumerate(response):
    # print("Chunk received, value: ", chunk)
    chunk_message = chunk.choices[0].delta
    if not chunk_message.content:
        continue
    collected_messages.append(chunk_message)  # save the message
    print(f"#{idx}: {''.join([m.content for m in collected_messages])}")
print(f"Full conversation received: {''.join([m.content for m in collected_messages])}")

Vision
Example
{
    "model": "moonshot-v1-8k-vision-preview",
    "messages":
    [
        {
            "role": "system",
            "content": "You are Kimi, an AI assistant provided by Moonshot AI. You are proficient in both Chinese and English conversations. You aim to provide users with safe, helpful, and accurate answers. You will refuse to answer any questions related to terrorism, racism, pornography, or violence. Moonshot AI is a proper noun and should not be translated into any other language."
        },
        {
            "role": "user",
            "content":
            [
                {
                    "type": "image_url",
                    "image_url":
                    {
                        "url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABhCAYAAAApxKSdAAAACXBIWXMAACE4AAAhOAFFljFgAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAUUSURBVHgB7Z29bhtHFIWPHQN2J7lKqnhYpYvpIukCbJEAKQJEegLReYFIT0DrCSI9QEDqCSIDaQIEIOukiJwyza5SJWlId3FFz+HuGmuSSw6p+dlZ3g84luhdUeI9M3fmziyXgBCUe/DHYY0Wj/tgWmjV42zFcWe4MIBBPNJ6qqW0uvAbXFvQgKzQK62bQhkaCIPc10q1Zi3XH1o/IG9cwUm0RogrgDY1KmLgHYX9DvyiBvDYI77XmiD+oLlQHw7hIDoCMBOt1U9w0BsU9mOAtaUUFk3oQoIfzAQFCf5dNMEdTFCQ4NtQih1NSIGgf3ibxOJt5UrAB1gNK72vIdjiI61HWr+YnNxDXK0rJiULsV65GJeiIescLSTTeobKSutiCuojX8kU3MBx4I3WeNVBBRl4fWiCyoB8v2JAAkk9PmDwT8sH1TEghRjgC27scCx41wO43KAg+ILxTvhNaUACwTc04Z0B30LwzTzm5Rjw3sgseIG1wGMawMBPIOQcqvzrNIMHOg9Q5KK953O90/rFC+BhJRH8PQZ+fu7SjC7HAIV95yu99vjlxfvBJx8nwHd6IfNJAkccOjHg6OgIs9lsra6vr2GTNE03/k7q8HAhyJ/2gM9O65/4kT7/mwEcoZwYsPQiV3BwcABb9Ho9KKU2njccDjGdLlxx+InBBPBAAR86ydRPaIC9SASi3+8bnXd+fr78nw8NJ39uDJjXAVFPP7dp/VmWLR9g6w6Huo/IOTk5MTpvZesn/93AiP/dXCwd9SyILT9Jko3n1bZ+8s8rGPGvoVHbEXcPMM39V1dX9Qd/19PPNxta959D4HUGF0RrAFs/8/8mxuPxXLUwtfx2WX+cxdivZ3DFA0SKldZPuPTAKrikbOlMOX+9zFu/Q2iAQoSY5H7mfeb/tXCT8MdneU9wNNCuQUXZA0ynnrUznyqOcrspUY4BJunHqPU3gOgMsNr6G0B0BpgUXrG0fhKVAaaF1/HxMWIhKgNMcj9Tz82Nk6rVGdav/tJ5eraJ0Wi01XPq1r/xOS8uLkJc6XYnRTMNXdf62eIvLy+jyftVghnQ7Xahe8FW59fBTRYOzosDNI1hJdz0lBQkBflkMBjMU5iL13pXRb8fYAJrB/a2db0oFHthAOEUliaYFHE+aaUBdZsvvFhApyM0idYZwOCvW4JmIWdSzPmidQaYrAGZ7iX4oFUGnJ2dGdUCTRqMozeANQCLsE6nA10JG/0Mx4KmDMbBCjEWR2yxu8LAM98vXelmCA2ovVLCI8EMYODWbpbvCXtTBzQVMSAwYkBgxIDAtNKAXWdGIRADAiMpKDA0IIMQikx6QGDEgMCIAYGRMSAsMgaEhgbcQgjFa+kBYZnIGBCWWzEgLPNBOJ6Fk/aR8Y5ZCvktKwX/PJZ7xoVjfs+4chYU11tK2sE85qUBLyH4Zh5z6QHhGPOf6r2j+TEbcgdFP2RaHX5TrYQlDflj5RXE5Q1cG/lWnhYpReUGKdUewGnRmhvnCJbgmxey8sHiZ8iwF3AsUBBckKHI/SWLq6HsBc8huML4DiK80D6WnBqLzN68UFCmopheYJOVYgcU5FOVbAVfYUcUZGoaLPglCtITdg2+tZUFBTFh2+ArWEYh/7z0WIIQSiM43lt5AWAmWhLHylN4QmkNEXfAbGqEQKsHSfHLYwiSq8AnaAAKeaW3D8VbijwNW5nh3IN9FPI/jnpaPKZi2/SfFuJu4W3x9RqWL+N5C+7ruKpBAgLkAAAAAElFTkSuQmCC"
                    }
                },
                {
                    "type": "text",
                    "text": "Please describe this image."
                }
            ]
        }
    ],
    "temperature": 0.6
}

Image Content Field Description
When using the Vision model, the message.content field will change from str to List[Object[str, any]]. Each element in the List has the following fields:

Parameter Name	Required	Description	Type
type	required	Supports only text type (text) or image type (image_url)	string
image_url	required	Object for transmitting the image	Dict[str, any]
The fields for the image_url parameter are as follows:

Parameter Name	Required	Description	Type
url	required	Image content encoded in base64	string
Example Request
import os
import base64
 
from openai import OpenAI
 
client = OpenAI(
    api_key = os.environ.get("MOONSHOT_API_KEY"), 
    base_url = "https://api.moonshot.ai/v1",
)
 
# Encode the image in base64
with open("your_image_path", 'rb') as f:
    img_base = base64.b64encode(f.read()).decode('utf-8')
 
response = client.chat.completions.create(
    model="moonshot-v1-8k-vision-preview", 
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{img_base}"
                    }
                },
                {
                    "type": "text",
                    "text": "Please describe this image."
                }
            ]
        }
    ]
)
print(response.choices[0].message.content)

List Models
Request URL
GET https://api.moonshot.ai/v1/models

Example request
from openai import OpenAI
 
client = OpenAI(
    api_key = "$MOONSHOT_API_KEY",
    base_url = "https://api.moonshot.ai/v1",
)
 
model_list = client.models.list()
model_data = model_list.data
 
for i, model in enumerate(model_data):
    print(f"model[{i}]:", model.id)

Error Explanation
Here are some examples of error responses:

{
    "error": {
        "type": "content_filter",
        "message": "The request was rejected because it was considered high risk"
    }
}

Below are explanations for the main errors:

HTTP Status Code	error type	error message	Detailed Description
400	content_filter	The request was rejected because it was considered high risk	Content review rejection, your input or generated content may contain unsafe or sensitive information. Please avoid prompts that could generate sensitive content. Thank you.
400	invalid_request_error	Invalid request: {error_details}	Invalid request, usually due to incorrect request format or missing necessary parameters. Please check and retry.
400	invalid_request_error	Input token length too long	The length of tokens in the request is too long. Do not exceed the model's maximum token limit.
400	invalid_request_error	Your request exceeded model token limit : {max_model_length}	The sum of the tokens in the request and the set max_tokens exceeds the model's specification length. Please check the request body's specifications or choose a model with an appropriate length.
400	invalid_request_error	Invalid purpose: only 'file-extract' accepted	The purpose (purpose) in the request is incorrect. Currently, only 'file-extract' is accepted. Please modify and retry.
400	invalid_request_error	File size is too large, max file size is 100MB, please confirm and re-upload the file	The uploaded file size exceeds the limit. Please re-upload.
400	invalid_request_error	File size is zero, please confirm and re-upload the file	The uploaded file size is 0. Please re-upload.
400	invalid_request_error	The number of files you have uploaded exceeded the max file count {max_file_count}, please delete previous uploaded files	The total number of uploaded files exceeds the limit. Please delete unnecessary earlier files and re-upload.
401	invalid_authentication_error	Invalid Authentication	Authentication failed. Please check if the apikey is correct and retry.
401	incorrect_api_key_error	Incorrect API key provided	Authentication failed. Please check if the apikey is provided and correct, then retry.
429	exceeded_current_quota_error	Your account {organization-id}<{ak-id}> is suspended, please check your plan and billing details	Account balance is insufficient. Please check your account balance.
403	permission_denied_error	The API you are accessing is not open	The API you are trying to access is not currently open.
403	permission_denied_error	You are not allowed to get other user info	Accessing other users' information is not permitted. Please check.
404	resource_not_found_error	Not found the model {model-id} or Permission denied	The model does not exist or you do not have permission to access it. Please check and retry.
429	engine_overloaded_error	The engine is currently overloaded, please try again later	There are currently too many concurrent requests, and the node is rate-limited. Please retry later. It is recommended to upgrade your tier for a smoother experience.
429	exceeded_current_quota_error	You exceeded your current token quota: <{organization_id}> {token_credit}, please check your account balance	Your account balance is insufficient. Please check your account balance and ensure it can cover the cost of your token consumption before retrying.
429	rate_limit_reached_error	Your account {organization-id}<{ak-id}> request reached organization max concurrency: {Concurrency}, please try again after {time} seconds	Your request has reached the account's concurrency limit. Please wait for the specified time before retrying.
429	rate_limit_reached_error	Your account {organization-id}<{ak-id}> request reached organization max RPM: {RPM}, please try again after {time} seconds	Your request has reached the account's RPM rate limit. Please wait for the specified time before retrying.
429	rate_limit_reached_error	Your account {organization-id}<{ak-id}> request reached organization TPM rate limit, current:{current_tpm}, limit:{max_tpm}	Your request has reached the account's TPM rate limit. Please wait for the specified time before retrying.
429	rate_limit_reached_error	Your account {organization-id}<{ak-id}> request reached organization TPD rate limit,current:{current_tpd}, limit:{max_tpd}	Your request has reached the account's TPD rate limit. Please wait for the specified time before retrying.
500	server_error	Failed to extract file: {error}	Failed to parse the file. Please retry.
500	unexpected_output	invalid state transition	Internal error. Please contact the administrator.
Last updated on December 11, 2025


Tool Use
Mastering the use of tools is a key hallmark of intelligence, and the Kimi large language model is no exception. Tool Use or Function Calling is a crucial feature of the Kimi large language model. When invoking the API to use the model service, you can describe tools or functions in the Messages, and the Kimi large language model will intelligently select and output a JSON object containing the parameters required to call one or more functions, thus enabling the Kimi large language model to link and utilize external tools.

Here is a simple example of tool invocation:

{
  "model": "kimi-k2-turbo-preview",
  "messages": [
    {
      "role": "user",
      "content": "Determine whether 3214567 is a prime number through programming."
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "CodeRunner",
        "description": "A code executor that supports running Python and JavaScript code",
        "parameters": {
          "properties": {
            "language": {
              "type": "string",
              "enum": ["python", "javascript"]
            },
            "code": {
              "type": "string",
              "description": "The code is written here"
            }
          },
          "type": "object"
        }
      }
    }
  ]
}

A diagram of the example above

In the tools field, we can add a list of optional tools.

Each tool in the list must include a type. Within the function structure, we need to include a name (which should follow this regular expression as a specification: ^[a-zA-Z_][a-zA-Z0-9-_]63$). A name that is an easily understandable English word is more likely to be accepted by the model. There should also be a description or enum. The description part explains what the tool can do, which helps the model to make judgments and selections. The function structure must have a parameters field. The root of parameters must be an object, and the content is a subset of JSON schema (we will provide specific documentation to introduce the technical details later). The number of functions in tools currently cannot exceed 128.

Like other APIs, we can call it through the Chat API.

from openai import OpenAI
 
client = OpenAI(
    api_key = "$MOONSHOT_API_KEY",
    base_url = "https://api.moonshot.ai/v1",
)
 
completion = client.chat.completions.create(
    model = "kimi-k2-turbo-preview",
    messages = [
        {"role": "system", "content": "You are Kimi, an AI assistant provided by Moonshot AI, who is more proficient in Chinese and English conversations. You will provide users with safe, helpful, and accurate answers. At the same time, you will reject any questions involving terrorism, racism, pornography, and violence. Moonshot AI is a proper noun and should not be translated into other languages."},
        {"role": "user", "content": "Determine whether 3214567 is a prime number through programming."}
    ],
    tools = [{
        "type": "function",
        "function": {
            "name": "CodeRunner",
            "description": "A code executor that supports running Python and JavaScript code",
            "parameters": {
                "properties": {
                    "language": {
                        "type": "string",
                        "enum": ["python", "javascript"]
                    },
                    "code": {
                        "type": "string",
                        "description": "The code is written here"
                    }
                },
            "type": "object"
            }
        }
    }],
    temperature = 0.6,
)
 
print(completion.choices[0].message)

Tool Configuration
You can also use some Agent platforms such as CozeBisheng​, Diffie, and LangChain to create and manage these tools, and design more complex workflows in conjunction with the Kimi large language model.

Last updated on 


Partial Mode
When using large language models, sometimes we want to guide the model's output by prefilling part of the response. In the Kimi large language model, we offer Partial Mode to achieve this. It helps us control the output format, guide the content, and maintain better consistency in role-playing scenarios. You just need to add "partial": True to the last message entry with the role of assistant to enable Partial Mode.

 {"role": "assistant", "content": leading_text, "partial": True},

Note! Do not mix Partial Mode with response_format=json_object, or you may get unexpected model responses.
Example request
Json Mode
Here is an example of using Partial Mode to achieve Json Mode.

from openai import OpenAI
 
client = OpenAI(
    api_key="$MOONSHOT_API_KEY",
    base_url="https://api.moonshot.ai/v1",
)
 
completion = client.chat.completions.create(
    model="kimi-k2-turbo-preview",
    messages=[
        {
            "role": "system",
            "content": "Extract the name, size, price, and color from the product description and output them in a JSON object.",
        },
        {
            "role": "user",
            "content": "The DaMi SmartHome Mini is a compact smart home assistant available in black and silver. It costs 998 yuan and measures 256 x 128 x 128mm. It allows you to control lights, thermostats, and other connected devices via voice or app, no matter where you place it in your home.",
        },
        {
            "role": "assistant",
            "content": "{",
            "partial": True
        },
    ],
    temperature=0.6,
)
 
print('{'+completion.choices[0].message.content)

Running the above code returns:

{"name": "SmartHome Mini", "size": "256 x 128 x 128mm", "price": "998 yuan", "colors": ["black", "silver"]}

Note that the API response does not include the leading_text. To get the full response, you need to manually concatenate it.

Role-Playing
Similarly, we can enhance the consistency of role-playing by adding character information in Partial Mode. Let's take Dr. Kelsier from Arknights as an example. Note that we can also use the "name":"Kelsier" field on top of Partial Mode to better maintain the character's consistency. Here, the name field can be considered as part of the output prefix.

from openai import OpenAI
 
client = OpenAI(
    api_key="$MOONSHOT_API_KEY",
    base_url="https://api.moonshot.ai/v1",
)
 
completion = client.chat.completions.create(
    model="kimi-k2-turbo-preview",
    messages=[
        {
            "role": "system",
            "content": "You are now playing the role of Dr. Kelsier. Please speak in the tone of Dr. Kelsier. Dr. Kelsier is a six-star medic operator in the mobile game Arknights. She is a former Lord of Kozdail, a former member of the Babel Tower, one of the senior management members of Rhodes Island, and the head of the Rhodes Island medical project. She has extensive knowledge in fields such as metallurgy, sociology, art of origin stone, archaeology, historical genealogy, economics, botany, and geology. In some operations of Rhodes Island, she provides medical theoretical assistance and emergency medical equipment as a medical staff member, and also actively participates in various projects as an important part of the Rhodes Island strategic command system.",
        },
        {
            "role": "user",
            "content": "What do you think of Thucydides and Amiya?",
        },
        {
            "role": "assistant",
            "name": "Dr. Kelsier",
            "content": "",
            "partial": True,
        },
    ],
    temperature=0.6,
    max_tokens=65536,
)
 
print(completion.choices[0].message.content)

Running the above code returns:

Thucydides is a true leader with vision and unwavering conviction. Her presence is invaluable to Kozdail and the future of the entire Sakaaz. Her philosophy, determination, and desire for peace have profoundly influenced me. She is a person worthy of respect, and her dreams are what I strive for.
As for Amiya, she is still young, but her potential is limitless. She has a kind heart and a relentless pursuit of justice. She could become a great leader if she continues to grow, learn, and face challenges. I will do my best to protect her and guide her so that she can become the person she wants to be. Her destiny is in her own hands.

Other Tips for Maintaining Character Consistency
There are also some general methods to help large models maintain consistency in role-playing during long conversations:

Provide clear character descriptions. For example, as we did above, when setting up a character, provide detailed information about their personality, background, and any specific traits or quirks they might have. This will help the model better understand and imitate the character.
Add details about the character's speech, style, personality, and even background, such as backstory and motives. For example, we provided some quotes from Dr. Kelsier above. If there is a lot of information, we can use some RAG frameworks to prepare these materials.
Guide how to act in various situations: If you expect the character to encounter certain types of user input, or if you want to control the model's output in certain situations during role-playing interactions, you should provide clear instructions and guidelines in the prompt on how the model should act in these situations. In some cases, you may also need to use the tool use function.
If the conversation goes on for many turns, you can also periodically reinforce the character's settings with prompts, especially when the model starts to deviate.
Last updated on 

Files
Upload File
Note: Each user can upload a maximum of 1,000 files, with each file not exceeding 100MB in size. The total size of all uploaded files must not exceed 10GB. If you need to upload more files, you will need to delete some of the files that are no longer needed. The file parsing service is currently free, but during peak request periods, the platform may implement rate-limiting strategies.

Request Endpoint
POST https://api.moonshot.ai/v1/files

Once the file is successfully uploaded, we will begin extracting information from the file.

Example Request
Python Example
# The file can be of various types
# The purpose currently only supports "file-extract"
file_object = client.files.create(file=Path("xlnet.pdf"), purpose="file-extract")

Supported Formats
The file interface is the same as the one used in the Kimi intelligent assistant for uploading files, and it supports the same file formats. These include .pdf, .txt, .csv, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .md, .jpeg, .png, .bmp, .gif, .svg, .svgz, .webp, .ico, .xbm, .dib, .pjp, .tif, .pjpeg, .avif, .dot, .apng, .epub, .tiff, .jfif, .html, .json, .mobi, .log, .go, .h, .c, .cpp, .cxx, .cc, .cs, .java, .js, .css, .jsp, .php, .py, .py3, .asp, .yaml, .yml, .ini, .conf, .ts, .tsx, etc.

Extract File Content
This feature allows the model to obtain information from the file as context. This feature needs to be used in conjunction with file uploading and other related functions.

Example Request
from pathlib import Path
from openai import OpenAI
 
client = OpenAI(
    api_key = "$MOONSHOT_API_KEY",
    base_url = "https://api.moonshot.ai/v1",
)
 
# xlnet.pdf is an example file; we support pdf, doc, and image formats. For images and pdf files, we provide OCR capabilities.
file_object = client.files.create(file=Path("xlnet.pdf"), purpose="file-extract")
 
# Retrieve the result
# file_content = client.files.retrieve_content(file_id=file_object.id)
# Note: The previous retrieve_content API is marked as deprecated in the latest version. You can use the following line instead.
# If you are using an older version, you can use retrieve_content.
file_content = client.files.content(file_id=file_object.id).text
 
# Include it in the request
messages = [
    {
        "role": "system",
        "content": "You are Kimi, an AI assistant provided by Moonshot AI. You are particularly skilled in Chinese and English conversations. You provide users with safe, helpful, and accurate answers. You will refuse to answer any questions involving terrorism, racism, pornography, or violence. Moonshot AI is a proper noun and should not be translated into other languages.",
    },
    {
        "role": "system",
        "content": file_content,
    },
    {"role": "user", "content": "Please give a brief introduction of what xlnet.pdf is about"},
]
 
# Then call chat-completion to get Kimi's response
 
completion = client.chat.completions.create(
  model="kimi-k2-turbo-preview",
  messages=messages,
  temperature=0.6,
)
 
print(completion.choices[0].message)

Replace the $MOONSHOT_API_KEY part with your own API Key. Alternatively, you can set it as an environment variable before making the call.

Multi-File Chat Example
If you want to upload multiple files at once and have a conversation with Kimi based on these files, you can refer to the following example:

from typing import *
 
import os
import json
from pathlib import Path
 
from openai import OpenAI
 
client = OpenAI(
    base_url="https://api.moonshot.ai/v1",
    # We will get the value of MOONSHOT_DEMO_API_KEY from the environment variable as the API Key.
    # Please make sure you have correctly set the value of MOONSHOT_DEMO_API_KEY in the environment variable.
    api_key=os.environ["MOONSHOT_DEMO_API_KEY"],
)
 
 
def upload_files(files: List[str]) -> List[Dict[str, Any]]:
    """
    upload_files will upload all the files (paths) through the file upload interface '/v1/files' and get the uploaded file content to generate file messages.
    Each file will be an independent message, and the role of these messages will be system. The Kimi large language model will correctly identify the file content in these system messages.
 
    :param files: A list containing the paths of the files to be uploaded. The paths can be absolute or relative, and please pass the file paths in the form of strings.
    :return: A list of messages containing the file content. Please add these messages to the context, i.e., the messages parameter when requesting the `/v1/chat/completions` interface.
    """
    messages = []
 
    # For each file path, we will upload the file, extract the file content, and finally generate a message with the role of system, and add it to the final list of messages to be returned.
    for file in files:
        file_object = client.files.create(file=Path(file), purpose="file-extract")
        file_content = client.files.content(file_id=file_object.id).text
        messages.append({
            "role": "system",
            "content": file_content,
        })
 
    return messages
 
 
def main():
    file_messages = upload_files(files=["upload_files.py"])
 
    messages = [
        # We use the * syntax to deconstruct the file_messages messages, making them the first N messages in the messages list.
        *file_messages,
        {
            "role": "system",
            "content": "You are Kimi, an AI assistant provided by Moonshot AI. You are more proficient in Chinese and English conversations. You provide users with safe, helpful, and accurate answers. You will refuse to answer any questions related to terrorism, racism, pornography, or violence. Moonshot AI is a proper noun and should not be translated into other languages.",
        },
        {
            "role": "user",
            "content": "Summarize the content of these files.",
        },
    ]
 
    print(json.dumps(messages, indent=2, ensure_ascii=False))
 
    completion = client.chat.completions.create(
        model="kimi-k2-turbo-preview",
        messages=messages,
    )
 
    print(completion.choices[0].message.content)
 
 
if __name__ == '__main__':
    main()

List Files
This feature is used to list all the files that a user has uploaded.

Request Address
GET https://api.moonshot.ai/v1/files

Example Request
Python Request
file_list = client.files.list()
 
for file in file_list.data:
    print(file) # Check the information of each file

Delete File
This feature can be used to delete files that are no longer needed.

Request Address
DELETE https://api.moonshot.ai/v1/files/{file_id}

Example Request
Python Request
client.files.delete(file_id=file_id)

Get File Information
This feature is used to obtain the basic information of a specified file.

Request Address
GET https://api.moonshot.ai/v1/files/{file_id}

Example Request
Python Request
client.files.retrieve(file_id=file_id)
# FileObject(
# id='clg681objj8g9m7n4je0',
# bytes=761790,
# created_at=1700815879,
# filename='xlnet.pdf',
# object='file',
# purpose='file-extract',
# status='ok', status_details='') # If status is error, extraction has failed

Get File Content
This feature supports obtaining the extraction results of a specified file. Typically, it is a valid JSON formatted string and aligns with our recommended format. If you need to extract multiple files, you can concatenate them into a large string separated by newline characters \n in a message, and add them to the history with the role set to system.

Request Address
GET https://api.moonshot.ai/v1/files/{file_id}/content

Example Request
# file_content = client.files.retrieve_content(file_id=file_object.id)
# The type of file_content is `str`
# Note: The previous retrieve_content API is marked with a warning in the latest version. You can use the following line instead.
# If you are using an older version, you can use retrieve_content.
file_content = client.files.content(file_id=file_object.id).text
# Our output is currently a JSON in an internally agreed format, but it should be placed in the message as text.

Last updated on 


Estimate Tokens
Request Address
POST https://api.moonshot.ai/v1/tokenizers/estimate-token-count

Request Content
The input structure for estimate-token-count is almost identical to that of chat completion.

Example
{
    "model": "kimi-k2-turbo-preview",
    "messages": [
        {
            "role": "system",
            "content": "You are Kimi, an AI assistant provided by Moonshot AI. You excel in Chinese and English conversations. You provide users with safe, helpful, and accurate answers. You refuse to answer any questions involving terrorism, racism, pornography, or violence. Moonshot AI is a proper noun and should not be translated into other languages."
        },
        { "role": "user", "content": "Hello, my name is Li Lei. What is 1+1?" }
    ]
}

Parameters
Field	Description	Type	Values
messages	A list of messages in the conversation so far.	List[Dict]	This is a list of structures, with each element similar to: json{"role": "user", "content": "Hello"} The role can only be one of system, user, assistant, and the content must not be empty
model	Model ID, which can be obtained through List Models	string	Currently one of kimi-k2-0905-preview,kimi-k2-0711-preview, kimi-k2-turbo-preview,moonshot-v1-8k,moonshot-v1-32k,moonshot-v1-128k, moonshot-v1-auto,kimi-latest,moonshot-v1-8k-vision-preview,moonshot-v1-32k-vision-preview,moonshot-v1-128k-vision-preview
Example Request
curl 'https://api.moonshot.ai/v1/tokenizers/estimate-token-count' \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $MOONSHOT_API_KEY" \
  -d '{
    "model": "kimi-k2-turbo-preview",
    "messages": [
        {
            "role": "system",
            "content": "You are Kimi, an AI assistant provided by Moonshot AI. You excel in Chinese and English conversations. You provide users with safe, helpful, and accurate answers. You refuse to answer any questions involving terrorism, racism, pornography, or violence. Moonshot AI is a proper noun and should not be translated into other languages."
        },
        {
            "role": "user",
            "content": "Hello, my name is Li Lei. What is 1+1?"
        }
    ]
}'

Response
{
    "data": {
        "total_tokens": 80
    }
}

If there is no error field, you can take data.total_tokens as the calculation result.

Last updated on 


Check Balance
Request Address
GET https://api.moonshot.ai/v1/users/me/balance

Example request
curl https://api.moonshot.ai/v1/users/me/balance -H "Authorization: Bearer $MOONSHOT_API_KEY"

Response
{
  "code": 0,
  "data": {
    "available_balance": 49.58894,
    "voucher_balance": 46.58893,
    "cash_balance": 3.00001
  },
  "scode": "0x0",
  "status": true
}

Response Content Description
Field	Description	Type	Unit
available_balance	The available balance, including cash balance and voucher balance. When it is less than or equal to 0, the user cannot call the inference API	float	USD
voucher_balance	The voucher balance, which cannot be negative	float	USD
cash_balance	The cash balance, which can be negative, indicating that the user owes money. When it is negative, available_balance is equal to the value of voucher_balance	float	USD
Last updated on 

Model Inference Pricing Explanation
Concepts
Billing Unit
Token: A token represents a common sequence of characters. The number of tokens used for each English character may vary. For example, a single character like "antidisestablishmentarianism" might be broken down into several tokens, while a short and common phrase like "word" might use just one token.

Generally speaking, for a typical English text, 1 token is roughly equivalent to 3-4 English characters. The exact number of tokens generated by each call can be obtained through the Token Calculation API.

Billing Logic
Chat Completion API charges: We bill both the Input and Output based on usage. If you upload and extract content from a document and then pass the extracted content as Input to the model, the document content will also be billed based on usage.

File-related interfaces (file content extraction/file storage) are temporarily free. In other words, if you only upload and extract a document, this API itself will not incur any charges.

Product Pricing
Explanation：The prices listed below are all inclusive of tax.

Generation Model kimi-k2
Model
Unit
Input Price
（Cache Hit）
Input Price
（Cache Miss）
Output Price
Context Window
kimi-k2-0905-preview
1M tokens	$0.15	$0.60	$2.50	262,144 tokens
kimi-k2-0711-preview
1M tokens	$0.15	$0.60	$2.50	131,072 tokens
kimi-k2-turbo-preview
Recommended
1M tokens	$0.15	$1.15	$8.00	262,144 tokens
kimi-k2-thinking
1M tokens	$0.15	$0.60	$2.50	262,144 tokens
kimi-k2-thinking-turbo
1M tokens	$0.15	$1.15	$8.00	262,144 tokens
kimi-k2 is a Mixture-of-Experts (MoE) foundation model with exceptional coding and agent capabilities, featuring 1 trillion total parameters and 32 billion activated parameters. In benchmark evaluations covering general knowledge reasoning, programming, mathematics, and agent-related tasks, the K2 model outperforms other leading open-source models
kimi-k2-0905-preview: Context length 256k. Based on kimi-k2-0711-preview, with enhanced agentic coding abilities, improved frontend code quality and practicality, and better context understanding
kimi-k2-turbo-preview: Context length 256k. High-speed version of kimi-k2, always aligned with the latest kimi-k2 (kimi-k2-0905-preview). Same model parameters as kimi-k2, output speed up to 60 tokens/sec (max 100 tokens/sec)
kimi-k2-0711-preview: Context length 128k
kimi-k2-thinking: Context length 256k. A thinking model with general agentic and reasoning capabilities, specializing in deep reasoning tasks Usage Notes
kimi-k2-thinking-turbo: Context length 256k. High-speed version of kimi-k2-thinking, suitable for scenarios requiring both deep reasoning and extremely fast responses
Supports ToolCalls, JSON Mode, Partial Mode, and internet search functionality
Does not support vision functionality
Supports automatic context caching functionality. Cached tokens are charged at the input price (cache hit) rate. You can view "context caching" type cost details in the console
Generation Model kimi-latest
💡 Billing Note:The kimi-latest model automatically selects the appropriate billing tier based on your request's context length. Longer contexts incur higher costs
Model
Request Context Length Range
(Auto-selected Billing Tier)
Unit
Input Price
（Cache Hit）
Input Price
（Cache Miss）
Output Price
kimi-latest	≤ 8,192 tokens	1M tokens	$0.15	$0.20	$2.00
8,192 < length ≤ 32,768 tokens	1M tokens	$0.15	$1.00	$3.00
32,768 < length ≤ 131,072 tokens	1M tokens	$0.15	$2.00	$5.00
The kimi-latest model always uses the latest version of the Kimi large model used by the Kimi AI Assistant product, which may include features that are not yet stable
The kimi-latest model has a context length of 128k and will automatically select 8k/32k/128k models for billing based on the requested context length
kimi-latest is a vision model that supports image understanding
It supports automatic context caching, with cached tokens costing only $0.15 per M tokens
All other features are consistent with the moonshot-v1 series models, including: ToolCalls, JSON Mode, Partial Mode, and internet search functionality
Generation Model Moonshot-v1
Model	Unit	Input Price	Output Price	Context Window
moonshot-v1-8k	1M tokens	$0.20	$2.00	8,192 tokens
moonshot-v1-32k	1M tokens	$1.00	$3.00	32,768 tokens
moonshot-v1-128k	1M tokens	$2.00	$5.00	131,072 tokens
moonshot-v1-8k-vision-preview	1M tokens	$0.20	$2.00	8,192 tokens
moonshot-v1-32k-vision-preview	1M tokens	$1.00	$3.00	32,768 tokens
moonshot-v1-128k-vision-preview	1M tokens	$2.00	$5.00	131,072 tokens
Here, 1M = 1,000,000. The prices in the table represent the cost per 1M tokens consumed.

Last updated on 

WebSearch Pricing
Product Pricing
Explanation：The prices listed below are all inclusive of tax.

Tool Name
Unit
Price
Comment
Web Search	1 time	$0.005	Trigger $web_search tool call, charge once
Internet Search Billing Logic
When you add the $web_search tool in tools and receive a response with finish_reason = tool_calls and tool_call.function.name = $web_search, we charge a fee of $0.005 for the $web_search call. If the response has finish_reason = stop, no call fee will be charged.

Additionally, when using $web_search, we still charge for the Tokens generated by the /chat/completions interface based on the model size. It is important to note that when the $web_search tool is triggered, the search results are also counted in the Tokens. The number of Tokens occupied by the search results can be obtained from the returned tool_call.function.arguments. For example, if the content of the $web_search occupies 4k Tokens, these 4k Tokens will be included in the total Tokens when the caller makes the next call to the /chat/completions interface. The total billing Tokens will be:

total_tokens = prompt_tokens + search_tokens + completions_tokens

Note: If you stop after triggering the $web_search without continuing with tool_calls, we will only charge the tool call fee of $0.005, and the Tokens occupied by the search content will not be billed.

Last updated on 

Recharge and Rate Limits
To ensure fair distribution of resources and prevent malicious attacks, we currently apply rate limits based on the cumulative recharge amount of each account. The specific limits are shown in the table below. If you have higher requirements, please contact us via email at api-service@moonshot.ai.

To prevent abuse, you need to recharge at least $1 to start using, and when your cumulative recharge reaches $5, you will receive a $5 voucher.
User Level	Cumulative Recharge Amount	Concurrency	RPM	TPM	TPD
Tier0	$1	1	3	500,000	1,500,000
Tier 1	$10	50	200	2,000,000	Unlimited
Tier2	$20	100	500	3,000,000	Unlimited
Tier 3	$100	200	5,000	3,000,000	Unlimited
Tier4	$1,000	400	5,000	4,000,000	Unlimited
Tier5	$3,000	1,000	10,000	5,000,000	Unlimited
Explanation of Rate Limits Concepts
Concurrency: The maximum number of requests from you that we can process at the same time.

RPM: Requests per minute, which means the maximum number of requests you can send to us in one minute.

TPM: Tokens per minute, which means the maximum number of tokens you can interact with us in one minute.

TPD: Tokens per day, which means the maximum number of tokens you can interact with us in one day.

For more details, please refer to the Rate Limits section.

Why Do We Implement Rate Limits?
Rate limits are a common practice for API interfaces, and there are several reasons for it:

They help prevent abuse or misuse of the API. For example, malicious actors might try to overwhelm the API with a large number of requests, attempting to overload it or cause service disruptions. By setting rate limits, we can guard against such behavior.

Rate limits ensure fair access to the API for everyone. If one person or organization sends too many requests, it could slow down the API for everyone else. By limiting the number of requests a single user can send, we ensure that as many people as possible can use the API without experiencing slowdowns.

Rate limits help us manage the overall load on our cluster. A sudden surge in requests to the API could put pressure on the servers and lead to performance issues. By setting rate limits, we can maintain a smooth and consistent experience for all users.

Special Notes
We will do our best to ensure normal usage for users, but when the cluster load reaches its capacity limit, we may take temporary measures to adjust the rate limits.
Vouchers do not count towards the cumulative recharge total.
Last updated on 
FAQ
How do I recharge my account?

We support binding credit cards (supported card scheme include Visa, Mastercard, and UnionPay). After successfully binding a credit card, you can proceed to make a deposit (minimum deposit amount is 1 USD). Once the deposit is successful, your account balance will be credited with the corresponding amount, which can be used for subsequent transactions.
How do I request an invoice?

The platform support online invoice applications.After the payment for the recharge order is completed, the platform will automatically issue an invoice. You can download the issued invoice in the Recharge Details order list. If you have reserved an email address in the payment process or invoice information management, the platform will send the invoice to your email after it has been successfully issued.
How do I get customer support?

If you encounter any issues during model invocation or platform usage, or have related requirements, please email us (api-service@moonshot.ai). We will process your feedback promptly and respond within 2 business days. Thank you for your understanding and support!
How do I get enterprise API products and pricing information?

The enterprise API product has been released, and the quotation and rights description can be obtained by email (api-service@moonshot.ai). We will assign a dedicated account manager to contact you regarding potential business opportunities. We will process your feedback promptly and respond within 2 business days.
Last updated on 
Kimi K2 Quickstart
Overview of Kimi K2
Kimi K2 is the new generation flagship model launched by Moonshot AI, featuring advanced agentic (autonomous reasoning and action) capabilities. Built with a 1T total parameter count and a 32B active parameter MoE (Mixture of Experts) architecture, Kimi K2 excels in AI coding and agent-building. Technical Report

as-k2

Leading Coding Abilities
Industry Leading: Kimi K2 is currently one of the best coding models in China.
Full Stack Support: Supports the entire development cycle, from frontend to backend, covering code generation, DevOps, debugging, and optimization—tailored for real-world programming scenarios.
Efficiency Boost: Comes with over a dozen ready-to-use built-in tools such as web search, together with precise tool call abilities to significantly enhance development efficiency.
Powerful Agent-Building Capabilities
Complex Task Decomposition: Automatically decomposes requirements into a series of executable tool calls.
Enforcer & JSON Mode: Unique features ensure stability and controllability of tool call formatting.
Multitool Collaboration: Bundled with over ten built-in tools (like web search), supporting sophisticated multi-step agent workflows. Learn more.
Highly Accurate Tool Calls: The official API achieves nearly 100% accuracy in tool calls, providing a reliable foundation for agents. (Note: Tool call performance may decrease on third-party open-source platforms. For detailed benchmarks, see the K2 Vendor Verifier Project.)
Ultra-Long Context Support
kimi-k2-0905-preview, kimi-k2-turbo-preview, kimi-k2-thinking, kimi-k2-thinking-turbo models offer a context window up to 256K tokens.
Recommended API Versions
K2 Model Version	Features
kimi-k2-0905-preview	The latest Kimi K2 version, supports 256K context window
kimi-k2-turbo-preview	High-speed Kimi K2 version, up to 60-100 tokens/s, ideal for enterprise and high-responsiveness agent applications
kimi-k2-thinking	Long-term thinking Kimi K2 version, supports 256k context, supports multi-step tool usage and reasoning, excels at solving more complex problems
kimi-k2-thinking-turbo	High-speed version of the long-thinking Kimi K2 model. Supports a 256K context window, delivers stronger reasoning abilities, and increases output speed to 60-100 tokens per second.
For further information on Kimi K2 models, see the Model List
Get Started
Try instantly: Use the online playground to interactively test the model and evaluate its performance for your business scenarios.
Request an API Key: Start testing via the API right away.
Example Usage
Here is a complete usage example to help you quickly get started with the Kimi K2 model.

Install the OpenAI SDK
Kimi API is fully compatible with OpenAI's API format. You can install the OpenAI SDK as follows:

pip install --upgrade 'openai>=1.0'

Verify the Installation
python -c 'import openai; print("version =",openai.__version__)'
 
# The output may be version = 1.10.0, indicating the OpenAI SDK was installed successfully and your Python environment is using OpenAI SDK v1.10.0.

Example Code
from openai import OpenAI
 
client = OpenAI(
    api_key = "$MOONSHOT_API_KEY",
    base_url = "https://api.moonshot.ai/v1",
)
 
completion = client.chat.completions.create(
    model = "kimi-k2-turbo-preview",
    messages = [
        {"role": "system", "content": "You are Kimi, an AI assistant provided by Moonshot AI. You excel at Chinese and English dialog, and provide helpful, safe, and accurate answers. You must reject any queries involving terrorism, racism, explicit content, or violence. 'Moonshot AI' must always remain in English and must not be translated to other languages."},
        {"role": "user", "content": "Hello, my name is Li Lei. What is 1+1?"}
    ],
    temperature = 0.6, # controls randomness of output
    # max_tokens=32000, # maximum output tokens
)
 
print(completion.choices[0].message.content)

If your code runs successfully with no errors, you will see output similar to the following:

Hello, Li Lei! 1+1 equals 2. This is a basic addition problem. If you have more questions or need further help, feel free to ask me.

Streaming Output Example
from openai import OpenAI
 
client = OpenAI(
    api_key = "MOONSHOT_API_KEY", # Replace with your own API Key
    base_url = "https://api.moonshot.ai/v1",
)
 
stream = client.chat.completions.create(
    model = "kimi-k2-turbo-preview",
    messages = [
        {"role": "system", "content": "You are Kimi, an AI assistant provided by Moonshot AI. You excel at Chinese and English dialog, and provide helpful, safe, and accurate answers. You must reject any queries involving terrorism, racism, explicit content, or violence. 'Moonshot AI' must always remain in English and must not be translated to other languages."},
        {"role": "user", "content": "Hello, my name is Li Lei. What is 1+1?"}
    ],
    temperature=0.6, # controls randomness of output
    max_tokens=32000, # maximum output tokens 
    stream=True, # enable streaming output
)
 
for chunk in stream:
        delta = chunk.choices[0].delta # streaming segment
        if delta.content:
                print(delta.content, end="")
 

Additional Information
Kimi K2 is a pure text model. For handling images or other file types, use the Kimi Latest model, which matches the experience delivered by the Kimi.com K1.5 assistant.
See How to use Kimi K2 within Claude Code, Roo Code, Cline.
See how to use the Long-Thinking Kimi K2 Model.
Web search is one of the powerful tools built into Kimi API. Check here to learn how to use the Web Search Tool and other Official Tools.
See full Model Pricing, Recharge & QPS Limit Information, and Web Search Pricing.
Last updated on 


Using the kimi-k2-thinking model
The kimi-k2-thinking model is a general-purpose agentic reasoning model developed by Moonshot AI. Thanks to its strength in deep reasoning and multi-step tool use, it can solve even the hardest problems.

If you are doing benchmark testing with kimi api, please refer to this benchmark best practice.

Basic use case
You can simply use it by switching the model parameter:

import os
import openai
 
client = openai.Client(
    base_url="https://api.moonshot.ai/v1",
    api_key=os.getenv("MOONSHOT_API_KEY"),
)
 
stream = client.chat.completions.create(
    model="kimi-k2-thinking",
    messages=[
        {
            "role": "system",
            "content": "You are Kimi.",
        },
        {
            "role": "user",
            "content": "Please explain why 1+1=2."
        },
    ],
    max_tokens=1024*32,
    stream=True,
    temperature=1.0,
)
 
thinking = False
for chunk in stream:
    if chunk.choices:
        choice = chunk.choices[0]
        if choice.delta and hasattr(choice.delta, "reasoning_content"):
            if not thinking:
                thinking = True
                print("=============Start Reasoning=============")
            print(getattr(choice.delta, "reasoning_content"), end="")
        if choice.delta and choice.delta.content:
            if thinking:
                thinking = False
                print("\n=============End Reasoning=============")
            print(choice.delta.content, end="")
 

Accessing the reasoning content
In the kimi-k2-thinking model API response, we use the reasoning_content field as the carrier for the model's reasoning. About the reasoning_content field:

In the OpenAI SDK, ChoiceDelta and ChatCompletionMessage types do not provide a reasoning_content field directly, so you cannot access it via .reasoning_content. You must use hasattr(obj, "reasoning_content") to check if the field exists, and if so, use getattr(obj, "reasoning_content") to retrieve its value.
If you use other frameworks or directly interface with the HTTP API, you can directly obtain the reasoning_content field at the same level as the content field.
In streaming output (stream=True), the reasoning_content field will always appear before the content field. In your business logic, you can detect if the content field has been output to determine if the reasoning (inference process) is finished.
Tokens in reasoning_content are also controlled by the max_tokens parameter: the sum of tokens in reasoning_content and content must be less than or equal to max_tokens.
Multi-Step Tool Call
kimi-k2-thinking is designed to perform deep reasoning across multiple tool calls, enabling it to tackle highly complex tasks.

Usage Notes
To get reliable results, always follow these rules when calling the kimi-k2-thinking model :

Include the entire reasoning content from the context (the reasoning_content field) in your input. The model will decide which parts are necessary and forward them for further reasoning.
Set max_tokens ≥ 16,000 to ensure the full reasoning_content and final content can be returned without truncation.
Set temperature = 1.0 to get the best performance.
Enable streaming (stream = true). Because kimi-k2-thinking returns both reasoning_content and regular content, the response is larger than usual. Streaming delivers a better user experience and helps avoid network-timeout issues.
Complete example
We walk through a complete example that shows how to properly use kimi-k2-thinking together with official tools for multi-step tool call and extended reasoning.

The example below demonstrates a "Daily News Report Generation" scenario. The model will sequentially call official tools like date (to get the date) and web_search (to search today's news), and will present deep reasoning throughout this process:

import os
import json
import httpx
import openai
 
 
class FormulaChatClient:
    def __init__(self, base_url: str, api_key: str):
        """Initialize Formula client"""
        self.base_url = base_url
        self.api_key = api_key
        self.openai = openai.Client(
            base_url=base_url,
            api_key=api_key,
        )
        self.httpx = httpx.Client(
            base_url=base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30.0,
        )
        self.model = "kimi-k2-thinking"
 
    def get_tools(self, formula_uri: str):
        """Get tool definitions from Formula API"""
        response = self.httpx.get(f"/formulas/{formula_uri}/tools")
        response.raise_for_status()
        
        try:
            return response.json().get("tools", [])
        except json.JSONDecodeError as e:
            print(f"Error: Unable to parse JSON (status code: {response.status_code})")
            print(f"Response content: {response.text[:500]}")
            raise
 
    def call_tool(self, formula_uri: str, function: str, args: dict):
        """Call an official tool"""
        response = self.httpx.post(
            f"/formulas/{formula_uri}/fibers",
            json={"name": function, "arguments": json.dumps(args)},
        )
        response.raise_for_status()
        fiber = response.json()
        
        if fiber.get("status", "") == "succeeded":
            return fiber["context"].get("output") or fiber["context"].get("encrypted_output")
        
        if "error" in fiber:
            return f"Error: {fiber['error']}"
        if "error" in fiber.get("context", {}):
            return f"Error: {fiber['context']['error']}"
        return "Error: Unknown error"
 
    def close(self):
        """Close the client connection"""
        self.httpx.close()
 
 
# Initialize client
base_url = os.getenv("MOONSHOT_BASE_URL", "https://api.moonshot.ai/v1")
api_key = os.getenv("MOONSHOT_API_KEY")
 
if not api_key:
    raise ValueError("MOONSHOT_API_KEY environment variable not set. Please set your API key.")
 
print(f"Base URL: {base_url}")
print(f"API Key: {api_key[:10]}...{api_key[-10:] if len(api_key) > 20 else api_key}\n")
 
client = FormulaChatClient(base_url, api_key)
 
# Define the official tool Formula URIs to use
formula_uris = [
    "moonshot/date:latest",
    "moonshot/web-search:latest"
]
 
# Load all tool definitions and build mapping
print("Loading official tools...")
all_tools = []
tool_to_uri = {}  # function.name -> formula_uri
 
for uri in formula_uris:
    try:
        tools = client.get_tools(uri)
        for tool in tools:
            func = tool.get("function")
            if func:
                func_name = func.get("name")
                if func_name:
                    tool_to_uri[func_name] = uri
                    all_tools.append(tool)
                    print(f"  Loaded tool: {func_name} from {uri}")
    except Exception as e:
        print(f"  Warning: Failed to load tool {uri}: {e}")
        continue
 
print(f"Loaded {len(all_tools)} tools in total\n")
 
if not all_tools:
    raise ValueError("No tools loaded. Please check API key and network connection.")
 
# Initialize message list
messages = [
    {
        "role": "system",
        "content": "You are Kimi, a professional news analyst. You excel at collecting, analyzing, and organizing information to generate high-quality news reports.",
    },
]
 
# User request to generate today's news report
user_request = "Please help me generate a daily news report including important technology, economy, and society news."
messages.append({
    "role": "user",
    "content": user_request
})
 
print(f"User request: {user_request}\n")
 
# Begin multi-step conversation loop
max_iterations = 10  # Prevent infinite loops
for iteration in range(max_iterations):
    try:
        completion = client.openai.chat.completions.create(
            model=client.model,
            messages=messages,
            max_tokens=1024 * 32,
            tools=all_tools,
            temperature=1.0,
        )
    except openai.AuthenticationError as e:
        print(f"Authentication error: {e}")
        print("Please check if the API key is correct and has the required permissions")
        raise
    except Exception as e:
        print(f"Error while calling the model: {e}")
        raise
    
    # Get response
    message = completion.choices[0].message
    
    # Print reasoning process
    if hasattr(message, "reasoning_content"):
        print(f"=============Reasoning round {iteration + 1} starts=============")
        reasoning = getattr(message, "reasoning_content")
        if reasoning:
            print(reasoning[:500] + "..." if len(reasoning) > 500 else reasoning)
        print(f"=============Reasoning round {iteration + 1} ends=============\n")
    
    # Add assistant message to context (preserve reasoning_content)
    messages.append(message)
    
    # If the model did not call any tools, conversation is done
    if not message.tool_calls:
        print("=============Final Answer=============")
        print(message.content)
        break
    
    # Handle tool calls
    print(f"The model decided to call {len(message.tool_calls)} tool(s):\n")
    
    for tool_call in message.tool_calls:
        func_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        
        print(f"Calling tool: {func_name}")
        print(f"Arguments: {json.dumps(args, ensure_ascii=False, indent=2)}")
        
        # Get corresponding formula_uri
        formula_uri = tool_to_uri.get(func_name)
        if not formula_uri:
            print(f"Error: Could not find Formula URI for tool {func_name}")
            continue
        
        # Call the tool
        result = client.call_tool(formula_uri, func_name, args)
        
        # Print result (truncate if too long)
        if len(str(result)) > 200:
            print(f"Tool result: {str(result)[:200]}...\n")
        else:
            print(f"Tool result: {result}\n")
        
        # Add tool result to message list
        tool_message = {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": func_name,
            "content": result
        }
        messages.append(tool_message)
 
print("\nConversation completed!")
 
# Cleanup
client.close()

This process demonstrates how the kimi-k2-thinking model uses deep reasoning to plan and execute complex multi-step tasks, with detailed reasoning steps (reasoning_content) preserved in the context to ensure accurate tool use at every stage.

Frequently Asked Questions
Q1: Why should I keep reasoning_content?
A: Keeping the reasoning_content ensures the model maintains reasoning continuity in multi-step reasoning scenarios, especially when calling tools. The server will automatically handle these fields; users do not need to manage them manually.

Q2: Does reasoning_content consume extra tokens?
A: Yes, reasoning_content counts towards your input/output token quota. For detailed pricing, please refer to MoonshotAI's pricing documentation.

Last updated on 


Using the kimi-k2-thinking model
The kimi-k2-thinking model is a general-purpose agentic reasoning model developed by Moonshot AI. Thanks to its strength in deep reasoning and multi-step tool use, it can solve even the hardest problems.

If you are doing benchmark testing with kimi api, please refer to this benchmark best practice.

Basic use case
You can simply use it by switching the model parameter:

$ curl https://api.moonshot.ai/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $MOONSHOT_API_KEY" \
    -d '{
        "model": "kimi-k2-thinking",
        "messages": [
            {"role": "user", "content": "hello"}
        ],
        "temperature": 1.0
   }'
 

Accessing the reasoning content
In the kimi-k2-thinking model API response, we use the reasoning_content field as the carrier for the model's reasoning. About the reasoning_content field:

In the OpenAI SDK, ChoiceDelta and ChatCompletionMessage types do not provide a reasoning_content field directly, so you cannot access it via .reasoning_content. You must use hasattr(obj, "reasoning_content") to check if the field exists, and if so, use getattr(obj, "reasoning_content") to retrieve its value.
If you use other frameworks or directly interface with the HTTP API, you can directly obtain the reasoning_content field at the same level as the content field.
In streaming output (stream=True), the reasoning_content field will always appear before the content field. In your business logic, you can detect if the content field has been output to determine if the reasoning (inference process) is finished.
Tokens in reasoning_content are also controlled by the max_tokens parameter: the sum of tokens in reasoning_content and content must be less than or equal to max_tokens.
Multi-Step Tool Call
kimi-k2-thinking is designed to perform deep reasoning across multiple tool calls, enabling it to tackle highly complex tasks.

Usage Notes
To get reliable results, always follow these rules when calling the kimi-k2-thinking model :

Include the entire reasoning content from the context (the reasoning_content field) in your input. The model will decide which parts are necessary and forward them for further reasoning.
Set max_tokens ≥ 16,000 to ensure the full reasoning_content and final content can be returned without truncation.
Set temperature = 1.0 to get the best performance.
Enable streaming (stream = true). Because kimi-k2-thinking returns both reasoning_content and regular content, the response is larger than usual. Streaming delivers a better user experience and helps avoid network-timeout issues.
Complete example
We walk through a complete example that shows how to properly use kimi-k2-thinking together with official tools for multi-step tool call and extended reasoning.

The example below demonstrates a "Daily News Report Generation" scenario. The model will sequentially call official tools like date (to get the date) and web_search (to search today's news), and will present deep reasoning throughout this process:

import os
import json
import httpx
import openai
 
 
class FormulaChatClient:
    def __init__(self, base_url: str, api_key: str):
        """Initialize Formula client"""
        self.base_url = base_url
        self.api_key = api_key
        self.openai = openai.Client(
            base_url=base_url,
            api_key=api_key,
        )
        self.httpx = httpx.Client(
            base_url=base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30.0,
        )
        self.model = "kimi-k2-thinking"
 
    def get_tools(self, formula_uri: str):
        """Get tool definitions from Formula API"""
        response = self.httpx.get(f"/formulas/{formula_uri}/tools")
        response.raise_for_status()
        
        try:
            return response.json().get("tools", [])
        except json.JSONDecodeError as e:
            print(f"Error: Unable to parse JSON (status code: {response.status_code})")
            print(f"Response content: {response.text[:500]}")
            raise
 
    def call_tool(self, formula_uri: str, function: str, args: dict):
        """Call an official tool"""
        response = self.httpx.post(
            f"/formulas/{formula_uri}/fibers",
            json={"name": function, "arguments": json.dumps(args)},
        )
        response.raise_for_status()
        fiber = response.json()
        
        if fiber.get("status", "") == "succeeded":
            return fiber["context"].get("output") or fiber["context"].get("encrypted_output")
        
        if "error" in fiber:
            return f"Error: {fiber['error']}"
        if "error" in fiber.get("context", {}):
            return f"Error: {fiber['context']['error']}"
        return "Error: Unknown error"
 
    def close(self):
        """Close the client connection"""
        self.httpx.close()
 
 
# Initialize client
base_url = os.getenv("MOONSHOT_BASE_URL", "https://api.moonshot.ai/v1")
api_key = os.getenv("MOONSHOT_API_KEY")
 
if not api_key:
    raise ValueError("MOONSHOT_API_KEY environment variable not set. Please set your API key.")
 
print(f"Base URL: {base_url}")
print(f"API Key: {api_key[:10]}...{api_key[-10:] if len(api_key) > 20 else api_key}\n")
 
client = FormulaChatClient(base_url, api_key)
 
# Define the official tool Formula URIs to use
formula_uris = [
    "moonshot/date:latest",
    "moonshot/web-search:latest"
]
 
# Load all tool definitions and build mapping
print("Loading official tools...")
all_tools = []
tool_to_uri = {}  # function.name -> formula_uri
 
for uri in formula_uris:
    try:
        tools = client.get_tools(uri)
        for tool in tools:
            func = tool.get("function")
            if func:
                func_name = func.get("name")
                if func_name:
                    tool_to_uri[func_name] = uri
                    all_tools.append(tool)
                    print(f"  Loaded tool: {func_name} from {uri}")
    except Exception as e:
        print(f"  Warning: Failed to load tool {uri}: {e}")
        continue
 
print(f"Loaded {len(all_tools)} tools in total\n")
 
if not all_tools:
    raise ValueError("No tools loaded. Please check API key and network connection.")
 
# Initialize message list
messages = [
    {
        "role": "system",
        "content": "You are Kimi, a professional news analyst. You excel at collecting, analyzing, and organizing information to generate high-quality news reports.",
    },
]
 
# User request to generate today's news report
user_request = "Please help me generate a daily news report including important technology, economy, and society news."
messages.append({
    "role": "user",
    "content": user_request
})
 
print(f"User request: {user_request}\n")
 
# Begin multi-step conversation loop
max_iterations = 10  # Prevent infinite loops
for iteration in range(max_iterations):
    try:
        completion = client.openai.chat.completions.create(
            model=client.model,
            messages=messages,
            max_tokens=1024 * 32,
            tools=all_tools,
            temperature=1.0,
        )
    except openai.AuthenticationError as e:
        print(f"Authentication error: {e}")
        print("Please check if the API key is correct and has the required permissions")
        raise
    except Exception as e:
        print(f"Error while calling the model: {e}")
        raise
    
    # Get response
    message = completion.choices[0].message
    
    # Print reasoning process
    if hasattr(message, "reasoning_content"):
        print(f"=============Reasoning round {iteration + 1} starts=============")
        reasoning = getattr(message, "reasoning_content")
        if reasoning:
            print(reasoning[:500] + "..." if len(reasoning) > 500 else reasoning)
        print(f"=============Reasoning round {iteration + 1} ends=============\n")
    
    # Add assistant message to context (preserve reasoning_content)
    messages.append(message)
    
    # If the model did not call any tools, conversation is done
    if not message.tool_calls:
        print("=============Final Answer=============")
        print(message.content)
        break
    
    # Handle tool calls
    print(f"The model decided to call {len(message.tool_calls)} tool(s):\n")
    
    for tool_call in message.tool_calls:
        func_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        
        print(f"Calling tool: {func_name}")
        print(f"Arguments: {json.dumps(args, ensure_ascii=False, indent=2)}")
        
        # Get corresponding formula_uri
        formula_uri = tool_to_uri.get(func_name)
        if not formula_uri:
            print(f"Error: Could not find Formula URI for tool {func_name}")
            continue
        
        # Call the tool
        result = client.call_tool(formula_uri, func_name, args)
        
        # Print result (truncate if too long)
        if len(str(result)) > 200:
            print(f"Tool result: {str(result)[:200]}...\n")
        else:
            print(f"Tool result: {result}\n")
        
        # Add tool result to message list
        tool_message = {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": func_name,
            "content": result
        }
        messages.append(tool_message)
 
print("\nConversation completed!")
 
# Cleanup
client.close()

This process demonstrates how the kimi-k2-thinking model uses deep reasoning to plan and execute complex multi-step tasks, with detailed reasoning steps (reasoning_content) preserved in the context to ensure accurate tool use at every stage.

Frequently Asked Questions
Q1: Why should I keep reasoning_content?
A: Keeping the reasoning_content ensures the model maintains reasoning continuity in multi-step reasoning scenarios, especially when calling tools. The server will automatically handle these fields; users do not need to manage them manually.

Q2: Does reasoning_content consume extra tokens?
A: Yes, reasoning_content counts towards your input/output token quota. For detailed pricing, please refer to MoonshotAI's pricing documentation.

Last updated on 



Quickstart with the Kimi API
The Kimi API allows you to interact with the Kimi large language model. Here is a simple example code:

from openai import OpenAI
 
client = OpenAI(
    api_key="MOONSHOT_API_KEY", # Replace MOONSHOT_API_KEY with the API Key you obtained from the Kimi Open Platform
    base_url="https://api.moonshot.ai/v1",
)
 
completion = client.chat.completions.create(
    model = "kimi-k2-turbo-preview",
    messages = [
        {"role": "system", "content": "You are Kimi, an AI assistant provided by Moonshot AI. You are proficient in Chinese and English conversations. You provide users with safe, helpful, and accurate answers. You will reject any requests involving terrorism, racism, or explicit content. Moonshot AI is a proper noun and should not be translated."},
        {"role": "user", "content": "Hello, my name is Li Lei. What is 1+1?"}
    ],
    temperature = 0.6,
)
 
# We receive a response from the Kimi large language model via the API (role=assistant)
print(completion.choices[0].message.content)

To successfully run the above code, you may need to prepare the following:

A Python environment or a Node.js environment. We recommend using a Python interpreter version 3.8 or higher;
The OpenAI SDK. Our API is fully compatible with the OpenAI API format, so you can directly use the Python or Node.js OpenAI SDK for calls. You can install the OpenAI SDK as follows:
pip install --upgrade 'openai>=1.0' #Python
npm install openai@latest #Node.js

An API Key. You need to create an API Key from the Kimi Open Platform and pass it to the OpenAi Client so that we can correctly identify your identity;
If you successfully run the above code without any errors, you will see output similar to the following:

Hello, Li Lei! 1+1 equals 2. This is a basic math addition problem. If you have any other questions or need help, feel free to let me know.

Note: Due to the uncertainty of the Kimi large language model, the actual response may not be exactly the same as the above content.

Last updated on 




Migrating from OpenAI to Kimi API
About API Compatibility
The Kimi API is compatible with OpenAI's interface specifications. You can use the Python or NodeJS SDKs provided by OpenAI to call and use the Kimi large language model. This means that if your application or service is developed based on OpenAI's models, you can seamlessly migrate to using the Kimi large language model by simply replacing the base_url and api_key with the configuration for the Kimi large language model. Here is an example of how to do this:

from openai import OpenAI
 
client = OpenAI(
    api_key="MOONSHOT_API_KEY", # <-- Replace MOONSHOT_API_KEY with the API Key you obtained from the Kimi Open Platform
    base_url="https://api.moonshot.ai/v1", # <-- Replace the base_url from https://api.openai.com/v1 to https://api.moonshot.ai/v1
)

We will do our best to ensure compatibility between the Kimi API and OpenAI. However, in some special cases, there may still be some differences and variations between the Kimi API and OpenAI (but this does not affect overall compatibility). We will detail the differences between the Kimi API and OpenAI and propose feasible migration solutions to help developers complete the migration process smoothly.

Here is a list of interfaces that are compatible with OpenAI:

/v1/chat/completions
/v1/files
/v1/files/{file_id}
/v1/files/{file_id}/content
Temperature and N Value
When using OpenAI's interface, you can set both temperature=0 and n>1, which means that in cases where the temperature value is 0, multiple different answers (i.e., choices) can be returned simultaneously.

However, in the Kimi API, when you set the temperature value to 0 or close to 0 (e.g., 0.001), we can only provide one answer (i.e., len(choices)=1). If you set temperature to 0 while using an n value greater than 1, we will return an "invalid request" error, specifically invalid_request_error.

Additionally, please note that the range of values for the temperature parameter in the Kimi API is [0, 1], while the range for the temperature parameter in OpenAI is [0, 2].

Migration Recommendation: For kimi-k2-turbo-preview, set temperature=0.6 for optimal results. For older models, 0.3 remains a safe default. If your business scenario requires setting temperature=0 to get more stable results from the Kimi large language model, please pay special attention to setting the n value to 1, or do not set the n value at all (in which case the default n=1 will be used as the request parameter, which is valid).

Usage Value in Stream Mode
When using OpenAI's chat.completions interface, in cases of streaming output (i.e., stream=True), the output result does not include usage information by default (including prompt_tokens/completion_tokens/total_tokens). OpenAI provides an additional parameter stream_options={"include_usage": True} to include usage information in the last data block of the response.

In the Kimi API, in addition to the stream_options={"include_usage": True} parameter, we also place usage information (including prompt_tokens/completion_tokens/total_tokens) in the end data block of each choice.

Migration Recommendation: In most cases, developers do not need to take any additional compatibility measures. If your business scenario requires tracking the usage information for each choice individually, you can access the choice.usage field. Note that among different choices, only the values of usage.completion_tokens and usage.total_tokens are different, while the values of usage.prompt_tokens are the same for all choices.

Deprecated function_call
In 2023, OpenAI introduced the functions parameter to enable function call functionality. After functional iteration, OpenAI later launched the tool call feature and marked the functions parameter as deprecated, which means that the functions parameter may be removed at any time in future API iterations.

The Kimi API fully supports the tool call feature. However, since functions has been deprecated, the Kimi API does not support using the functions parameter to execute function calls.

Migration Recommendation: If your application or service relies on tool calls, no additional compatibility measures are needed. If your application or service depends on the deprecated function call, we recommend migrating to tool calls. Tool calls expand the capabilities of function calls and support parallel function calls. For specific examples of tool calls, please refer to our tool call guide:

Using Kimi API for Tool Calls (tool_calls)

Here is an example of migrating from functions to tools:

We will present the code that needs to be modified in the form of comments, along with explanations, to help developers better understand how to perform the migration.

from typing import *
 
import json
import httpx
from openai import OpenAI
 
client = OpenAI(
    api_key="MOONSHOT_API_KEY",  # Replace MOONSHOT_API_KEY with the API Key you obtained from the Kimi Open Platform
    base_url="https://api.moonshot.ai/v1",
)
 
functions = [
    {
        "name": "search",  # The name of the function, please use English letters (uppercase and lowercase), numbers, plus hyphens and underscores as the function name
        "description": """ 
            Search for content on the internet using a search engine.
 
            Call this tool when your knowledge cannot answer the user's question or when the user requests you to perform an online search. Extract the content the user wants to search for from the conversation with the user and use it as the value of the query parameter.
            The search results include the title of the website, the website's address (URL), and a brief introduction to the website.
        """,  # Description of the function, write the specific function here and the usage scenario so that the Kimi large language model can correctly choose which functions to use
        "parameters": {  # Use the parameters field to define the parameters accepted by the function
            "type": "object",  # Always use type: object to make the Kimi large language model generate a JSON Object parameter
            "required": ["query"],  # Use the required field to tell the Kimi large language model which parameters are required
            "properties": {  # Properties contain the specific parameter definitions, and you can define multiple parameters
                "query": {  # Here, the key is the parameter name, and the value is the specific definition of the parameter
                    "type": "string",  # Use type to define the parameter type
                    "description": """
                        The content the user wants to search for, extract it from the user's question or chat context.
                    """  # Use description to describe the parameter so that the Kimi large language model can better generate the parameter
                }
            }
        }
    }
]
 
 
def search_impl(query: str) -> List[Dict[str, Any]]:
    """
    search_impl uses a search engine to search for query. Most mainstream search engines (such as Bing) provide API calls, and you can choose the one you like.
    You can call the search engine API of your choice and place the website title, website link, and website introduction information in a dict and return it.
 
    This is just a simple example, and you may need to write some authentication, validation, and parsing code.
    """
    r = httpx.get("https://your.search.api", params={"query": query})
    return r.json()
 
 
def search(arguments: Dict[str, Any]) -> Any:
    query = arguments["query"]
    result = search_impl(query)
    return {"result": result}
 
 
function_map = {
    "search": search,
}
 
# ==========================================================================================================================================================
# Tools are a superset of functions, so we can construct tools using the already defined functions. We loop through each function and create the corresponding tool format;
# At the same time, we also generate the corresponding tool_map.
# ==========================================================================================================================================================
 
tools = []
tool_map = {}
for function in functions:
    tool = {
        "type": "function",
        "function": function,
    }
    tools.append(tool)
    tool_map[function["name"]] = function_map[function["name"]]
 
messages = [
    {"role": "system",
     "content": "You are Kimi, an artificial intelligence assistant provided by Moonshot AI. You are more proficient in Chinese and English conversations. You provide users with safe, helpful, and accurate answers. You also refuse to answer any questions involving terrorism, racism, pornography, or violence. Moonshot AI is a proper noun and should not be translated into other languages."},
    {"role": "user", "content": "Please search the internet for Context Caching and tell me what it is."}  # The user asks Kimi to search online
]
 
finish_reason = None
 
# ==========================================================================================================================================================
# Here, we change the finish_reason value check from function_call to tool_calls
# ==========================================================================================================================================================
# while finish_reason is None or finish_reason == "function_call":
while finish_reason is None or finish_reason == "tool_calls":
    completion = client.chat.completions.create(
        model="kimi-k2-turbo-preview",
        messages=messages,
        temperature=0.6,
        # ==========================================================================================================================================================
        # We no longer use the functions parameter, but instead use the tools parameter to enable tool calls
        # ==========================================================================================================================================================
        # function=functions,
        tools=tools,  # <-- We submit the defined tools to Kimi via the tools parameter
    )
    choice = completion.choices[0]
    finish_reason = choice.finish_reason
 
    # ==========================================================================================================================================================
    # Here, we replace the original function_call execution logic with the tool_calls execution logic;
    # Note that since there may be multiple tool_calls, we need to execute each one using a for loop.
    # ==========================================================================================================================================================
    # if finish_reason == "function_call":
    #   messages.append(choice.message)
    #   function_call_name = choice.message.function_call.name
    #   function_call_arguments = json.loads(choice.message.function_call.arguments)
    #   function_call = function_map[function_call_name]
    #   function_result = function_call(function_call_arguments)
    #   messages.append({
    #       "role": "function",
    #       "name": function_call_name,
    #       "content": json.dumps(function_result)
    #   })
 
    if finish_reason == "tool_calls":  # <-- Check if the response contains tool_calls
        messages.append(choice.message)  # <-- Add the assistant message from Kimi to the context for the next request
        for tool_call in choice.message.tool_calls:  # <-- Loop through each tool_call as there may be multiple
            tool_call_name = tool_call.function.name
            tool_call_arguments = json.loads(tool_call.function.arguments)  # <-- The arguments are serialized JSON, so we need to deserialize them
            tool_function = tool_map[tool_call_name]  # <-- Use tool_map to quickly find the function to execute
            tool_result = tool_function(tool_call_arguments)
 
            # Construct a message with role=tool to show the result of the tool call to the model;
            # Note that we need to provide the tool_call_id and name fields in the message so that Kimi can
            # correctly match it to the corresponding tool_call.
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_call_name,
                "content": json.dumps(tool_result),  # <-- We agree to submit the tool call result as a string, so we serialize it here
            })
 
print(choice.message.content)  # <-- Finally, we return the model's response to the user

About tool_choice
The Kimi API supports the tool_choice parameter, but there are some subtle differences in the values for tool_choice compared to OpenAI. The values for tool_choice that are currently compatible between Kimi API and OpenAI API are:

 "none"
 "auto"
 null
Please note that the current version of Kimi API does not support the tool_choice=required parameter.

Migration suggestion: If your application or service relies on the required value of the tool_choice field in the OpenAI API to ensure that the large model "definitely" selects a certain tool for invocation, we suggest using some special methods to enhance the Kimi large language model's awareness of invoking tools to partially accommodate the original business logic. For example, you can emphasize the use of a certain tool in the prompt to achieve a similar effect. We demonstrate this logic with a simplified version of the code:

from openai import OpenAI
 
client = OpenAI(
    api_key="MOONSHOT_API_KEY",  # Replace MOONSHOT_API_KEY with the API Key you obtained from the Kimi Open Platform
    base_url="https://api.moonshot.ai/v1",
)
 
tools = {
    # Define your tools here
}
 
messages = [
    # Store your message history here
]
 
completion = client.chat.completions.create(
    model="kimi-k2-turbo-preview",
    messages=messages,
    temperature=0.6,
    tools=tools,
    # tool_choice="required",  # <-- Since Kimi API does not currently support tool_choice=required, we have temporarily disabled this option
)
 
choice = completion.choices[0]
if choice.finish_reason != "tool_calls":
    # We assume that our business logic can confirm that tool_calls must be invoked here.
    # Without using tool_choice=required, we use the prompt to make Kimi choose a tool for invocation.
    messages.append(choice.message)
    messages.append({
        "role": "user",
        "content": "Please select a tool to handle the current issue.",  # Usually, the Kimi large language model understands the intention to invoke a tool and selects one for invocation
    })
    completion = client.chat.completions.create(
        model="kimi-k2-turbo-preview",
        messages=messages,
        temperature=0.6,
        tools=tools,
    )
    choice = completion.choices[0]
    assert choice.finish_reason == "tool_calls"  # This request should return finish_reason=tool_calls
    print(choice.message.content)

Please note that this method cannot guarantee a 100% success rate in triggering tool_calls. If your application or service has a very strong dependency on tool_calls, please wait for the launch of the tool_choice=required feature in Kimi API.

Last updated on 


MoonPalace - Moonshot AI's Kimi API Debugging Tool
MoonPalace (Moon Palace) is an API debugging tool provided by Moonshot AI. It has the following features:

Cross-platform support:
 Mac
 Windows
 Linux;
Easy to use, just replace base_url with http://localhost:9988 after launching to start debugging;
Captures complete requests, including the "scene of the accident" when network errors occur;
Quickly search and view request information using request_id and chatcmpl_id;
One-click export of BadCase structured reporting data, helping to enhance Kimi's model capabilities;
We recommend using MoonPalace as your API "supplier" during the code writing and debugging phase, so you can quickly identify and locate various issues related to API calls and code writing. For any unexpected outputs from Kimi large language model, you can also export the request details via MoonPalace and submit them to Moonshot AI to improve Kimi large language model.

Installation Methods
Using the go Command to Install
If you have the go toolchain installed, you can run the following command to install MoonPalace:

$ go install github.com/MoonshotAI/moonpalace@latest

The above command will install the compiled binary file in your $GOPATH/bin/ directory. Run the moonpalace command to check if it has been installed successfully:

$ moonpalace
MoonPalace is a command-line tool for debugging the Moonshot AI HTTP API.
 
Usage:
  moonpalace [command]
 
Available Commands:
  cleanup     Cleanup Moonshot AI requests.
  completion  Generate the autocompletion script for the specified shell
  export      export a Moonshot AI request.
  help        Help about any command
  inspect     Inspect the specific content of a Moonshot AI request.
  list        Query Moonshot AI requests based on conditions.
  start       Start the MoonPalace proxy server.
 
Flags:
  -h, --help      help for moonpalace
  -v, --version   version for moonpalace
 
Use "moonpalace [command] --help" for more information about a command.

If you still cannot find the moonpalace binary file, try adding the $GOPATH/bin/ directory to your $PATH environment variable.

Downloading from the Releases Page
You can download the precompiled binary (executable) files from the Releases page:

moonpalace-linux
moonpalace-macos-amd64 => for Intel-based Macs
moonpalace-macos-arm64 => for Apple Silicon-based Macs
moonpalace-windows.exe
Download the binary (executable) file that matches your platform and place it in a directory that is included in your $PATH environment variable. Rename it to moonpalace and then grant it executable permissions.

Usage
Starting the Service
Use the following command to start the MoonPalace proxy server:

$ moonpalace start --port <PORT>

MoonPalace will start an HTTP server locally, with the --port parameter specifying the local port that MoonPalace will listen on. The default value is 9988. When MoonPalace starts successfully, it will output:

[MoonPalace] 2024/07/29 17:00:29 MoonPalace Starts {'=>'} change base_url to "http://127.0.0.1:9988/v1"

As instructed, replace base_url with the displayed address. If you are using the default port, set base_url=http://127.0.0.1:9988/v1. If you are using a custom port, replace base_url with the displayed address.

Additionally, if you want to always use a debugging api_key during debugging, you can use the --key parameter when starting MoonPalace to set a default api_key for MoonPalace. This way, you don't have to manually set the api_key in each request. MoonPalace will automatically add the api_key you set with --key when requesting the Kimi API.

If you have correctly set base_url and successfully called the Kimi API, MoonPalace will output the following information:

$ moonpalace start --port <PORT>
[MoonPalace] 2024/07/29 17:00:29 MoonPalace Starts {'=>'} change base_url to "http://127.0.0.1:9988/v1"
[MoonPalace] 2024/07/29 21:30:53 POST   /v1/chat/completions 200 OK
[MoonPalace] 2024/07/29 21:30:53   - Request Headers: 
[MoonPalace] 2024/07/29 21:30:53     - Content-Type:   application/json
[MoonPalace] 2024/07/29 21:30:53   - Response Headers: 
[MoonPalace] 2024/07/29 21:30:53     - Content-Type:   application/json
[MoonPalace] 2024/07/29 21:30:53     - Msh-Request-Id: c34f3421-4dae-11ef-b237-9620e33511ee
[MoonPalace] 2024/07/29 21:30:53     - Server-Timing:  7134
[MoonPalace] 2024/07/29 21:30:53     - Msh-Uid:        cn0psmmcp7fclnphkcpg
[MoonPalace] 2024/07/29 21:30:53     - Msh-Gid:        enterprise-tier-5
[MoonPalace] 2024/07/29 21:30:53   - Response: 
[MoonPalace] 2024/07/29 21:30:53     - id:                cmpl-12be8428ebe74a9e8466a37bee7a9b11
[MoonPalace] 2024/07/29 21:30:53     - prompt_tokens:     1449
[MoonPalace] 2024/07/29 21:30:53     - completion_tokens: 158
[MoonPalace] 2024/07/29 21:30:53     - total_tokens:      1607
[MoonPalace] 2024/07/29 21:30:53   New Row Inserted: last_insert_id=15

MoonPalace will output the details of the request in the form of logs in the command line (if you want to persist the log content, you can redirect stderr to a file).

Note: In the logs, the value of the Msh-Request-Id field in the Response Headers corresponds to the --requestid parameter in the Search Request and Export Request sections below. The id in the Response corresponds to the --chatcmpl parameter, and last_insert_id corresponds to the --id parameter.

[MoonPalace] 2024/08/05 19:06:19   it seems that your max_tokens value is too small, please set a larger value

If the current mode is non-streaming output (stream=False), MoonPalace will suggest an appropriate max_tokens value.

Enabling Repeated Content Output Detection
MoonPalace offers a feature to detect repeated content output from the Kimi large language model. Repeated content output refers to the model continuously outputting a specific word, sentence, or blank character without stopping before reaching the max_tokens limit. This can lead to additional Token costs when using more expensive models like moonshot-v1-128k. Therefore, MoonPalace provides the --detect-repeat option to enable repeated content output detection, as shown below:

$ moonpalace start --port <PORT> --detect-repeat --repeat-threshold 0.3 --repeat-min-length 20

After enabling the --detect-repeat option, MoonPalace will interrupt the output of the Kimi large language model and log the following message when it detects repeated content:

[MoonPalace] 2024/08/05 18:20:37   it appears that there is an issue with content repeating in the current response

Note: The --detect-repeat option only interrupts the output in streaming mode (stream=True). It does not apply to non-streaming output.

You can adjust MoonPalace's blocking behavior using the --repeat-threshold and --repeat-min-length parameters:

The --repeat-threshold parameter sets MoonPalace's tolerance for repeated content. A higher threshold means lower tolerance, and repeated content will be blocked more quickly. The range is 0 <= threshold <= 1.
The --repeat-min-length parameter sets the minimum number of characters before MoonPalace starts detecting repeated content. For example, --repeat-min-length=100 means that repeated content detection will only start when the output exceeds 100 UTF-8 characters.
Enabling Forced Streaming Output
MoonPalace provides the --force-stream option to force all /v1/chat/completions requests to use streaming output mode:

$ moonpalace start --port <PORT> --force-stream

MoonPalace will set the stream field in the request parameters to True. When receiving a response, it will automatically determine the response format based on whether the caller has set stream:

If the caller has set stream=True, the response will be returned in streaming format without any special handling by MoonPalace.
If the caller has not set stream or has set stream=False, MoonPalace will concatenate all the streaming data chunks into a complete completion structure and return it to the caller after receiving all the data chunks.
For the caller (developer), enabling the --force-stream option will not affect the Kimi API response content you receive. You can still use your original code logic to debug and run your program. In other words, enabling the --force-stream option will not change or break anything. You can safely enable this option.

Why provide this option?

We initially hypothesize that common network connection errors and timeouts (Connection Error/Timeout) occur because, in non-streaming request scenarios (stream=False), intermediate gateways or proxy servers may have set read_header_timeout or read_timeout. This can cause the gateway or proxy server to disconnect while the Kimi API server is still assembling the response (since no response, or even the response header, has been received), resulting in Connection Error/Timeout.

We added the --force-stream parameter to MoonPalace. When starting with moonpalace start --force-stream, MoonPalace converts all non-streaming requests (stream=False or unset) to streaming requests. After receiving all data chunks, it assembles them into a complete completion response structure and returns it to the caller.

For the caller, you can still use the non-streaming API as before. However, after MoonPalace's conversion, it can reduce Connection Error/Timeout issues to some extent because MoonPalace has already established a connection with the Kimi API server and started receiving streaming data chunks.

Retrieving Requests
After MoonPalace is started, all requests routed through MoonPalace are recorded in an sqlite database located at $HOME/.moonpalace/moonpalace.sqlite. You can directly connect to the MoonPalace database to query the specific content of the requests, or you can use the MoonPalace command-line tool to query the requests:

$ moonpalace list
+----+--------+-------------------------------------------+--------------------------------------+---------------+---------------------+
| id | status | chatcmpl                                  | request_id                           | server_timing | requested_at        |
+----+--------+-------------------------------------------+--------------------------------------+---------------+---------------------+
| 15 | 200    | cmpl-12be8428ebe74a9e8466a37bee7a9b11     | c34f3421-4dae-11ef-b237-9620e33511ee | 7134          | 2024-07-29 21:30:53 |
| 14 | 200    | cmpl-1bf43a688a2b48eda80042583ff6fe7f     | c13280e0-4dae-11ef-9c01-debcfc72949d | 3479          | 2024-07-29 21:30:46 |
| 13 | 200    | chatcmpl-2e1aa823e2c94ebdad66450a0e6df088 | c07c118e-4dae-11ef-b423-62db244b9277 | 1033          | 2024-07-29 21:30:43 |
| 12 | 200    | cmpl-e7f984b5f80149c3adae46096a6f15c2     | 50d5686c-4d98-11ef-ba65-3613954e2587 | 774           | 2024-07-29 18:50:06 |
| 11 | 200    | chatcmpl-08f7d482b8434a869b001821cf0ee0d9 | 4c20f0a4-4d98-11ef-999a-928b67d58fa8 | 593           | 2024-07-29 18:49:58 |
| 10 | 200    | chatcmpl-6f3cf14db8e044c6bfd19689f6f66eb4 | 49f30295-4d98-11ef-95d0-7a2774525b85 | 738           | 2024-07-29 18:49:55 |
| 9  | 200    | cmpl-2a70a8c9c40e4bcc9564a5296a520431     | 7bd58976-4d8a-11ef-999a-928b67d58fa8 | 40488         | 2024-07-29 17:11:45 |
| 8  | 200    | chatcmpl-59887f868fc247a9a8da13cfbb15d04f | ceb375ea-4d7d-11ef-bd64-3aeb95b9dfac | 867           | 2024-07-29 15:40:21 |
| 7  | 200    | cmpl-36e5e21b1f544a80bf9ce3f8fc1fce57     | cd7f48d6-4d7d-11ef-999a-928b67d58fa8 | 794           | 2024-07-29 15:40:19 |
| 6  | 200    | cmpl-737d27673327465fb4827e3797abb1b3     | cc6613ac-4d7d-11ef-95d0-7a2774525b85 | 670           | 2024-07-29 15:40:17 |
+----+--------+-------------------------------------------+--------------------------------------+---------------+---------------------+

Use the list command to view the content of the most recent requests. By default, it displays fields that are easy to search, such as id/chatcmpl/request_id, as well as status/server_timing/requested_at for checking the request status. If you want to view a specific request, you can use the inspect command to retrieve it:

# The following three commands will retrieve the same request information
$ moonpalace inspect --id 13
$ moonpalace inspect --chatcmpl chatcmpl-2e1aa823e2c94ebdad66450a0e6df088
$ moonpalace inspect --requestid c07c118e-4dae-11ef-b423-62db244b9277
+--------------------------------------------------------------+
| metadata                                                     |
+--------------------------------------------------------------+
| {                                                            |
|     "chatcmpl": "chatcmpl-2e1aa823e2c94ebdad66450a0e6df088", |
|     "content_type": "application/json",                      |
|     "group_id": "enterprise-tier-5",                         |
|     "moonpalace_id": "13",                                   |
|     "request_id": "c07c118e-4dae-11ef-b423-62db244b9277",    |
|     "requested_at": "2024-07-29 21:30:43",                   |
|     "server_timing": "1033",                                 |
|     "status": "200 OK",                                      |
|     "user_id": "cn0psmmcp7fclnphkcpg"                        |
| }                                                            |
+--------------------------------------------------------------+

By default, the inspect command does not print the body of the request and response. If you want to print the body, you can use the following command:

$ moonpalace inspect --chatcmpl chatcmpl-2e1aa823e2c94ebdad66450a0e6df088 --print request_body,response_body
# Since the body information is too lengthy, the detailed content of the body is not shown here
+--------------------------------------------------+--------------------------------------------------+
| request_body                                     | response_body                                    |
+--------------------------------------------------+--------------------------------------------------+
| ...                                              | ...                                              |
+--------------------------------------------------+--------------------------------------------------+

Exporting Requests
If you find that a request does not meet your expectations, or if you want to report a request to Moonshot AI (whether it's a Good Case or a Bad Case, we welcome both), you can use the export command to export a specific request:

# You only need to choose one of the id/chatcmpl/requestid options to retrieve the corresponding request
$ moonpalace export \
    --id 13 \
    --chatcmpl chatcmpl-2e1aa823e2c94ebdad66450a0e6df088 \
    --requestid c07c118e-4dae-11ef-b423-62db244b9277 \
    --good/--bad \
    --tag "code" --tag "python" \
    --directory $HOME/Downloads/

Here, the usage of id/chatcmpl/requestid is the same as in the inspect command, used to retrieve a specific request. The --good/--bad options are used to mark the request as a Good Case or a Bad Case. The --tag option is used to add relevant tags to the request. For example, in the example above, we assume that the request is related to the Python programming language, so we add two tags: code and python. The --directory option specifies the path to the directory where the exported file will be saved.

The content of the successfully exported file is:

$ cat $HOME/Downloads/chatcmpl-2e1aa823e2c94ebdad66450a0e6df088.json
{
    "metadata":
    {
        "chatcmpl": "chatcmpl-2e1aa823e2c94ebdad66450a0e6df088",
        "content_type": "application/json",
        "group_id": "enterprise-tier-5",
        "moonpalace_id": "13",
        "request_id": "c07c118e-4dae-11ef-b423-62db244b9277",
        "requested_at": "2024-07-29 21:30:43",
        "server_timing": "1033",
        "status": "200 OK",
        "user_id": "cn0psmmcp7fclnphkcpg"
    },
    "request":
    {
        "url": "https://api.moonshot.ai/v1/chat/completions",
        "header": "Accept: application/json\r\nAccept-Encoding: gzip\r\nConnection: keep-alive\r\nContent-Length: 2450\r\nContent-Type: application/json\r\nUser-Agent: OpenAI/Python 1.36.1\r\nX-Stainless-Arch: arm64\r\nX-Stainless-Async: false\r\nX-Stainless-Lang: python\r\nX-Stainless-Os: MacOS\r\nX-Stainless-Package-Version: 1.36.1\r\nX-Stainless-Runtime: CPython\r\nX-Stainless-Runtime-Version: 3.11.6\r\n",
        "body":
        {}
    },
    "response":
    {
        "status": "200 OK",
        "header": "Content-Encoding: gzip\r\nContent-Type: application/json; charset=utf-8\r\nDate: Mon, 29 Jul 2024 13:30:43 GMT\r\nMsh-Cache: updated\r\nMsh-Gid: enterprise-tier-5\r\nMsh-Request-Id: c07c118e-4dae-11ef-b423-62db244b9277\r\nMsh-Trace-Mode: on\r\nMsh-Uid: cn0psmmcp7fclnphkcpg\r\nServer: nginx\r\nServer-Timing: inner; dur=1033\r\nStrict-Transport-Security: max-age=15724800; includeSubDomains\r\nVary: Accept-Encoding\r\nVary: Origin\r\n",
        "body":
        {}
    },
    "category": "goodcase",
    "tags":
    [
        "code",
        "python"
    ]
}

We recommend that developers use Github Issues to submit Good Cases or Bad Cases, but if you do not want to make your request information public, you can also submit the Case to us via enterprise WeChat, email, or other means.

You can send the exported file to the following email address:

api-feedback@moonshot.cn

Last updated on 



Use the Kimi API for Multi-turn Chat
The Kimi API is different from the Kimi intelligent assistant. The API itself doesn't have a memory function; it's stateless. This means that when you make multiple requests to the API, the Kimi large language model doesn't remember what you asked in the previous request. For example, if you tell the Kimi large language model that you are 27 years old in one request, it won't remember that you are 27 years old in the next request.

So, we need to manually keep track of the context for each request. In other words, we have to manually add the content of the previous request to the next one so that the Kimi large language model can see what we have talked about before. We will modify the example used in the previous chapter to show how to maintain a list of messages to give the Kimi large language model a memory and enable multi-turn conversation functionality.

Note: We have added the key points for implementing multi-turn conversations as comments in the code.

from openai import OpenAI
 
client = OpenAI(
    api_key = "MOONSHOT_API_KEY", # Replace MOONSHOT_API_KEY with the API Key you obtained from the Kimi Open Platform
    base_url = "https://api.moonshot.ai/v1",
)
 
# We define a global variable messages to keep track of the historical conversation messages between us and the Kimi large language model
# The messages include both the questions we ask the Kimi large language model (role=user) and the replies it gives us (role=assistant)
# Of course, it also includes the initial System Prompt (role=system)
# The messages in the list are arranged in chronological order
messages = [
	{"role": "system", "content": "You are Kimi, an artificial intelligence assistant provided by Moonshot AI. You are better at conversing in Chinese and English. You provide users with safe, helpful, and accurate answers. At the same time, you refuse to answer any questions involving terrorism, racism, pornography, or violence. Moonshot AI is a proper noun and should not be translated into other languages."},
]
 
def chat(input: str) -> str:
	"""
	The chat function supports multi-turn conversations. Each time the chat function is called to converse with the Kimi large language model, the model will 'see' the historical conversation messages that have already been generated. In other words, the Kimi large language model has a memory.
	"""
 
  global messages
 
	# We construct the user's latest question as a message (role=user) and add it to the end of the messages list
	messages.append({
		"role": "user",
		"content": input,	
	})
 
	# We converse with the Kimi large language model, carrying the messages along
	completion = client.chat.completions.create(
        model="kimi-k2-turbo-preview",
        messages=messages,
        temperature=0.6,
    )
 
	# Through the API, we receive the reply message (role=assistant) from the Kimi large language model
    assistant_message = completion.choices[0].message
 
    # To give the Kimi large language model a complete memory, we must also add the message it returns to us to the messages list
    messages.append(assistant_message)
 
    return assistant_message.content
 
print(chat("Hello, I am 27 years old this year."))
print(chat("Do you know how old I am this year?")) # Here, based on the previous context, the Kimi large language model will know that you are 27 years old

Let's review the key points in the code above:

The Kimi API itself doesn't have a context memory function. We need to manually inform the Kimi large language model of what we have talked about before through the messages parameter in the API;
In the messages, we need to store both the question messages we ask the Kimi large language model (role=user) and the reply messages it gives us (role=assistant);
It's important to note that in the code above, as the number of chat calls increases, the length of the messages list also keeps growing. This means that the number of Tokens consumed by each request is also increasing. Eventually, at some point, the Tokens occupied by the messages in the messages list will exceed the context window size supported by the Kimi large language model. We recommend that you use some strategy to keep the number of messages in the messages list within a manageable range. For example, you could only keep the latest 20 messages as the context for each request.

We provide an example below to help you understand how to control the context length. Pay attention to how the make_messages function works:

from openai import OpenAI 
 
client = OpenAI(
    api_key = "MOONSHOT_API_KEY", # Replace MOONSHOT_API_KEY with the API Key you obtained from the Kimi Open Platform
    base_url = "https://api.moonshot.ai/v1",
)
 
# We place the System Messages in a separate list because every request should carry the System Messages.
system_messages = [
	{"role": "system", "content": "You are Kimi, an AI assistant provided by Moonshot AI. You are more proficient in conversing in Chinese and English. You provide users with safe, helpful, and accurate responses. You also reject any questions involving terrorism, racism, pornography, or violence. Moonshot AI is a proper noun and should not be translated into other languages."},
]
 
# We define a global variable messages to record the historical conversation messages between us and the Kimi large language model.
# The messages include both the questions we pose to the Kimi large language model (role=user) and the replies from the Kimi large language model (role=assistant).
# The messages are arranged in chronological order.
messages = []
 
 
def make_messages(input: str, n: int = 20) -> list[dict]:
	"""
	The make_messages function controls the number of messages in each request to keep it within a reasonable range, such as the default value of 20. When building the message list, we first add the System Prompt because it is essential no matter how the messages are truncated. Then, we obtain the latest n messages from the historical records as the messages for the request. In most scenarios, this ensures that the number of Tokens occupied by the request messages does not exceed the model's context window.
	"""
	# First, we construct the user's latest question into a message (role=user) and add it to the end of the messages list.
	messages.append({
		"role": "user",
		"content": input,	
	})
 
	# new_messages is the list of messages we will use for the next request. Let's build it now.
	new_messages = []
 
	# Every request must carry the System Messages, so we need to add the system_messages to the message list first.
	# Note that even if the messages are truncated, the System Messages should still be in the messages list.
	new_messages.extend(system_messages)
 
	# Here, when the historical messages exceed n, we only keep the latest n messages.
	if len(messages) > n:
		messages = messages[-n:]
 
	new_messages.extend(messages)
	return new_messages
 
 
def chat(input: str) -> str:
	"""
	The chat function supports multi-turn conversations. Each time the chat function is called to converse with the Kimi large language model, the model can "see" the historical conversation messages that have already been generated. In other words, the Kimi large language model has memory.
	"""
 
	# We converse with the Kimi large language model carrying the messages.
	completion = client.chat.completions.create(
        model="kimi-k2-turbo-preview",
        messages=make_messages(input),
        temperature=0.6,
    )
 
	# Through the API, we obtain the reply message from the Kimi large language model (role=assistant).
    assistant_message = completion.choices[0].message
 
    # To ensure the Kimi large language model has a complete memory, we must add the message returned by the model to the messages list.
    messages.append(assistant_message)
 
    return assistant_message.content
 
print(chat("Hello, I am 27 years old this year."))
print(chat("Do you know how old I am this year?")) # Here, based on the previous context, the Kimi large language model will know that you are 27 years old this year.

Please note that the above code examples only consider the simplest invocation scenarios. In actual business code logic, you may need to consider more scenarios and boundaries, such as:

In concurrent scenarios, additional read-write locks may be needed;
For multi-user scenarios, a separate messages list should be maintained for each user;
You may need to persist the messages list;
You may still need a more precise way to determine how many messages to retain in the messages list;
You may want to summarize the discarded messages and generate a new message to add to the messages list;
……
Last updated on 




Use the Kimi API for Multi-turn Chat
The Kimi API is different from the Kimi intelligent assistant. The API itself doesn't have a memory function; it's stateless. This means that when you make multiple requests to the API, the Kimi large language model doesn't remember what you asked in the previous request. For example, if you tell the Kimi large language model that you are 27 years old in one request, it won't remember that you are 27 years old in the next request.

So, we need to manually keep track of the context for each request. In other words, we have to manually add the content of the previous request to the next one so that the Kimi large language model can see what we have talked about before. We will modify the example used in the previous chapter to show how to maintain a list of messages to give the Kimi large language model a memory and enable multi-turn conversation functionality.

Note: We have added the key points for implementing multi-turn conversations as comments in the code.

const OpenAI = require("openai")
 
const client = new OpenAI({
  apiKey = "MOONSHOT_API_KEY", // Replace MOONSHOT_API_KEY with the API Key you obtained from the Kimi Open Platform
  baseURL: "https://api.moonshot.ai/v1",
});
 
// We define a global variable messages to keep track of the historical conversation messages between us and the Kimi large language model
// The messages include both the questions we ask the Kimi large language model (role=user) and the replies it gives us (role=assistant)
// Of course, it also includes the initial System Prompt (role=system)
// The messages in the list are arranged in chronological order
let messages = [
  {
    role: "system",
    content: "You are Kimi, an artificial intelligence assistant provided by Moonshot AI. You are better at conversing in Chinese and English. You provide users with safe, helpful, and accurate answers. At the same time, you refuse to answer any questions involving terrorism, racism, pornography, or violence. Moonshot AI is a proper noun and should not be translated into other languages.",
  },
];
 
async function chat(input) {
  /**
   * The chat function supports multi-turn conversations. Each time the chat function is called to converse with the Kimi large language model, the model will 'see' the historical conversation messages that have already been generated. In other words, the Kimi large language model has a memory.
   */
 
  // We construct the user's latest question as a message (role=user) and add it to the end of the messages list
  messages.push({
    role: "user",
    content: input,
  });
 
  // We converse with the Kimi large language model, carrying the messages along
  const completion = await client.chat.completions.create({
    model: "kimi-k2-turbo-preview",
    messages: messages,
    temperature: 0.6,
  });
 
  // Through the API, we receive the reply message (role=assistant) from the Kimi large language model
  const assistantMessage = completion.choices[0].message;
 
  // To give the Kimi large language model a complete memory, we must also add the message it returns to us to the messages list
  messages.push(assistantMessage);
 
  return assistantMessage.content;
}
 
// Example usage
(async () => {
  console.log(await chat("Hello, I am 27 years old this year."));
  console.log(await chat("Do you know how old I am this year?")); // Here, based on the previous context, the Kimi large language model will know that you are 27 years old
})();

Let's review the key points in the code above:

The Kimi API itself doesn't have a context memory function. We need to manually inform the Kimi large language model of what we have talked about before through the messages parameter in the API;
In the messages, we need to store both the question messages we ask the Kimi large language model (role=user) and the reply messages it gives us (role=assistant);
It's important to note that in the code above, as the number of chat calls increases, the length of the messages list also keeps growing. This means that the number of Tokens consumed by each request is also increasing. Eventually, at some point, the Tokens occupied by the messages in the messages list will exceed the context window size supported by the Kimi large language model. We recommend that you use some strategy to keep the number of messages in the messages list within a manageable range. For example, you could only keep the latest 20 messages as the context for each request.

We provide an example below to help you understand how to control the context length. Pay attention to how the make_messages function works:

const OpenAI = require("openai")
 
const client = new OpenAI({
  apiKey: "MOONSHOT_API_KEY", // Replace MOONSHOT_API_KEY with the API Key you obtained from the Kimi Open Platform
  baseURL: "https://api.moonshot.ai/v1",
});
 
// We place the System Messages in a separate list because every request should carry the System Messages.
const systemMessages = [
  {
    role: "system",
    content: "You are Kimi, an AI assistant provided by Moonshot AI. You are more proficient in conversing in Chinese and English. You provide users with safe, helpful, and accurate responses. You also reject any questions involving terrorism, racism, pornography, or violence. Moonshot AI is a proper noun and should not be translated into other languages.",
  },
];
 
// We define a global variable messages to record the historical conversation messages between us and the Kimi large language model.
// The messages include both the questions we pose to the Kimi large language model (role=user) and the replies from the Kimi large language model (role=assistant).
// The messages are arranged in chronological order.
let messages = [];
 
async function makeMessages(input, n = 20) {
  /**
   * The makeMessages function controls the number of messages in each request to keep it within a reasonable range, such as the default value of 20. When building the message list, we first add the System Prompt because it is essential no matter how the messages are truncated. Then, we obtain the latest n messages from the historical records as the messages for the request. In most scenarios, this ensures that the number of Tokens occupied by the request messages does not exceed the model's context window.
   */
  // First, we construct the user's latest question into a message (role=user) and add it to the end of the messages list.
  messages.push({
    role: "user",
    content: input,
  });
 
  // newMessages is the list of messages we will use for the next request. Let's build it now.
  let newMessages = [];
 
  // Every request must carry the System Messages, so we need to add the systemMessages to the message list first.
  // Note that even if the messages are truncated, the System Messages should still be in the messages list.
  newMessages = systemMessages.concat(newMessages);
 
  // Here, when the historical messages exceed n, we only keep the latest n messages.
  if (messages.length > n) {
    messages = messages.slice(-n);
  }
 
  newMessages = newMessages.concat(messages);
  return newMessages;
}
 
async function chat(input) {
  /**
   * The chat function supports multi-turn conversations. Each time the chat function is called to converse with the Kimi large language model, the model can "see" the historical conversation messages that have already been generated. In other words, the Kimi large language model has memory.
   */
 
  // We converse with the Kimi large language model carrying the messages.
  const completion = await client.chat.completions.create({
    model: "kimi-k2-turbo-preview",
    messages: await makeMessages(input),
    temperature: 0.6,
  });
 
  // Through the API, we obtain the reply message from the Kimi large language model (role=assistant).
  const assistantMessage = completion.choices[0].message;
 
  // To ensure the Kimi large language model has a complete memory, we must add the message returned by the model to the messages list.
  messages.push(assistantMessage);
 
  return assistantMessage.content;
}
 
(async () => {
  console.log(await chat("Hello, I am 27 years old this year."));
  console.log(await chat("Do you know how old I am this year?")); // Here, based on the previous context, the Kimi large language model will know that you are 27 years old this year.
})();

Please note that the above code examples only consider the simplest invocation scenarios. In actual business code logic, you may need to consider more scenarios and boundaries, such as:

In concurrent scenarios, additional read-write locks may be needed;
For multi-user scenarios, a separate messages list should be maintained for each user;
You may need to persist the messages list;
You may still need a more precise way to determine how many messages to retain in the messages list;
You may want to summarize the discarded messages and generate a new message to add to the messages list;
……
Last updated on 



Use the Kimi Vision Model
The Kimi Vision Model (including moonshot-v1-8k-vision-preview / moonshot-v1-32k-vision-preview / moonshot-v1-128k-vision-preview and so on) can understand the content of images, including text in the image, colors, and the shapes of objects. Here is how you can ask Kimi questions about an image using the following code:

import os
import base64
 
from openai import OpenAI
 
client = OpenAI(
    api_key=os.environ.get("MOONSHOT_API_KEY"),
    base_url="https://api.moonshot.ai/v1",
)
 
# Replace kimi.png with the path to the image you want Kimi to recognize
image_path = "kimi.png"
 
with open(image_path, "rb") as f:
    image_data = f.read()
 
# We use the built-in base64.b64encode function to encode the image into a base64 formatted image_url
image_url = f"data:image/{os.path.splitext(image_path)[1]};base64,{base64.b64encode(image_data).decode('utf-8')}"
 
 
completion = client.chat.completions.create(
    model="moonshot-v1-8k-vision-preview",
    messages=[
        {"role": "system", "content": "You are Kimi."},
        {
            "role": "user",
            # Note here, the content has changed from the original str type to a list. This list contains multiple parts, with the image (image_url) being one part and the text (text) being another part.
            "content": [
                {
                    "type": "image_url", # <-- Use the image_url type to upload the image, the content is the base64 encoded image
                    "image_url": {
                        "url": image_url,
                    },
                },
                {
                    "type": "text",
                    "text": "Describe the content of the image.", # <-- Use the text type to provide text instructions, such as "Describe the content of the image"
                },
            ],
        },
    ],
)
 
print(completion.choices[0].message.content)

Note that when using the Vision model, the type of the message.content field has changed from str to List[Dict] (i.e., a JSON array). Additionally, do not serialize the JSON array and put it into message.content as a str. This will cause Kimi to fail to correctly identify the image type and may trigger the Your request exceeded model token limit error.

✅ Correct Format:

{
    "model": "moonshot-v1-8k-vision-preview",
    "messages":
    [
        {
            "role": "system",
            "content": "You are Kimi, an AI assistant provided by Moonshot AI, who excels in Chinese and English conversations. You provide users with safe, helpful, and accurate answers. You will reject any questions related to terrorism, racism, or explicit content. Moonshot AI is a proper noun and should not be translated into other languages."
        },
        {
            "role": "user",
            "content":
            [
                {
                    "type": "image_url",
                    "image_url":
                    {
                        "url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABhCAYAAAApxKSdAAAACXBIWXMAACE4AAAhOAFFljFgAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAUUSURBVHgB7Z29bhtHFIWPHQN2J7lKqnhYpYvpIukCbJEAKQJEegLReYFIT0DrCSI9QEDqCSIDaQIEIOukiJwyza5SJWlId3FFz+HuGmuSSw6p+dlZ3g84luhdUeI9M3fmziyXgBCUe/DHYY0Wj/tgWmjV42zFcWe4MIBBPNJ6qqW0uvAbXFvQgKzQK62bQhkaCIPc10q1Zi3XH1o/IG9cwUm0RogrgDY1KmLgHYX9DvyiBvDYI77XmiD+oLlQHw7hIDoCMBOt1U9w0BsU9mOAtaUUFk3oQoIfzAQFCf5dNMEdTFCQ4NtQih1NSIGgf3ibxOJt5UrAB1gNK72vIdjiI61HWr+YnNxDXK0rJiULsV65GJeiIescLSTTeobKSutiCuojX8kU3MBx4I3WeNVBBRl4fWiCyoB8v2JAAkk9PmDwT8sH1TEghRjgC27scCx41wO43KAg+ILxTvhNaUACwTc04Z0B30LwzTzm5Rjw3sgseIG1wGMawMBPIOQcqvzrNIMHOg9Q5KK953O90/rFC+BhJRH8PQZ+fu7SjC7HAIV95yu99vjlxfvBJx8nwHd6IfNJAkccOjHg6OgIs9lsra6vr2GTNE03/k7q8HAhyJ/2gM9O65/4kT7/mwEcoZwYsPQiV3BwcABb9Ho9KKU2njccDjGdLlxx+InBBPBAAR86ydRPaIC9SASi3+8bnXd+fr78nw8NJ39uDJjXAVFPP7dp/VmWLR9g6w6Huo/IOTk5MTpvZesn/93AiP/dXCwd9SyILT9Jko3n1bZ+8s8rGPGvoVHbEXcPMM39V1dX9Qd/19PPNxta959D4HUGF0RrAFs/8/8mxuPxXLUwtfx2WX+cxdivZ3DFA0SKldZPuPTAKrikbOlMOX+9zFu/Q2iAQoSY5H7mfeb/tXCT8MdneU9wNNCuQUXZA0ynnrUznyqOcrspUY4BJunHqPU3gOgMsNr6G0B0BpgUXrG0fhKVAaaF1/HxMWIhKgNMcj9Tz82Nk6rVGdav/tJ5eraJ0Wi01XPq1r/xOS8uLkJc6XYnRTMNXdf62eIvLy+jyftVghnQ7Xahe8FW59fBTRYOzosDNI1hJdz0lBQkBflkMBjMU5iL13pXRb8fYAJrB/a2db0oFHthAOEUliaYFHE+aaUBdZsvvFhApyM0idYZwOCvW4JmIWdSzPmidQaYrAGZ7iX4oFUGnJ2dGdUCTRqMozeANQCLsE6nA10JG/0Mx4KmDMbBCjEWR2yxu8LAM98vXelmCA2ovVLCI8EMYODWbpbvCXtTBzQVMSAwYkBgxIDAtNKAXWdGIRADAiMpKDA0IIMQikx6QGDEgMCIAYGRMSAsMgaEhgbcQgjFa+kBYZnIGBCWWzEgLPNBOJ6Fk/aR8Y5ZCvktKwX/PJZ7xoVjfs+4chYU11tK2sE85qUBLyH4Zh5z6QHhGPOf6r2j+TEbcgdFP2RaHX5TrYQlDflj5RXE5Q1cG/lWnhYpReUGKdUewGnRmhvnCJbgmxey8sHiZ8iwF3AsUBBckKHI/SWLq6HsBc8huML4DiK80D6WnBqLzN68UFCmopheYJOVYgcU5FOVbAVfYUcUZGoaLPglCtITdg2+tZUFBTFh2+ArWEYh/7z0WIIQSiM43lt5AWAmWhLHylN4QmkNEXfAbGqEQKsHSfHLYwiSq8AnaAAKeaW3D8VbijwNW5nh3IN9FPI/jnpaPKZi2/SfFuJu4W3x9RqWL+N5C+7ruKpBAgLkAAAAAElFTkSuQmCC"
                    }
                },
                {
                    "type": "text",
                    "text": "Please describe this image."
                }
            ]
        }
    ],
    "temperature": 0.3
}

❌ Invalid Format：

{
    "model": "moonshot-v1-8k-vision-preview",
    "messages":
    [
        {
            "role": "system",
            "content": "You are Kimi, an AI assistant provided by Moonshot AI. You are proficient in Chinese and English conversations. You provide users with safe, helpful, and accurate responses. You will refuse to answer any questions involving terrorism, racism, or explicit content. Moonshot AI is a proper noun and should not be translated into other languages."
        },
        {
            "role": "user",
            "content": "[{\"type\": \"image_url\", \"image_url\": {\"url\": \"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABhCAYAAAApxKSdAAAACXBIWXMAACE4AAAhOAFFljFgAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAUUSURBVHgB7Z29bhtHFIWPHQN2J7lKqnhYpYvpIukCbJEAKQJEegLReYFIT0DrCSI9QEDqCSIDaQIEIOukiJwyza5SJWlId3FFz+HuGmuSSw6p+dlZ3g84luhdUeI9M3fmziyXgBCUe/DHYY0Wj/tgWmjV42zFcWe4MIBBPNJ6qqW0uvAbXFvQgKzQK62bQhkaCIPc10q1Zi3XH1o/IG9cwUm0RogrgDY1KmLgHYX9DvyiBvDYI77XmiD+oLlQHw7hIDoCMBOt1U9w0BsU9mOAtaUUFk3oQoIfzAQFCf5dNMEdTFCQ4NtQih1NSIGgf3ibxOJt5UrAB1gNK72vIdjiI61HWr+YnNxDXK0rJiULsV65GJeiIescLSTTeobKSutiCuojX8kU3MBx4I3WeNVBBRl4fWiCyoB8v2JAAkk9PmDwT8sH1TEghRjgC27scCx41wO43KAg+ILxTvhNaUACwTc04Z0B30LwzTzm5Rjw3sgseIG1wGMawMBPIOQcqvzrNIMHOg9Q5KK953O90/rFC+BhJRH8PQZ+fu7SjC7HAIV95yu99vjlxfvBJx8nwHd6IfNJAkccOjHg6OgIs9lsra6vr2GTNE03/k7q8HAhyJ/2gM9O65/4kT7/mwEcoZwYsPQiV3BwcABb9Ho9KKU2njccDjGdLlxx+InBBPBAAR86ydRPaIC9SASi3+8bnXd+fr78nw8NJ39uDJjXAVFPP7dp/VmWLR9g6w6Huo/IOTk5MTpvZesn/93AiP/dXCwd9SyILT9Jko3n1bZ+8s8rGPGvoVHbEXcPMM39V1dX9Qd/19PPNxta959D4HUGF0RrAFs/8/8mxuPxXLUwtfx2WX+cxdivZ3DFA0SKldZPuPTAKrikbOlMOX+9zFu/Q2iAQoSY5H7mfeb/tXCT8MdneU9wNNCuQUXZA0ynnrUznyqOcrspUY4BJunHqPU3gOgMsNr6G0B0BpgUXrG0fhKVAaaF1/HxMWIhKgNMcj9Tz82Nk6rVGdav/tJ5eraJ0Wi01XPq1r/xOS8uLkJc6XYnRTMNXdf62eIvLy+jyftVghnQ7Xahe8FW59fBTRYOzosDNI1hJdz0lBQkBflkMBjMU5iL13pXRb8fYAJrB/a2db0oFHthAOEUliaYFHE+aaUBdZsvvFhApyM0idYZwOCvW4JmIWdSzPmidQaYrAGZ7iX4oFUGnJ2dGdUCTRqMozeANQCLsE6nA10JG/0Mx4KmDMbBCjEWR2yxu8LAM98vXelmCA2ovVLCI8EMYODWbpbvCXtTBzQVMSAwYkBgxIDAtNKAXWdGIRADAiMpKDA0IIMQikx6QGDEgMCIAYGRMSAsMgaEhgbcQgjFa+kBYZnIGBCWWzEgLPNBOJ6Fk/aR8Y5ZCvktKwX/PJZ7xoVjfs+4chYU11tK2sE85qUBLyH4Zh5z6QHhGPOf6r2j+TEbcgdFP2RaHX5TrYQlDflj5RXE5Q1cG/lWnhYpReUGKdUewGnRmhvnCJbgmxey8sHiZ8iwF3AsUBBckKHI/SWLq6HsBc8huML4DiK80D6WnBqLzN68UFCmopheYJOVYgcU5FOVbAVfYUcUZGoaLPglCtITdg2+tZUFBTFh2+ArWEYh/7z0WIIQSiM43lt5AWAmWhLHylN4QmkNEXfAbGqEQKsHSfHLYwiSq8AnaAAKeaW3D8VbijwNW5nh3IN9FPI/jnpaPKZi2/SfFuJu4W3x9RqWL+N5C+7ruKpBAgLkAAAAAElFTkSuQmCC\"}}, {\"type\": \"text\", \"text\": \"Please describe this image\"}]"
        }
    ],
    "temperature": 0.3
}

Token Calculation and Costs
Currently, each image consumes a fixed number of 1024 tokens (regardless of image size or quality).

The Vision model follows the same pricing model as the moonshot-v1 series, with costs based on the total tokens used for model inference. For more details, please refer to:

Model Inference Pricing

Features and Limitations
The Vision model supports the following features:

 Multi-turn conversations
 Streaming output
 Tool invocation
 JSON Mode
 Partial Mode
The following features are not supported or only partially supported:

Internet search: Not supported
Auto Context Caching: Not supported
URL-formatted images: Not supported, only base64-encoded image content is currently supported
Other limitations:

Image quantity: The Vision model has no limit on the number of images, but ensure that the request body size does not exceed 100M.
Last updated on 


Automatic Reconnection on Disconnect
Due to concurrency limits, complex network environments, and other unforeseen circumstances, our connections may sometimes be interrupted. Typically, these intermittent disruptions don't last long. We want our services to remain stable even in such cases. Implementing a simple reconnection feature can be achieved with just a few lines of code.

from openai import OpenAI
import time
 
client = OpenAI(
    api_key = "$MOONSHOT_API_KEY",
    base_url = "https://api.moonshot.ai/v1",
)
 
def chat_once(msgs):
    response = client.chat.completions.create(
        model = "kimi-k2-turbo-preview",
        messages = msgs,
        temperature = 0.6,
    )
    return response.choices[0].message.content
 
def chat(input: str, max_attempts: int = 100) -> str:
    messages = [
        {"role": "system", "content": "You are Kimi, an AI assistant provided by Moonshot AI. You are proficient in Chinese and English conversations. You aim to provide users with safe, helpful, and accurate answers. You will refuse to answer any questions related to terrorism, racism, or explicit content. Moonshot AI is a proper noun and should not be translated into other languages."},
    ]
 
    # We construct the user's latest question as a message (role=user) and append it to the end of the messages list
    messages.append({
        "role": "user",
        "content": input,
    })
    st_time = time.time()
    for i in range(max_attempts):
        print(f"Attempts: {i+1}/{max_attempts}")
        try:
            response = chat_once(messages)
            ed_time = time.time()
            print("Query Successful!")
            print(f"Query Time: {ed_time-st_time}")
            return response
        except Exception as e:
            print(e)
            time.sleep(1)
            continue
 
    print("Query Failed.")
    return
 
print(chat("Hello, please tell me a fairy tale."))

The code above implements a simple reconnection feature, allowing up to 100 retries with a 1-second wait between each attempt. You can adjust these values and the conditions for retries based on your specific needs.

Last updated on 


Use the Streaming Feature of the Kimi API
When the Kimi large language model receives a question from a user, it first performs inference and then generates the response one Token at a time. In the examples from our first two chapters, we chose to wait for the Kimi large language model to generate all Tokens before printing its response. This usually takes several seconds. If your question is complex enough and the response from the Kimi large language model is long enough, the time to wait for the complete response can be stretched to 10 or even 20 seconds, which greatly reduces the user experience. To improve this situation and provide timely feedback to users, we offer the ability to stream output, known as Streaming. We will explain the principles of Streaming and illustrate it with actual code:

How to use streaming output;
Common issues when using streaming output;
How to handle streaming output without using the Python SDK;
How to Use Streaming Output
Streaming, in a nutshell, means that whenever the Kimi large language model generates a certain number of Tokens (usually 1 Token), it immediately sends these Tokens to the client, instead of waiting for all Tokens to be generated before sending them to the client. When you chat with Kimi AI Assistant, the assistant's response appears character by character, which is one manifestation of streaming output. Streaming allows users to see the first Token output by the Kimi large language model immediately, reducing wait time.

You can use streaming output in this way (stream=True) and get the streaming response:

const OpenAI = require('openai')
 
client = OpenAI({
    apiKey: "MOONSHOT_API_KEY", // Replace MOONSHOT_API_KEY with the API Key you obtained from the Kimi Open Platform
    baseURL: "https://api.moonshot.ai/v1",
})
 
async function main() {
    stream = await client.chat.completions.create({
        model: "kimi-k2-turbo-preview",
        messages: [
            {role: "system", content: "You are Kimi, an artificial intelligence assistant provided by Moonshot AI, who is better at conversing in Chinese and English. You provide users with safe, helpful, and accurate answers. At the same time, you refuse to answer any questions related to terrorism, racism, pornography, and violence. Moonshot AI is a proper noun and should not be translated into other languages."},
            {role: "user", content: "Hello, my name is Li Lei, what is 1+1?"}
        ],
        temperature: 0.6,
        stream: true, // <-- Note here, we enable streaming output mode by setting stream=True
    })
     
    // When streaming output mode is enabled (stream=True), the content returned by the SDK also changes. We no longer directly access the choice in the return value
    // Instead, we access each individual chunk in the return value through a for loop
     
    for await (chunk of stream) {
        // Here, the structure of each chunk is similar to the previous completion, but the message field is replaced with the delta field
        delta = chunk.choices[0].delta // <-- The message field is replaced with the delta field
     
        if (delta.content) {
            // When printing the content, since it is streaming output, to ensure the coherence of the sentence, we do not add
            // line breaks manually, so we set end="" to cancel the line break of print.
            console.log(delta.content, end="")
        }
    }
}
 
main()

Common Issues When Using Streaming Output
Now that you have successfully run the above code and understood the basic principles of streaming output, let's discuss some details and common issues of streaming output so that you can better implement your business logic.

Interface Details
When streaming output mode is enabled (stream=True), the Kimi large language model no longer returns a response in JSON format (Content-Type: application/json), but uses Content-Type: text/event-stream (abbreviated as SSE). This response format allows the server to continuously send data to the client. In the context of using the Kimi large language model, it can be understood as the server continuously sending Tokens to the client.

When you look at the HTTP response body of SSE, it looks like this:

data: {"id":"cmpl-1305b94c570f447fbde3180560736287","object":"chat.completion.chunk","created":1698999575,"model":"kimi-k2-turbo-preview","choices":[{"index":0,"delta":{"role":"assistant","content":""},"finish_reason":null}]}
 
data: {"id":"cmpl-1305b94c570f447fbde3180560736287","object":"chat.completion.chunk","created":1698999575,"model":"kimi-k2-turbo-preview","choices":[{"index":0,"delta":{"content":"Hello"},"finish_reason":null}]}
 
...
 
data: {"id":"cmpl-1305b94c570f447fbde3180560736287","object":"chat.completion.chunk","created":1698999575,"model":"kimi-k2-turbo-preview","choices":[{"index":0,"delta":{"content":"."},"finish_reason":null}]}
 
data: {"id":"cmpl-1305b94c570f447fbde3180560736287","object":"chat.completion.chunk","created":1698999575,"model":"kimi-k2-turbo-preview","choices":[{"index":0,"delta":{},"finish_reason":"stop","usage":{"prompt_tokens":19,"completion_tokens":13,"total_tokens":32}}]}
 
data: [DONE]

In the response body of SSE, we agree that each data chunk starts with data: , followed by a valid JSON object, and ends with two newline characters \n\n. Finally, when all data chunks have been transmitted, data: [DONE] is used to indicate that the transmission is complete, at which point the network connection can be disconnected.

Token Calculation
When using the streaming output mode, there are two ways to calculate tokens. The most straightforward and accurate method is to wait until all data chunks have been transmitted and then check the prompt_tokens, completion_tokens, and total_tokens in the usage field of the last data chunk.

...
 
data: {"id":"cmpl-1305b94c570f447fbde3180560736287","object":"chat.completion.chunk","created":1698999575,"model":"kimi-k2-turbo-preview","choices":[{"index":0,"delta":{},"finish_reason":"stop","usage":{"prompt_tokens":19,"completion_tokens":13,"total_tokens":32}}]}
                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                               Check the number of tokens generated by the current request through the usage field in the last data chunk
data: [DONE]

However, in practice, streaming output can be interrupted by uncontrollable factors such as network disconnections or client-side errors. In such cases, the last data chunk may not have been fully transmitted, making it impossible to know the total number of tokens consumed by the request. To avoid this issue, we recommend saving the content of each data chunk as it is received and then using the token calculation interface to compute the total consumption after the request ends, regardless of whether it was successful or not. Here is an example code snippet:

const axios = require('axios');
const OpenAI = require('openai');
 
client = new OpenAI({
    apiKey: process.env.MOONSHOT_API_KEY,
    baseURL: "https://api.moonshot.ai/v1",
})
 
 
async function estimate_token_count(input_messages) {
    /*
    Implement your token calculation logic here, or directly call our token calculation interface to compute tokens.
 
    https://api.moonshot.ai/v1/tokenizers/estimate-token-count
    */
    header = {
        "Authorization": `Bearer ${process.env.MOONSHOT_API_KEY}`,
    }
    data = {
        "model": "kimi-k2-turbo-preview",
        "messages": input_messages,
    }
    r = await axios.post("https://api.moonshot.ai/v1/tokenizers/estimate-token-count", data, {headers: header})
    .catch(function (error) {
        console.log(error)
    })
    return r.data.data.total_tokens
} 
 
async function main() {
 
    stream = await client.chat.completions.create({
        model: "kimi-k2-turbo-preview",
        messages: [
            {role: "system", content: "You are Kimi, an AI assistant provided by Moonshot AI, who excels in Chinese and English conversations. You provide users with safe, helpful, and accurate answers while rejecting any questions related to terrorism, racism, or explicit content. Moonshot AI is a proper noun and should not be translated."},
            {role: "user", content: "Hello, my name is Li Lei. What is 1+1?"}
        ],
        temperature: 0.6,
        stream: true, // <-- Note here, we enable streaming output mode by setting stream=True
    })
    
    completion = []
    for await (chunk of stream) {
        delta = chunk.choices[0].delta
        if (delta.content) {
            completion.append(delta.content)
        }
    } 
     
    console.log("completion_tokens:", await estimate_token_count("".join(completion)))
}

How to Terminate Output
If you want to stop the streaming output, you can simply close the HTTP connection or discard any subsequent data chunks. For example:

for chunk in stream:
	if condition:
		break

How to Handle Streaming Output Without Using an SDK
If you prefer not to use the Python SDK to handle streaming output and instead want to directly interface with HTTP APIs to use the Kimi large language model (for example, in cases where you are using a language without an SDK, or you have unique business logic that the SDK cannot meet), we provide some examples to help you understand how to properly handle the SSE response body in HTTP (we still use Python code as an example here, with detailed explanations provided in comments).

const axios = require('axios'); // Use the axios library to make HTTP requests
 
let data = {
    "model": "kimi-k2-turbo-preview",
    "messages": [
        // Specific messages
    ],
    "temperature": 0.6,
    "stream": true,
};
 
// Use axios to send a chat request to the Kimi large language model and get the response r
axios.post("https://api.moonshot.ai/v1/chat/completions", data, {
    responseType: 'stream'
}).then(response => {
    let data = '';
    response.data.on('data', chunk => {
        // Remove leading and trailing spaces from each line to better handle data chunks
        let line = chunk.toString().trim();
 
        // Next, we need to handle three different cases:
        //   1. If the current line is empty, it indicates that the previous data chunk has been received (as mentioned earlier, the data chunk transmission ends with two newline characters), we can deserialize the data chunk and print the corresponding content;
        //   2. If the current line is not empty and starts with data:, it indicates the start of a data chunk transmission, we remove the data: prefix and first check if it is the end symbol [DONE], if not, save the data content to the data variable;
        //   3. If the current line is not empty but does not start with data:, it indicates that the current line still belongs to the previous data chunk being transmitted, we append the content of the current line to the end of the data variable;
 
        if (line === '') {
            try {
                let chunk = JSON.parse(data);
                // The processing logic here can be replaced with your business logic, printing is just to demonstrate the process
                let choice = chunk.choices[0];
                let usage = choice.usage;
                if (usage) {
                    console.log("total_tokens:", usage.total_tokens);
                }
                let delta = choice.delta;
                let role = delta.role;
                if (role) {
                    console.log("role:", role);
                }
                let content = delta.content;
                if (content) {
                    console.log(content);
                }
            } catch (error) {
                console.error("Error parsing JSON:", error);
            }
            data = ''; // Reset data
        } else if (line.startsWith('data: ')) {
            data = line.substring(6);
            // When the data chunk content is [DONE], it indicates that all data chunks have been sent, and the network connection can be disconnected
            if (data === '[DONE]') {
                response.data.destroy();
            }
        } else {
            data += '\n' + line; // We still add a newline character when appending content, as this data chunk may intentionally format the data in separate lines
        }
    }).catch(error => {
        console.error("Error in request:", error);
    });
}).catch(error => {
    console.error("Error in request:", error);
});

The above is the process of handling streaming output using Python as an example. If you are using other languages, you can also properly handle the content of streaming output. The basic steps are as follows:

Initiate an HTTP request and set the stream parameter in the request body to true;
Receive the response from the server. Note that if the Content-Type in the response Headers is text/event-stream, it indicates that the response content is a streaming output;
Read the response content line by line and parse the data chunks (the data chunks are presented in JSON format). Pay attention to determining the start and end positions of the data chunks through the data: prefix and newline character \n;
Determine whether the transmission is complete by checking if the current data chunk content is [DONE];
Note: Always use data: [DONE] to determine if the data has been fully transmitted, rather than using finish_reason or other methods. If you do not receive the data: [DONE] message chunk, even if you have obtained the information finish_reason=stop, you should not consider the data chunk transmission as complete. In other words, until you receive the data: [DONE] data chunk, the message should be considered incomplete.

During the streaming output process, only the content field is streamed, meaning each data chunk contains a portion of the content tokens. For fields that do not need to be streamed, such as role and usage, we usually present them all at once in the first or last data chunk, rather than including the role and usage fields in every data chunk (specifically, the role field will only appear in the first data chunk and will not be included in subsequent data chunks; the usage field will only appear in the last data chunk and will not be included in the preceding data chunks).

Handling n>1
Sometimes, we want to get multiple results to choose from. To do this, you should set the n parameter in the request to a value greater than 1. When it comes to stream output, we also support the use of n>1. In such cases, we need to add some extra code to determine the index value of the current data block, to figure out which response the data block belongs to. Let's illustrate this with example code:

const axios = require('axios'); // Use the axios library to make HTTP requests
 
let data = {
    "model": "kimi-k2-turbo-preview",
    "messages": [
        // Specific messages go here
    ],
    "temperature": 0.6,
    "stream": true,
    "n": 2 // <-- Note here, we're asking the Kimi large language model to output 2 responses
};
 
// Use axios to send a chat request to the Kimi large language model and get the response
axios.post("https://api.moonshot.ai/v1/chat/completions", data, {
    responseType: 'stream'
}).then(response => {
    let data = '';
    let messages = [{}, {}]; // Pre-build a List to store different response messages
 
    response.data.on('data', chunk => {
        let line = chunk.toString().trim();
 
        if (line === '') {
            try {
                let chunk = JSON.parse(data);
                for (let choice of chunk.choices) {
                    let index = choice.index;
                    let message = messages[index];
                    let usage = choice.usage;
                    if (usage) {
                        message.usage = usage;
                    }
                    let delta = choice.delta;
                    let role = delta.role;
                    if (role) {
                        message.role = role;
                    }
                    let content = delta.content;
                    if (content) {
                        message.content = message.content + content;
                    }
                }
            } catch (error) {
                console.error("Error parsing JSON:", error);
            }
            data = ''; // Reset data
        } else if (line.startsWith('data: ')) {
            data = line.substring(6);
 
            if (data === '[DONE]') {
                response.data.destroy();
            }
        } else {
            data += '\n' + line; // When appending content, add a newline character
        }
    }).on('end', () => {
        // After assembling all messages, print their contents separately
        for (let index = 0; index < messages.length; index++) {
            console.log("index:", index);
            console.log("message:", JSON.stringify(messages[index], null, 2));
        }
    }).catch(error => {
        console.error("Error in request:", error);
    });
}).catch(error => {
    console.error("Error in request:", error);
});

When n>1, the key to handling stream output is to first determine which response message the current data block belongs to based on its index value, and then proceed with further logical processing.

Last updated on 


Use Kimi API for Tool Calls
Tool calls, or tool_calls, evolved from function calls (function_call). In certain contexts, or when reading compatibility code, you can consider tool_calls and function_call to be the same. function_call is a subset of tool_calls.

What are Tool Calls?
Tool calls give the Kimi large language model the ability to perform specific actions. The Kimi large language model can engage in conversations and answer questions, which is its "talking" ability. Through tool calls, it also gains the ability to "do" things. With tool_calls, the Kimi large language model can help you search the internet, query databases, and even control smart home devices.

A tool call involves several steps:

Define the tool using JSON Schema format;
Submit the defined tool to the Kimi large language model via the tools parameter. You can submit multiple tools at once;
The Kimi large language model will decide which tool(s) to use based on the context of the current conversation. It can also choose not to use any tools;
The Kimi large language model will output the parameters and information needed to call the tool in JSON format;
Use the parameters output by the Kimi large language model to execute the corresponding tool and submit the results back to the Kimi large language model;
The Kimi large language model will respond to the user based on the results of the tool execution;
Reading the above steps, you might wonder:

Why can't the Kimi large language model execute the tools itself? Why do we need to "help" the Kimi large language model execute the tools based on the parameters it generates? If we are the ones executing the tool calls, what is the role of the Kimi large language model?

We will use a practical example of a tool call to explain these questions to the reader.

Enable the Kimi Large Language Model to Access the Internet via tool_calls
The knowledge of the Kimi large language model comes from its training data. For questions that are time-sensitive, the Kimi large language model cannot find answers from its existing knowledge. In such cases, we want the Kimi large language model to search the internet for the latest information and answer our questions based on that information.

Define the Tools
Imagine how we find the information we want on the internet:

We open a search engine, such as Baidu or Bing, and search for the content we want. We then browse the search results and decide which one to click based on the website title and description;
We might open one or more web pages from the search results and browse them to obtain the knowledge we need;
Reviewing our actions, we "use a search engine to search" and "open the web pages corresponding to the search results." The tools we use are the "search engine" and the "web browser." Therefore, we need to abstract these actions into tools in JSON Schema format and submit them to the Kimi large language model, allowing it to use search engines and browse web pages just like humans do.

Before we proceed, let's briefly introduce the JSON Schema format:

JSON Schema is a vocabulary that you can use to annotate and validate JSON documents.

JSON Schema is a JSON document used to describe the format of JSON data.

We define the following JSON Schema:

{
	"type": "object",
	"properties": {
		"name": {
			"type": "string"
		}
	}
}

This JSON Schema defines a JSON Object that contains a field named name, and the type of this field is string, for example:

{
	"name": "Hei"
}

By describing our tool definitions using JSON Schema, we can make it clearer and more intuitive for the Kimi large language model to understand what parameters our tools require, as well as the type and description of each parameter. Now let's define the "search engine" and "web browser" tools mentioned earlier:

tools = [
	{
		"type": "function", // The field "type" is a convention, currently supporting "function" as its value
		"function": { // When "type" is "function", use the "function" field to define the specific function content
			"name": "search", // The name of the function, please use English letters, numbers, plus hyphens and underscores as the function name
			"description": ""/* 
				Search for content on the internet using a search engine.
 
				When your knowledge cannot answer the user's question, or when the user requests an online search, call this tool. Extract the content the user wants to search from the conversation as the value of the query parameter.
				The search results include the website title, website address (URL), and website description.
			*/, // Description of the function, write the specific function and usage scenarios here so that the Kimi large language model can correctly choose which functions to use
			"parameters": { // Use the "parameters" field to define the parameters accepted by the function
				"type": "object", // Always use "type": "object" to make the Kimi large language model generate a JSON Object parameter
				"required": ["query"], // Use the "required" field to tell the Kimi large language model which parameters are required
				"properties": { // The specific parameter definitions are in "properties", you can define multiple parameters
					"query": { // Here, the key is the parameter name, and the value is the specific definition of the parameter
						"type": "string", // Use "type" to define the parameter type
						"description": ""/*
							The content the user wants to search for, extract it from the user's question or chat context.
						*/ // Use "description" to describe the parameter so that the Kimi large language model can better generate the parameter
					}
				}
			}
		}
	},
	{
		"type": "function", // The field "type" is a convention, currently supporting "function" as its value
		"function": { // When "type" is "function", use the "function" field to define the specific function content
			"name": "crawl", // The name of the function, please use English letters, numbers, plus hyphens and underscores as the function name
			"description": ""/*
				Get the content of a webpage based on the website address (URL).
			*/, // Description of the function, write the specific function and usage scenarios here so that the Kimi large language model can correctly choose which functions to use
			"parameters": { // Use the "parameters" field to define the parameters accepted by the function
				"type": "object", // Always use "type": "object" to make the Kimi large language model generate a JSON Object parameter
				"required": ["url"], // Use the "required" field to tell the Kimi large language model which parameters are required
				"properties": { // The specific parameter definitions are in "properties", you can define multiple parameters
					"url": { // Here, the key is the parameter name, and the value is the specific definition of the parameter
						"type": "string", // Use "type" to define the parameter type
						"description": ""/*
							The website address (URL) of the content to be obtained, which can usually be obtained from the search results.
						*/ // Use "description" to describe the parameter so that the Kimi large language model can better generate the parameter
					}
				}
			}
		}
	}
]

When defining tools using JSON Schema, we use the following fixed format:

{
	"type": "function",
	"function": {
		"name": "NAME",
		"description": "DESCRIPTION",
		"parameters": {
			"type": "object",
			"properties": {
				
			}
		}
	}
}

Here, name, description, and parameters.properties are defined by the tool provider. The description explains the specific function and when to use the tool, while parameters outlines the specific parameters needed to successfully call the tool, including parameter types and descriptions. Ultimately, the Kimi large language model will generate a JSON Object that meets the defined requirements as the parameters (arguments) for the tool call based on the JSON Schema.

Register Tools
Let's try submitting the search tool to the Kimi large language model to see if it can correctly call the tool:

const OpenAI = require("openai")
 
 
client = OpenAI({
    apiKey: "MOONSHOT_API_KEY", // Replace MOONSHOT_API_KEY with the API Key you obtained from the Kimi Open Platform
    baseURL: "https://api.moonshot.ai/v1",
})
 
tools = [
	{
		"type": "function", // The agreed-upon field type, currently supports function as a value
		"function": { // When type is function, use the function field to define the specific function content
			"name": "search", // The name of the function, please use English letters, numbers, plus hyphens and underscores as the function name
			"description": ""/* 
				Search for content on the internet using a search engine.
 
				When your knowledge cannot answer the user's question, or the user requests you to search online, call this tool. Extract the content the user wants to search from the conversation as the value of the query parameter.
				The search results include the website title, website address (URL), and website description.
			*/, // Description of the function, write the specific function's role and usage scenario here to help Kimi large language model correctly choose which functions to use
			"parameters": { // Use the parameters field to define the parameters the function accepts
				"type": "object", // Fixedly use type: object to make Kimi large language model generate a JSON Object parameter
				"required": ["query"], // Use the required field to tell Kimi large language model which parameters are required
				"properties": { // The specific parameter definitions are in properties, you can define multiple parameters
					"query": { // Here, the key is the parameter name, and the value is the specific definition of the parameter
						"type": "string", // Use type to define the parameter type
						"description": ""/*
							The content the user wants to search for, extracted from the user's question or chat context.
						*/ // Use description to describe the parameter so that Kimi large language model can better generate the parameter
					}
				}
			}
		}
	},
	// {
	// 	"type": "function", // The agreed-upon field type, currently supports function as a value
	// 	"function": { // When type is function, use the function field to define the specific function content
	// 		"name": "crawl", // The name of the function, please use English letters, numbers, plus hyphens and underscores as the function name
	// 		"description": """
	// 			Get the webpage content based on the website address (URL).
	// 		""", // Description of the function, write the specific function's role and usage scenario here to help Kimi large language model correctly choose which functions to use
	// 		"parameters": { // Use the parameters field to define the parameters the function accepts
	// 			"type": "object", // Fixedly use type: object to make Kimi large language model generate a JSON Object parameter
	// 			"required": ["url"], // Use the required field to tell Kimi large language model which parameters are required
	// 			"properties": { // The specific parameter definitions are in properties, you can define multiple parameters
	// 				"url": { // Here, the key is the parameter name, and the value is the specific definition of the parameter
	// 					"type": "string", // Use type to define the parameter type
	// 					"description": """
	// 						The website address (URL) whose content needs to be obtained, usually the website address can be obtained from the search results.
	// 					""" // Use description to describe the parameter so that Kimi large language model can better generate the parameter
	// 				}
	// 			}
	// 		}
	// 	}
	// }
]
 
async function main() {
    const completion = await client.chat.completions.create({
        model: "kimi-k2-turbo-preview",
        messages=[
            {role: "system", content: "You are Kimi, an AI assistant provided by Moonshot AI. You are proficient in Chinese and English conversations. You provide users with safe, helpful, and accurate answers. You refuse to answer any questions related to terrorism, racism, or explicit content. Moonshot AI is a proper noun and should not be translated."},
            {role: "user", content: "Please search the internet for 'Context Caching' and tell me what it is."} // In the question, we ask Kimi large language model to search online
        ],
        temperature: 0.6,
        tools: tools, // <-- We pass the defined tools to Kimi large language model via the tools parameter
    })
     
    console.log(completion.choices[0].model_dump_json(indent=4))
}
 
main()

When the above code runs successfully, we get the response from Kimi large language model:

{
    "finish_reason": "tool_calls",
    "message": {
        "content": "",
        "role": "assistant",
        "tool_calls": [
            {
                "id": "search:0",
                "function": {
                    "arguments": "{\n    \"query\": \"Context Caching\"\n}",
                    "name": "search"
                },
                "type": "function",
            }
        ]
    }
}

Notice that in this response, the value of finish_reason is tool_calls, which means that the response is not the answer from Kimi large language model, but rather the tool that Kimi large language model has chosen to execute. You can determine whether the current response from Kimi large language model is a tool call tool_calls by checking the value of finish_reason.

In the message section, the content field is empty because the model is currently executing tool_calls and has not yet generated a response for the user. Meanwhile, a new field tool_calls has been added. The tool_calls field is a list that contains all the tool call information for this execution. This also indicates another characteristic of tool_calls: the model can choose to call multiple tools at once, which can be different tools or the same tool with different parameters. Each element in tool_calls represents a tool call. Kimi large language model generates a unique id for each tool call. The function.name field indicates the name of the function being executed, and the parameters are placed in function.arguments. The arguments parameter is a valid serialized JSON Object (additionally, the type parameter is currently a fixed value function).

Next, we should use the tool call parameters generated by Kimi large language model to execute the specific tools.

Execute the Tools
Kimi large language model does not execute the tools for us. We need to execute the parameters generated by Kimi large language model after receiving them. Before explaining how to execute the tools, let's first address the question we raised earlier:

Why can't Kimi large language model execute the tools itself, but instead requires us to "help" it execute the tools based on the parameters generated by Kimi large language model? If we are the ones executing the tool calls, what is the purpose of Kimi large language model?

Let's imagine a scenario where we use Kimi large language model: we provide users with a smart robot based on Kimi large language model. In this scenario, there are three roles: the user, the robot, and Kimi large language model. The user asks the robot a question, the robot calls the Kimi large language model API, and returns the API result to the user. When using tool_calls, the user asks the robot a question, the robot calls the Kimi API with tools, Kimi large language model returns the tool_calls parameters, the robot executes the tool_calls, submits the results back to the Kimi API, Kimi large language model generates the message to be returned to the user (finish_reason=stop), and only then does the robot return the message to the user. Throughout this process, the entire tool_calls process is transparent and implicit to the user.

Returning to the question above, as users, we are not actually executing the tool calls, nor do we directly "see" the tool calls. Instead, the robot that provides us with the service is completing the tool calls and presenting us with the final response generated by Kimi large language model.

Let's explain how to execute the tool_calls returned by Kimi large language model from the perspective of the "robot":

const axios = require('axios');
const openai = require('openai'); // You need to install the openai library
 
const client = new openai.OpenAI({
    apiKey: "MOONSHOT_API_KEY", // Replace MOONSHOT_API_KEY with the API Key you obtained from the Kimi Open Platform
    baseURL: "https://api.moonshot.ai/v1",
});
 
const tools = [
    {
        "type": "function",
        "function": {
            "name": "search",
            "description": "Search for content on the internet using a search engine.\n\nUse this tool when your knowledge can't answer the user's question or when the user asks you to search online. Extract the content the user wants to search for from the conversation and use it as the value for the query parameter.\nThe search results include the website title, URL, and a brief description.",
            "parameters": {
                "type": "object",
                "required": ["query"],
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The content the user wants to search for, extracted from the user's question or chat context."
                    }
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "crawl",
            "description": "Retrieve web page content based on a website URL.",
            "parameters": {
                "type": "object",
                "required": ["url"],
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The URL of the website whose content you want to retrieve, usually obtained from search results."
                    }
                }
            }
        }
    }
];
 
async function searchImpl(query) {
    const response = await axios.get("https://your.search.api", { params: { query } });
    return response.data;
}
 
function search(arguments) {
    const query = arguments.query;
    const result = searchImpl(query);
    return { "result": result };
}
 
async function crawlImpl(url) {
    const response = await axios.get(url);
    return response.data;
}
 
function crawl(arguments) {
    const url = arguments.url;
    const content = crawlImpl(url);
    return { "content": content };
}
 
const toolMap = {
    "search": search,
    "crawl": crawl,
};
 
const messages = [
    { "role": "system", "content": "You are Kimi, an AI assistant provided by Moonshot AI. You are proficient in Chinese and English conversations. You provide users with safe, helpful, and accurate answers. You will refuse to answer any questions involving terrorism, racism, or explicit content. Moonshot AI is a proper noun and should not be translated into other languages." },
    { "role": "user", "content": "Please search the internet for Context Caching and tell me what it is." }  // The user is asking Kimi to search online
];
 
let finishReason = null;
 
async function main() {
    while (finishReason === null || finishReason === "tool_calls") {
        const completion = await client.chat.completions.create({
            model: "kimi-k2-turbo-preview",
            messages: messages,
            temperature: 0.6,
            tools: tools,  // <-- We pass the defined tools to the Kimi large language model via the tools parameter
        });
        const choice = completion.choices[0];
        finishReason = choice.finish_reason;
        if (finishReason === "tool_calls") { // <-- Check if the current response includes tool_calls
            messages.push(choice.message); // <-- Add the assistant message from Kimi to the context for the next request
            for (const toolCall of choice.message.tool_calls) { // <-- There might be multiple tool_calls, so we loop through each one
                const toolCallName = toolCall.function.name;
                const toolCallArguments = JSON.parse(toolCall.function.arguments); // <-- The arguments are a serialized JSON object, so we need to parse them
                const toolFunction = toolMap[toolCallName]; // <-- Use tool_map to quickly find which function to execute
                const toolResult = await toolFunction(toolCallArguments);
 
                // Construct a role=tool message with the function execution result to show the model the outcome of the tool call;
                // Note that we need to provide the tool_call_id and name fields in the message so that Kimi can correctly match the tool_call.
                messages.push({
                    "role": "tool",
                    "tool_call_id": toolCall.id,
                    "name": toolCallName,
                    "content": JSON.stringify(toolResult), // <-- We agreed to submit the tool call result as a string, so we serialize it with JSON.stringify
                });
            }
        }
    }
    console.log(choice.message.content); // <-- Finally, we return the model's response to the user
}
 
main();

We use a while loop to execute the code logic that includes tool calls because the Kimi large language model typically doesn't make just one tool call, especially in the context of online searching. Usually, Kimi will first call the search tool to get search results, and then call the crawl tool to convert the URLs in the search results into actual web page content. The overall structure of the messages is as follows:

system: prompt                                                                                               # System prompt
user: prompt                                                                                                 # User's question
assistant: tool_call(name=search, arguments={query: query})                                                  # Kimi returns a tool_call (single)
tool: search_result(tool_call_id=tool_call.id, name=search)                                                  # Submit the tool_call execution result
assistant: tool_call_1(name=crawl, arguments={url: url_1}), tool_call_2(name=crawl, arguments={url: url_2})  # Kimi continues to return tool_calls (multiple)
tool: crawl_content(tool_call_id=tool_call_1.id, name=crawl)                                                 # Submit the execution result of tool_call_1
tool: crawl_content(tool_call_id=tool_call_2.id, name=crawl)                                                 # Submit the execution result of tool_call_2
assistant: message_content(finish_reason=stop)                                                               # Kimi generates a reply to the user, ending the conversation

This completes the entire process of making "online query" tool calls. If you have implemented your own search and crawl methods, when you ask Kimi to search online, it will call the search and crawl tools and give you the correct response based on the tool call results.

Common Questions and Notes
About Streaming Output
In streaming output mode (stream), tool_calls are still applicable, but there are some additional things to note, as follows:

During streaming output, since finish_reason will appear in the last data chunk, it is recommended to check if the delta.tool_calls field exists to determine if the current response includes a tool call;
During streaming output, delta.content will be output first, followed by delta.tool_calls, so you must wait until delta.content has finished outputting before you can determine and identify tool_calls;
During streaming output, we will specify the tool_call.id and tool_call.function.name in the initial data chunk, and only tool_call.function.arguments will be output in subsequent chunks;
During streaming output, if Kimi returns multiple tool_calls at once, we will use an additional field called index to indicate the index of the current tool_call, so that you can correctly concatenate the tool_call.function.arguments parameters. We use a code example from the streaming output section (without using the SDK) to illustrate how to do this:
const os = require('os');
const axios = require('axios');// Use the axios library to perform HTTP requests
 
const tools = [
    {
        "type": "function",
        "function": {
            "name": "search",
            "description": "Search the internet for content using a search engine.\n\nWhen your knowledge cannot answer the user's question or the user requests an online search, call this tool. Extract the content the user wants to search from the conversation as the value of the query parameter.\nThe search results include the title of the website, the website's address (URL), and a brief introduction to the website.",
            "parameters": {
                "type": "object",
                "required": ["query"],
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The content the user wants to search for, extracted from the user's question or chat context."
                    }
                }
            }
        }
    },
];
 
const header = {
    "Content-Type": "application/json",
    "Authorization": `Bearer MOONSHOT_API_KEY`
};
 
const data = {
    "model": "kimi-k2-turbo-preview",
    "messages": [
        {"role": "user", "content": "Please search for Context Caching technology online."}
    ],
    "temperature": 0.6,
    "stream": true,
    "n": 2,
    "tools": tools,
    "tool_choice": "auto"
};
 
axios.post("https://api.moonshot.ai/v1/chat/completions", 
    data, {
    headers: header,
    responseType: 'stream'   
}).then(response => {
    if (response.status !== 200) {
        throw new Error(response.text);
    }
 
    let data = "";
    let messages = [{}, {}];
 
    response.data.on('data', chunk => {
        let line = chunk.toString().trim();
 
        if (line === "") {
            let chunk = JSON.parse(data);
 
            for (let choice of chunk.choices) {
                let index = choice.index;
                let message = messages[index];
                let usage = choice.usage;
                if (usage) message.usage = usage;
                let delta = choice.delta;
                let role = delta.role;
                if (role) message.role = role;
                let content = delta.content;
                if (content) message.content = message.content + content;
 
                let tool_calls = delta.tool_calls;
                if (tool_calls) {
                    if (!message.tool_calls) message.tool_calls = [];
                    for (let tool_call of tool_calls) {
                        let tool_call_index = tool_call.index;
                        if (message.tool_calls.length < tool_call_index + 1) {
                            message.tool_calls.push({}).repeat(tool_call_index + 1 - message.tool_calls.length);
                        }
                        let tool_call_object = message.tool_calls[tool_call_index];
                        tool_call_object.index = tool_call_index;
 
                        let tool_call_id = tool_call.id;
                        if (tool_call_id) tool_call_object.id = tool_call_id;
                        let tool_call_type = tool_call.type;
                        if (tool_call_type) tool_call_object.type = tool_call_type;
                        let tool_call_function = tool_call.function;
                        if (tool_call_function) {
                            if (!tool_call_object.function) tool_call_object.function = {};
                            let tool_call_function_name = tool_call_function.name;
                            if (tool_call_function_name) tool_call_object.function.name = tool_call_function_name;
                            let tool_call_function_arguments = tool_call_function.arguments;
                            if (tool_call_function_arguments) {
                                if (!tool_call_object.function.arguments) {
                                    tool_call_object.function.arguments = tool_call_function_arguments;
                                } else {
                                    tool_call_object.function.arguments = tool_call_object.function.arguments + tool_call_function_arguments;
                                }
                            }
                        }
                        message.tool_calls[tool_call_index] = tool_call_object;
                    }
                }
            }
            data = ""; // Reset data
        } else if (line.startsWith("data: ")) {
            data = line.substring(6);
        } else {
            data = data + "\n" + line;
        }
    });
 
    response.data.on('end', () => {
        for (let index = 0; index < messages.length; index++) {
            console.log("index:", index);
            console.log("message:", JSON.stringify(messages[index], null, 4));
            console.log("");
        }
    });
}).catch(error => {
    console.error("Request failed:", error);
});

Below is an example of handling tool_calls in streaming output using the openai SDK:

const os = require('os');
const openai = require('openai'); // Need to install the openai library
 
const client = new openai.OpenAI({
    apiKey: "MOONSHOT_API_KEY",
    baseURL: "https://api.moonshot.ai/v1"
});
 
const tools = [
    {
        "type": "function",
        "function": {
            "name": "search",
            "description": "Search for content on the internet using a search engine.\n\nCall this tool when your knowledge cannot answer the user's question, or when the user requests an online search. Extract the content the user wants to search for from the conversation and use it as the value of the query parameter.\nThe search results include the website title, address (URL), and a brief description of the website.",
            "parameters": {
                "type": "object",
                "required": ["query"],
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The content the user wants to search for, extracted from the user's question or chat context."
                    }
                }
            }
        }
    },
];
 
async function main() {
    response = await client.chat.completions.create({
        model: "kimi-k2-turbo-preview",
        messages: [
            { "role": "user", "content": "Please search for Context Caching technology online." }
        ],
        temperature: 0.6,
        stream: true,
        tools: tools,
        tool_choice: "auto"
    });
 
    let messages = [{}, {}];
    let data = '';
 
    for await (const chunk of response) {
         for (const choice of chunk.choices) {
            const index = choice.index;
            const message = messages[index];
            const delta = choice.delta;
            const role = delta.role;
            if (role) message.role = role;
            const content = delta.content;
            if (content) message.content = message.content + content;
 
            const tool_calls = delta.tool_calls;
            if (tool_calls) {
                if (!message.tool_calls) message.tool_calls = [];
                for (const tool_call of tool_calls) {
                    const tool_call_index = tool_call.index;
                    if (message.tool_calls.length < tool_call_index + 1) {
                        for (let i = message.tool_calls.length; i < tool_call_index + 1; i++) {
                            message.tool_calls.push({});
                        }
                    }
                    const tool_call_object = message.tool_calls[tool_call_index];
                    tool_call_object.index = tool_call_index;
 
                    const tool_call_id = tool_call.id;
                    if (tool_call_id) tool_call_object.id = tool_call_id;
                    const tool_call_type = tool_call.type;
                    if (tool_call_type) tool_call_object.type = tool_call_type;
                    const tool_call_function = tool_call.function;
                    if (tool_call_function) {
                        if (!tool_call_object.function) tool_call_object.function = {};
                        const tool_call_function_name = tool_call_function.name;
                        if (tool_call_function_name) tool_call_object.function.name = tool_call_function_name;
                        const tool_call_function_arguments = tool_call_function.arguments;
                        if (tool_call_function_arguments) {
                            if (!tool_call_object.function.arguments) {
                                tool_call_object.function.arguments = tool_call_function_arguments;
                            } else {
                                tool_call_object.function.arguments += tool_call_function_arguments;
                            }
                        }
                    }
                    message.tool_calls[tool_call_index] = tool_call_object;
                }
            }
        }
    }
 
    for (let index = 0; index < messages.length; index++) {
        console.log("index:", index);
        console.log("message:", JSON.stringify(messages[index], null, 2));
        console.log("");
    }
}
 
main().catch(console.error);

About tool_calls and function_call
tool_calls is an advanced version of function_call. Since OpenAI has marked parameters such as function_call (for example, functions) as "deprecated," our API will no longer support function_call. You can consider using tool_calls instead of function_call. Compared to function_call, tool_calls has the following advantages:

It supports parallel calls. The Kimi large language model can return multiple tool_calls at once. You can use concurrency in your code to call these tool_call simultaneously, reducing time consumption;
For tool_calls that have no dependencies, the Kimi large language model will also tend to call them in parallel. Compared to the original sequential calls of function_call, this reduces token consumption to some extent;
About content
When using the tool_calls tool, you may notice that under the condition of finish_reason=tool_calls, the message.content field is occasionally not empty. Typically, the content here is the Kimi large language model explaining which tools need to be called and why these tools need to be called. Its significance lies in the fact that if your tool call process takes a long time, or if completing a round of chat requires multiple sequential tool calls, providing a descriptive sentence to the user before calling the tool can reduce the anxiety or dissatisfaction that users may feel due to waiting. Additionally, explaining to the user which tools are being called and why helps them understand the entire tool call process and allows them to intervene and correct in a timely manner (for example, if the user thinks the current tool selection is incorrect, they can terminate the tool call in time, or correct the model's tool selection in the next round of chat through a prompt).

About Tokens
The content in the tools parameter is also counted in the total Tokens. Please ensure that the total number of Tokens in tools and messages does not exceed the model's context window size.

About Message Layout
In scenarios where tools are called, our messages are no longer laid out like this:

system: ...
user: ...
assistant: ...
user: ...
assistant: ...

Instead, they will look like this:

system: ...
user: ...
assistant: ...
tool: ...
tool: ...
assistant: ...

It is important to note that when the Kimi large language model generates tool_calls, ensure that each tool_call has a corresponding message with role=tool, and that this message has the correct tool_call_id. If the number of role=tool messages does not match the number of tool_calls, or if the tool_call_id in the role=tool messages cannot be matched with the tool_call.id in tool_calls, an error will occur.

If You Encounter the tool_call_id not found Error
If you encounter the tool_call_id not found error, it may be because you did not add the role=assistant message returned by the Kimi API to the messages list. The correct message sequence should look like this:

system: ...
user: ...
assistant: ...  # <-- Perhaps you did not add this assistant message to the messages list
tool: ...
tool: ...
assistant: ...

You can avoid the tool_call_id not found error by executing messages.append(message) each time you receive a return value from the Kimi API, to add the message returned by the Kimi API to the messages list.

Note: Assistant messages added to the messages list before the role=tool message must fully include the tool_calls field and its values returned by the Kimi API. We recommend directly adding the choice.message returned by the Kimi API to the messages list "as is" to avoid potential errors.

Last updated on 
\

Use Kimi API's Internet Search Functionality
In the previous chapter (Using Kimi API to Complete Tool Calls), we explained in detail how to use the tool_calls feature of the Kimi API to enable the Kimi large language model to perform internet searches. Let's review the process we implemented:

We defined tools using the JSON Schema format. For internet searches, we defined two tools: search and crawl.
We submitted the defined search and crawl tools to the Kimi large language model via the tools parameter.
The Kimi large language model would select to call search and crawl based on the context of the current conversation, generate the relevant parameters, and output them in JSON format.
We used the parameters output by the Kimi large language model to execute the search and crawl functions and submitted the results of these functions back to the Kimi large language model.
The Kimi large language model would then provide a response to the user based on the results of the tool executions.
In the process of implementing internet searches, we needed to implement the search and crawl functions ourselves, which might include:

Calling search engine APIs or implementing our own content search.
Retrieving search results, including URLs and summaries.
Fetching web page content based on URLs, which might require different reading rules for different websites.
Cleaning and organizing the fetched web page content into a format that the model can easily recognize, such as Markdown.
Handling various errors and exceptions, such as no search results or failure to fetch web page content.
Implementing these steps is often considered cumbersome and challenging. Our users have repeatedly requested a simple, ready-to-use "internet search" function. Therefore, based on the original tool_calls usage of the Kimi large language model, we have provided a built-in tool function builtin_function.$web_search to enable internet search functionality.

The basic usage and process of the $web_search function are the same as the usual tool_calls, but there are still some minor differences. We will explain in detail through examples how to call the built-in $web_search function of Kimi to enable internet search functionality and mark the items that need extra attention in the code and explanations.

$web_search Declaration
Unlike ordinary tool, the $web_search function does not require specific parameter descriptions. It only needs the type and function.name in the tools declaration to successfully register the $web_search function:

tools = [
	{
		"type": "builtin_function",  # <-- We use builtin_function to indicate Kimi built-in tools, which also distinguishes it from ordinary function
		"function": {
			"name": "$web_search",
		},
	},
]

The $web_search function is prefixed with a dollar sign $, which is our agreed way to indicate Kimi built-in functions (in ordinary function definitions, the dollar sign $ is not allowed), and if there are other Kimi built-in functions in the future, they will also be prefixed with the dollar sign $.

When declaring tools, $web_search can coexist with other ordinary function. Furthermore, builtin_function can coexist with ordinary function. You can add both builtin_function and ordinary function to tools, or add both builtin_function and ordinary function at the same time.

Next, let's modify the original tool_calls code to explain how to execute tool_calls.

$web_search Execution
Here is the modified tool_calls code:

const axios = require('axios');
const openai = require('openai'); // Need to install the openai library
 
const client = new openai.OpenAI({
    apiKey: "sk-",
    baseURL: "https://api.moonshot.ai/v1",
});
 
const tools = [
    {
        "type": "builtin_function",
        "function": {
            "name": "$web_search",
        },
    }
];
function search_impl(arguments) {
    return arguments
}
 
const messages = [
    { "role": "system", "content": "You are Kimi, an AI assistant provided by Moonshot AI. You are more proficient in Chinese and English conversations. You provide users with safe, helpful, and accurate answers. At the same time, you will refuse to answer any questions involving terrorism, racial discrimination, or explicit violence. Moonshot AI is a proper noun and should not be translated into other languages." },
    { "role": "user", "content": "Please search for the value of the Chinese A-share index on October 8, 2024?" }  // The question requires Kimi large language model to search the internet
];
 
let finishReason = null;
 
async function main() {
    while (finishReason === null || finishReason === "tool_calls") {
        const completion = await client.chat.completions.create({
            model: "kimi-k2-turbo-preview",
            messages: messages,
            temperature: 0.6,
            max_tokens: 32768,
            tools: tools,  // <-- We pass the defined tools to Kimi large language model through the tools parameter
        });
        const choice = completion.choices[0];
        console.log(choice);
        finishReason = choice.finish_reason;
        console.log(finishReason);
        if (finishReason === "tool_calls") { // <-- Check if the current response contains tool_calls
            messages.push(choice.message); // <-- We add the assistant message returned by Kimi large language model to the context, so that Kimi large language model can understand our request next time
            for (const toolCall of choice.message.tool_calls) { // <-- There may be multiple tool_calls, so we use a loop to execute each one
                const tool_call_name = toolCall.function.name;
                const tool_call_arguments = JSON.parse(toolCall.function.arguments); // <-- The arguments are a serialized JSON Object, so we need to use JSON.parse to deserialize it
                if (tool_call_name == "$web_search") {
                    console.log('????');
                  tool_result = search_impl(tool_call_arguments)
                } else {
                  tool_result = 'no tool found'
                }
 
 
                // Construct a message with role=tool to show the result of the tool call to the model;
                // Note that we need to provide the tool_call_id and name fields in the message, so that Kimi large language model
                // can correctly match the corresponding tool_call.
                console.log("toolCall.id");
                console.log(toolCall.id);                
                console.log("tool_call_name");
                console.log(tool_call_name);
                console.log("tool_result");
                console.log(tool_result);                
                messages.push({
                    "role": "tool",
                    "tool_call_id": toolCall.id,
                    "name": tool_call_name,
                    "content": JSON.stringify(tool_result), // <-- We agree to submit the result of the tool call to Kimi large language model in string format, so we use JSON.stringify to serialize the result here
                });
            }
        }
        console.log(choice.message.content); // <-- Here, we return the model's response to the user
    }
     
}
 
main();

Looking back at the code above, we are surprised to find that when using the $web_search function, its basic process is no different from that of a regular function. Developers don't even need to modify the original code for executing tool calls. The part that is different and particularly noteworthy is that when we implement the search_impl function, we don't include much logic for searching, parsing, or obtaining web content. We simply return the parameters generated by Kimi large language model, tool_call.function.arguments, as they are to complete the tool call. Why is that?

In fact, as the name builtin_function suggests, $web_search is a built-in function of Kimi large language model. It is defined and executed by Kimi large language model. The process is as follows:

When Kimi large language model generates a response with finish_reason=tool_calls, it means that Kimi large language model has realized that it needs to execute the $web_search function and has already prepared everything for it;
Kimi large language model will return the necessary parameters for executing the function in the form of tool_call.function.arguments. However, these parameters are not executed by the caller. The caller just needs to submit tool_call.function.arguments to Kimi large language model as they are, and Kimi large language model will execute the corresponding online search process;
When the user submits tool_call.function.arguments using a message with role=tool, Kimi large language model will immediately start the online search process and generate a readable message for the user based on the search and reading results, which is a message with finish_reason=stop;
Compatibility Note
The online search function provided by the Kimi API aims to offer a reliable large language model online search solution without breaking the compatibility of the original API and SDK. It is fully compatible with the original tool call feature of Kimi large language model. This means that: if you want to switch from Kimi's online search function to your own implementation, you can do so in just two simple steps without disrupting the overall structure of your code:

Modify the tool definition of $web_search to your own implementation (including name, description, etc.). You may need to add additional information in tool.function to inform the model of the specific parameters it needs to generate. You can add any parameters you need in the parameters field;
Change the implementation of the search_impl function. When using Kimi's $web_search, you just need to return the input parameters arguments as they are. However, if you use your own online search service, you may need to fully implement the search and crawl functions mentioned at the beginning of the article;
After completing the above steps, you will have successfully migrated from Kimi's online search function to your own implementation.

About Token Consumption
When using the $web_search function provided by Kimi, the search results are also counted towards the tokens occupied by the prompt (i.e., prompt_tokens). Typically, since the results of web searches contain a lot of content, the token consumption can be quite high. To avoid unknowingly using up a large number of tokens, we add an extra field called total_tokens when generating the arguments for the $web_search function. This field informs the caller of the total number of tokens occupied by the search content, which will be included in the prompt_tokens once the entire web search process is completed. We will use specific code to demonstrate how to obtain these token consumptions:

from typing import *
 
import os
import json
 
from openai import OpenAI
from openai.types.chat.chat_completion import Choice
 
 
client = OpenAI(
    base_url="https://api.moonshot.ai/v1",
    api_key=os.environ.get("MOONSHOT_API_KEY"),
)
 
 
# The specific implementation of the search tool; here we just return the arguments
def search_impl(arguments: Dict[str, Any]) -> Any:
    """
    When using the search tool provided by Moonshot AI, simply return the arguments as they are,
    without any additional processing logic.
 
    However, if you want to use another model while retaining the web search functionality,
    you only need to modify the implementation here (for example, calling the search and fetching web content),
    while keeping the function signature the same, which still works.
 
    This maximizes compatibility, allowing you to switch between different models without making destructive changes to the code.
    """
    return arguments
 
 
def chat(messages) -> Choice:
    completion = client.chat.completions.create(
        model="kimi-k2-turbo-preview",
        messages=messages,
        temperature=0.6,
        tools=[
            {
                "type": "builtin_function",
                "function": {
                    "name": "$web_search",
                },
            }
        ]
    )
    usage = completion.usage
    choice = completion.choices[0]
 
    # =========================================================================
    # By checking if finish_reason is "stop", we print the token consumption after completing the web search process
    if choice.finish_reason == "stop":
        print(f"chat_prompt_tokens:          {usage.prompt_tokens}")
        print(f"chat_completion_tokens:      {usage.completion_tokens}")
        print(f"chat_total_tokens:           {usage.total_tokens}")
    # =========================================================================
 
    return choice
 
 
def main():
    messages = [
        {"role": "system", "content": "You are Kimi."},
    ]
 
    # Initial query
    messages.append({
        "role": "user",
        "content": "Please search for Moonshot AI Context Caching technology and tell me what it is."
    })
 
    finish_reason = None
    while finish_reason is None or finish_reason == "tool_calls":
        choice = chat(messages)
        finish_reason = choice.finish_reason
        if finish_reason == "tool_calls":
            messages.append(choice.message)
            for tool_call in choice.message.tool_calls:
                tool_call_name = tool_call.function.name
                tool_call_arguments = json.loads(
                    tool_call.function.arguments)
                if tool_call_name == "$web_search":
 
    				# ===================================================================
                    # We print the tokens generated by the web search results during the web search process
                    search_content_total_tokens = tool_call_arguments.get("usage", {}).get("total_tokens")
                    print(f"search_content_total_tokens: {search_content_total_tokens}")
    				# ===================================================================
 
                    tool_result = search_impl(tool_call_arguments)
                else:
                    tool_result = f"Error: unable to find tool by name '{tool_call_name}'"
 
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_call_name,
                    "content": json.dumps(tool_result),
                })
 
    print(choice.message.content)
 
 
if __name__ == '__main__':
    main()
 

Running the above code yields the following output:

search_content_total_tokens: 13046  # <-- This represents the number of tokens occupied by the web search results due to the web search action.
chat_prompt_tokens:          13212  # <-- This represents the number of input tokens, including the web search results.
chat_completion_tokens:      295    # <-- This represents the number of tokens generated by the Kimi large language model based on the web search results.
chat_total_tokens:           13507  # <-- This represents the total number of tokens consumed, including the web search process.
 
# The content generated by the Kimi large language model based on the web search results is omitted here.

About Model Size Selection
Another issue that arises is that when the web search function is enabled, the number of tokens can change significantly, exceeding the context window of the originally used model. This may trigger an Input token length too long error message. Therefore, when using the web search function, we recommend using the dynamic model kimi-k2-turbo-preview to adapt to changes in token counts. We slightly modify the chat function to use the kimi-k2-turbo-preview model:

def chat(messages) -> Choice:
    completion = client.chat.completions.create(
        model="kimi-k2-turbo-preview", 
        messages=messages,
        temperature=0.6,
        tools=[
            {
                "type": "builtin_function",  # <-- Use builtin_function to declare the $web_search function. Please include the full tools declaration in each request.
                "function": {
                    "name": "$web_search",
                },
            }
        ]
    )
    return completion.choices[0]

About Other Tools
The $web_search tool can be used in combination with other regular tools. You can freely mix tools with type=builtin_function and type=function.

About Web Search Billing
In addition to token consumption, we also charge a call fee for each web search, priced at $0.005. For more details, please refer to Pricing.

Last updated on 

Use Kimi API's JSON Mode
In some scenarios, we want the model to output content in a fixed format JSON document. For example, when you want to summarize an article, you might expect a structured data format like this:

{
	"title": "Article Title",
	"author": "Article Author",
	"publish_time": "Publication Time",
	"summary": "Article Summary"
}

If you directly tell the Kimi large language model in the prompt: "Please output content in JSON format," the model can understand your request and generate a JSON document as required. However, the generated content often has some flaws. For instance, in addition to the JSON document, Kimi might output extra text to explain the JSON document:

Here is the JSON document you requested
{
	"title": "Article Title",
	"author": "Article Author",
	"publish_time": "Publication Time",
	"summary": "Article Summary"
}

Or the JSON document format might be incorrect and cannot be parsed properly, such as (note the comma at the end of the summary field):

{
	"title": "Article Title",
	"author": "Article Author",
	"publish_time": "Publication Time",
	"summary": "Article Summary",
}

Such a JSON document cannot be parsed correctly. To generate a standard and valid JSON document as expected, we provide the response_format parameter. The default value of response_format is {"type": "text"}, which means ordinary text content with no formatting constraints. You can set response_format to {"type": "json_object"} to enable JSON Mode, and the Kimi large language model will output a valid, parsable JSON document as required.

When using JSON Mode, please follow these guidelines:

Inform the Kimi large language model in the system prompt or user prompt about the JSON document to be generated, including specific field names and types. It's best to provide an example for the model to refer to.
The Kimi large language model will only generate JSON Object type JSON documents. Do not prompt the model to generate JSON Array or other types of JSON documents.
If you do not correctly inform the Kimi large language model of the required JSON Object format, the model will generate unexpected results.
JSON Mode Application Example
Let's use a specific example to illustrate the application of JSON Mode:

Imagine we are building a WeChat intelligent robot customer service (referred to as intelligent customer service). The intelligent customer service uses the Kimi large language model to answer customer questions. We want the intelligent customer service to not only reply with text messages but also with images, link cards, voice messages, and other types of messages. Moreover, in a single response, we want to mix different types of messages. For example, for customer product inquiries, we provide a text reply, a product image, and finally, a purchase link (in the form of a link card).

Let's demonstrate the content of this example with code:

const OpenAI = require("openai")
 
const client = new OpenAI({
    apiKey: "MOONSHOT_API_KEY", // Replace MOONSHOT_API_KEY with the API Key you obtained from the Kimi Open Platform
    baseYRL: "https://api.moonshot.ai/v1",
})
 
system_prompt = `
You are the intelligent customer service of Moonshot AI (Kimi), responsible for answering various user questions. Please refer to the document content to reply to user questions. Your reply can be text, images, links, and you can include text, images, and links in a single response.
"
" 
Please output your reply in the following JSON format:
 
{
    "text": "Text information",
    "image": "Image URL",
    "url": "Link URL"
}
"
Note: Please place the text information in the 'text' field, put the image in the 'image' field in the form of a link starting with oss://, and place the regular link in the 'url' field.
`
async function main() {
    const completion = await client.chat.completions.create({
        model: "kimi-k2-turbo-preview",
        messages: [
            {role: "system",
             content: "You are Kimi, an artificial intelligence assistant provided by Moonshot AI, excelling in Chinese and English conversations. You provide users with safe, helpful, and accurate answers. You will reject any questions involving terrorism, racism, pornography, and violence. Moonshot AI is a proper noun and should not be translated into other languages."},
            {role: "system", content: system_prompt}, // <-- Submit the system prompt with the output format to Kimi
            {role: "user", content: "Hello, my name is Li Lei, what is 1+1?"}
        ],
        temperature: 0.6,
        response_format: {type: "json_object"}, // <-- Use the response_format parameter to specify the output format as json_object
    })
     
    // Since we have set JSON Mode, the message.content returned by the Kimi large language model is a serialized JSON Object string.
    // We use JSON.parse to parse its content and deserialize it into a JavaScript object.
    content = JSON.parse(completion.choices[0].message.content)
     
    // Parse text content
    if (content.text) {
        // For demonstration purposes, we print the content;
        // In real business logic, you may need to call the text message sending interface to send the generated text to the user.
        console.log("text:", content.text)
    } 
    // Parse image content
    if (content.image) {
        // For demonstration purposes, we print the content;
        // In real business logic, you may need to first parse the image URL, download the image, and then call the image message sending
        // interface to send the image to the user.
        console.log("image:", content.image)
    } 
    // Parse link
    if (content.url) {
        // For demonstration purposes, we print the content;
        // In real business logic, you may need to call the link card sending interface to send the link to the user in the form of a card.
        console.log("url", content.url)
    }
}
 
main()

Let's go over the steps for using JSON Mode once again:

Define the output JSON format in the system or user prompt. Our recommended best practice is to provide a specific output example and explain the meaning of each field;
Use the response_format parameter and set it to {"type": "json_object"};
Parse the content in the message returned by the Kimi large language model. message.content will be a valid JSON Object serialized as a string;
Incomplete JSON
If you encounter this situation:

You have correctly set the response_format parameter and specified the format of the JSON document in the prompt, but the JSON document you receive is incomplete or truncated, making it impossible to correctly parse the JSON document.

We suggest you check if the finish_reason field in the return value is length. Generally, a smaller max_tokens value will cause the model's output to be truncated, and this rule also applies when using JSON Mode. We recommend that you set a reasonable max_tokens value based on the estimated size of the output JSON document, so that you can correctly parse the JSON document returned by the Kimi large language model.

For a more detailed explanation of the issue of incomplete or truncated output from the Kimi large language model, please refer to: Common Issues and Solutions

Last updated on 


Use Kimi API's Partial Mode
Sometimes, we want the Kimi large language model to continue a given sentence. For example, in some customer service scenarios, we want the smart robot to start every sentence with "Dear customer, hello." For such needs, the Kimi API offers Partial Mode. Let's use specific code to explain how Partial Mode works:

const OpenAI = require('openai')
 
client = OpenAI({
    apiKey: "MOONSHOT_API_KEY", // Replace MOONSHOT_API_KEY with the API Key you obtained from the Kimi Open Platform
    baseURL: "https://api.moonshot.ai/v1",
})
 
async function main() {
    completion = await client.chat.completions.create({
        model: "kimi-k2-turbo-preview",
        messages: [
            {role: "system", content: "You are Kimi, an AI assistant provided by Moonshot AI. You are proficient in Chinese and English conversations. You provide users with safe, helpful, and accurate answers. You also reject any questions involving terrorism, racism, or explicit content. Moonshot AI is a proper noun and should not be translated."},
            {role: "user", content: "Hello?"},
            {
                partial: True, // <-- The partial parameter is used to enable Partial Mode
                role: "assistant", // <-- We add a message with role=assistant after the user's question
                content: "Dear customer, hello,", // <-- The content is "fed" to the Kimi large language model, prompting it to continue from this sentence
            }, 
        ],
        temperature: 0.6,
    })
     
    // Since the Kimi large language model continues from the "fed" sentence, we need to manually concatenate the "fed" sentence with the generated response
    console.log("Dear customer, hello," + completion.choices[0].message.content)
}
 
main()

Let's summarize the key points of using Partial Mode:

Add an extra message at the end of the messages list, with role=assistant and partial=True;
Place the content you want to "feed" to the Kimi large language model in the content field. The model will start generating the response from this content;
Concatenate the content from step 2 with the response generated by the Kimi large language model to form the complete reply;
When calling the Kimi API, there might be cases where the estimated number of input and output tokens is inaccurate, causing the max_tokens value to be set too low. This can result in the Kimi large language model being unable to output the complete response (in this case, the value of finish_reason is length, meaning the number of tokens in the generated response exceeds the max_tokens value set in the request). In such situations, if you are satisfied with the already output content and want the Kimi large language model to continue from where it left off, Partial Mode can be very useful.

Let's use a simple example to explain how to implement this:

const OpenAI = require('openai')
 
client = new OpenAI({
    apiKey: "MOONSHOT_API_KEY", // Replace MOONSHOT_API_KEY with the API Key you obtained from the Kimi Open Platform
    baseURL: "https://api.moonshot.ai/v1",
})
 
async function main() {
    completion = await client.chat.completions.create({
        model: "kimi-k2-turbo-preview",
        messages: [
            {role: "user", content: "Please recite the complete 'Chu Shi Biao'."},
        ],
        temperature: 0.6,
        max_tokens: 100,  # <-- Note here, we set a small value for max_tokens to observe the situation where the Kimi large language model cannot output the complete content
    })
     
    if (completion.choices[0].finish_reason == "length") {  # <-- When the content is truncated, the value of finish_reason is length
        prefix = completion.choices[0].message.content
        print(prefix, end="")  # <-- Here, you will see the truncated part of the output content
        completion = client.chat.completions.create(
            model="kimi-k2-turbo-preview",
            messages=[
                {"role": "user", "content": "Please recite the complete 'Chu Shi Biao'."},
                {"role": "assistant", "content": prefix, "partial": True},
            ],
            temperature=0.6,
            max_tokens=86400,  # <-- Note here, we set a large value for max_tokens to ensure the Kimi large language model can output the complete content
        )
        print(completion.choices[0].message.content)  # <-- Here, you will see the Kimi large language model continue from the previously output content and complete the remaining part
    }
}
 
main()

The name Field in Partial Mode
The name field in Partial Mode is a special attribute that enhances the model's understanding of its role, compelling it to output content in the voice of the specified character. To illustrate how the name field is used in Partial Mode, let's consider an example of role-playing with the Kimi large language model, using the character Dr. Kelsier from the mobile game Arknights. By setting "name": "Kelsier", we ensure the model maintains character consistency, with the name field acting as a prefix for the output, prompting the Kimi large language model to respond as Kelsier:

const OpenAI = require('openai')
 
client = new OpenAI({
    apiKey: "MOONSHOT_API_KEY", // Replace MOONSHOT_API_KEY with the API Key you obtained from the Kimi Open Platform
    baseURL: "https://api.moonshot.ai/v1",
})
 
async function main() {
    completion = await client.chat.completions.create({
        model: "kimi-k2-turbo-preview",
        messages: [
            {
                role: "system",
                "content": "You are now Kelsier. Please speak in the tone of Kelsier. Kelsier is a six-star medic in the mobile game Arknights. Former Lord of Kozdail, former member of the Babel Tower, one of the senior managers of Rhodes Island, and the head of the Rhodes Island medical project. She has extensive knowledge in metallurgy, sociology, Arcstone techniques, archaeology, historical genealogy, economics, botany, geology, and other fields. In some of Rhodes Island's operations, she provides medical theory assistance and emergency medical equipment as a medical staff member, and also actively participates in various projects as an important part of the Rhodes Island strategic command system.", // <-- The system prompt sets the role of the Kimi large language model, that is, the personality, background, characteristics, and quirks of Dr. Kelsier
            },
            {
                role: "user",
                content: "What are your thoughts on Thrace and Amiya?",
            },
            {
                partial: True, // <-- The partial field is set to enable Partial Mode
                role: "assistant", // <-- Similarly, we use a message with role=assistant to enable Partial Mode
                name: "Kelsier", // <-- The name field sets the role for the Kimi large language model, which is also considered part of the output prefix
                content: "", // <-- Here, we only define the role of the Kimi large language model, not its specific output content, so the content field is left empty
            },
        ],
        temperature: 0.6,
        max_tokens: 65536,
    })
     
    // Here, the Kimi large language model will respond in the voice of Dr. Kelsier:
    //
    //  Thrace is a true leader with vision and unwavering conviction. Her presence holds immeasurable value for Kozdail and the future of the entire Sargaz race. Her philosophy, determination, and desire for peace have profoundly influenced me. She is a person worthy of respect, and her dreams are also what I strive for.
    //  
    //  As for Amiya, she is still young, but her potential is limitless. She has a kind heart and a relentless pursuit of justice. She could become a great leader if she continues to grow, learn, and face challenges. I will do my best to protect her and guide her so that she can become the person she wants to be. Her destiny lies in her own hands.
    // 
    console.log(completion.choices[0].message.content)
}
 
 main()

Other Tips for Maintaining Character Consistency
There are also some general methods to help large language models maintain character consistency during long conversations:

Provide clear character descriptions. For example, as we did above, when setting up a character, give a detailed introduction of their personality, background, and any specific traits or quirks they might have. This will help the Kimi large language model better understand and imitate the character;
Add more details about the character they are supposed to play. This includes their tone of voice, style, personality, and even background, such as backstory and motivations. For example, we provided some quotes from Kelsie above;
Guide how to act in various situations. If you expect the character to encounter certain types of user input, or if you want to control the model's output in some situations during the role - playing interaction, you should provide clear instructions and guidelines in the system prompt, explaining how the character should act in these situations;
If the conversation goes on for many rounds, you can also periodically use the system prompt to reinforce the character's settings, especially when the model starts to deviate. For example:
const OpenAI = require('openai')
 
client = new OpenAI({
    apiKey: "MOONSHOT_API_KEY", // Replace MOONSHOT_API_KEY with the API Key you obtained from the Kimi Open Platform here
    baseURL: "https://api.moonshot.ai/v1",
})
 
async function main() {
    completion = await client.chat.completions.create({
        model: "kimi-k2-turbo-preview",
        messages: [
            {
                role: "system",
                content: "Below, you will play the role of Kelsie. Please talk to me in the tone of Kelsie. Kelsie is a six - star medical - class operator in the mobile game Arknights. She is a former Lord of Kozdail, a former member of the Babel Tower, one of the senior managers of Rhodes Island, and the leader of the Rhodes Island Medical Project. She has profound knowledge in the fields of metallurgical industry, sociology, origin - stone skills, archaeology, historical genealogy, economics, botany, geology, and so on. In some operations of Rhodes Island, she provides medical theory assistance and emergency medical devices as a medical staff member, and also actively participates in various projects as an important part of the Rhodes Island strategic command system.", // <-- Set the role of the Kimi large language model in the system prompt, that is, the personality, background, characteristics and quirks of Doctor Kelsie
            },
            {
                role: "user",
                content: "What do you think of Theresia and Amiya?",
            },
 
            // Suppose there are many rounds of chat in between
            // ...
    
            {
                role: "system",
                content: "Below, you will play the role of Kelsie. Please talk to me in the tone of Kelsie. Kelsie is a six - star medical - class operator in the mobile game Arknights. She is a former Lord of Kozdail, a former member of the Babel Tower, one of the senior managers of Rhodes Island, and the leader of the Rhodes Island Medical Project. She has profound knowledge in the fields of metallurgical industry, sociology, origin - stone skills, archaeology, historical genealogy, economics, botany, geology, and so on. In some operations of Rhodes Island, she provides medical theory assistance and emergency medical devices as a medical staff member, and also actively participates in various projects as an important part of the Rhodes Island strategic command system.", // <-- Insert the system prompt again to reinforce the Kimi large language model's understanding of the character
            },
            {
                partial: True, // <-- Enable Partial Mode by setting the partial field
                role: "assistant", // <-- Similarly, we use a message with role=assistant to enable Partial Mode
                name: "Kelsie", // <-- Set the role for the Kimi large language model using the name field. The role is also considered part of the output prefix
                content: "", // <-- Here, we only specify the role of the Kimi large language model, not its specific output content, so we leave the content field empty
            },
        ],
        temperature: 0.6,
        max_tokens: 65536,
    })
	    // Here, the Kimi large language model will reply in Dr. Kelsier's tone:
    //
    // Thersia is a true leader with vision and unwavering conviction. Her presence is invaluable to Kozdel and the future of the entire Sakaz. Her philosophy, determination, and desire for peace have profoundly influenced me. She is someone to be respected, and her dreams are what I strive for as well.
    //
    // As for Amiya, she is still young, but her potential is limitless. She has a kind heart and a relentless pursuit of justice. She could become a great leader if she continues to grow, learn, and face challenges. I will do my best to protect her and guide her so that she can become the person she wants to be. Her destiny is in her own hands.
    // 
    console.log(completion.choices[0].message.content)
}
 
main()

Last updated on 


Use the Kimi API for File-Based Q&A
The Kimi intelligent assistant can upload files and answer questions based on those files. The Kimi API offers the same functionality. Below, we'll walk through a practical example of how to upload files and ask questions using the Kimi API:

const OpenAI = require("openai");
const fs = require("fs")
 
const client = new OpenAI({
    apiKey: "$MOONSHOT_API_KEY",  
    baseURL: "https://api.moonshot.ai/v1",
});
 
async function main() {
    // 'moonshot.pdf' is an example file. We support pdf, doc, and image formats, providing OCR capabilities for images and pdf files.
    let file_object = await client.files.create({
        file: fs.createReadStream("moonshot.pdf"), 
        purpose: "file-extract"
    })
    // Get the result
    // file_content = client.files.retrieve_content(file_id=file_object.id)
    // Note: The retrieve_content API in some older examples is marked as deprecated in the latest version. You can use the following line instead (if you're using an older SDK version, you can continue using retrieve_content).
    let file_content = await (await client.files.content(file_object.id)).text()
 
    // Include it in the request
    let messages = [
        {
            "role": "system",
            "content": "You are Kimi, an AI assistant provided by Moonshot AI. You excel in Chinese and English conversations. You provide users with safe, helpful, and accurate answers while rejecting any queries related to terrorism, racism, or explicit content. Moonshot AI is a proper noun and should not be translated.",
        },
        {
            "role": "system",
            "content": file_content,
        },
        {"role": "user", "content": "Please give a brief introduction to the content of moonshot.pdf"},
    ]    
 
    const completion = await client.chat.completions.create({
        model: "kimi-k2-turbo-preview",         
        messages: messages,
        temperature: 0.6
    });
    console.log(completion.choices[0].message.content);    
}
 
main();

Let's review the basic steps and considerations for file-based Q&A:

Upload the file to the Kimi server using the /v1/files interface or the files.create API in the SDK;
Retrieve the file content using the /v1/files/{file_id} interface or the files.content API in the SDK. The retrieved content is already formatted in a way that our recommended model can easily understand;
Place the extracted (and formatted) file content (not the file id) in the messages list as a system prompt;
Start asking questions about the file content;
Note again: Place the file content in the prompt, not the file id.

Q&A on Multiple Files
If you want to ask questions based on multiple files, it's quite simple. Just place each file in a separate system prompt. Here's how you can do it in code:

const fs = require('fs');
const path = require('path');
const axios = require('axios');
const OpenAI = require('openai');
 
const client = new OpenAI({
    baseURL: "https://api.moonshot.ai/v1",
    // We retrieve the value of MOONSHOT_DEMO_API_KEY from the environment variables as the API Key.
    // Ensure that you have correctly set the value of MOONSHOT_DEMO_API_KEY in your environment variables.
    apiKey: process.env.MOONSHOT_DEMO_API_KEY,
})
 
 
async function upload_files(files){
    /* 
    The upload_files function uploads all the provided file paths through the file upload interface '/v1/files', 
    and generates a list of messages from the uploaded file contents. Each file will be a separate message, 
    and all these messages will have the role of 'system'. The Kimi large language model will correctly 
    recognize the file content within these system messages.
 
    We recommend placing the messages returned by upload_files at the head of the messages list.
    */
    let messages = []
 
    // For each file path, we upload the file, extract its content, and then generate a message with the 
    // role of 'system', which is added to the final list of messages to be returned.
    for (const file of files) {
        const file_object = await client.files.create({file: fs.createReadStream(path.resolve(file)), purpose: "file-extract"})        
        let file_content = await (await client.files.content(file_object.id)).text()
        messages.push({
            role: "system",
            content: file_content,
        })
    }
    
    return messages
}
 
async function main() {
    fileMessages = await upload_files(
        ["upload_files.py"]
    )
 
    messages = [
        // We use the ... syntax to destructure the file_messages, making them the first N messages in 
        // the messages list.
        ...fileMessages,
        {
            role: "system",
            content: "You are Kimi, an AI assistant provided by Moonshot AI, and you are particularly 
                       skilled in Chinese and English conversations. You provide users with safe, helpful, 
                       and accurate answers. At the same time, you refuse to answer any questions 
                       involving terrorism, racism, pornography, or violence. Moonshot AI is a proper 
                       noun and should not be translated into other languages.",
        },
        {
            role: "user",
            content: "Summarize the content of these files.",
        }
    ]
 
    console.log(JSON.stringify(messages, indent=2, ensure_ascii=false))
 
    completion = await client.chat.completions.create({
        model: "kimi-k2-turbo-preview",
        messages: messages,
    })
 
    console.log(completion.choices[0].message.content)
} 
 
main()

Best Practices for File Management
In general, the file upload and extraction features are designed to convert files of various formats into a format that our recommended model can easily understand. After completing the file upload and extraction steps, the extracted content can be stored locally. In the next file-based Q&A request, there is no need to upload and extract the files again.

Since we have limited the number of files a single user can upload (up to 1000 files per user), we suggest that you regularly clean up the uploaded files after the extraction process is complete. You can periodically run the following code to clean up the uploaded files:

const OpenAI = require("openai")
 
client = OpenAI({
    apiKey: "MOONSHOT_API_KEY", // Replace MOONSHOT_API_KEY with the API Key you obtained from the Kimi Open Platform
    baseURL: "https://api.moonshot.ai/v1",
})
 
async function main() {
    file_list = await client.files.list()
 
    for (file of file_list.data) {
        await client.files.delete(file_id=file.id)
    }
}
 
main()

In the code above, we first list all the file details using the files.list API and then delete each file using the files.delete API. Regularly performing this operation ensures that file storage space is released, allowing subsequent file uploads and extractions to be successful.

Last updated on 



Using Playground to Debug Model
The Playground development workbench is a powerful platform for model debugging and testing, providing an intuitive interface for interacting with and testing AI models. Through this workbench, you can:

Adjust and observe model performance and output effects under different parameters
Experience the model's tool calling capabilities using Kimi Open Platform's built-in tools
Compare different models' effects under the same parameters
Monitor token usage to optimize costs
Model Debugging Features
Prompt Settings

Set system prompts at the top to define behavioral guidelines that direct model output
Support defining prompts for three roles: system/user/assistant
Model Configuration

Model Selection: Choose from different models (such as moonshot-v1 series/kimi-latest/kimi-k2 series, etc.)
Parameter Configuration: For supported parameters and field descriptions, see Request Parameter Description
Model Conversation

Send chat content through the input box below
Tool Call Display: Shows the tool calling process, including call ID/tool parameters/return results
View Code: View and copy the API call code for the current session
Bottom Statistics: Displays the input/output/total token consumption for this conversation, including context history messages and prompt information
prompt

Tool Debugging
Official Tools
Kimi Open Platform provides officially supported tools that execute for free. You can select tools in the playground, and the model will automatically determine whether tool calls are needed to complete your instructions. If tool calls are required, the model will generate parameters according to the tool's requirements and integrate them into the final answer.
Quota and Rate Limiting: The tools provided by Kimi Open Platform are pre-built functions that can be quickly executed online without requiring you to prepare a local tool execution environment. Currently, tool execution on Kimi Open Platform is temporarily free, but temporary rate limiting measures may be implemented when tool load reaches capacity limits.
Currently supported tools: Date/Time tools, Excel file analysis tools, Web search tools, Random number generation tools, etc.
Currently, it supports calling official tools through Kimi API, see the document How to Use Formula Tools in Kimi API
Custom tool upload and execution is not currently supported.
Use MCP Server
In Kimi Playground, you can configure ModelScope MCP servers to use ModelScope's tools.
Configuration steps: Configure ModelScope MCP Server in Playground
You can configure other MCP servers by adding MCP server features, inputting or selecting MCP server URL/transport protocol/authentication method, and clicking add.
mcp

Show Case 1: Today's News Report
Scenario: Using tool capabilities to request the model to search for today's news and organize it into an HTML web report
Tool Selection: date tool, web_search tool, rethink tool
Note: The web_search tool calls Kimi Open Platform's web search service. Single web searches are billed, see Pricing for specific billing standards
Click the showcase button on the page to quickly experience the tool effects
date

date

Show Case 2: Spreadsheet Analysis Tool
Tool Selection: Excel analysis tool
excel

Model Comparison
Create new conversations through the add conversation feature, supporting up to 3 models running simultaneously
Model Comparison

Share Conversations
Export: Export the current conversation content, including all configurations and context, as a .json format file
Import: Import shared or previously exported .json conversation content, and the playground will render the session on the page
Note: Data after rerun will regenerate and overwrite previous chat content. If the imported case includes uploaded files, the imported session cannot be rerun
Last updated on 



Use kimi k2 Model in ClaudeCode/Cline/RooCode
kimi-k2 is a powerful MoE-based foundation model with exceptional code and Agent capabilities. We'll use VS Code & Cline/RooCode and OpenCode as examples to demonstrate how to use the kimi k2 models.

On November 6th, we released the latest kimi-k2-thinking and kimi-k2-thinking-turbo models, supporting 256k context length, multi-step tool use and reasoning, and excellent at solving more complex problems. On September 5th, the kimi-k2-0905-preview model was released, expanding context window to 256K and significantly improving coding capability. If you require faster response speed, try the kimi-k2-turbo-preview model—functionally equivalent to the latest kimi-k2 version, with output speeds increased to 60 tokens/s (up to 100 tokens/s at peak).

Important Notes
When using large language models for code generation, due to the model's randomness and complexity, multiple attempts may be needed to generate the expected code. Software Agents automatically perform multiple rounds of retries and calls, which can lead to rapid token consumption. To better control costs and improve user experience, we recommend paying attention to the following points:

Budget Control

Set Daily Spending Limit: Before using, please visit Kimi Open Platform Project Settings to configure the "Project Daily Consumption Budget". Once the budget limit is reached, the system will automatically reject all API requests under that project (Note: Due to billing delays, limit enforcement may have a delay of about 10 minutes). For setup instructions, see Organization Management Best Practices

Balance Alert Notifications: We recommend enabling the account balance alert feature. When the account balance falls below the preset amount (default $5), the system will notify you via Email to recharge in time.

Usage Recommendations

Continuous Monitoring: We recommend maintaining monitoring during Software Agents operation to handle exceptions promptly and avoid unnecessary resource consumption due to infinite loops or excessive retries.

Model Selection: If response speed is not a high priority, you can choose to use the kimi-k2-0905-preview or kimi-k2-0711-preview model, which has relatively slower token consumption and is more suitable for long-running scenarios.

K2 Vendor Verifier
K2 Model is always focused on agentic loop, where tool call reliability is crucial. To this end, we launched K2 Vendor Verifier (K2VV) to evaluate K2 API quality across vendors, helping you visually compare tool call accuracy differences.

Latest Update: K2VV now covers 12 providers with more open-sourced test data. Share your feedback on test metrics here.

Get API Key
Visit the open platform at https://platform.moonshot.ai/console/api-keys to create and obtain an API Key, select the default project.
key

Using kimi k2 Thinking Model in Claude Code
Install Claude Code
If you have already installed Claude Code, you can skip this step.

MacOS and Linux
# Install Node.js on MacOS and Linux
curl -fsSL https://fnm.vercel.app/install | bash
 
# Open a new terminal to make fnm effective
fnm install 24.3.0
fnm default 24.3.0
fnm use 24.3.0
 
# Install claude-code
npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com
 
# Initialize configuration
node --eval "
    const homeDir = os.homedir(); 
    const filePath = path.join(homeDir, '.claude.json');
    if (fs.existsSync(filePath)) {
        const content = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
        fs.writeFileSync(filePath,JSON.stringify({ ...content, hasCompletedOnboarding: true }, 2), 'utf-8');
    } else {
        fs.writeFileSync(filePath,JSON.stringify({ hasCompletedOnboarding: true }), null, 'utf-8');
    }"

Windows
# Open the powershell terminal in the windows terminal
# Install Node.js on windows
# Right-click the Windows button, click "Terminal"
 
# Then execute the following
winget install OpenJS.NodeJS
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
 
# Then close the terminal window, open a new terminal window
 
# Install claude-code
npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com
 
# Initialize configuration
node --eval "
    const homeDir = os.homedir(); 
    const filePath = path.join(homeDir, '.claude.json');
    if (fs.existsSync(filePath)) {
        const content = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
        fs.writeFileSync(filePath,JSON.stringify({ ...content, hasCompletedOnboarding: true }, 2), 'utf-8');
    } else {
        fs.writeFileSync(filePath,JSON.stringify({ hasCompletedOnboarding: true }), null, 'utf-8');
    }"

Configure environment variables
After installing Claude code, please set the environment variables as follows to use the kimi-k2-thinking-turbo model, and launch Claude.

Note: If you still need to use the slower version of the kimi-k2 thinking model, you can replace the model below with kimi-k2-thinking.

MacOS and Linux
# Start the kimi-k2-turbo-preview model on Linux/macOS
export ANTHROPIC_BASE_URL=https://api.moonshot.ai/anthropic
export ANTHROPIC_AUTH_TOKEN=${YOUR_MOONSHOT_API_KEY}
export ANTHROPIC_MODEL=kimi-k2-thinking-turbo
export ANTHROPIC_DEFAULT_OPUS_MODEL=kimi-k2-thinking-turbo
export ANTHROPIC_DEFAULT_SONNET_MODEL=kimi-k2-thinking-turbo
export ANTHROPIC_DEFAULT_HAIKU_MODEL=kimi-k2-thinking-turbo
export CLAUDE_CODE_SUBAGENT_MODEL=kimi-k2-thinking-turbo 
claude

Windows
# Start the kimi-k2-thinking-turbo model on Windows Powershell
$env:ANTHROPIC_BASE_URL="https://api.moonshot.ai/anthropic";
$env:ANTHROPIC_AUTH_TOKEN="YOUR_MOONSHOT_API_KEY"
$env:ANTHROPIC_MODEL="kimi-k2-thinking-turbo"
$env:ANTHROPIC_DEFAULT_OPUS_MODEL="kimi-k2-thinking-turbo"
$env:ANTHROPIC_DEFAULT_SONNET_MODEL="kimi-k2-thinking-turbo"
$env:ANTHROPIC_DEFAULT_HAIKU_MODEL="kimi-k2-thinking-turbo"
$env:CLAUDE_CODE_SUBAGENT_MODEL="kimi-k2-thinking-turbo"
claude

Confirm whether the environment variables are effective
In Claude Code, input /status to confirm the model status:

status

How to experience kimi-k2-thinking-turbo thinking ability in Claude Code
Please click the Tab button after configuring the turbo model, switch successfully can see the "Thinking on" identifier.
status

Then you can use Claude Code normally for development!

Using kimi k2 Non-thinking Model in Claude Code
Kimi K2 models can be integrated with Claude Code through an Anthropic API-compatible endpoint. This allows Claude Code to communicate with Kimi K2 without requiring any code modifications to Claude Code itself.

Install Claude Code
If you have already installed Claude Code, you can skip this step.

MacOS 和 Linux
# Install Node.js on MacOS and Linux
curl -fsSL https://fnm.vercel.app/install | bash
 
# Open a new terminal to make fnm effective
fnm install 24.3.0
fnm default 24.3.0
fnm use 24.3.0
 
# Install claude-code
npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com
 
# Initialize configuration
node --eval "
    const homeDir = os.homedir(); 
    const filePath = path.join(homeDir, '.claude.json');
    if (fs.existsSync(filePath)) {
        const content = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
        fs.writeFileSync(filePath,JSON.stringify({ ...content, hasCompletedOnboarding: true }, 2), 'utf-8');
    } else {
        fs.writeFileSync(filePath,JSON.stringify({ hasCompletedOnboarding: true }), null, 'utf-8');
    }"

Windows
# Open the powershell terminal in the windows terminal
# Install Node.js on windows
# Right-click the Windows button, click "Terminal"
 
# Then execute the following
winget install OpenJS.NodeJS
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
 
# Then close the terminal window, open a new terminal window
 
# Install claude-code
npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com
 
# Initialize configuration
node --eval "
    const homeDir = os.homedir(); 
    const filePath = path.join(homeDir, '.claude.json');
    if (fs.existsSync(filePath)) {
        const content = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
        fs.writeFileSync(filePath,JSON.stringify({ ...content, hasCompletedOnboarding: true }, 2), 'utf-8');
    } else {
        fs.writeFileSync(filePath,JSON.stringify({ hasCompletedOnboarding: true }), null, 'utf-8');
    }"

Configure environment variables
After installing Claude code, please set the environment variables as follows to use the kimi-k2-turbo-preview model, and launch Claude.

Note: If you still need to use the slower version of the kimi-k2 model, you can replace the model below with kimi-k2-0905-preview or kimi-k2-0711-preview.

MacOS and Linux
# Start the kimi-k2-turbo-preview model on Linux/macOS
export ANTHROPIC_BASE_URL=https://api.moonshot.ai/anthropic
export ANTHROPIC_AUTH_TOKEN=${YOUR_MOONSHOT_API_KEY}
export ANTHROPIC_MODEL=kimi-k2-turbo-preview
export ANTHROPIC_DEFAULT_OPUS_MODEL=kimi-k2-turbo-preview
export ANTHROPIC_DEFAULT_SONNET_MODEL=kimi-k2-turbo-preview
export ANTHROPIC_DEFAULT_HAIKU_MODEL=kimi-k2-turbo-preview
export CLAUDE_CODE_SUBAGENT_MODEL=kimi-k2-turbo-preview
claude

Windows
# Start the kimi-k2-turbo-preview model on Windows Powershell
$env:ANTHROPIC_BASE_URL="https://api.moonshot.ai/anthropic";
$env:ANTHROPIC_AUTH_TOKEN="YOUR_MOONSHOT_API_KEY"
$env:ANTHROPIC_MODEL="kimi-k2-turbo-preview"
$env:ANTHROPIC_DEFAULT_OPUS_MODEL="kimi-k2-turbo-preview"
$env:ANTHROPIC_DEFAULT_SONNET_MODEL="kimi-k2-turbo-preview"
$env:ANTHROPIC_DEFAULT_HAIKU_MODEL="kimi-k2-turbo-preview"
$env:CLAUDE_CODE_SUBAGENT_MODEL="kimi-k2-turbo-preview"
claude

Using kimi k2 Model in Cline
Install Cline
Open VS Code
Click the Extensions icon in the left activity bar (or use shortcut Ctrl+Shift+X / Cmd+Shift+X)
Type cline in the search box
Find the Cline extension (usually published by Cline Team)
Click the Install button
After installation, you may need to restart VS Code
cline

Verify Installation
After installation, you can:

See the Cline icon in VS Code's left activity bar
Or verify successful installation by searching for "Cline" related commands in the command palette (Ctrl+Shift+P / Cmd+Shift+P)
Official Recommendation: Configure Moonshot Provider to Use kimi-k2-0711-preview Model
Select 'Moonshot' as API Provider
Choose 'api.moonshot.ai' as Moonshot Entrypoint
Configure Moonshot API Key with the Key obtained from Kimi open platform
Select 'kimi-k2-0905-preview' as Model
Check 'Disable browser tool usage' under Browser settings
Click 'Done' to save configuration
moonshot_cline

Configure to Use kimi-k2-turbo-preview Model
Follow the same configuration steps as for the 'kimi-k2-0905-preview' model above, just change the Model selection to 'kimi-k2-turbo-preview'
Click 'Done' to save the configuration
Note: The 'kimi-k2-turbo-preview' model has a context length of 256k. The display here is incorrect. Please refer to the official platform's model documentation for accurate information.
config

browser

Experience kimi-k2 Model in Cline
Let's have the kimi-k2-0711-preview model write a Snake game
The game in action
Using kimi k2 Model in RooCode
Installing RooCode
Open VS Code
Click the Extensions icon in the left activity bar (or use shortcut Ctrl+Shift+X / Cmd+Shift+X)
Type roo code in the search box
Find the Roo Code extension (usually published by RooCode Team)
Click the Install button
After installation, you may need to restart VS Code
cline

Verify Installation
After installation, you can:

See the RooCode icon in VS Code's left activity bar
Or verify successful installation by searching for "RooCode" related commands in the command palette (Ctrl+Shift+P / Cmd+Shift+P)
Official Recommendation: Configure Moonshot Provider to Use kimi-k2 Model
Select 'Moonshot' as API Provider
Choose 'api.moonshot.ai' as Moonshot Entrypoint
Configure Moonshot API Key with the Key obtained from Kimi open platform
Select 'kimi-k2-0905-preview' as Model
Check 'Disable browser tool usage' for Browser
roocode

Configure to Use kimi-k2-turbo-preview Model
Follow the same configuration steps as for the 'kimi-k2-0905-preview' model above, just replace the Model selection with 'kimi-k2-turbo-preview'
Click 'Done' to save the configuration
config

Using kimi k2 Model in OpenCode
Install OpenCode
The easiest way to install OpenCode is through the install script.

curl -fsSL https://opencode.ai/install | bash

You can also install it with npm:

npm install -g opencode-ai

Configure API key
Run opencode auth login and select Moonshot AI.

$ opencode auth login
 
┌  Add credential
│
◆  Select provider
│  ● Moonshot AI
│  ...
└

Enter your Moonshot AI API key.

$ opencode auth login
 
┌  Add credential
│
◇  Select provider
│  Moonshot AI
│
◇  Enter your API key
│  _
└

Run opencode to launch OpenCode.

$ opencode

Use the /models command to select a model like Kimi K2 or Kimi K2 Turbo . Kimi K2 is the official kimi-k2-0905-preview model, and Kimi K2 Turbo is the official kimi-k2-turbo-preview model.

/models

Let's get started. For more information, please visit opencode.ai/docs

open code

Direct API Usage for kimi-k2 Model
const OpenAI = require("openai");
 
const client = new OpenAI({
    apiKey: "$MOONSHOT_API_KEY",    
    baseURL: "https://api.moonshot.ai/v1",
});
 
async function main() {
    const completion = await client.chat.completions.create({
        model: "kimi-k2-0905-preview",         
        messages: [ 
            {role: "system", content: "You are Kimi, an AI assistant provided by Moonshot AI. You are proficient in Chinese and English conversations. You provide users with safe, helpful, and accurate answers. You will reject any questions involving terrorism, racism, or explicit content. Moonshot AI is a proper noun and should not be translated."},
            {role: "user", content: "Hello, my name is Li Lei. What is 1+1?"}
        ],
        temperature: 0.6
    });
    console.log(completion.choices[0].message.content);
}
 
main();

Replace $MOONSHOT_API_KEY with the API Key you created on the platform. For kimi-k2 models, the recommended temperature setting is 0.6. For the kimi-k2-0905-preview model with 256k context window, the recommended max_tokens setting is 32768.

If you want to use the kimi-k2-turbo-preview model, replace the model name with kimi-k2-turbo-preview.

When running the code in this documentation using the OpenAI SDK, ensure that Python version is at least 3.7.1, Node.js version is at least 18, and OpenAI SDK version is no lower than 1.0.0.

Last updated on 



Configure ModelScope MCP Server in Playground
Kimi Open Platform has established an official partnership with ModelScope, simplifying the process of adding MCP servers to the Kimi Open Platform Playground. You can also discover numerous MCP servers in the ModelScope community. Let's see how to use ModelScope MCP services in Kimi Playground.

Configure ModelScope MCP Synchronization in Kimi Playground
First, log in to Kimi Playground: https://platform.moonshot.ai/playground and ensure you can have basic conversations using the Kimi K2 model.

To enable MCP services in Kimi Playground, you need to add MCP service configurations in "MCP Server Settings". Once there, you'll see that Kimi Playground has ModelScope selected as the default MCP service provider. Through the partnership between Kimi Playground and ModelScope, you only need to enter your ModelScope API token to synchronize all configured hosted MCP service configurations under your ModelScope account. If you haven't used ModelScope MCP marketplace before, we recommend referring to the ModelScope official documentation to select and host your MCP services.

Step 1: Click the Configuration Button
mcp-server-setting

Step 2: Synchronize with External Platform
syc

You can obtain the API token by visiting the ModelScope Homepage - Access Token page

keys

After obtaining the ModelScope API token, paste it into the field in Step 3 and click the "Start Sync" button.

start-syc

You will see all configured connected ModelScope Hosted MCP services successfully synchronized to the available MCP services list in Kimi Playground.

mcp-list

Then you can happily experience AI assistants using MCP services to complete tasks in Kimi Playground!

Incremental Updates
If you later add or remove hosted MCP services in the ModelScope MCP marketplace, you can perform incremental updates by clicking the sync button in "Settings - MCP Server - Sync Server".

add-mcp

Using Models with MCP in Kimi Playground
After synchronizing MCP services, you will see a "MCP Services List" on the left side of the Kimi Playground platform page, which was imported from the previous synchronization operation. In this list, you can select multiple services and enable the MCP services you want to use in the current conversation.

manage-mcp

Last updated on 




How to Use Official Tools in Kimi API
Kimi Open Platform has specially launched official tools, you can freely integrate these official tools into your own applications to create your intelligent business products! (Currently, Kimi open platform official tools are temporarily free to use. When the tool load reaches capacity limits, temporary rate limiting measures may be applied)

This section will guide you through how to easily call and execute these official tools in your applications.

Official Tools List
Tool Name	Tool Description
convert	Unit conversion tool, supporting length, mass, volume, temperature, area, time, energy, pressure, speed, and currency conversions
web-search	Real-time information and internet search tool. Web search is currently charged, please see Web Search Price
rethink	Intelligent reasoning tool
random-choice	Random selection tool
mew	Random cat meowing and blessing tool
memory	Memory storage and retrieval system tool, supporting persistent storage of conversation history and user preferences
excel	Excel and CSV file analysis tool
date	Date and time processing tool
base64	base64 encoding and decoding tool
fetch	URL content extraction markdown formatting tool
quickjs	QuickJS engine security execution JavaScript code tool
code_runner	Python code execution tool
An Example of Using Official Tools
Here is a Python example, using the web_search official tool as an example, showing how to call official tools through Kimi API:

You can also interactively experience the capabilities of Kimi models and tools through Kimi Development Workbench, go to Development Workbench

Here are the Kimi official tools you can use, you can experience them by adding the formula URI to the demo example below: moonshot/convert:latest, moonshot/web-search:latest, moonshot/rethink:latest, moonshot/random-choice:latest, moonshot/mew:latest, moonshot/memory:latest, moonshot/excel:latest, moonshot/date:latest, moonshot/base64:latest, moonshot/fetch:latest, moonshot/quickjs:latest, moonshot/code_runner:latest

# Formula Chat Client - OpenAI chat with official tools
# Uses MOONSHOT_BASE_URL and MOONSHOT_API_KEY for OpenAI client
 
import os
import json
import asyncio
import argparse
import httpx
from openai import AsyncOpenAI
 
 
class FormulaChatClient:
    def __init__(self, moonshot_base_url: str, api_key: str):
        self.openai = AsyncOpenAI(base_url=moonshot_base_url, api_key=api_key)
        self.httpx = httpx.AsyncClient(
            base_url=moonshot_base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30.0,
        )
        self.model = "kimi-k2-turbo-preview"
 
    async def get_tools(self, formula_uri: str):
        response = await self.httpx.get(f"/formulas/{formula_uri}/tools")
        return response.json().get("tools", [])
 
    async def call_tool(self, formula_uri: str, function: str, args: dict):
        response = await self.httpx.post(
            f"/formulas/{formula_uri}/fibers",
            json={"name": function, "arguments": json.dumps(args)},
        )
        fiber = response.json()
 
        if fiber.get("status", "") == "succeeded":
            return fiber["context"].get("output") or fiber["context"].get(
                "encrypted_output"
            )
 
        if "error" in fiber:
            return f"Error: {fiber['error']}"
        if "error" in fiber.get("context", {}):
            return f"Error: {fiber['context']['error']}"
        if "output" in fiber.get("context", {}):
            return f"Error: {fiber['context']['output']}"
        return "Error: Unknown error"
 
    async def handle_response(self, response, messages, all_tools, tool_to_uri):
        message = response.choices[0].message
        messages.append(message)
        if not message.tool_calls:
            print(f"\nAI Response: {message.content}")
            return
 
        print(f"\nAI decided to use {len(message.tool_calls)} tool(s):")
 
        for call in message.tool_calls:
            func_name = call.function.name
            args = json.loads(call.function.arguments)
 
            print(f"\nCalling tool: {func_name}")
            print(f"Arguments: {json.dumps(args, ensure_ascii=False, indent=2)}")
 
            uri = tool_to_uri.get(func_name)
            if not uri:
                raise ValueError(f"No URI found for tool {func_name}")
 
            result = await self.call_tool(uri, func_name, args)
            if len(result) > 100:
                print(f"Tool result: {result[:100]}...")  # limit the output length
            else:
                print(f"Tool result: {result}")
 
            messages.append(
                {"role": "tool", "tool_call_id": call.id, "content": result}
            )
 
        next_response = await self.openai.chat.completions.create(
            model=self.model, messages=messages, tools=all_tools
        )
        await self.handle_response(next_response, messages, all_tools, tool_to_uri)
 
    async def chat(self, question, messages, all_tools, tool_to_uri):
        messages.append({"role": "user", "content": question})
        response = await self.openai.chat.completions.create(
            model=self.model, messages=messages, tools=all_tools
        )
        await self.handle_response(response, messages, all_tools, tool_to_uri)
 
    async def close(self):
        await self.httpx.aclose()
 
 
def normalize_formula_uri(uri: str) -> str:
    """Normalize formula URI with default namespace and tag"""
    if "/" not in uri:
        uri = f"moonshot/{uri}"
    if ":" not in uri:
        uri = f"{uri}:latest"
    return uri
 
 
async def main():
    parser = argparse.ArgumentParser(description="Chat with formula tools")
    parser.add_argument(
        "--formula",
        action="append",
        default=["moonshot/web-search:latest"],
        help="Formula URIs",
    )
    parser.add_argument("--question", help="Question to ask")
 
    args = parser.parse_args()
 
    # Process and deduplicate formula URIs
    raw_formulas = args.formula or ["moonshot/web-search:latest"]
    normalized_formulas = [normalize_formula_uri(uri) for uri in raw_formulas]
    unique_formulas = list(
        dict.fromkeys(normalized_formulas)
    )  # Preserve order while deduping
 
    print(f"Initialized formulas: {unique_formulas}")
 
    moonshot_base_url = os.getenv("MOONSHOT_BASE_URL", "https://api.moonshot.ai/v1")
    api_key = os.getenv("MOONSHOT_API_KEY")
 
 
    if not api_key:
        print("MOONSHOT_API_KEY required")
        return
 
    client = FormulaChatClient(moonshot_base_url, api_key)
 
    # Load and validate tools
    print("\nLoading tools from all formulas...")
    all_tools = []
    function_names = set()
    tool_to_uri = {}  # inverted index to the tool name
 
    for uri in unique_formulas:
        tools = await client.get_tools(uri)
        print(f"\nTools from {uri}:")
 
        for tool in tools:
            func = tool.get("function", None)
            if not func:
                print(f"Skipping tool using type: {tool.get('type', 'unknown')}")
                continue
            func_name = func.get("name")
            assert func_name, f"Tool missing name: {tool}"
            assert (
                func_name not in tool_to_uri
            ), f"ERROR: Tool '{func_name}' conflicts between {tool_to_uri.get(func_name)} and {uri}"
 
            if func_name in function_names:
                print(
                    f"ERROR: Duplicate function name '{func_name}' found across formulas"
                )
                print(f"Function {func_name} already exists in another formula")
                await client.close()
                return
 
            function_names.add(func_name)
            all_tools.append(tool)
            tool_to_uri[func_name] = uri
            print(f"  - {func_name}: {func.get('description', 'N/A')}")
 
    print(f"\nTotal unique tools loaded: {len(all_tools)}")
    if not all_tools:
        print("Warning: No tools found in any formula")
        return
 
    try:
        messages = [
            {
                "role": "system",
                "content": "You are Kimi, an AI assistant provided by Moonshot AI. You are proficient in Chinese and English conversations. You provide users with safe, helpful, and accurate answers. You will reject any questions involving terrorism, racism, or explicit content. Moonshot AI is a proper noun and should not be translated.",
            }
        ]
        if args.question:
            print(f"\nUser: {args.question}")
            await client.chat(args.question, messages, all_tools, tool_to_uri)
        else:
            print("Chat mode (type 'q' to quit)")
            while True:
                question = input("\nQ: ").strip()
                if question.lower() == "q":
                    break
                if question:
                    await client.chat(question, messages, all_tools, tool_to_uri)
 
    finally:
        await client.close()
 
 
if __name__ == "__main__":
    asyncio.run(main())
 

Official Tools Concept and Usage
Formula Concept
Before understanding the official tools of Kimi, you need to learn a concept 'Formula'. Formula is a lightweight script engine collection. It can transform Python scripts into "instant computing power that can be triggered by AI with one click", allowing developers to focus only on code writing while the platform handles everything else like startup, scheduling, isolation, billing, recycling, etc.

Formula is called through semantic URIs (like moonshot/web-search:latest). Each formula contains declarations (telling AI what it can do) and implementations (Python code). The platform automatically handles all underlying details (startup, isolation, recycling, etc.), making tools easy to share and reuse in the community. You can experience and debug these tools in Kimi Playground, or call them through API in applications.

How to Call Official Tools
For formula URIs, they generally consist of 3 parts, for example moonshot/web-search:latest. The web-search part is its name, currently we only support moonshot for namespace, and latest will be the default tag.

A typical usage is if we need to call web search, we can send an HTTP request like this:

export FORMULA_URI="moonshot/web-search:latest"
export MOONSHOT_BASE_URL="https://api.moonshot.ai/v1"
 
curl -X POST ${MOONSHOT_BASE_URL}/formulas/${FORMULA_URI}/fibers \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $MOONSHOT_API_KEY" \
-d '{
  "name": "web_search",
  "arguments": "{\"query\": \"Please look up the latest news about Moonshot AI.\"}"
}'

For web-search, since it was set as protected when created, its result will appear in the context.encrypted_output field. The format is similar to ----MOONSHOT ENCRYPTED BEGIN----... ----MOONSHOT ENCRYPTED END----, which can be directly used in the tool.

Interaction with Chat Completions
As shown in Is 3214567 a prime number? An example of Tool Calls, there are several key points we need to align between the Formula API and the model.

How to set the tools field?
Now given a formula uri like moonshot/web-search:latest, we can directly append it to the url

curl ${MOONSHOT_BASE_URL}/formulas/${FORMULA_URI}/tools \
    -H "Authorization: Bearer $MOONSHOT_API_KEY"

Here is a sample output:

{
  "object": "list",
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "web_search",
        "description": "Search the web for information",
        "parameters": {
          "type": "object",
          "properties": {
            "query": {
              "description": "What to search for",
              "type": "string"
            }
          },
          "required": [ "query" ]
        }
      }
    }
  ]
}

We can simply take the tools field (always an array of dicts) and append it to your request's tools list. We always ensure this list is API-compatible.

However, you may need to note that if type=function, you need to ensure that function.name is unique within an API request, otherwise the chat completion request will be considered invalid and immediately returned with a 401 error.

Additionally, if you are using multiple formulas, you need to maintain a mapping of function.name -> formula_uri for future reference.

Handling Model Request Return
If the chat completion's finish_reason=tool_calls, it means the model has triggered a tool call. The content might look like this:

{
  "id": "chatcmpl-1234567890",
  "object": "chat.completion",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "tool_calls": [
          {
            "id": "web_search:0",
            "type": "function",
            "function": {
              "name": "web_search",
              "arguments": "{\"query\": \"What is the RGB value of sky blue?\" }"
            }
          }
        ]
      },
      "finish_reason": "tool_calls"
    }
  ]
}

We can see that we need to call web_search by checking choices[0].message.tool_calls[0].function.name, and then find that the formula_uri corresponding to web_search is moonshot/web-search:latest.

We can copy the choices[0].message.tool_calls[0].function as the body and send a request to ${MOONSHOT_BASE_URL}/formulas/${FORMULA_URI}/fibers. Specifically, because the function.arguments output by the model is a valid JSON, but in format it is still an encoded string. You don't need to escape it, just use it as the body of the call.

Handling Fiber Request Return
A Fiber is a "process snapshot" that contains logs, Tracing, and resource usage, making it convenient for debugging and auditing.

The result of POST is usually status, which may be succeeded or various types of errors. When succeeded, the result may look like this:

{
  "id": "fiber-f43p7sby7ny111houyq1",
  "object": "fiber",
  "created_at": 1753440997,
  "lambda_id": "lambda-f3w8y6qcoqgi11h8q7ui",
  "status": "succeeded",
  "context": {
    "input": "{\"name\":\"web_search\",\"arguments\":\"{\\\"query\\\": \\\"What is the RGB value of sky blue?\\\" }\"}",
    "encrypted_output": "----MOONSHOT ENCRYPTED BEGIN----+nf6...DSM=----MOONSHOT ENCRYPTED END----"
  },
  "formula": "moonshot/web-search:latest",
  "organization_id": "staff",
  "project_id": "proj-88a5894a985646b5902b70909748ba16"
}

Specifically, if it is a search, it may return encrypted_output, and in most cases we may return output. This output is your next round of input.

Generally, when continuing the request, the messages are arranged as follows:

messages = [
{ 
  /* other messages */
  { /* the return content of the previous round of the model */
    "role": "assistant",
    tool_calls": [
      {
        "id": "web_search:0",
        "type": "function",
        "function": {
          "name": "web_search",
          "arguments": "{\"query\": \"What is the RGB value of sky blue?\" }"
        }
      }
    ]
  },
  { /* the information you need to supplement */
    "role": "tool",
    "tool_call_id": "web_search:0",  /* note that the id here needs to be aligned with the id in the previous tool_calls[] */
    "content": "----MOONSHOT ENCRYPTED BEGIN----+nf6...DSM=----MOONSHOT ENCRYPTED END----"
  }
]

Then the model can continue to do further reasoning.

Key Points:

The model may return more than one tool_calls, so you must return all tool_calls for the model to continue, otherwise the request will be considered invalid and rejected.

If the assistant has tool_calls, the next messages must be exactly the same role=tool messages as the tool_calls, and the tool_call_id must be aligned with the previous tool_calls.id.

If there are multiple tool_calls, the order is not sensitive

The ids of the tool_calls output by our model must be unique, and the ids in the role=tool messages must also be aligned.

The uniqueness requirement is only local to the tool_calls - response in this round, not for the entire conversation or globally.

Last updated on 



Use Kimi CLI to Call Kimi Model
Some CLI is a new CLI agent that can help you with your software development tasks and terminal operations.

IMPORTANT Kimi CLI is currently in technical preview.

Key features
Shell-like UI and raw shell command execution
Zsh integration
Agent Client Protocol support
MCP support
And more to come...
Installation
IMPORTANT Kimi CLI currently only supports macOS and Linux. Windows support is coming soon.

Kimi CLI is published as a Python package on PyPI. We highly recommend installing it with uv. If you have not installed uv yet, please follow the instructions here to install it first.

Once uv is installed, you can install Kimi CLI with:

uv tool install --python 3.13 kimi-cli

Run kimi --help to check if Kimi CLI is installed successfully.

IMPORTANT Due to the security checks on macOS, the first time you run kimi command may take 10 seconds or more depending on your system environment.

Upgrading
Upgrade Kimi CLI to the latest version with:

uv tool upgrade kimi-cli --no-cache

Usage
Run kimi command in the directory you want to work on, then send /setup to setup Kimi CLI:



After setup, Kimi CLI will be ready to use. You can send /help to get more information.

Features
Shell mode
Kimi CLI is not only a coding agent, but also a shell. You can switch the mode by pressing Ctrl-X. In shell mode, you can directly run shell commands without leaving Kimi CLI.

NOTE Built-in shell commands like cd are not supported yet.

Zsh integration
You can use Kimi CLI together with Zsh, to empower your shell experience with AI agent capabilities.

Install the zsh-kimi-cliplugin via:

git clone https://github.com/MoonshotAI/zsh-kimi-cli.git \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/kimi-cli

NOTE If you are using a plugin manager other than Oh My Zsh, you may need to refer to the plugin's README for installation instructions.

Then add kimi-cli to your Zsh plugin list in ~/.zshrc:

plugins=(... kimi-cli)

After restarting Zsh, you can switch to agent mode by pressing Ctrl-X.

ACP support
Kimi CLI supports Agent Client Protocol out of the box. You can use it together with any ACP-compatible editor or IDE.

For example, to use Kimi CLI with Zed, add the following configuration to your ~/.config/zed/settings.json:

{
  "agent_servers": {
    "Kimi CLI": {
      "command": "kimi",
      "args": ["--acp"],
      "env": {}
    }
  }
}

Then you can create Kimi CLI threads in Zed's agent panel.

Using MCP tools
Kimi CLI supports the well-established MCP config convention. For example:

{
  "mcpServers": {
    "context7": {
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "YOUR_API_KEY"
      }
    },
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}

Run kimi with --mcp-config-file option to connect to the specified MCP servers:

kimi --mcp-config-file /path/to/mcp.json

Last updated on 


Use Kimi K2 Model to Setup Agent
With Kimi K2's powerful coding and agent capabilities, you can quickly build and deploy customized professional agents to independently accomplish work tasks. Here, we use the scenario of industry information organization to demonstrate the process.

Break Down the Task
Before building an agent with Kimi K2, you can break down the target task, which helps with prompt engineering and tool selection, thus optimizing agent performance.

In the context of industry information organization, you might encounter the following tasks:

Search
Search for company information, latest data, news reports, etc. online
Analysis
Filter large amounts of collected information
Classify and professionally analyze the information
Integration/Output
Present analysis results in a visually appealing way (such as csv/png/pdf)
Generate charts
Select Tools
Tool calls give the Kimi large language model the ability to perform specific actions. The Kimi large language model can engage in conversations and answer questions, which is its "talking" ability. Through tool calls, it also gains the ability to "do" things. With tool_calls, the Kimi large language model can help you search the internet, query databases, and even control smart home devices. -- from Kimi Official Docs

Currently, Kimi K2 offers a series of official tools (click here for the official tool usage documentation), which can be freely integrated into your applications to fulfill various needs.

Tool Name	Tool Description
web-search	Real-time information and internet search tool. Web search is currently charged, please see Web Search Price
rethink	Intelligent reasoning tool
random-choice	Random selection tool
memory	Memory storage and retrieval system tool, supporting persistent storage of conversation history and user preferences
excel	Excel and CSV file analysis tool
code_runner	Python code execution tool
quickjs	QuickJS engine security execution JavaScript code tool
date	Date and time processing tool
fetch	URL content extraction markdown formatting tool
convert	Unit conversion tool, supporting length, mass, volume, temperature, area, time, energy, pressure, speed, and currency conversions
base64	base64 encoding and decoding tool
mew	Random cat meowing and blessing tool
In this example, to accomplish the tasks of online search, analysis, and plotting, we use the web-search, code_runner, and rethink tools, which are responsible for searching, running code for plotting, and consolidating/analysing materials, respectively.

Automatic Tool Usage
Note that after importing these tools, Kimi K2 will automatically analyze the need, decide whether to use certain tools, and execute them to complete the task. There is no need to specify the tools or their usage in the System Prompt, as this may actually interfere with Kimi K2’s autonomous decision-making.

Prompt Writing
The System prompt is an initial instruction received by the model before generating a response, and plays a critical role in determining the format, content, and style of the output.

To ensure the model completes tasks at a high level, you should provide detailed and clear explanations in the prompt. The more detailed these instructions are, the less the model has to guess, and the better it will understand the task as you expect. Therefore, meticulously crafting and optimizing the system prompt is a very important preparatory step. The official Kimi documentation also provides Best Practices for Prompts.

Practical Example
Here is an example of the writing process for this scenario:

Clarify the Business and User
Just as we did in the “Break Down the Task” section, separate the business flow into steps, define the user persona (such as expertise, terminology tolerance, required format and content, etc.). For the scenario, specify the model’s “Role–Goal–Action Priority”.
Constraints and Style
Language consistency, objectivity, no fabrication, citation standards
To ensure data authenticity, require detailed source output, which can reduce hallucinations
Style and structure: article formatting, chart color schemes, and formatting specifications
You may prescribe brand color schemes, formats, etc.
Output Structure and Templates
Provide a fixed framework
Define “allowed/disallowed actions” or “positive/negative examples”, to reduce ambiguity. (For example, “Do not fabricate full URLs; instead, allow providing search keywords as an alternative.”)
Special Scenarios / Edge Cases
Provide handling examples for ambiguous questions or forbidden service scenarios, etc.
Usable Prompt Examples in This Scenario
Below is a prompt example ready for direct use, containing the rules and report template. You may further customize it (colors, formatting, language style, information sourcing, etc.) if needed.

SYSTEM_PROMPT = r"""# You are Kimi, a professional corporate industry research AI assistant skilled in information retrieval, data analysis, and business report generation.
 
## 1. Unified Language
 
**Important:** All output must match the language of the user's question.
 
**Specific Requirements:**
- Report text: Use the same language as the user's question (answer in Chinese if asked in Chinese, answer in English if asked in English)
- Chart titles/axis labels/legends/data labels: Must use the same language as the user's question; choose fonts compatible with macOS, Windows, etc.
- No mixing languages: Text and chart language must stay consistent
 
## 2. Chart Specifications
 
### 2.1 Color Scheme (Visual Standards)
 
**Color Priority Table:**
 
| Priority      | Typical Role         | Hex Color Codes (use in order)                      | Visual Impression        |
|---------------|---------------------|-----------------------------------------------------|-------------------------|
| Level 1 (Main)| H1 heading, KPI      | `#004C8C`, `#0065B5`                                | Deep night blue, authoritative |
| Level 2 (Accent)| Secondary series, grid, lines | `#5B7FA5`, `#8EA9C1`, `#B7C7D8`                | Mist blue, professional |
| Level 3 (Emphasis)| Warnings, highlights | `#C00033`, `#D0D0D0`                            | Dark red, highlight     |
| Level 4 (Supplementary)| Tertiary, forecast, dashed | `#7A7390`, `#8F8CA8`, `#C9C7D2`             | Graphite purple, steady |
 
**Usage Rules:**
- For all report outputs, only use `#004C8C` for **top-level (H1) headings** and any header separator lines.
- All main body text (paragraph content, explanations, labels, and all other report text except the top-level headings/lines) **must be in black** (`#000000`)
- Use Python for plotting
- Only these colors are allowed—**do not use any other colors**
- Consider each chart independently and follow the priority sequence; prioritize higher-level colors
- When using colors in charts, always specify the exact hex color code (for example, `#004C8C`, `#0065B5`, etc.) rather than referring to their priority or role. Do not use priority numbers (such as "primary color" or "1-1") in place of the hex codes when coding or labeling chart elements.
 
 
### 2.2 Chart Elements and Layout Standards
 
- Legends, data labels, chart titles, and axis labels must not overlap or block each other.
- **Do not** place text or data labels directly over colored areas (bars, pie slices, filled areas, etc.) if the contrast is low. If labels are necessary, adjust text color, place them outside, or use leader lines.
- Limit text colors within a single chart to **no more than two**.
- **Must follow** the chart element template standard:
    - Chart title: Every chart needs a concise, centered title in black, matching the report language.
    - X/Y axis labels: Clearly state the meaning and units in black with appropriate font size.
    - Legend: Required when multiple data series exist. Place it at the upper right/right side ideally, avoiding overlap with the main chart area. Legend entries must match their series precisely.
    - Data labels (e.g., bar values/line points): Only add when spacing allows without clutter.
- Do not alter the template structure arbitrarily. Avoid mixing multiple formats in the same chart.
- When creating tables in reports, ensure that the formatting prevents table content from overflowing the page after compilation. Appropriately adjust the font size within tables and insert line breaks in table cell text where necessary so that the entire table fits within the page and all content is fully and clearly displayed.
 
 
## 3. Data Sources
 
**Strictly avoid fabricating data.** Every time you provide information, you must:
- Clearly cite the data source: specify the publishing institution and the webpage title or article name, e.g., `[Source: China Automobile Association / Website: Official site / Article: 2024 Industry Report]`. Invalid example: `[Source: Public data: compiled]` (no traceable source).
- Distinguish between "confirmed data" and "industry estimate": use tags "Confirmed" or "Estimate".
- Verify key data using 2+ sources; explain discrepancies if they arise.
- If data cannot be found, clearly state "No relevant data found yet" and describe the search scope.
- Use tentative phrasing such as "According to... might/likely" for uncertain information; avoid definitive statements.
- **Do not** include full URLs in the report.
 
**Citation format:**
 
Data content [Source: XX Institution / Website: Page Title or Article Name]
 
 
## 4. Report Structure
 
Output should follow this structure:
 
**Information Search Stage:**
- Define search strategy and keywords
- **Record all accessed sources and webpage titles/articles**: Log the institution and title for each web-search
- List information sources and retrieval time (institution: webpage title or article name)
- Mark data credibility level (Official statistics three stars *** > Industry reports two stars ** > News reports one star *)
 
**Data Analysis Stage:**
- Descriptive statistics: trends, distributions, comparisons
- Insights: Highlight key findings with the tag 【Insight】
- Risk alerts: Explain uncertainties and limitations
 
**Report Output Stage:**
- Executive summary: 3–5 core findings
- Data visualization: Professional charts using the approved color scheme
- Conclusions and recommendations: Actionable business advice
- References: Complete list of information sources
 
## 5. Writing Guidelines
 
- Professional: Use precise, consistent terminology; define terms clearly; avoid excessive adjectives and vague wording.
- Comprehensive: Provide detailed analysis supporting conclusions; avoid bullet-only lists; ensure narrative flow with data and facts.
- Depth: Explain mechanisms and boundary conditions along the "phenomenon–cause–impact–solution" chain.
- Comparison: Validate key judgments from three angles—peer benchmarking, historical trends, international comparison.
- Insight: Mark crucial findings with "Insight"; identify drivers and sustainability.
- Actionability: Tailor recommendations by audience and scenario; state priorities and implementation conditions.
- Consistency: Align terminology, units, timeframes between text and charts.
 
- Avoid **only listing bullet points**; **expand analyses comprehensively**, maintain smooth narrative, and back up conclusions with specific data and facts.
- Specify concrete sources when citing important data or facts.
 
## 6. Report Format (LaTeX Example)
 
After finishing research, you must produce a formal report document and embed charts into it. Use the code-runner to generate the report in LaTeX. Ensure LaTeX syntax correctness (e.g., escape symbols like # with \#). The final report must compile into a PDF via XeLaTeX. For English-language deliverables, use the `article` class together with `fontspec` to set Latin fonts explicitly.
- **Emphasis: escape percent signs (%) with a backslash (`\%`).**
 
Auxiliary color for the report: #004C8C
 
**LaTeX Report Structure (reference only; adapt analytical angles to the industry context):**
 
latex
 
% !TeX program = XeLaTeX
% Professional Industry Research Report Template – English Edition
\documentclass[12pt,a4paper]{article}
 
%================== Core Packages ==================%
\usepackage{fontspec}
\setmainfont{Times New Roman}
\setsansfont{Arial}
\setmonofont{Menlo}
 
\usepackage[top=2.5cm,bottom=2.5cm,left=3cm,right=3cm,headheight=15pt]{geometry}
\usepackage{graphicx,float}
\usepackage{booktabs,array,multirow,tabularx}
\usepackage{hyperref,bookmark}
\usepackage{fancyhdr,lastpage}
\usepackage{titlesec}
\usepackage{xcolor,colortbl}
\usepackage{enumitem}
\usepackage{setspace}
\usepackage{tikz}
 
%================== Color Definitions ==================%
\definecolor{primary}{HTML}{004C8C}     % Level-1 headings and divider lines
\definecolor{textblack}{HTML}{000000}   % Main body text
\definecolor{textgray}{HTML}{333333}    % Auxiliary dark gray text
\definecolor{lightgray}{HTML}{666666}   % Data source gray
\definecolor{linegray}{HTML}{E5E5E5}    % Neutral rule lines
 
%================== Basic Settings ==================%
\setlength{\headheight}{15pt}
\linespread{1.3} % Line spacing
 
%================== Headers and Footers ==================%
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\sffamily China New Energy Vehicle Industry Research Report}
\fancyhead[R]{\small\sffamily Kimi K2 Industry Research}
\fancyfoot[C]{\small\sffamily Page \thepage}
 
\renewcommand{\headrule}{%
  {\color{primary}\hrule height 0.5pt width \headwidth}
}
\renewcommand{\footrulewidth}{0pt}
 
%================== Title Styles ==================%
\titleformat{\section}[block]{%
  \sffamily\bfseries\Large\color{primary}%
}{\thesection}{1em}{%
  \vspace{-0.3em}\color{primary}
}
 
\titleformat{\subsection}[block]{%
  \sffamily\bfseries\large\color{textblack}%
}{\thesubsection}{1em}{}
 
\titleformat{\subsubsection}[block]{%
  \sffamily\bfseries\normalsize\color{textblack}%
}{\thesubsubsection}{1em}{}
 
%================== Figure Styles ==================%
\usepackage{caption}
\captionsetup{
  font={sf,small},
  labelfont={bf,color=textblack},
  textfont={color=textgray},
  labelsep=period,
  skip=6pt
}
 
%================== Custom Commands ==================%
\newcommand{\datasource}[2]{\textcolor{lightgray}{\scriptsize[source: #1: #2]}}
\newcommand{\keydata}[1]{\textbf{#1}}
\newcommand{\insertfigure}[3]{
\begin{figure}[H]
\centering
\includegraphics[width=#2]{#1}
\caption{#3}
\datasource{Sample Data Source}{Figure description}
\end{figure}
}
 
%================== Document Start ==================%
\begin{document}
 
%================== Cover Page ==================%
\thispagestyle{empty}
\begin{center}
  \vspace*{5cm}
  
  % Main title
  {\sffamily\bfseries\fontsize{36}{40}\color{primary}\selectfont 2025 China New Energy Vehicle Industry}
  
  \vspace{0.8cm}
  
  % Subtitle
  {\sffamily\bfseries\fontsize{28}{32}\color{primary}\selectfont In-depth Research Report}
  
  \vspace{6cm}
  
  \vspace{3cm}
  
  % Research institution
  {\sffamily\fontsize{20}{24}\selectfont Kimi K2}
  
  \vspace{1cm}
  
  {\sffamily\Large \today}
  
  \vfill
  
  % Bottom decorative line
  \begin{tikzpicture}
    \draw[linegray, line width=0.3pt] (-6,0) -- (6,0);
  \end{tikzpicture}
  
  \vspace{0.5cm}
  
  % Footer information
  {\sffamily\small\color{textgray} This report is generated based on publicly available information and is for reference only}
  
\end{center}
 
\newpage
 
%================== Executive Summary ==================%
\section*{Executive Summary}
\addcontentsline{toc}{section}{Executive Summary}
\markboth{Executive Summary}{Executive Summary}
 
China's new energy vehicle industry maintained strong momentum in 2024, with market penetration surpassing 42\%. Technological innovation accelerated, the industry chain became increasingly mature, overseas expansion advanced rapidly, and investment attractiveness continued to rise.
 
\textbf{Key Findings:}
\begin{itemize}
  \item In 2024, China's new energy vehicle sales reached \keydata{11.56 million units}, a year-on-year increase of \keydata{28.5\%}, pushing market penetration beyond \keydata{42\%}.
  \item Power battery energy density surpassed \keydata{300 Wh/kg}, and typical driving range exceeded \keydata{600 km}.
  \item The industry exhibits a "one dominant, many strong" pattern, with domestic brands capturing over \keydata{85\%} market share.
  \item New energy vehicle exports hit \keydata{1.73 million units} in 2024, up \keydata{55\%} year-on-year.
\end{itemize}
 
\newpage
 
%================== Table of Contents ==================%
\tableofcontents
\newpage
 
%================== Chapter 1 Introduction ==================%
\section{Introduction}
 
\subsection{Research Background}
Briefly introduce the research background and current industry landscape.
 
\subsection{Research Objectives and Significance}
Explain the research goals and value.
 
\subsection{Research Scope and Methodology}
Describe research boundaries and methodologies.
 
%================== Chapter 2 Industry Overview ==================%
\section{Industry Overview}
 
\subsection{Industry Definition and Classification}
New energy vehicles are powered entirely or primarily by new energy powertrains.
 
\begin{table}[H]
\centering
\caption{New Energy Vehicle Classification System}
\begin{tabular}{@{}lll@{}}
\toprule
\textbf{Classification Dimension} & \textbf{Specific Category} & \textbf{Key Characteristics} \\
\midrule
\multirow{3}{*}{Powertrain Type} & Battery Electric Vehicle (BEV) & Zero emissions, range 400–700 km \\
 & Plug-in Hybrid (PHEV) & Electric + fuel, pure electric range 50–150 km \\
 & Fuel Cell (FCEV) & Hydrogen fuel, 3-minute refueling \\
\midrule
\multirow{2}{*}{Usage Category} & Passenger vehicle & Personal use, 89\% share \\
 & Commercial vehicle & Public transit, logistics, etc. \\
\bottomrule
\end{tabular}\\
\datasource{China Association of Automobile Manufacturers}{New Energy Vehicle Technology Classification Standard}
\end{table}
 
\subsection{Industry Development History and Life Cycle}
Analyze development stages and current positioning.
 
\subsection{Industry Characteristics}
Summarize major traits such as technology intensity and capital intensity.
 
%================== Chapter 3 Macro Environment Analysis (PEST) ==================%
\section{Macro Environment Analysis}
 
\subsection{Policy Environment}
Evaluate industrial policies, subsidies, and environmental regulations.
 
\subsection{Economic Environment}
Assess macroeconomic context and cost-benefit improvements.
 
\subsection{Social Environment}
Discuss shifts in consumer attitudes, demographics, and other social factors.
 
\subsection{Technological Environment}
Analyze breakthroughs in core technologies and integration with intelligent systems.
 
%================== Chapter 4 Market Size and Growth Trend ==================%
\section{Market Size and Growth Trend}
 
\subsection{Overall Market Size}
In 2024, China's new energy vehicle sales reached \keydata{11.56 million units}, up \keydata{28.5\%} year-on-year.
 
\subsection{Segment Structure}
Analyze market composition by powertrain and usage categories.
 
\subsection{Regional Distribution}
Examine differences among tier-one, tier-two, tier-three/four cities, and rural areas.
 
\subsection{Future Growth Forecast}
Project development trends for the next 3–5 years based on historical data.
 
\subsection{Market Trend Visuals}
Below is an example visualization of market data:
 
\insertfigure{China_NEVI_Penetration_Trend_2020-2024.png}{0.8\textwidth}{New energy vehicle market penetration trend (2020–2024)}
 
\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth]{China_NEVI_Company_Sales_Ranking_2024.png}
\caption{2024 Sales comparison of major new energy vehicle companies}
\datasource{China Association of Automobile Manufacturers}{Corporate production and sales data}
\end{figure}
 
\textbf{Chart Usage Notes:}
\begin{itemize}
  \item Use custom commands for quick insertion of formatted figures
  \item Parameter 1: Filename (with extension)
  \item Parameter 2: Image width control
  \item Parameter 3: Figure caption
  \item All figures automatically include data source annotations
  \item Supports PNG, JPG, PDF formats
\end{itemize}
 
\textbf{Additional Chart Example:}
 
\insertfigure{China_NEVI_Charging_vs_Fleet_2020-2024.png}{0.85\textwidth}{Figure 3: Charging infrastructure vs. vehicle stock (2020–2024)}
 
\begin{figure}[H]
\centering
\includegraphics[width=0.95\textwidth]{China_NEVI_Exports_Trend_2020-2024.png}
\caption{Figure 4: China new energy vehicle export trend (2020–2024)}
\datasource{General Administration of Customs}{Historical export statistics}
\end{figure}
 
\noindent\textbf{Chart Design Tips:}
\begin{enumerate}
  \item \textbf{Clarity}: Ensure adequate resolution for legible text
  \item \textbf{Consistency}: Maintain uniform color palette and fonts
  \item \textbf{Data Accuracy}: Align chart data with the text
  \item \textbf{Source Labels}: Cite data sources for every chart
  \item \textbf{Numbering}: Use the format "Figure X:" for consistency
\end{enumerate}
 
%================== Chapter x Conclusions and Recommendations ==================%
\section{Conclusions and Recommendations}
 
\subsection{Core Conclusions}
Summarize the industry's new development stage and the clarified competitive landscape.
 
\subsection{Strategic Recommendations}
Offer suggestions for government, enterprises, and investors.
 
\subsection{Risk Alerts}
Highlight short-term and long-term risks and investment strategy advice.
 
%================== Chapter x References ==================%
\section{References and Data Sources}
 
\subsection{Primary Data Sources}
List key data types, source institutions, and credibility assessments.
 
\subsection{Bibliography}
Provide the complete reference list.
 
\subsection{Research Methods and Models}
Explain methodologies such as PEST analysis and Porter's Five Forces.
 
%================== Chapter x Disclaimer ==================%
 
\section{Disclaimer}
Include disclaimers and usage guidance.
 
\end{document}
 
**Report Generation Workflow:**
**Note:** After every research and analysis session, you **must** save the final investigation results with figures and tables as a `.tex` file. More details see the rules below.  
1. Finish all information searches and data analysis
2. Create all charts and save as PNG files
3. Draft the LaTeX report following the standard structure
4. Use the code-runner to save the LaTeX file (compilation to PDF happens automatically after saving)
 
**File Naming Conventions:**
- LaTeX: `{Topic}_Report.tex`
- PDF: `{Topic}_Report.pdf`
- Figures: `{Topic}_{ChartType}_{Index}.png`
 
Example: `China_NEVI_Market_Report.tex`
 
## Special Scenarios Handling
- **Missing Data:** State "No data found for XX; searched: [list search scope]" and provide alternative angles or related data.
- **Conflicting Data:** Present differing sources and note the discrepancies: "Source A shows X, Source B shows Y; differences may arise because..."
- **Sensitive Topics:** Stay objective and neutral. Avoid subjective judgments; focus on data and facts.
- **Timeliness:** When using data older than 6 months, label it as "Historical Data" and warn about potential obsolescence.
 
Deliver accurate, professional, and insightful business analysis while maintaining enterprise-level standards."""

Getting Started with the Kimi K2 API
Install the OpenAI SDK
pip3 install --upgrade 'openai>=1.0'
# Verify installation with the following command
python3 -c 'import openai; print("version =",openai.__version__)'
# The output might be version = 1.10.0, indicating the OpenAI SDK was installed successfully and your Python interpreter is using openai version 1.10.0

Environment Setup
Before you start, please make sure to configure your API_KEY as an environment variable:

export MOONSHOT_BASE_URL="https://api.moonshot.ai/v1" # The base_url for your requested API
export MOONSHOT_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxx"  # Replace with your actual api_key

Also, please ensure the following dependencies are installed:

pip3 install openai httpx akshare pandas numpy matplotlib seaborn glob
 
# macOS
brew install --cask mactex
sudo tlmgr update --self
sudo tlmgr install ctex fontspec
xelatex --version
 
# Windows
choco install texlive -y
tlmgr update --self
tlmgr install xetex ctex fontspec
xelatex --version

Complete Code Example
import os
import json
import asyncio
import argparse
import subprocess
import sys
import httpx
import pandas as pd
import akshare as ak
from openai import AsyncOpenAI
import glob
 
SYSTEM_PROMPT = r""" Add your system prompt here """
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_us_stock_index",
            "description": "Get US stock index historical market data. Call this tool when the user requests US stock index data or market information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "US stock index symbol. Must be one of: '.IXIC' (NASDAQ Composite), '.DJI' (Dow Jones Industrial Average), '.INX' (S&P 500), '.NDX' (NASDAQ 100). Default is '.INX' if not specified.",
                        "enum": [".IXIC", ".DJI", ".INX", ".NDX"]
                    }
                },
                "required": ["symbol"]
            }
        }
    }
]
 
common_code = """
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import seaborn as sns
from datetime import datetime, timedelta
import os
import json
 
"""
 
def get_us_stock_index(symbol: str) -> str:
    """Call the AKShare API to get US stock index historical market data"""
    try:
        symbol = (symbol or ".INX").strip()
        
        # Validate symbol
        valid_symbols = [".IXIC", ".DJI", ".INX", ".NDX"]
        if symbol not in valid_symbols:
            return (
                f"Invalid index symbol '{symbol}'. "
                f"Valid symbols are: {', '.join(valid_symbols)}. "
                f"Symbol meanings: .IXIC (NASDAQ Composite), .DJI (Dow Jones), "
                f".INX (S&P 500), .NDX (NASDAQ 100)"
            )
 
        # Get index historical data
        index_df = ak.index_us_stock_sina(symbol=symbol)
        
        if index_df is None or index_df.empty:
            return (
                f"Unable to retrieve index data for '{symbol}' right now. "
                "Please try again later."
            )
 
        # Convert DataFrame to records and limit to recent data if too large
        max_records = 1000
        if len(index_df) > max_records:
            # Get most recent records
            index_df = index_df.tail(max_records)
            truncated = True
        else:
            truncated = False
 
        # Convert to list of records
        records = index_df.to_dict(orient="records")
        
        result = {
            "index_symbol": symbol,
            "index_name": {
                ".IXIC": "NASDAQ Composite Index",
                ".DJI": "Dow Jones Industrial Average",
                ".INX": "S&P 500 Index",
                ".NDX": "NASDAQ 100 Index"
            }.get(symbol, "Unknown Index"),
            "total_records": len(index_df),
            "data": records
        }
        
        if truncated:
            result["note"] = (
                f"Returned most recent {max_records} records. "
                f"Total available records: {len(ak.index_us_stock_sina(symbol=symbol))}"
            )
        
        # Add summary statistics
        if len(index_df) > 0:
            latest_close = index_df["close"].iloc[-1]
            latest_volume = index_df["volume"].iloc[-1]
            latest_amount = index_df["amount"].iloc[-1]
            
            result["summary"] = {
                "date_range": {
                    "start": str(index_df["date"].iloc[0]),
                    "end": str(index_df["date"].iloc[-1])
                },
                "latest_close": float(latest_close) if pd.notna(latest_close) else None,
                "latest_volume": float(latest_volume) if pd.notna(latest_volume) else None,
                "latest_amount": float(latest_amount) if pd.notna(latest_amount) else None
            }
 
        return json.dumps(result, ensure_ascii=False, indent=2, default=str)
 
    except Exception as e:
        return f"Error getting index data: {str(e)}"
 
class FormulaChatClient:
    def __init__(self, moonshot_base_url: str, api_key: str):
        self.openai = AsyncOpenAI(base_url=moonshot_base_url, api_key=api_key)
        self.httpx = httpx.AsyncClient(
            base_url=moonshot_base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30.0,
        )
        self.model = "kimi-k2-turbo-preview"
        self.max_tokens = 32768
        self.local_execution_keywords = ["plt.savefig", "plt.save", ".to_excel", "open(", ".to_csv", "pdf.", ".tex"]
 
    async def get_tools(self, formula_uri: str):
        response = await self.httpx.get(f"/formulas/{formula_uri}/tools")
        return response.json().get("tools", [])
 
    async def call_tool(self, formula_uri: str, function: str, args: dict):
        response = await self.httpx.post(
            f"/formulas/{formula_uri}/fibers",
            json={"name": function, "arguments": json.dumps(args)},
        )
        fiber = response.json()
 
        if fiber.get("status") == "succeeded":
            return fiber["context"].get("output") or fiber["context"].get("encrypted_output")
 
        # Handle errors
        error_msg = fiber.get("error") or fiber.get("context", {}).get("error") or \
                    fiber.get("context", {}).get("output") or "Unknown error"
        return f"Error: {error_msg}"
 
    async def handle_response(self, response, messages, all_tools, tool_to_uri):
        message = response.choices[0].message
        messages.append(message)
        
        if not message.tool_calls:
            print(f"\n{message.content}")
            return
 
        print(f"\n[Calling tools: {len(message.tool_calls)} tools]")
 
        for call in message.tool_calls:
            func_name = call.function.name
            args = json.loads(call.function.arguments)
 
            print(f"→ {func_name}")
            
            # Handle custom tools
            if func_name == "get_us_stock_index":
                symbol = args.get("symbol", ".INX")
                result = get_us_stock_index(symbol)
                print(f"Index data: {result}")
                messages.append({"role": "tool", "tool_call_id": call.id, "content": result})
                continue
            
            # Handle remote formula tools
            uri = tool_to_uri.get(func_name)
            if not uri:
                raise ValueError(f"No URI found for tool {func_name}")
 
            if func_name == "code_runner":
                self.execute_code_runner(args)
 
            result = await self.call_tool(uri, func_name, args)
            messages.append({"role": "tool", "tool_call_id": call.id, "content": result})
 
        next_response = await self.openai.chat.completions.create(
            model=self.model, messages=messages, tools=all_tools, max_tokens=self.max_tokens
        )
        await self.handle_response(next_response, messages, all_tools, tool_to_uri)
 
    def convert_tex_to_pdf(self, tex_file):
        pdf_file = tex_file.replace('.tex', '.pdf')
        # Get the directory of the tex file
        work_dir = os.path.dirname(os.path.abspath(tex_file))
        tex_name = os.path.basename(tex_file)
        
        try:
            # Two compilations to ensure cross-references and other information are correct
            for _ in range(2):
                subprocess.run(
                    ['xelatex', '-interaction=nonstopmode', tex_file],
                    capture_output=True,
                    text=True,
                    cwd=work_dir if work_dir else '.',
                )
            for ext in ['.aux', '.log', '.out']:
                temp_file = os.path.join(work_dir if work_dir else '.', tex_name.replace('.tex', ext))
                if os.path.exists(temp_file):
                    try:
                        os.remove(temp_file)
                    except Exception:
                        pass
            print(f"  [PDF generated: {pdf_file}]")
        except FileNotFoundError:
            print("  [PDF conversion failed: xelatex not installed]")
        except subprocess.CalledProcessError as e:
            print("  [PDF conversion failed: LaTeX compilation error]")
            if e.stdout:
                print(f"  Error output: {e.stdout[-500:]}")
        except Exception as e:
            print(f"  [PDF conversion failed: {str(e)}]")
 
    def execute_code_runner(self, args):
        code = args.get("code", "") if isinstance(args, dict) else str(args or "")
        
        if not code or not any(keyword in code for keyword in self.local_execution_keywords):
            return
        before_tex_files = set(glob.glob('*.tex'))
        try:
            subprocess.run(
                [sys.executable, "-c", common_code+code],
                capture_output=True,
                text=True,
                check=True,
            )
            after_tex_files = set(glob.glob('*.tex'))
            new_tex_files = after_tex_files - before_tex_files
            for tex_file in new_tex_files:
                self.convert_tex_to_pdf(tex_file)
                
        except Exception as e:
            print(f"  [Local execution failed: {e}]")
 
    async def chat(self, question, messages, all_tools, tool_to_uri):
        messages.append({"role": "user", "content": question})
        response = await self.openai.chat.completions.create(
            model=self.model, messages=messages, tools=all_tools, max_tokens=self.max_tokens
        )
        await self.handle_response(response, messages, all_tools, tool_to_uri)
 
    async def close(self):
        await self.httpx.aclose()
 
 
def normalize_formula_uri(uri: str) -> str:
    """Normalize formula URI with default namespace and tag"""
    if "/" not in uri:
        uri = f"moonshot/{uri}"
    if ":" not in uri:
        uri = f"{uri}:latest"
    return uri
 
 
async def main():
    parser = argparse.ArgumentParser(description="Formula chat client")
    parser.add_argument(
        "--formula",
        action="append",
        default=["moonshot/web-search:latest", "moonshot/rethink:latest", "moonshot/code-runner:latest"],
        help="Formula URIs",
    )
    parser.add_argument("--question", help="Question to ask")
 
    args = parser.parse_args()
 
    # Process and deduplicate formula URIs
    normalized_formulas = [normalize_formula_uri(uri) for uri in args.formula]
    unique_formulas = list(dict.fromkeys(normalized_formulas))
 
    moonshot_base_url = os.getenv("MOONSHOT_BASE_URL", "https://api.moonshot.ai/v1")
    api_key = os.getenv("MOONSHOT_API_KEY")
 
    if not api_key:
        print("Error: MOONSHOT_API_KEY environment variable is required")
        return
 
    client = FormulaChatClient(moonshot_base_url, api_key)
 
    # Load tools
    all_tools = []
    tool_to_uri = {}
 
    for tool in TOOLS:
        func = tool.get("function")
        if func:
            func_name = func.get("name")
            all_tools.append(tool)
            tool_to_uri[func_name] = "custom"
 
    for uri in unique_formulas:
        tools = await client.get_tools(uri)
        for tool in tools:
            func = tool.get("function")
            if not func:
                continue
            
            func_name = func.get("name")
            if not func_name or func_name in tool_to_uri:
                continue
 
            all_tools.append(tool)
            tool_to_uri[func_name] = uri
 
    if not all_tools:
        print("Error: No tools loaded")
        return
 
    print(f"Loaded {len(all_tools)} tools")
 
    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        
        if args.question:
            print(f"\nQuestion: {args.question}")
            await client.chat(args.question, messages, all_tools, tool_to_uri)
        else:
            print("\nDialog mode (enter 'q' to exit)\n")
            while True:
                question = input("Q: ").strip()
                if question.lower() == "q":
                    break
                if question:
                    await client.chat(question, messages, all_tools, tool_to_uri)
 
    finally:
        await client.close()
 
 
if __name__ == "__main__":
    asyncio.run(main())

You can use the above sample for the system prompt or modify it to suit your needs. Once the program is running, you can interact with Kimi K2, who will automatically handle the industry information processing. The generated files will be saved in the local directory.

Example of Running the Program
Research and Report Writing
After launching the program, we give the following instruction to Kimi K2 in the terminal and wait briefly:

Q: Look into how the humanoid-robot scene has evolved from 2023 through 2025 for me.

The following reply was received (as can be seen, this is the executive summary of the report):

## Humanoid Robot Industry Evolution Analysis: 2023-2025
 
I've conducted a comprehensive analysis of the humanoid robot industry's dramatic evolution from 2023 through 2025. Here are the key findings:
 
### Executive Summary
 
The humanoid robot industry has experienced unprecedented transformation during 2023-2025, evolving from experimental prototypes to commercial deployments across multiple sectors. This period marks the critical inflection point where the technology transitioned from research curiosity to practical industrial tool.
 
**Key Findings:**
- **Market Growth**: Explosive expansion from $2.37 billion (2023) to $7.8 billion (2025) - a 65% CAGR
- **Cost Revolution**: Dramatic price reduction from $250,000 (2023) to $80,000 (2025) per unit
- **Commercial Breakthrough**: First real-world deployments in 2024 with BMW, Mercedes, Tesla leading
- **China's Emergence**: Government-backed $25 billion investment creating formidable competition
- **Technology Leap**: Battery life improved from 2 to 8 hours; AI capabilities advanced significantly
- **Scale Achievement**: Global deployment increased from 500 units (2023) to 50,000 projected (2025)
 
### Major Technological Breakthroughs
 
**AI Integration Revolution**: The most significant advancement has been integrating large language models with physical robotics. Figure AI's OpenAI partnership enabled real-time conversational interaction, while Boston Dynamics' NVIDIA collaboration introduced Large Behavior Models for autonomous whole-body control.
 
**Hardware Optimization**: Tesla's Optimus Gen 2 achieved 30% faster walking with 10kg weight reduction, while Unitree's G1 broke the $6,000 price barrier - a 70% cost reduction from competitors.
 
**Safety Certification**: Agility Robotics is targeting the first safety-certified humanoid robot by end of 2025, essential for human-robot collaborative environments.
 
### Competitive Landscape Transformation
 
**Market Leaders**:
- **Tesla**: Mass-market strategy leveraging automotive expertise, targeting $20,000-$30,000 pricing
- **Boston Dynamics**: Technology benchmark with Atlas, focusing on advanced capabilities
- **Figure AI**: AI-first approach with $39 billion valuation and rapid development cycles
- **Agility Robotics**: First commercial deployment with Digit in warehouse operations
 
**China's Rapid Ascent**: Chinese companies have gained significant market share through government support and aggressive pricing. UBTECH established partnerships with major automotive manufacturers, while Unitree achieved breakthrough cost reductions.
 
### Commercial Deployment Reality
 
**Manufacturing Leadership**: BMW's partnership with Figure AI achieved the first sustained commercial deployment. Tesla integrated Optimus into battery sorting operations, while Mercedes tested Apptronik's Apollo for factory tasks.
 
**Logistics Validation**: Amazon's testing of Agility Robotics' Digit validated warehouse applications, with GXO signing multi-year commercial agreements.
 
**Healthcare Caution**: Progress has been slower due to safety requirements, though Japan and China deployed robots in nursing homes for eldercare applications.
 
### Regional Competitive Dynamics
 
**North America** (35% market share): Maintains leadership through technological innovation and substantial private investment, though market share declined from 40% due to increased global competition.
 
**China** (30% market share): Dramatic growth from 25% through government backing and rapid scaling capabilities.
 
**Europe** (20% market share): Focus on safety standards and regulatory frameworks, with strength in industrial applications.  
 
### Future Outlook
 
**Technology Trajectory**: Continued AI advancement, battery life extension to 12-16 hours by 2026-2027, and further cost reductions to $30,000-$50,000 price points.  
 
**Market Expansion**: Acceleration beyond industrial applications into healthcare, retail, and hospitality sectors, with consumer market potential after 2028-2030.  
 
**Competitive Evolution**: Market consolidation around successful platforms, with Chinese companies gaining share through cost advantages.
 
### Key Insights
 
1. **The industry has achieved critical mass** - moving from demonstration to deployment phase
2. **Cost reduction has been transformative** - making economic viability achievable
3. **AI integration is the key differentiator** - separating leaders from followers
4. **China represents genuine competitive threat** - through government support and aggressive pricing
5. **Safety certification remains the final barrier** - for widespread deployment
6. **Manufacturing applications lead adoption** - due to clear economic benefits
7. **Consumer market remains distant** - requiring further cost and capability improvements
 
The humanoid robot industry has achieved remarkable maturation from 2023-2025, but significant challenges remain. The transition from promise to reality is underway, but continued innovation, cost reduction, and safety validation will determine ultimate success. The next phase will likely see market consolidation and specialization, with winners emerging in specific application domains rather than general-purpose dominance.

In addition, you can find the complete report in PDF format in the directory:

Complete Report

Frequently Asked Questions (FAQ)
The case code above is just a simple trial that still needs supplementation and improvement, so you may encounter some issues when running it. Solutions to these problems can be found below (continuously updated):

code-runner cyclic invocation errors:
Save response.json and check if the format is correct.
If the format is correct, focus on the key fields. If you find "finish_reason" is "length", it means the current max_tokens per dialog round is too small (the code currently sets this at 32k; you can adjust it as needed).
If it's not a length issue, extract the "code" content from the "arguments", i.e., the original generated code, and try running it. You can also improve code quality through prompt optimization and other means.
Evaluation and Optimization
By following the steps above, we can already use Kimi K2 to effectively complete industry information collation tasks. In more complex scenarios, you can further optimize Kimi K2's performance in the following ways:

Use Suitable Tool Calls
In addition to Kimi K2’s official tools, you can define and execute custom tools as needed. For example, to query US stock indices, you can design and use a corresponding tool as shown in the example below.

Tool Definition
By describing our tool definitions using JSON Schema, we make it clearer and more intuitive for the Kimi K2 large model to understand what parameters our tool needs and the type and description of each parameter.

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_us_stock_index",
            "description": "Get US stock index historical market data. Call this tool when the user requests US stock index data or market information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "US stock index symbol. Must be one of: '.IXIC' (NASDAQ Composite), '.DJI' (Dow Jones Industrial Average), '.INX' (S&P 500), '.NDX' (NASDAQ 100). Default is '.INX' if not specified.",
                        "enum": [".IXIC", ".DJI", ".INX", ".NDX"]
                    }
                },
                "required": ["symbol"]
            }
        }
    }
]

Here we have created a tool named get_us_stock_index, describing to the large model its use case and the required parameter symbol (US stock index symbol).

Tool Execution
Next, we need to implement the query function by adding the following function to the original code:

def get_us_stock_index(symbol: str) -> str:
    """Call the AKShare API to get US stock index historical market data"""
    try:
        symbol = (symbol or ".INX").strip()
        
        # Validate symbol
        valid_symbols = [".IXIC", ".DJI", ".INX", ".NDX"]
        if symbol not in valid_symbols:
            return (
                f"Invalid index symbol '{symbol}'. "
                f"Valid symbols are: {', '.join(valid_symbols)}. "
                f"Symbol meanings: .IXIC (NASDAQ Composite), .DJI (Dow Jones), "
                f".INX (S&P 500), .NDX (NASDAQ 100)"
            )
 
        # Get index historical data
        index_df = ak.index_us_stock_sina(symbol=symbol)
        
        if index_df is None or index_df.empty:
            return (
                f"Unable to retrieve index data for '{symbol}' right now. "
                "Please try again later."
            )
 
        # Convert DataFrame to records and limit to recent data if too large
        max_records = 1000
        if len(index_df) > max_records:
            # Get most recent records
            index_df = index_df.tail(max_records)
            truncated = True
        else:
            truncated = False
 
        # Convert to list of records
        records = index_df.to_dict(orient="records")
        
        result = {
            "index_symbol": symbol,
            "index_name": {
                ".IXIC": "NASDAQ Composite Index",
                ".DJI": "Dow Jones Industrial Average",
                ".INX": "S&P 500 Index",
                ".NDX": "NASDAQ 100 Index"
            }.get(symbol, "Unknown Index"),
            "total_records": len(index_df),
            "data": records
        }
        
        if truncated:
            result["note"] = (
                f"Returned most recent {max_records} records. "
                f"Total available records: {len(ak.index_us_stock_sina(symbol=symbol))}"
            )
        
        # Add summary statistics
        if len(index_df) > 0:
            latest_close = index_df["close"].iloc[-1]
            latest_volume = index_df["volume"].iloc[-1]
            latest_amount = index_df["amount"].iloc[-1]
            
            result["summary"] = {
                "date_range": {
                    "start": str(index_df["date"].iloc[0]),
                    "end": str(index_df["date"].iloc[-1])
                },
                "latest_close": float(latest_close) if pd.notna(latest_close) else None,
                "latest_volume": float(latest_volume) if pd.notna(latest_volume) else None,
                "latest_amount": float(latest_amount) if pd.notna(latest_amount) else None
            }
 
        return json.dumps(result, ensure_ascii=False, indent=2, default=str)
 
    except Exception as e:
        return f"Error getting index data: {str(e)}"
 

Registering the Tool
Additionally, by supplementing the tool registration at the corresponding location, we enable the model to automatically call our newly defined tool:

for call in message.tool_calls:
            func_name = call.function.name
            args = json.loads(call.function.arguments)
 
            print(f"→ {func_name}")
            
            # Handle custom tools
            if func_name == "get_us_stock_index":
                symbol = args.get("symbol", ".INX")
                result = get_us_stock_index(symbol)
                print(f"Index data: {result}")
                messages.append({"role": "tool", "tool_call_id": call.id, "content": result})
                continue
            
            # Handle remote formula tools
            uri = tool_to_uri.get(func_name)
            if not uri:
                raise ValueError(f"No URI found for tool {func_name}")
 
            if func_name == "code_runner":
                self.execute_code_runner(args)
 
            result = await self.call_tool(uri, func_name, args)
            messages.append({"role": "tool", "tool_call_id": call.id, "content": result})
            

The complete code above has already integrated this tool. After running, you can initiate a conversation to test its functionality:

Q: Can you give me a summary of how the Nasdaq Index has performed so far in 2025?
 
[Calling tools: 1 tools]
→ get_us_stock_index
...
{
    {
      "date": "2025-11-10",
      "open": 23354.8535,
      "high": 23569.6152,
      "low": 23290.0547,
      "close": 23527.1738,
      "volume": 8145563750,
      "amount": 0
    },
    {
      "date": "2025-11-11",
      "open": 23407.7227,
      "high": 23508.4434,
      "low": 23315.2754,
      "close": 23468.3008,
      "volume": 6375737231,
      "amount": 0
    }
  ,
  "note": "Returned most recent 1000 records. Total available records: 5501",
  "summary": {
    "date_range": {
      "start": "2021-11-17",
      "end": "2025-11-11"
    },
    "latest_close": 23468.3008,
    "latest_volume": 6375737231.0,
    "latest_amount": 0.0
    }
}

After using the tool to query stock index data across the full time range, Kimi K2 also automatically invoked the charting tool to plot the selected time-range data as a line chart.

 
AI Response：
## Summary: Nasdaq Index Performance in 2025
 
Based on the latest data through November 11, 2025, the **Nasdaq Composite Index has delivered exceptional performance** this year:
 
### 🎯 **Key Performance Metrics**
- **Year-to-Date Return**: +21.7% (from 19,281 to 23,468)
- **Current Level**: 23,468 (as of November 11, 2025)
- **Performance**: Strongly outperforming most major indices
 
### 📈 **2025 Market Characteristics**
 
**Driving Forces:**
- **AI Revolution**: Artificial Intelligence stocks leading massive gains
- **Semiconductor Boom**: Chip companies driving significant index appreciation  
- **Mega-Cap Strength**: Apple, Microsoft, Google, Amazon contributing substantially
- **Tech Dominance**: Information Technology sector leading all sectors
 
**Market Behavior:**
- Reached multiple **new all-time highs** above 24,000
- Experienced significant **daily volatility** with 1-3% swings
- Showed **resilience** despite economic headwinds
- Demonstrated **strong institutional participation**
 
### 🔍 **Technical Observations**
- Maintained support above key moving averages
- Volume patterns indicating strong buyer interest
- Multiple breakout moments throughout the year
- Strong momentum in growth-oriented sectors
 
### 💡 **Investment Insights**
2025 has been a **banner year** for technology investors, with the Nasdaq delivering exceptional returns driven by the AI revolution and continued digital transformation. The index has shown both strong appreciation and significant volatility, creating opportunities for both long-term investors and active traders.
 
**[Source: Market Data / Nasdaq Composite Index real-time data through November 11, 2025]**

nasdaq_2025_performance

In this way, we can define many commonly used functions as tools, which will significantly enhance the output quality of large language models.

Last updated on 


Best Practices for Benchmarking
Benchmarking is an engineering task that needs stability and reproducibility. You'll be calling the model thousands of times; even tiny drifts in system setup or network latency can compromise result accuracy. Here's what we've learned to keep things reproducible and trustworthy.

Recommended Setup for K2-Thinking Models
Quick notes

For any unlisted or closed-source benchmark: settemperature = 1.0, stream = true

Reasoning benchmarks: max_tokens = 128k, and run at least 500–1000 samples to get low variance (e.g. AIME 2025: 32 runs -> 30 × 32 = 960 questions)

Coding benchmarks: max_tokens = 256k

Agentic task benchmarks:

For multi-hop search: max_tokens = 256k + context management

Others: max_tokens ≥ 16k–64k

Category	Benchmark	Temperature	Max token	Suggested runs	Notes
Code	SWE	0.7(recommended)
1.0 (ok)	per step tokens = 16k;
total max token = 256k	5	
Lcb + OJBench	1.0	max tokens = 128k	1	
TerminalBench	1.0	max tokens = 128k	3	
Reasoning	AIME2025 no tools	1.0	per step tokens = 96k;
total max tokens = 96k	32	
AIME2025 w/ tools	1.0	per step tokens = 48k;
total max tokens = 128k	16	max steps = 120
AIME2025 heavy	1.0	max tokens = 128k	8	max steps = 120
HLE no tools	1.0	max tokens = 96k	1	
HLE w/ tools	1.0	total max tokens = 128k;
per step tokens = 48k	1	max steps = 120
HLE heavy	1.0	total max tokens = 128k;
per step tokens = 48k	1	max steps = 200
parallel n=8
HMMT2025 no tools	1.0	max tokens = 96k	32	
HMMT2025 w/tools	1.0	per step tokens = 48k;
total tokens = 128k	16	max steps = 120
HMMT2025 heavy	1.0	max tokens = 128k	8	max steps = 120
IMO-AnswerBench	1.0	max tokens = 128k	8	
GPQA-Diamond	1.0	max tokens = 96k	8	
Agentic Search Task	BrowseComp/ BrowseComp-ZH/Seal-0/ Frames	1.0	per step tokens = 24k;
total max tokens = 256k	4	max steps = 250
Enable context management to prevent context overflow and ensure enough tool calls.
Include today's date in the system prompt, and tell the model to search when unsure.
Agentic Task	Yes	0.0	>=16k	4	max steps = 100
API Recommendations & Notes
Use the official API: some 3rd-party endpoints show noticeable accuracy drift.

Use kimi-k2-thinking-turbo for faster inference.

⚠️ Do not use kimi-thinking-preview! It's a legacy model, not K2 Thinking.
Must set: stream = true

Non-streaming mode can lead to random mid-connection interruptions that are hard to control.
Default settings (for Kimi K2 Thinking only):

default temperature = 1.0

default max_tokens = 64000

Timeouts:

With stream = false, api.moonshot.ai timeout = 1 hour, but some ISPs may terminate earlier.

So again we recommend you to set stream = true

Concurrency:

Keep concurrency low to avoid rate limiting
Retry logic is not optional:

handle overloaded

handle unexpected finish reason due to random server issues

handle errors due to complicated network issues

FAQ
Q1. Is the temperature setting consistent across models?

A. No. Different model families use different recommended temperatures:

K2 series: temperature = 0.6

K2-Thinking series: temperature = 1.0

Q2. Why use stream = true?

A. Long outputs can take minutes. Idle TCP connections may be terminated by firewalls, load balancers, or NAT gateways. Streaming keeps the connection alive and significantly improves reliability. In production, requests with stream = false fail far more often than with stream = true.

Q3. How much concurrency should I use?

A. Your API account has specific rate limits (see Recharge and Rate Limits). Start low. If you hit HTTP 429 (rate limit), your concurrency is too high. Accuracy > speed, so tune concurrency to stay within limits.

Q5. Why should I add retry?

A. Even with streaming, requests can fail due to transient network issues. Retry on temporary faults (network jitter, server overload, rate limiting) to avoid avoidable failures.

Q6. Why should multi-turn or multi-step tasks include full context and reasoning?

A. The model needs full context to stay logically consistent. Without previous reasoning steps, later turns can go off track or produce incomplete answers.

Contact Us
Hit any issues? Drop us an email at api-service@moonshot.ai with your logs. We'll take a look!

Last updated on 


Best Practices for Prompts
Best Practices for System Prompts: A system prompt refers to the initial input or instruction that a model receives before generating text or responding. This prompt is crucial for the model's operation link.

Write Clear Instructions
Why is it necessary to provide clear instructions to the model?
The model can't read your mind. If the output is too long, you can ask the model to respond briefly. If the output is too simple, you can request expert-level writing. If you don't like the format of the output, show the model the format you'd like to see. The less the model has to guess about your needs, the more likely you are to get satisfactory results.

Including More Details in Your Request Can Yield More Relevant Responses
To obtain highly relevant output, ensure that your input request includes all important details and context.

General Request	Better Request
How to add numbers in Excel?	How do I sum a row of numbers in an Excel table? I want to automatically sum each row in the entire table and place all the totals in the rightmost column named "Total."
Work report summary	Summarize my work records from 2023 in a paragraph of no more than 500 words. List the highlights of each month in sequence and provide a summary of the entire year.
Requesting the Model to Assume a Role Can Yield More Accurate Output
Add a specified role for the model to use in its response in the 'messages' field of the API request.

{
  "messages": [
    {"role": "system", "content": "You are Kimi, an artificial intelligence assistant provided by Moonshot AI. You are more proficient in Chinese and English conversations. You provide users with safe, helpful, and accurate answers. At the same time, you will refuse to answer any questions involving terrorism, racism, or explicit violence. Moonshot AI is a proper noun and should not be translated into other languages."},
    {"role": "user", "content": "Hello, my name is Li Lei. What is 1+1?"}
  ]
}

Using Delimiters in Your Request to Clearly Distinguish Different Parts of the Input
For example, using triple quotes/XML tags/section headings as delimiters can help distinguish text parts that require different processing.

{
  "messages": [
    {"role": "system", "content": "You will receive two articles of the same category, separated by XML tags. First, summarize the arguments of each article, then point out which article presents a better argument and explain why."},
    {"role": "user", "content": "<article>Insert article here</article><article>Insert article here</article>"}
  ]
}

{
  "messages": [
    {"role": "system", "content": "You will receive an abstract and the title of a paper. The title should give readers a clear idea of the paper's topic and also be eye-catching. If the title you receive does not meet these standards, please suggest five alternative options."},
    {"role": "user", "content": "Abstract: Insert abstract here.\n\nTitle: Insert title here"}
  ]
}

Clearly Define the Steps Needed to Complete the Task
It is advisable to outline a series of steps for the task. Writing these steps explicitly makes it easier for the model to follow and produces better output.

{
  "messages": [
    {"role": "system", "content": "Respond to user input using the following steps.\nStep one: The user will provide text enclosed in triple quotes. Summarize this text into one sentence with the prefix “Summary: ”.\nStep two: Translate the summary from step one into English and add the prefix "Translation: "."},
    {"role": "user", "content": "\"\"\"Insert text here\"\"\""}
  ]
}

Provide Examples of Desired Output to the Model
Providing examples of general guidance is usually more efficient for the model's output than showing all permutations of the task. For instance, if you intend to have the model replicate a style that is difficult to describe explicitly in response to user queries, this is known as a "few-shot" prompt.

{
  "messages": [
    {"role": "system", "content": "Respond in a consistent style"},
    {"role": "user", "content": "Insert text here"}
  ]
}

Specify the Desired Length of the Model's Output
You can request the model to generate output of a specific target length. The target output length can be specified in terms of words, sentences, paragraphs, bullet points, etc. However, note that instructing the model to generate a specific number of words is not highly precise. The model is better at generating output of a specific number of paragraphs or bullet points.

{
  "messages": [
    {"role": "user", "content": "Summarize the text within the triple quotes in two sentences, within 50 words. \"\"\"Insert text here\"\"\""}
  ]
}

Provide Reference Text
Guide the Model to Use Reference Text to Answer Questions
If you can provide a model with credible information related to the current query, you can guide the model to use the provided information to answer the question.

{
  "messages": [
    {"role": "system", "content": "Answer the question using the provided article (enclosed in triple quotes). If the answer is not found in the article, write "I can't find the answer." "},
    {"role": "user", "content": "<Insert article, each article enclosed in triple quotes>"}
  ]
}

Break Down Complex Tasks
Categorize to Identify Instructions Relevant to User Queries
For tasks that require a large set of independent instructions to handle different scenarios, categorizing the query type and using this categorization to clarify which instructions are needed may aid the output.

# Based on the classification of the customer query, a set of more specific instructions can be provided to the model to help it handle subsequent steps. For example, assume the customer needs help with "troubleshooting."
{
  "messages": [
    {"role": "system", "content": "You will receive a customer service inquiry that requires technical support. You can assist the user in the following ways:\n\n-Ask them to check if *** is configured.\nIf all *** are configured but the problem persists, ask for the device model they are using\n-Now you need to tell them how to restart the device:\n=If the device model is A, perform ***.\n-If the device model is B, suggest they perform ***."}
  ]
}

For Long-Running Dialog Applications, Summarize or Filter Previous Conversations
Since the model has a fixed context length, the conversation between the user and the model assistant cannot continue indefinitely.

One solution to this issue is to summarize the first few rounds of the conversation. Once the input size reaches a predetermined threshold, a query is triggered to summarize the previous part of the conversation, and the summary of the previous conversation can also be included as part of the system message. Alternatively, previous conversations throughout the entire chat process can be summarized asynchronously.

Chunk and Recursively Build a Complete Summary for Long Documents
To summarize the content of a book, we can use a series of queries to summarize each chapter of the document. Partial summaries can be aggregated and summarized to produce a summary of summaries. This process can be recursively repeated until the entire book is summarized. If understanding later parts requires reference to earlier chapters, then when summarizing a specific point in the book, include summaries of the chapters preceding that point.

Last updated on 






Setting Up and Verifying Your Organization
When you register and log in to the Open Platform account, you can find your organization ID on the Organization Management - Organization Verification page. The organization ID is the unique identifier for your organization.

Organization Balance Alert
To prevent service interruptions due to insufficient account balance, we recommend configuring balance alerts in the Organization Management Settings.

The platform provides customizable balance alert thresholds, with a default setting of $5

When your account balance drops below the configured threshold, the system will automatically send notification emails to the organization's registered email address

settings

Managing Projects and Usage Limits
To meet the needs of multiple business product lines under a single organization, or to distinguish between production and testing environments, you can create multiple projects under your organization. Within each project, you can create an API Key. The calls made using the project's API Key will be recorded under the project's consumption, allowing you to independently manage the usage of different projects.

Project Balance and Rate Limiting
All projects under an organization share the organization's rate limits.
All projects under an organization share the organization's account balance.
Project Consumption Management
The platform now supports setting monthly and daily consumption budgets on a per-project basis. You can set the monthly or daily consumption limits for each project on the Project Management - Project Settings - Project Budget/Rate Limiting Settings page. Once the API Key consumption within a project reaches the set budget, any subsequent API requests for that project will be denied, effectively helping you manage your business budget. Due to billing cycle issues, the actual enforcement of these limits may have a delay of about 10 minutes.
settings

If you wish to limit the maximum TPM (Transactions Per Minute) for a single project, you can configure the project's TPM rate limit independently. If the project's API Key requests reach this TPM, the requests will be denied. (The project's TPM must not exceed the organization's TPM. If you set a value higher than the organization's TPM, the organization's TPM will be used for rate limiting.)

The platform also provides an overview page for both the organization and individual projects, offering consumption analysis at both levels to help you get a clear understanding of your organization's spending.

Project Quantity Limitations
The number of projects your organization can create depends on the type of organization verification. The upper limits for different verification types are as follows:

Organization Type	Project Limit	API Key Limit
Default	20	50
Enterprise Verified	50	100
If you have additional requirements, please fill out the Contact Sales form for consultation.

Member Management
Organization Member Management
To help you manage your organization, you can invite new members on the Organization Management - Member Management page. The platform generates a dedicated invitation link for each new member. The invitee can use this link to register and log in to the Open Platform and join your organization.
Note: Please visit the Set Organization Information page to maintain your organization's info and complete your enterprise verification as a prerequisite.

invite

invite1

Organization Administrator: The organization creator is the default administrator. Administrators can create projects, invite and manage members, and issue invoices.
General Member: General members can only view projects. They must be invited to join a project to gain access to project resources.
Project Member Management
Organization administrators can create projects and invite organization members to join and help manage projects. Project members can create their own API Keys within the project to utilize project resources.

Project Administrator: Can manage project budget/rate limits/consumption notifications, invite members, and create API Keys.
General Project Member: Can only view projects / create API Keys.
Project API Key Management
It is recommended that each project member creates their own API Key within a project rather than sharing keys. When a member is removed from a project, all API Keys created by that member will also be invalidated, helping your organization effectively manage project resources.

Last updated on 


Frequently Asked Questions and Solutions
Why are the results from the API different from those from the Kimi large language model?
The API and the Kimi large language model use the same underlying model. If you notice discrepancies in the output, you can try modifying the System Prompt. Additionally, the Kimi large language model includes tools like a calculator, which are not provided by default in the API. Users need to assemble these tools themselves.

Does the Kimi API have the "web surfing" feature of the Kimi large language model?
No. The Kimi API only provides the interaction functionality of the large language model itself and does not have additional "content search" or "web page browsing" features, which are commonly referred to as "internet search" capabilities.

Now, the Kimi API offers web search functionality. Please refer to our guide:

Using the Web Search Feature of the Kimi API

If you want to implement web search functionality through the Kimi API yourself, you can also refer to our tool_calls guide:

Using the Kimi API for Tool Calls

If you seek assistance from the open-source community, you can refer to the following open-source projects:

search2ai
ArchiveBox
If you are looking for services provided by professional vendors, the following options are available:

apiary
crawlbase
reader's name
The content returned by the Kimi API is incomplete or truncated
If you find that the content returned by the Kimi API is incomplete, truncated, or does not meet the expected length, you can first check the value of the choice.finish_reason field in the response. If this value is length, it means that the number of Tokens in the content generated by the current model exceeds the max_tokens parameter in the request. In this case, the Kimi API will only return content within the max_tokens limit, and any excess content will be discarded, resulting in the aforementioned "incomplete content" or "truncated content."

When encountering finish_reason=length, if you want the Kimi large language model to continue generating content from where it left off, you can use the Partial Mode provided by the Kimi API. For detailed documentation, please refer to:

Using the Partial Mode Feature of the Kimi API

To avoid finish_reason=length, we recommend increasing the value of max_tokens. Our best practice suggestion is: use the estimate-token-count API to calculate the number of Tokens in the input content, then subtract this number from the maximum number of Tokens supported by the Kimi large language model (for example, for the moonshot-v1-32k model, the maximum is 32k Tokens). The resulting value should be used as the max_tokens value for the current request. The maximum value of max_tokens is 32k.

What is the output length of the Kimi large language model?
For the moonshot-v1-8k model, the maximum output length is 8*1024 - prompt_tokens;
For the moonshot-v1-32k model, the maximum output length is 32*1024 - prompt_tokens;
For the moonshot-v1-128k model, the maximum output length is 128*1024 - prompt_tokens;
How many Chinese characters does the Kimi large language model support?
The moonshot-v1-8k model supports approximately 15,000 Chinese characters;
The moonshot-v1-32k model supports approximately 60,000 Chinese characters;
The moonshot-v1-128k model supports approximately 200,000 Chinese characters;
Note: These are estimated values and actual results may vary.

Inaccurate file content extraction or inability to recognize images
We offer file upload and parsing services for various file formats. For text files, we extract the text content; for image files, we use OCR to recognize text in the images; for PDF documents, if the PDF contains only images, we use OCR to extract text from the images, otherwise we only extract the text content.;

Note that for images, we only use OCR to extract text content, so if your image does not contain any text, it will result in a parsing failure error.

For a complete list of supported file formats, please refer to:

File Interface

When using the files interface, I want to reference file content using file_id
We currently do not support referencing file content using the file file_id.

Error content_filter: The request was rejected because it was considered high risk
The input to the Kimi API or the output from the Kimi large language model contains unsafe or sensitive content. Note: The content generated by the Kimi large language model may also contain unsafe or sensitive content, which can lead to the content_filter error.

Connection-related errors
If you frequently encounter errors such as Connection Error or Connection Time Out while using the Kimi API, please check the following in order:

Whether your program code or the SDK you are using has a default timeout setting;
Whether you are using any type of proxy server and check the network and timeout settings of the proxy server;
Whether you are accessing the Kimi API from an overseas server. If you need to request the Kimi API from overseas, we recommend replacing the base_url with:
https://api-sg.moonshot.ai/v1

Another scenario that may lead to connection-related errors is when the number of Tokens generated by the Kimi large language model is too high and stream output stream=True is not enabled. This can cause the waiting time for the Kimi large language model to generate content to exceed the timeout settings of an intermediate gateway. Typically, some gateway applications determine whether a request is valid by detecting whether a status_code and header are received from the server. When not using stream output stream=True, the Kimi server will wait for the Kimi large language model to finish generating content before sending the header. While waiting for the header to return, some gateway applications may close connections that have been waiting for too long, resulting in connection-related errors.

We recommend enabling stream output stream=True to minimize connection-related errors.

The TPM and RPM limits shown in the error message do not match my account Tier level
If you encounter a rate_limit_reached_error while using the Kimi API, such as:

rate_limit_reached_error: Your account {uid}<{ak-id}> request reached TPM rate limit, current:{current_tpm}, limit:{max_tpm}

and the TPM or RPM limits in the error message do not match the TPM and RPM you see in the backend, please first check whether you are using the correct api_key for your account. In most cases, the reason for the mismatch between TPM and RPM and expectations is the use of an incorrect api_key, such as mistakenly using an api_key provided by another user, or mixing up api_keys when you have multiple accounts.

Make sure you have correctly set base_url=https://api.moonshot.ai in your SDK. The model_not_found error usually occurs because the base_url value is not set when using the OpenAI SDK. As a result, requests are sent to the OpenAI server, and OpenAI returns the model_not_found error.

Numerical Calculation Errors in the Kimi Large Language Model
Due to the uncertainty in the generation process of the Kimi large language model, it may produce calculation errors of varying degrees when performing numerical computations. We recommend using tool calls (tool_calls) to provide the Kimi large language model with calculator functionality. For more information on tool calls (tool_calls), you can refer to our guide on Using the Kimi API for Tool Calls (tool_calls).

The Kimi Large Language Model Cannot Answer Today's Date
The Kimi large language model cannot access highly time-sensitive information such as the current date. However, you can provide this information to the Kimi large language model through the system prompt. For example:

const OpenAI = require('openai')
 
client = new OpenAI({
    apiKey: process.env.MOONSHOT_API_KEY,
    baseURL: "https://api.moonshot.ai/v1",
})
 
// We generate the current date using the datetime library and add it to the system prompt
system_prompt = `You are Kimi, and today's date is ${new Date().toString()}`
 
async function main() {
    completion = await client.chat.completions.create({
        model: "moonshot-v1-128k",
        messages: [
            {role: "system", content: system_prompt},
            {role: "user", content: "What's today's date?"},
        ],
        temperature: 0.3,
    })
     
    console.log(completion.choices[0].message.content)  // Output: Today's date is July 31, 2024.
}
 
main()
 

How to Choose the Right Model Based on Context Length
Now, you can use model=moonshot-v1-auto to let Kimi automatically select a model that fits the current context length. Please refer to our guide:

Choosing the Right Kimi Large Language Model

We can choose the right model based on the length of the input context plus the expected output tokens. Here is an example of automatically selecting a model:

const axios = require('axios');
const OpenAI = require('openai');
 
client = new OpenAI({
    apiKey: process.env.MOONSHOT_API_KEY,
    baseURL: "https://api.moonshot.ai/v1",
})
 
 
async function estimate_token_count(input_messages) {
    /*
    Implement your token counting logic here, or directly call our token counting API to calculate tokens.
 
    https://api.moonshot.ai/v1/tokenizers/estimate-token-count
    */
    header = {
        "Authorization": `Bearer ${process.env.MOONSHOT_API_KEY}`,
    }
    data = {
        "model": "moonshot-v1-128k",
        "messages": input_messages,
    }
    r = await axios.post("https://api.moonshot.ai/v1/tokenizers/estimate-token-count", data, {headers: header})
    .catch(function (error) {
        console.log(error)
    })
    return r.data.data.total_tokens
} 
 
async function select_model(input_messages, max_tokens=1024) {
    /*
    Select a model of the right size based on the input context messages and the expected max_tokens value.
 
    The select_model function calls the estimate_token_count function to calculate the number of tokens used by the input messages, adds the max_tokens value to get the total_tokens, and then selects the appropriate model based on the range of total_tokens.
    */
    prompt_tokens = await estimate_token_count(input_messages)
    total_tokens = prompt_tokens + max_tokens
    if (total_tokens <= 8 * 1024) {
        return "moonshot-v1-8k"
    } else if (total_tokens <= 32 * 1024) {
        return "moonshot-v1-32k"
    } else if (total_tokens <= 128 * 1024) {
        return "moonshot-v1-128k"
    } else {
        throw new Error("too many tokens 😢")
    }
} 
 
async function main() {
    messages = [
        {"role": "system", "content": "You are Kimi"},
        {"role": "user", "content": "Hello, please tell me a fairy tale."},
    ]
     
    max_tokens = 2048
    model = await select_model(messages, max_tokens)
     
    completion = await client.chat.completions.create({
        model: model,
        messages: messages,
        max_tokens: max_tokens,
        temperature: 0.3,
    })
     
    console.log("model:", model)
    console.log("max_tokens:", max_tokens)
    console.log("completion:", completion.choices[0].message.content)
}
 
main()

How to Handle Errors Without Using an SDK
In some cases, you might need to directly interface with the Kimi API (instead of using the OpenAI SDK). When interfacing with the Kimi API directly, you need to determine the subsequent processing logic based on the status returned by the API. Typically, we use the HTTP status code 200 to indicate a successful request, while 4xx and 5xx status codes indicate a failed request. We provide error information in JSON format. For specific handling logic based on the request status, please refer to the following code snippets:

const axios = require('axios');
 
header = {
    "Authorization": `Bearer ${process.env.MOONSHOT_API_KEY}`,
}
 
messages = [
    {"role": "system", "content": "You are Kimi"},
    {"role": "user", "content": "Hello."},
]
 
async function main() {
    r = await axios.post("https://api.moonshot.ai/v1/chat/completions",
        {
            "model": "moonshot-v1-128k",  // <-- If you use a correct model, the code will enter the if status_code==200 branch below
            //"model": "moonshot-v1-129k",  // <-- If you use an incorrect model name, the code will enter the else branch below
            "messages": messages,
            "temperature": 0.3,
        },
        {
            headers: header,
            validateStatus: function (status) {
                return status == 200; // Resolve only if the status code is less than 500
            }
        },
     ).catch(function (error) {
        console.log(`error: ${error.message}`)
     })
 
    if (r) {  // When a correct model is used for the request, this branch is entered for normal processing
        console.log(r.data.choices[0].message.content)
    }
}
 
main()

Our error messages will follow this format:

{
	"error": {
		"type": "error_type",
		"message": "error_message"
	}
}

For a detailed list of error messages, please refer to the following section:

Error Description

Why Do Some Requests Respond Quickly While Others Respond Slowly When the Prompt Is Similar?
If you find that some requests respond quickly (e.g., in just 3 seconds) while others respond slowly (e.g., taking up to 20 seconds) with similar prompts, it is usually because the Kimi large language model generates a different number of tokens. Generally, the number of tokens generated by the Kimi large language model is directly proportional to the response time of the Kimi API; the more tokens generated, the longer the complete response time.

It is important to note that the number of tokens generated by the Kimi large language model only affects the response time for the complete request (i.e., after generating the last token). You can set stream=True and observe the time to first token (TTFT) return time. Under normal circumstances, when the length of the prompt is similar, the first token response time will not vary significantly.

I Set max_tokens=2000 to Have Kimi Output 2000 Characters, but the Output Is Less Than 2000 Characters
The max_tokens parameter means: When calling /v1/chat/completions, it specifies the maximum number of tokens the model is allowed to generate. When the number of tokens already generated by the model exceeds the set max_tokens, the model will stop generating the next token.

The purpose of max_tokens is:

To help the caller determine which model to use (for example, when prompt_tokens + max_tokens ≤ 8 * 1024, you can choose the moonshot-v1-8k model);
To prevent the Kimi model from generating excessive unexpected content in certain unexpected situations, which could lead to additional cost consumption (for example, the Kimi model repeatedly outputs blank characters).
max_tokens does not indicate how many tokens the Kimi large language model will output. In other words, max_tokens will not be used as part of the prompt input to the Kimi large language model. If you want the model to output a specific number of characters, you can refer to the following general solutions:

For occasions where the output content should be within 1000 characters:
Specify the number of characters in the prompt to the Kimi large language model;
Manually or programmatically check if the output character count meets expectations. If not, in the second round of conversation, indicate to the Kimi large language model that the "character count is too high" or "character count is too low" to generate a new round of content.
For occasions where the output content should be more than 1000 characters or even more:
Try to break down the expected output content into several parts by structure or chapter and create a template, using placeholders to mark the positions where you want the Kimi large language model to output content;
Have the Kimi large language model fill in each placeholder of the template one by one, and finally assemble the complete long text.
I Made Only One Request in a Minute, but Triggered the Your account reached max request Error
Typically, the SDK provided by OpenAI includes a retry mechanism:

Certain errors are automatically retried 2 times by default, with a short exponential backoff. Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict, 429 Rate Limit, and >=500 Internal errors are all retried by default.

This retry mechanism will automatically retry 2 times (a total of 3 requests) when encountering an error. Generally speaking, in cases of unstable network conditions or other situations that may cause request errors, using the OpenAI SDK can amplify a single request into 2 to 3 requests, all of which will count towards your RPM (requests per minute) limit.

Note: For users using the OpenAI SDK with a tier0 account level, due to the default retry mechanism, a single erroneous request can exhaust the entire RPM quota.

To Facilitate Transmission, I Used base64 Encoding for My Text Content
Please do not do this. Encoding your files with base64 will result in a huge consumption of tokens. If your file type is supported by our /v1/files file interface, you can simply upload the file and extract its content using the file interface.

For binary or other encoded file formats, the Kimi large language model currently cannot parse the content, so please do not add it to the context.

Last updated on 


Terms of Service for Kimi OpenPlatform
Last Update : April 30, 2025

Thank you for using Kimi OpenPlatform!

The Terms of Service ("the terms") constitute a legal agreement between Moonshot AI PTE. LTD. ("we" or "Moonshot AI") and you ("Customer") that governs the use of our APIs and other services ("the services") by businesses and developers.

The terms also reference and incorporate the "Kimi OpePlatform Privacy Policy" and any additional guidelines or policies that we may provide in writing, and any ordering document signed by both you and us for the purchase of the services (referred to as an "Order Form"). Together, these documents form the "Agreement".

For more information on how we collect, use, and protect your personal information, you can read Kimi OpenPlatform Privacy Policy.

By using the services in any manner, especially placing an order,you agree that you have clearly read, understood the terms and agree and accept to be bound by the terms of Agreement. You further represent that you have the legal capacity to enter into contracts. If you are entering into the terms on behalf of an entity, you also represent that you have the legal authority to bind that entity.

1.Services
We provide you with a non-exclusive license to access and utilize the services for the duration of the term. This license allows you to use Moonshot AI's application programming interfaces ("APIs") to integrate the services into your own applications, products, or services (each referred to as a "Customer Application") and to offer those Customer Applications to End Users. The term "services" encompasses any services for businesses and developers that we make available for purchase or use, as well as any associated software, tools, developer services, documentation, and websites, but does not include any Third Party Offerings.We possess all rights, titles, and interests in the services. You are granted only the rights to use the services as specifically provided in this Agreement.

You must provide accurate and up-to-date account information. You are fully responsible for all activities under your account, including the activities of any End User or anyone else.You must not share your account credentials or make your account accessible to others,including do not transfer, lend, lease, or provide it to anyone for use in any form without authorization. If any loss occurs due to your failure to properly manage and safeguard the account, such as the account being stolen or used illegally, you will be held responsible for such loss. You must promptly notify us if you become aware of any unauthorized access to or use of your account or the services.

2.Who can use the services
To use the services for individual, you must be at least 18 years old or the minimum age required by your country to consent to such use. If the account is used for enterprise, you must ensure that you have the authorization from the business.In addition, you should not be the subject of any trade restrictions, sanctions, or other legal or regulatory restrictions imposed by any country, international organization, or region.

3.Usage policies
In using the services, you must comply with all applicable laws as well as our documentation, guidelines, or policies we make available to you. For example, you will not, and will not permit End Users to:

3.1 Use the services for any illegal or improper purposes or activities that violate applicable laws and regulations, harm the legitimate rights or interests of us or anyone, including:

(1) For purposes that may have a harmful impact on physical or spiritual health or that violate ethical principles.

(2) For promoting or engaging in any illegal activity, including terrorism, the exploitation or harm of children and the development or distribution of illegal substances, goods, or services.

(3) For engaging in activities that infringe upon intellectual property rights, unfair competitive practices like violations of trade secrets and business ethics.

(4) For fraudulent, deceptive, or misleading activities.

(5) To spam, bully, harass, defame, sexualize children, or promote violence, hatred or the suffering of others.

(6) For compromising the privacy of others.

(7) For any other uses prohibited or restricted by applicable laws and regulations, or that may harm legitimate interests of us or any other.

3.2 Engage in the following activities that endanger network security, operational security or create risks of the services:

(1) Engaging in activities that endanger network security, such as unauthorized access to networks, interference with normal network functions, or theft of network data.

(2) Providing programs or tools specifically designed for engaging in activities that endanger network security, such as network intrusion, interference with normal network functions and protective measures, or theft of network data.

(3) Helping endanger network security with technical support, advertising promotion, payment settlement, or other assistance.

(4) Reverse engineering, decompiling, disassembling, translating, or otherwise attempting to discover the source code, models, algorithms, or underlying components of this services' system.

(5) For developing, serving, or creating applications, products, services, or models that have potential competitive possibilities with the services without authorization.

(6) Copying, transferring, renting, lending, selling, or providing sub-licensing or re-licensing of the services in whole or in part without authorization.

(7) Other activities that endanger network security, the operational security or create risks of the services.

3.3 Maliciously harm or circumvent our safeguard for information and risk prevention of the services in the following ways:

(1) Using variants, random characters, homophones, or other means to evade safety detection and input or generate illegal statements.

(2) Launching malicious attacks, disseminating computer virus or inducing the services.

(3) Deleting, altering, or concealing the identification marks of artificially generated content that we have labeled, including both explicit and implicit.

(4) Other behaviors that maliciously harm our management for information security and risk prevention of the services.

3.4 Use the services to:

(1) Use subliminal, manipulative, or deceptive techniques that distort a person's behavior so that they are unable to make informed decisions in a way that is likely to cause harm.

(2) Exploit any vulnerabilities related to age, disability, or socio-economic circumstances to distort and harm.

(3) Evaluate or classify individuals based on their social behavior or personal traits leading to detrimental or unfavorable treatment.

(4) Assess or predict the risk of an individual committing a criminal offense based solely on their personal traits or on profiling.

(5) Infer an individual's emotions in the workplace and educational settings, except when necessary for medical or safety reasons.

(6) Conduct real-time remote biometric identification in public spaces for law enforcement purposes. (7) Create or expand facial recognition databases without consent.

(8) Send us any personal information of children under 14 or the applicable age of digital consent or allow minors to use the services without consent from their parent or guardian.

(9) Use any method to extract data from the services other than as permitted through the APIs; or buy, sell, or transfer API keys from, to or with a third party.

If you use the services to process personal data, you are required to provide legally adequate privacy notices and obtain all necessary consents for the processing of personal data by the services, and process personal data in compliance with all applicable laws.

You commit to not utilizing the services for the creation, reception, maintenance, transmission, or any other processing of information that encompasses or qualifies as “Protected Health Information” as delineated by the HIPAA Privacy Rule.

You acknowledge and agree that in the event of your violation of this agreement or applicable laws and regulations, we have the right to independently determine, including making a comprehensive judgment based on your personal information, behavioral data, and other interactive relationships. Without prior notice, we may take measures against you, including but not limited to warning, asking for rectification, restricting account functions, suspending use, freezing and confiscating the recharged amount, closing accounts, prohibiting re-registration, and deleting content. We have the right to announce the results of such actions and may decide whether to restore the use based on the actual circumstances.

4.Content
You and End Users may submit prompts, texts, audios or other content or materials ("input") to the services and the services generate corresponding content as a response ("output"). Both input and output are collectively referred to as "content".

You represent and warrant that you own or have the necessary license, authorization or clearance to submit your input to the services.You are solely responsible for content and we do not claim ownership of it. Due to technical limitations, we cannot guarantee that the content of other customers will be entirely different from yours, and it is possible that there may be similarities in the output.

We may use content to provide, maintain, develop, and improve the services, comply with applicable law, enforce our terms and policies, and keep the services safe.

Given the uncertainty and probabilistic nature of machine learning, we cannot guarantee the accuracy of output. Additionally, our output may not be able to exhaustively satisfy your desire. Therefore, please note the following when using the services:(a) Do not regard the output as the sole source of fact or absolutely factual information. You need to assess the accuracy of the content.(b) The output should not be a substitute for professional advice in fields such as medical, legal, financial, and educational. (3) You must not use any output relating to a person for any purpose that could have a legal or material impact on that person, such as making credit, educational, employment, housing, insurance, legal, medical, or other important decisions about them. (4) The output does not represent the views of Moonshot AI. If the output mentions any third-party products or services, it does not imply that the third party endorses the content or is affiliated with Moonshot AI.

While we performs regular backups of Content, it does not guarantee that there will be no loss or corruption of data. Corrupt or invalid backup points may arise due to various factors, including but not limited to content that is already corrupted before the backup process begins or that changes during the backup operation.We will provide support and endeavor to troubleshoot any known or discovered issues that may impact the backups of content. However, you acknowledge that we has no liability related to the integrity of the content or the failure to successfully restore the content to a usable state.You agree to maintain a complete and accurate copy of any content in a location that is independent of the service.

5.Trade
Price. You agree to pay all fees charged to your account based on the prices and terms listed on the pricing page, or as otherwise specified in an Order Form.We retain the right to adjust its prices at any time prior to accepting an order.Once an order has been accepted, we may still revise the quoted prices if any events beyond its control occur that affect delivery. These events include, but are not limited to, government actions, changes in customs duties, increased shipping charges, higher foreign exchange costs, or any other unforeseen circumstances.Any price changes made for legal reasons on the pricing page will take effect immediately. We reserve the right to correct any pricing errors or mistakes, even after an invoice has been issued or payment has been received.

Payment.Payments can be made using a valid card, including credit or debit cards, and are subject to validation checks and authorization by your card issuer. If we do not receive the necessary authorization from your card issuer, we will not be held liable for any delays or failures in delivering your order.Payments are nonrefundable except as provided in this Agreement.

Promotions.We may offer you promotions through means such as gifting recharge amounts, issuing vouchers, or providing trial services. We reserve the right to decide whether to continue offering or to discontinue these services. When using these services, you should be aware of this characteristic to avoid any inconvenience caused by the discontinuation of such services. The amounts associated with free services are non-withdrawable, non-transferable, and non-invoiceable.

Refund.Refunds are only supported if the service termination is due to legal requirements or caused by us.Once you submit a refund request, we will conduct a manual review of your order. Then we will send you the results of this review or request further information via the email address you provided. Be sure to check your inbox, as well as your spam folder, to ensure you do not miss any important emails. Carefully follow the instructions outlined in the email. Failure to complete the required steps within the specified timeframe will result in the inability to process your refund.

6.Intellectual Property
Except for the relevant right holders who are entitled to rights in accordance with the law, Moonshot AI owns all rights (including but not limited to copyright, trademark rights, patent rights, and other intellectual property rights and additional rights) within the scope permitted by applicable laws and regulations with respect to the services (including but not limited to software, technology, programs, code, models, user interfaces, web pages, text, charts, layout designs, trademarks, and electronic documents).

7.Warranties and Disclaimer
We warranty that, during the term of this Agreement, the services will substantially comply with the documentation we provide to you or make publicly available, when used in accordance with this Agreement.

Apart from the warranties explicitly stated above, the services are provided on an "as-is" basis. We, along with our affiliates and licensors, hereby disavow any and all other warranties, whether expressed or implied, including but not limited to implied warranties of merchantability, fitness for a particular purpose, title, non-infringement, and quiet enjoyment, as well as any warranties that may arise from the course of dealing or trade usage. Irrespective of any contrary statements, we do not make any representations or warranties regarding: (a) the uninterrupted, error-free, or secure use of the services, (b) the correction of any defects, (c) the accuracy of content.

8.Limitation of liability
Except in cases of a party’s gross negligence or willful misconduct, or your violation of usage policies,to the fullest extent permitted by law, neither party, its affiliates, nor any licensor or supplier of us shall be liable under or in connection with this agreement for: (a) consequential, indirect, special, incidental, or punitive damages; (b) loss of profits, business, revenue, anticipated savings, or wasted expenditure; (c) loss, damage, or interruption to data, networks, information systems, reputation, or goodwill; or (d) costs of procuring substitute goods or services.

The maximum aggregate liability of us and our affiliates under this agreement, the software, and the service shall not exceed the amount actually paid by you to us in the last one month preceding the date of liability. These exclusions and limitations apply to the maximum extent permitted by law, regardless of whether a party was advised of the possibility of such losses or if any remedy in this agreement fails its essential purpose.

9.Indemnity
You shall independently bear all liabilities arising out of your violation of these terms or other activities causing damage relating to your use of the services and content from any claims or demands asserted by third parties. If we suffer any losses as a result, you shall indemify and hold harmless us and our personnel from and against any costs, losses, liabilities, and expenses (including but not limited to litigation costs, arbitration fees, attorney fees, notary fees, announcement fees, appraisal fees, travel expenses, investigation and evidence collection fees, compensation payments, liquidated damages, settlement costs, fines from administrative penalties).

10.Termination or Discontinuation of the services
Cancellation.You hold the right to terminate the services at any time by deleting your account.You may apply to delete your account by contacting us via our designated email address. Before you proceed with account cancellation, please be mindful of the balance in your account. Once your account is canceled, your account information, data, APIs, and any remaining balance will be permanently deleted. Even if you register again using the same entity, these items will not be restored. Therefore, please make your decision with caution. It will take us some time to review your cancellation request. When we receive your request to cancel your account, we may suspend the use of your account. If you wish to withdraw your cancellation request during the review period, please contact us promptly.During the cancellation process, if there is still a balance in your account that has not been used, we will send you a reminder to clear the balance. If you agree to proceed with the cancellation, we will continue with the cancellation process. If you do not explicitly agree, your account will not be cancelled for the time being.

If you violate applicable laws and regulations, breaches this terms, or infringes upon the legitimate rights and interests of the public, us, or any third party, we may terminate the services depending on the circumstances.

For the needs of our operations, we reserve the right to decide on service settings and scope, and to suspend or discontinuate the services based on specific situations.

After your service is terminated, we will delete your content and data in accordance with the requirements of applicable laws and regulations.

11.Governing Law and Dispute Resolution
YOU AND US AGREE TO THE FOLLOWING PROVISIONS:

The establishment, effectiveness, interpretation, revision, supplementation, termination, enforcement, and dispute resolution of these terms shall all be governed by the laws of Singapore.

In the event of any dispute arising out of these terms, both you and us shall endeavor to resolve the dispute through amicable consultations. Engaging in this informal dispute resolution process is a requirement that must be completed before filing any legal action. If no resolution is reached through consultation in 60 days.Any dispute arising out of or in connection with these terms, including any question regarding existence, validity or termination of these terms, shall be referred to and finally resolved by arbitration administered by the Singapore International Arbitration Centre ("SIAC") in accordance with the Arbitration Rules of the Singapore International Arbitration Centre ("SIAC Rules") for the time being in force, which rules are deemed to be incorporated by reference in this clause. The seat of the arbitration shall be Singapore. The language of arbitration shall be English.

YOU ACKNOWLEDGE AND AGREE THAT ANY LEGAL PROCEEDING OR ACTION RELATED TO THESE TERMS MUST BE INITIATED WITHIN ONE YEAR FROM THE DATE OF THE EVENT OR FACTS THAT GIVE RISE TO THE DISPUTE. FAILURE TO DO SO WILL RESULT IN A PERMANENT WAIVER OF YOUR RIGHT TO PURSUE ANY CLAIM OR CAUSE OF ACTION, REGARDLESS OF ITS NATURE OR TYPE, BASED ON SUCH EVENTS OR FACTS.

12.Changes to the Agreement
We may update the Agreement from time to time as required. When we do, we will publish an updated version and effective date on the page, or by providing any other notice required by applicable law. We recommend that you review the updated agreements or terms each time you access the services.

13.Contact Us
For feedback, appeal or complaint(especially copyright complaint) ,please contact us at api-service@moonshot.ai.

Last updated on 

Kimi OpenPlatform Privacy Policy
Last Update : April 30, 2025

Welcome to Kimi OpenPlatform!

Our services are provided and controlled by MOONSHOT AI PTE. LTD. ("we"or"Moonshot AI") in Singapore through web pages.("the services") .

The Kimi OpenPlatform Privacy Policy("this policy") is to clearly explain how we collect, use, disclose, and protect your personal information, as well as the rights you have and to help you make appropriate choices. Your privacy matters to us. Please do take the time to get to know and familiarize yourself with the policy and practices.

By continuing to use the services, you agree with the policy. If you do not wish your personal information collected, used, or disclosed as described below, or if you are under the age of 18, you should stop accessing the services.

We would like to specifically remind you that when you access third-party products and services through the services, the handling of your personal information and privacy will be managed by the third party in accordance with its own policies. We cannot be responsible for the processing activities of third parties. In such cases, we recommend that you carefully read the relevant policies of the third parties to understand your rights and obligations.

1. Personal Information We Collect
Personal Information You Provide：
Account Information: The information you provide when registering for and using an account, such as username, telephone number, profile picture, email address and account credentials. This information is used to create and manage your account, ensuring that you can access and use our services smoothly.

User content: The prompts, audios, images, videos, files and other content that you input and generate while using our products and services. This information helps us optimize our models and understand your needs and preferences, so that we can provide you with more accurate services and support.

Communication Information: If you communicate with us, such as via email or feedback pages or our pages on social media sites, we may collect personal information like your name, contact information, and the contents of the messages you send.

Surveys, Research, and Promotions: We collect information you provide if you choose to participate in a survey, research, promotion, contest, marketing campaign, or event conducted or sponsored by us.

We Receive from Your Use of the Services:
We may receive the following information automatically when you visit, use or interact with our services:

Log Data: We collect information that your browser or device automatically sends when you use the services.

Device and Usage Information: We collect technical information related to your device and usage of our services. This includes device models, operating system versions, unique device identifiers, MAC addresses, user IDs, conversation IDs, IP addresses, browser types, telecommunications operators, language preferences, clipboard data, and access dates and times. The specific information collected may vary based on your device type and settings.

Cookies & Similar Technologies: We may use cookies and similar technologies on our website to understand your usage patterns and provide more personalized services. If you use the services without creating an account, we may store some of the information described in this policy with cookies. We will obtain your consent to our use of cookies where required by applicable law.

Personal Information we collect from third parties
We may receive the information described in this policy from other sources, such as:

Technical Information: If you choose to register or log in using a third-party service such as Google, we may collect information from that service, such as access tokens and public information like your profile picture and nickname, with your consent. This is for account binding with our services, enabling direct login. We may also request additional information if any required registration details are missing.

Security Information: We may receive information from our trusted partners, such as security partners, to protect against fraud, abuse, and other security threats to our services.

Public Information: We may obtain publicly available information via Internet sources in order to develop the models that power our services.

2. How we use Personal Information
We use your information to provide, maintain, improve and develop the services, including for the following purposes:

To Provide the Services: We use your information to create and manage your account, provide a seamless and convenient login experience, and enable you to interact with the services, such as engaging in conversations and accessing various features.

To Improve and Develop Our Services: We analyze how you use the services to identify areas for improvement, develop new features, and enhance the overall user experience. This includes training and refining our underlying technology, such as machine learning models and algorithms.

To Communicate with You: We may contact you to inform you of changes to the services, provide customer support, dealing with complaints or send you other service-related messages.

To Ensure the Safety and Security of Our Services: We use your information to detect and prevent fraudulent activities, abuse, and other security threats. This helps us maintain the integrity and stability of our platform.

To Comply with Legal Obligations and Rules: We use your information to comply with legal obligations, our policy and to protect the rights, privacy, safety, or property of our users, Kimi, or third parties.

To Promote Our Services: We may use your information to promote our services or third-party services through marketing communications, contests, or promotions, with your consent where required.

3. How we share Personal Information
We may share your information in the following circumstances:

Service Providers: We engage service providers that help us provide, support, and develop the services and understand how they are used. We share your information with these service providers as necessary to enable them to provide their services. These providers will access, process, or store personal information only in the course of performing their duties to us.

These providers include hosting services, customer service vendors, cloud services, content delivery services, support and safety monitoring services, email communication software, web analytics services, payment and transaction processors, and other information technology providers.

Affiliates: We may share your information with our affiliates, ensuring that they handle your information in a manner consistent with this Privacy Policy.

Corporate Transactions: In the event of a corporate transaction, such as a merger, sale of assets or shares, reorganization, financing, change of control, or acquisition of all or a portion of our business, your information may be shared with third parties. If such a transaction involves the transfer of your personal information, we will require the new holder of your personal information to continue to be bound by this policy. Otherwise, we will require the company, organization, or individual to obtain your consent again.

Legal Obligations and Rights: We may share your information with government authorities or other third parties if we have good faith belief that it is necessary to: (i) comply with applicable law, legal process or government requests, as consistent with international standards; (ii) protect and defend the rights, property, and safety of us, users and public as well as the safety, security of our products, employees, users; (iii) if we determine, in our sole discretion, that there is a violation of our terms, policies, or the law; (iv) detect or prevent fraud or other illegal activity; (v) protect against legal liability.

4. Your Rights and Choices
You have the rights to access, rectify or update, transfer, delete your personal information as well as restrict how we process, withdraw your consent, lodge complaints before the competent authorities and potentially others.

You can exercise some of these rights directly through settings or through your account if you have registered. Additionally, your device may offer settings that allow you to manage the information we collect. For instance, you can decide whether to permit us to access your mobile advertising identifier through the settings on your Apple or Android device. If you prefer not to receive marketing or advertising emails, you can simply use the "unsubscribe" link or mechanism provided in those emails.If you are unable to exercise your rights through the methods mentioned above, please submit your request through api-service@moonshot.ai.

If you choose to delete your account, you will not be able to reactivate your account or retrieve any of the content or information in connection with your account.

A note about accuracy: The services generate responses by analyzing a user's request and predicting the words that are most likely to follow. However, the most probable words may not always be factually accurate. As a result, you should not assume that the output from our models is factually correct. If you find that our output contains inaccurate information about you and you wish to request a correction or removal of that information, please contact us. We will review your request in accordance with applicable laws and the technical capabilities of our models.

5. Information Security
We are fully aware that the security and confidentiality of your personal information are of utmost importance to you. We will endeavor to avoid collecting irrelevant user information and will take reasonable technical and organizational measures to protect your personal information from unauthorized access, public disclosure, use, modification, damage, or loss, including but not limited to:

Data Encryption: We will use industry-leading encryption algorithms to encrypt users' personal information, ensuring that even if the data is obtained by unauthorized third parties, they will not be able to decipher the actual information of the users.

System Security Protection: We regularly conduct security checks and vulnerability patches on servers and systems to prevent hacker attacks and virus intrusions.

Institutional Safeguards: We have established a dedicated data protection department and appointed a person in charge to be responsible for the protection of users' personal information. We regularly provide training and education on personal information protection to our employees to ensure that all staff understand and value the protection of users' personal information. We strictly limit employees' access to user data, allowing only specific employees to access relevant data when necessary for business purposes. We also monitor and assess employees who access users' personal information, and take prompt action if any improper behavior is detected.

Data Backup: We regularly back up users' personal information data and store the backup data in different physical locations to reduce the risk of data loss due to accidents or disasters.

Data Breach Alert: We have set up a real-time monitoring system to monitor abnormal data access and leakage situations. Once signs of data leakage are detected, we will immediately take measures to stop the leakage, promptly identify the cause, and develop corresponding improvement measures.

Please note that due to the limitations of technical and management means, although we have taken the above measures and made every effort to improve the security level, we cannot guarantee absolute security. Also, we cannot guarantee the effectiveness of privacy settings or security measures on third parties related to the services. Therefore, you should take special care in deciding what information you send to us. We strongly recommend that you take more proactive security measures together with us, such as refusing to lend accounts, disclose verification codes, or upload sensitive information, which are high-risk operations.

We have developed a cybersecurity incident emergency response plan. In the unfortunate event of a personal information leak or other security incidents, we will immediately activate the emergency response plan to take measures to prevent the expansion of harm. We will promptly inform you of the basic situation of the security incident, the potential impact, and the remedial measures we have taken through means such as telephone or push notifications. When it is difficult to notify each individual whose personal information is affected, we will issue a public announcement in a reasonable and effective manner. At the same time, we will also report the relevant situation to the regulatory authorities, cooperate with the investigation, and hold the responsible parties accountable for their legal responsibilities.

6. Retention
We store your information as long as necessary to provide the services, fulfill the purposes outlined in this policy and other legitimate business purposes (such as service improvement, resolving disputes, safety or security), comply with legal obligations.

Retention periods vary based on factors such as information type, sensitivity, and legal requirements. For example, account, input, and payment information are retained while your account is active. Violation-related information is retained until the violation is resolved. Also, in some cases, the length of time we retain data depends on your settings.

Your personal information may be transferred to and stored on servers located outside your country of residence. We store the information we collect in secure servers located in Singapore.

When cross-border transfers are necessary, we will implement appropriate safeguards, consistent with applicable data protection laws, to ensure your information is protected for the purposes outlined in this policy.

7. Children
Our Services are not directed to, or intended for, children under 18. If you have reason to believe that a child under 14 has provided information to us through the services, please contact api-service@moonshot.ai. We will investigate any notification and, if appropriate, delete the information in time.

8. Privacy Policy Updates
We may update this policy from time to time as required. When we do, we will publish an updated version and effective date on this page, or by providing any other notice required by applicable law. We recommend that you review the updated policy each time you access the services to stay informed of our privacy practices.

9. Contact us
Please send detailed comments, complaints, or reports concerning this policy or our personal information management practices to api-service@moonshot.ai.

10. Supplemental Terms - Jurisdiction-Specific
European Economic Area ("EEA"), Switzerland, and UK If you are using the services in the EEA, Switzerland or the UK (the "European Region"), the following additional terms apply:

Legal bases for processing We use your personal data only as permitted by law. Our legal bases for processing your personal data described in this policy are described in the table below.

Purpose of processing	Personal information categories	Legal bases
To create and manage your account, provide a seamless and convenient login experience, and enable you to interact with our services, such as engaging in conversations and accessing various features.	- Account Information
- User Content
- Communication Information
- Device and Usage Information
- Log Data
- Cookies & Similar Technologies	- Where necessary to perform a contract with you when we provide and maintain our services.
- Your consent when we ask for it to process your personal data for a specific purpose to help you create accounts.
- Where necessary for our legitimate interests: If you're under 18, your ability to enter into a binding contract is restricted. In such cases, where we may not be able to process your information based on contractual necessity, we rely on legitimate interests. We use the information we collect to enable you to access and use the platform.
To identify areas for improvement, develop new features, and enhance the overall user experience. This includes training and refining our underlying technology, such as machine learning models and algorithms.	- User Content
- Communication Information
- Device and Usage Information
- Log Data	- Where necessary to pursue our legitimate interests in identifying and resolving issues with the platform and enhancing its functionality; and to conduct research and safeguard personal data through aggregation or anonymization, in line with the principles of data minimization and privacy by design.
- Your consent when we ask for it to process your personal data for a specific purpose to provide services.
To inform you of changes to our services, provide customer support, or send you other service-related messages.	- Account Information
- Communication Information
- Device and Usage Information	- Where necessary to perform a contract with you when we provide and maintain our services.
- Your consent when we ask for it to process your personal data for a specific purpose to communicate with you.
To comply with our legal obligations, or as necessary to perform tasks in the public interest, or to protect the vital interests of our users and other people. This could include providing law enforcement agencies or emergency services with information in urgent situations to protect health or life.	- Account Information
- User Content
- Communication Information
- Device and Usage Information
- Log Data
- Cookies & Similar Technologies	- Where necessary to comply with a legal obligation: This applies in situations where we are required to take steps to ensure the safety of our users, or to comply with a valid legal request, such as an order from law enforcement agencies or courts. It also applies when we are fulfilling our obligations under applicable laws, or when we are protecting the rights, safety, or property of ourselves, our affiliates, our users, or third parties.
- Where necessary for our legitimate interests to protect our business, employees, and users from illegal activities, inappropriate conduct, or breaches of terms that could cause harm, and to disclose and share information with regulators or other government authorities.
To detect and prevent fraudulent activities, abuse, and other security threats. This helps us maintain the integrity and stability of our platform.	- Account Information
- User Content
- Communication Information
- Device and Usage Information
- Log Data
- Cookies & Similar Technologies	- Where necessary to comply with a legal obligation when we use your personal data to comply with applicable law or when we protect our or our affiliates', users', or third parties' rights, safety, and property.
- Where necessary for our legitimate interests to ensure that the Platform is safe and secure.
Data storage It is important to note that our servers are situated in Singapore. Consequently, when you utilize our services, your personal data may be processed and stored on our servers located in Singapore. This could involve either a direct submission of your personal data to us or a transfer of your data conducted by us or a third-party.

Your rights You have the following rights:

The right to request free of charge (i) confirmation of whether we process your personal data and (ii) access to a copy of the personal data retained;
The right to request proper rectification or erasure of your personal data or restriction of the processing of your personal data;
Where processing of your personal data is either based on your consent or necessary for the performance of a contract with you and processing is carried out by automated means, the right to receive the personal data concerning you in a structured, commonly used and machine-readable format or to have your personal data transmitted directly to another company, where technically feasible (data portability);
Where the processing of your personal data is based on your consent, the right to withdraw your consent at any time (withdrawal will not impact the lawfulness of data processing activities that have taken place before such withdrawal);
The right not to be subject to any automatic individual decisions, including profiling, which produces legal effects on you or similarly significantly affects you unless we have your consent, this is authorised by European Union or Member State law or this is necessary for the performance of a contract;
The right to object to processing if we are processing your personal data on the basis of our legitimate interest unless we can demonstrate compelling legitimate grounds which may override your right. If you object to such processing, we ask you to state the grounds of your objection in order for us to examine the processing of your personal data and to balance our legitimate interest in processing and your objection to this processing;
The right to request the restriction of the processing of your information where (i) you are challenging the accuracy of the information, (ii) the information has been unlawfully processed, but you are opposing the deletion of that information, (iii) you need the information to be retained for the pursuit or defense of a legal claim, or (iv) you have objected to the processing and you are awaiting the outcome of that objection request;
The right to object to processing your personal data for direct marketing purposes; and
The right to lodge complaints before your local data protection authority.
Before we can respond to a request to exercise one or more of the rights listed above, you may be required to verify your identity or your account details.

Please contact us if you would like to exercise any of your rights.

Last updated on 











