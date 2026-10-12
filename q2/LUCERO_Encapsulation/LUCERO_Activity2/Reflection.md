How does using @property make your code easier to read compared to using 
traditional get_ and set_ methods?

    *Using @property makes Python code much easier to read because it lets you work with private attributes using clean dot notation (like rectangle.width = 10 or print(rectangle.width)).   
    Without @property, you'd have to use method calls with parentheses everywhere, like rectangle.set_width(10) or rectangle.get_width().   
    The main advantage is that it gives your code the clean syntax of regular variables while still doing all the heavy lifting behind the scenes—such as validating data and enforcing encapsulation to protect your variables.