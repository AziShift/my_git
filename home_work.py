def build_profile(name, **kwargs):
    print(f"Имя: {name}")
    
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

build_profile("Азирет", возраст=16, город="Бишкек")