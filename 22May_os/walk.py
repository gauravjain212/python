import os
import time

parent_path = input("Enter parent path to recursively search: ")

def walk_path(parent_path):
    print(f"Checking: {parent_path}")
    children = os.listdir(parent_path)
    for child in children:
        child_path = os.path.join(parent_path,child)
        if os.path.isfile(child_path):
            print(f"File: {child_path}")
            last_access = os.path.getatime(child_path)
            print(f"\tLast Access: {time.ctime(last_access)}")
            size = os.path.getsize(child_path)
            print(f"\tSize: {size} B")
        elif os.path.isdir(child_path):
            walk_path(child_path)

walk_path(parent_path)