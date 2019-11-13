# Keep track of todos using a list.
todo_list = []

# I need a way to add todos.
def add_todo(todo):
    # We receive a todo, which is a string
    todo_list.append(todo)

# print the empty todo list
print(todo_list)
# add a todo by calling our function
add_todo("feed the cat")
# print the todo list again, making sure our todo got added
print(todo_list)

# I need to be able to delete todos.
def delete_todo(index):
    # del todo_list[index]
    try:
        todo_list.pop(index)
    except IndexError:
        print("💩Sorry, we couldn't find that one.💩")

delete_todo(0)
print(todo_list)
delete_todo(0)
print(todo_list)


# I need to print my todos.

# Show user the main menu.

