import sys
import os


def validate_command():
    valid_commands = ["reverse", "copy",
                      "duplicate-contents", "replace-string"]
    if sys.argv[1] not in valid_commands:
        print(f"Error: Invalid command '{sys.argv[1]}'.")
        sys.exit(1)


def validate_arguments_for_command():
    if sys.argv[1] in ["reverse", "copy"] and len(sys.argv) != 4:
        print(f"Error: Command '{sys.argv[1]}' requires 2 arguments.")
        sys.exit(1)
    if sys.argv[1] in ["duplicate-contents", "replace-string"] and len(sys.argv) != 5:
        print(f"Error: Command '{sys.argv[1]}' requires 3 arguments.")
        sys.exit(1)


def validate_file():
    if not os.path.isfile(sys.argv[2]) or not os.access(sys.argv[2], os.R_OK):
        print(f"Error: File '{sys.argv[2]
                              }' does not exist or is not readable.")
        sys.exit(1)


def validate_replace_string():
    if sys.argv[1] == "replace-string":
        with open(sys.argv[2], 'r') as file:
            contents = file.read()
            if sys.argv[3] not in contents:
                print(f"Error: The string to be replaced '{
                      sys.argv[3]}' is not found in the file.")
                sys.exit(1)


def validate_args():
    validate_command()
    validate_arguments_for_command()
    validate_file()
    validate_replace_string()


def file_manipulator(command):
    validate_args()
    if command == "reverse":
        with open(sys.argv[2], 'r') as f:
            content = f.read()[::-1]
        with open(sys.argv[3], 'w') as f:
            f.write(content)
    elif command == "copy":
        with open(sys.argv[2], 'r') as f:
            content = f.read()
        with open(sys.argv[3], 'w') as f:
            f.write(content)
    elif command == "duplicate-contents":
        with open(sys.argv[2], 'r') as f:
            content = f.read()
        for _ in range(int(sys.argv[3])):
            with open(sys.argv[2], 'a') as f:
                f.write(content)
    elif command == "replace-string":
        with open(sys.argv[2], 'r') as f:
            content = f.read()
            original_string = sys.argv[3]
            new_string = sys.argv[4]
            modified_content = content.replace(original_string, new_string)
        with open(sys.argv[2], 'w') as f:
            f.write(modified_content)


file_manipulator(sys.argv[1])
