def sort_colors(colors):
    color_list = colors.split("-")
    color_list.sort()
    return "-".join(color_list)

colors = input("\nEnter colors separated by - : ")
print(sort_colors(colors), "\n")