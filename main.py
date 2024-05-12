from reactpy import *
from reactpy.backend.fastapi import configure
from fastapi import  FastAPI


@component
def Tailwind():
    return html.script({"src": "https://cdn.tailwindcss.com"})

@component
def App():
    return html.div({"class_name": "bg-black h-screen mt-0"},
        Tailwind(), 

        html.h1({"class_name": "text-white font-bold ml-5"}, "Hello World!")
        )

app = FastAPI()

configure(app, App)
