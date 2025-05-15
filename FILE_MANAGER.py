import os

def list_dir():
    try:
        files = os.listdir(os.getcwd())
        for f in files:
            print(f)
    except Exception as e:
        print("Error listing directory:", e)

def change_dir(folder):
    try:
        os.chdir(folder)
        print("Moved to:", os.getcwd())
    except Exception as e:
        print("Error:", e)

def touch_file(filename, content):
    try:
        with open(filename, "w") as f:
            f.write(content)
        print(f"File '{filename}' created with your text.")
    except Exception as e:
        print("Error creating file:", e)

def main():
    print("Simple Python File Manager")
    print("Commands: touch <filename> \"<text>\", ls, cd <folder>, exit")
    while True:
        cmd = input("\n>>> ").strip()
        if cmd == "ls":
            list_dir()
        elif cmd.startswith("cd "):
            folder = cmd[3:].strip()
            change_dir(folder)
        elif cmd.startswith("touch "):
            try:
                # Find first quote (")
                first_quote = cmd.find("\"")
                if first_quote == -1:
                    print("Usage: touch <filename> \"<text>\"")
                    continue
                filename = cmd[6:first_quote].strip()
                content = cmd[first_quote+1:-1] if cmd.endswith("\"") else cmd[first_quote+1:]
                touch_file(filename, content)
            except Exception as e:
                print("Usage: touch <filename> \"<text>\"")
        elif cmd == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Try: touch, ls, cd, exit.")

if __name__ == "__main__":
    main()
