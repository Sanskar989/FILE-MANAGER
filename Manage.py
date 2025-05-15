import os
import sys

def ls(path: str = ".") -> None:
    """List names in *path* (defaults to current directory)."""
    try:
        for name in sorted(os.listdir(path)):
            print(name)
    except Exception as e:
        print("⚠️", e)


def cd(path: str) -> None:
    """Change current working directory."""
    try:
        os.chdir(path)
    except Exception as e:
        print("⚠️", e)


def touch(fname: str) -> None:
    """Create or truncate a file."""
    try:
        with open(fname, "w", encoding="utf-8"):
            pass
        print("✔️ created", fname)
    except Exception as e:
        print("⚠️", e)


def cat(fname: str) -> None:
    """Print file contents."""
    try:
        with open(fname, encoding="utf-8") as f:
            print(f.read())
    except Exception as e:
        print("⚠️", e)


def rm(fname: str) -> None:
    """Delete a file."""
    try:
        os.remove(fname)
        print("🗑️ deleted", fname)
    except Exception as e:
        print("⚠️", e)

# ── interactive loop ────────────────────────────────────────────────

def main() -> None:
    print("Mini File‑Manager. Type 'help' for commands.")
    while True:
        try:
            cmd = input(f"{os.getcwd()}$ ").strip().split()
        except EOFError:
            print()  # neat newline on Ctrl‑D
            break
        if not cmd:
            continue

        action, *args = cmd

        if action == "exit":
            break
        elif action == "help":
            print("Commands: ls [dir], cd <dir>, touch <file>, cat <file>, rm <file>, exit")
        elif action == "ls":
            ls(args[0] if args else ".")
        elif action == "cd":
            cd(args[0]) if args else print("usage: cd <dir>")
        elif action == "touch":
            touch(args[0]) if args else print("usage: touch <file>")
        elif action == "cat":
            cat(args[0]) if args else print("usage: cat <file>")
        elif action == "rm":
            rm(args[0]) if args else print("usage: rm <file>")
        else:
            print("❓ unknown command – type 'help'")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
