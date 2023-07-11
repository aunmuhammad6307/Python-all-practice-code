def function_name_print(a, b, c, d, e):
    print(a, b, c, d, e)

function_name_print("Arslan", "Umar", "Safeer", "Aun", "Sohail")

def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")



person = ["Arslan", "Umar", "Safeer", "Awais", "Aun", "Sohail"]
normal = "I am a normal Argument and the students are:"
kw = {"Arslan":"Monitor", "Umar":"Fitness Instructor",
      "Aun": "Coordinator", "Sohail Nawaz":"Cook"}
funargs(normal, *person, **kw)
  
