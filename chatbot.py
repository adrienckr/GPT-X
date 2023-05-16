import openai 
openai.api_key='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'


#Throughout this tuto, we will use OpenAI's gpt-3.5-turbo model
#and the chat completions endpoint.

#Helper function
#Makes it easier to user prompts and look at the generated outputs

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{'role':'user', 'content':prompt}]
    response= openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, #this is the degree of randomness
    )
    return response.choices[0].message["content"]


text = f"""
You should express what you want a model to do by \ 
providing instructions that are as clear and \ 
specific as you can possibly make them. \ 
This will guide the model towards the desired output, \ 
and reduce the chances of receiving irrelevant \ 
or incorrect responses. Don't confuse writing a \ 
clear prompt with writing a short prompt. \ 
In many cases, longer prompts provide more clarity \ 
and context for the model, which can lead to \ 
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \ 
into a single sentence.
```{text}```
"""
response = get_completion(prompt)
print(response)