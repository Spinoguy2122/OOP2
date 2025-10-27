class employee:
    def __init__(self):
        print("emplyee created. ")
        
    def __del__(self):
        print("employee removed. ")
obj = employee()
del obj