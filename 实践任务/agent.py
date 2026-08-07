from ast import Try

from Tool import Tool



class Agent:
    """
    A simple agent class that can execute tasks.
    """
    # Initialize the agent with a tool instance
    def __init__(self):
        # Here you can initialize any necessary attributes or tools for the agent
        self.tool = Tool()
    # Execute the given task.
    def execute(self, task):
        try:
            if "时间" in task:
                return self.tool.get_time_str()
            elif "+" in task or "-" in task or "*" in task or "/" in task:
                # Extract the calculation expression from the task string
                import re
                match = re.search(r"(\d+)\s*([\+\-\*/])\s*(\d+)", task)
                if match:
                    a, operator, b = match.groups()
                    a, b = int(a), int(b)
                    return self.tool.calculate(a, b, operator)
            elif "hello" in task:# Handle the hello task
                name = task.split(" ")[-1]  # Assume the name is the last word in the task
                return self.tool.hello(name)        
            # Here you can implement the logic to handle different tasks
            # For demonstration purposes, we will just return a message
            result = f"Task '{task}' has been executed."
        except Exception as e:
            def catch_warnings():
                import warnings
                with warnings.catch_warnings():
                warnings.simplefilter("ignore")
            return str(e)