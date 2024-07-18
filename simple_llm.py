# Import necessary packages
from ibm_watson_machine_learning.foundation_models import Model
import gradio as gr

# Model and project settings
model_id = "meta-llama/llama-2-70b-chat"  # Directly specifying the LLAMA2 model

# Set credentials to use the model
my_credentials = {
    "url": "https://us-south.ml.cloud.ibm.com"
}

# Set necessary parameters
gen_parms = {
    #"max_new_tokens": 256,  # Specifying the max tokens you want to generate
    "max_new_tokens": 512,  # adjust the parameter `max_new_token` to a bigger value
    "temperature": 0.1    # Specifying the temperature which controls the randomness of the token generated
}
project_id = "skills-network"  # Specifying project_id as provided
space_id = None
verify = False
    
# Initialize the model
model = Model(model_id, my_credentials, gen_parms, project_id, space_id, verify)


def get_answer(prompt_txt):
    # Attempt to generate a response using the model with overridden parameters
    generated_response = model.generate(prompt_txt)
    generated_text = generated_response["results"][0]["generated_text"]
    return generated_text


# Define the interface
demo = gr.Interface(
    fn=get_answer, 
    inputs=[gr.Textbox(label="enter your prompt")], 
    outputs=gr.Textbox(value="", label="Answer")
)
# Launch the interface
demo.launch(server_name="0.0.0.0", server_port= 7860)
