from pyscript import document

def checkNum(e):
    num_bers = ["1", "67", "69", "3.1415", "6.022"]
    num1 = document.getElementById("num1").value
    name = "germ"
    message = (f'Sorry {name}, your number is not found.', f'Yey! {name}, your number is found.')
    confirm_num = num1 in num_bers

    document.getElementById("output1").innerHTML = message[confirm_num]