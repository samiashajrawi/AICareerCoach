import gradio as gr

def combine(str1, str2):
    return str1 + " " + str2

# Define the interface
demo = gr.Interface(
    fn=combine, 
    inputs=[gr.Textbox(label="Input 1"),gr.Textbox(label="Input 2")], 
    outputs=gr.Textbox(value="", label="Output")
)
# Launch the interface
demo.launch(server_name="0.0.0.0", server_port= 7860)