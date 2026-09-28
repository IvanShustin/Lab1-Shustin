def draw_function():
    width = 60
    height = 9
    max_x = 5

    def F(x):
        return x ** 0.5

    ys = [F(max_x * c / (width - 1)) for c in range(width)]
    max_y = max(ys)
    grid = [[False] * width for _ in range(height)]
    prev_h = 0
    for c in range(width):
        h = round(ys[c] / max_y * (height - 1))
        for hh in range(min(prev_h, h), max(prev_h, h) + 1):
            grid[(height - 1) - hh][c] = True
        prev_h = h
    for row in grid:
        line = ""
        for cell in row:
            if cell:
                line += "\033[48;2;30;144;255m \033[0m"
            else:
                line += " "
        print(line)
