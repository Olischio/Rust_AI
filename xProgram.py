import xFunctions as x

x.screenshot(3,2)


x_list = []
y_list = []

x_list, y_list = x.modelOG()

print(f"Dette er x_list {x_list} ----- Dette er y_list {y_list}")

# x.movemouse2(x_list, y_list)

x.movemousespray(x_list, y_list)