from dotenv import load_dotenv 
from openai import OpenAI

load_dotenv()

client = OpenAI()

text = "Eiffel tower  is in paris and is a famous landmark, it is 324 meter tall"

response = client.embeddings.create(
    input= text,
    model = "text-embedding-3-small"    #3d space  model  size 3 small
) 
print ("Vector Embeddings" , response.data[0].embedding )