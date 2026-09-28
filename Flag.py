def draw_flag():
    width = 30
    height = 3

    for i in range (height):
        print(f'\033[48;2;255;255;255m{" " * width}\033[0m')
    for i in range(height):
        print(f'\033[48;2;220;20;60m{" " * width}\033[0m')
    ##print(f'\033[48;2;R;G;Bm{" " * width}\033[0m')






