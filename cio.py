import time
import random
import os

def generate_binary_screen(rows, columns):
    screen = []
    for _ in range(rows):
        row = [random.choice("01") for _ in range(columns)]
        screen.append(" ".join(row))
    return "\n".join(screen)

def main():
    try:
        os.system("clear")
        os.system("stty cbreak -echo")

        while True:
            rows, columns = os.popen('stty size', 'r').read().split()
            rows, columns = int(rows), int(columns)
            
            binary_screen = generate_binary_screen(rows, columns)
            print(binary_screen)
            time.sleep(0.1)
    except KeyboardInterrupt as e:
        pass
    finally:
        os.system("stty cooked echo")
        os.system("clear")

if __name__ == "__main__":
    main()
