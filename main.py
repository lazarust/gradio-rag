import gradio as gr


def greet(name):
    return "Hello " + name + "!"


def main():
    demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    demo.launch()


if __name__ == "__main__":
    main()
