import time
class Tool:
    def get_time(self):
        
        return time.time()
    def get_time_str(self):
        import time
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def calculate(self, a, b, operator):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b    
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                return "除数不能为0"
            return a / b
    

    def hello(self, name):
        def get_name(name):
            return f"Hello, {name}!"
        
