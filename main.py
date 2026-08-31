from pyscript import document

name= "Sio Zia"
age= 15
height= 160.2
countries_visit= ["Malaysia", "Singapore", "China"]
student_type= False
student_info= {'color': "White", 'car_brand': "Honda", 'shoe_size': 7, 'best_friend': "Mio"}
fruits= ["Strawberry", "Blueberry", "Melon", "Watermelon", "Grape"]
week= ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


output= f"""
<p> name= {name} {type(name).__name__}</p>
<p> age= {age} {type(age).__name__}</p>
<p> height= {height} {type(height).__name__}</p>
<p> countries= {countries_visit} {type(countries_visit).__name__}</p>
<p> student_type= {student_type} {type(student_type).__name__}</p>
<p> student_info= {student_info} {type(student_info).__name__}</p>
<p> fruits= {fruits} {type(fruits).__name__}</p>
<p> days= {week} {type(week).__name__}</p>

"""

document.querySelector("#output").innerHTML = output