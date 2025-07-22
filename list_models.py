import google.generativeai as genai

genai.configure(api_key="AIzaSyCGNOYgo8FK0NdNpSIg4tEbJtFCISF7rd8")

models = genai.list_models()

for model in models:
    print(model.name, model.supported_generation_methods)
