def draw_pattern():
    repeats = 5
    width = 40
    thickness = 2
    gap1 = (width//2) - (thickness//2) ## Расстояние до центральной верт. полосы
    gap2 = (width//4) - (thickness//2) ## Расстояние до нижних верт. полос
    gap3 = width - ((gap2 * 2) + (thickness*2)) ## Расстояние между нижними верт. полосами
    segment1 = f"\033[48;2;255;255;255m{' ' * width}\033[0m" ## Горизонтальная полоса
    segment2 = f"{' ' * gap1}\033[48;2;255;255;255m{' ' * thickness}\033[0m{' ' * gap1}\033[0m" ## Верт. полосы в центре
    segment4 = f"{' ' * gap2}\033[48;2;255;255;255m{' ' * thickness}\033[0m{' ' * gap3}\033[48;2;255;255;255m{' ' * thickness}\033[0m{' ' * gap2}\033[0m" ## Нижние верт. полосы
    print(segment1 * repeats) ## Горизонтальная полоса
    print(segment2 * repeats) ## Верт. полоса
    print(segment1 * repeats) ## Горизонтальная полоса
    print(segment4 * repeats) ## Верт. полосы
    print(segment1 * repeats) ## Горизонтальная полоса


draw_pattern()
