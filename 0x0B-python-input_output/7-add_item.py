#!/usr/bin/python3

""" function that load_from_json_file """
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

""" function that save_to_json_file """
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

if not exists("add_item.json") or os.stat("add_item.json").st_size == 0:
    save_to_json_file([], "add_item.json")

argv_cpy = load_from_json_file("add_item.json")

for i in range(1, len(sys.argv)):
    argv_cpy.append(sys.argv[i])

save_to_json_file(argv_cpy, "add_item.json")
