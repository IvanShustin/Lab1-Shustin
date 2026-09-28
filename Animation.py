import os
import time


def draw_animation():
    width = 20
    delay = 0.4
    loops = 10
    main_color = (225, 154, 53)
    bg_color = (20, 20, 20)

    positions = [0, width // 4, width // 2, width * 3 // 4, width - 1]

    for _ in range(loops):
        for pos in positions:
            frame = ""
            for col in range(width):
                if col == pos:
                    r, g, b = main_color
                else:
                    r, g, b = bg_color
                frame += f"\033[48;2;{r};{g};{b}m \033[0m"

            os.system("cls" if os.name == "nt" else "clear")
            print(frame)
            time.sleep(delay)



draw_animation()