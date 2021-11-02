END = '\033[0m'

class TextColorUnix:
    END = END
    BLACK  = '\033[30m'
    RED    = '\033[31m'
    GREEN  = '\033[32m'
    YELLOW = '\033[33m'
    BLUE   = '\033[34m'
    PURPLE = '\033[35m'
    CYAN   = '\033[36m'
    WHITE  = '\033[37m'
    BLACK_LIGHT  = '\033[90m'
    RED_LIGHT    = '\033[91m'
    GREEN_LIGHT  = '\033[92m'
    YELLOW_LIGHT = '\033[93m'
    BLUE_LIGHT   = '\033[94m'
    PURPLE_LIGHT = '\033[95m'
    CYAN_LIGHT   = '\033[96m'
    WHITE_LIGHT  = '\033[97m'

class BackgroundColorUnix:
    END = END
    BLACK  = '\033[40m'
    RED    = '\033[41m'
    GREEN  = '\033[42m'
    YELLOW = '\033[43m'
    BLUE   = '\033[44m'
    PURPLE = '\033[45m'
    CYAN   = '\033[46m'
    WHITE  = '\033[47m'
    BLACK_LIGHT  = '\033[100m'
    RED_LIGHT    = '\033[101m'
    GREEN_LIGHT  = '\033[102m'
    YELLOW_LIGHT = '\033[103m'
    BLUE_LIGHT   = '\033[104m'
    PURPLE_LIGHT = '\033[105m'
    CYAN_LIGHT   = '\033[106m'
    WHITE_LIGHT  = '\033[107m'

class StyleUnix:
    END = END
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'


def _format(cls: object, param_name: str, text: str) -> str:
    """
    Helper function for color(), bg_color() and style()

    Args:
        cls (object): from which enum take values
        param_name (str): what value to take
        text (str): to what text should this be applied

    Returns:
        str: formatted text
    """
    param = getattr(cls, param_name.upper(), '')
    end = '' if len(param) == 0 else getattr(cls, 'END', END)
    return param + text + end


def color(color: str, text: str) -> str:
    """ Set text color """
    return _format(TextColorUnix, color, text)


def bg_color(color: str, text: str) -> str:
    """ Set background color """
    return _format(BackgroundColorUnix, color, text)


def style(style: str, text: str) -> str:
    """ Set text style """
    return _format(StyleUnix, style, text)


def _show_color_grid():
    """ Show grid with each combination of text and background color """
    colors = [i for i in TextColorUnix.__dict__ if i != 'END' and not i.startswith('_')]
    backgrounds = [i for i in BackgroundColorUnix.__dict__ if i != 'END' and not i.startswith('_')]
    max_b = max(len(b) for b in backgrounds)
    max_c = max(len(c) for c in colors)
    colors_label = []
    for i in range(max_c):
        letters = ''
        for j in range(len(colors)):
            l = colors[j][-(i+1)] if i < len(colors[j]) else ' '
            letters += f' {l} '
        colors_label.append(letters)
    for line in colors_label[::-1]:
        print(' ' * (max_b + 1) + line)
    
    for b in backgrounds:
        line = f'{b:{max_b}} '
        for c in colors:
            line += bg_color(b, color(c, ' 1 '))
        print(line)
    
if __name__ == '__main__':
    print(style('bold', 'This is a module for creating nice cmd output'))
    print()
    print('Possible styles:')
    print(' * ' + style('bold', 'bold'))
    print(' * ' + style('underline', 'underline'))
    print()
    print('Color grid: (background x text color)')
    _show_color_grid()
    print()
    print(style('underline', 'Usage example'))
    print('You can use auto-defined functions:')
    print()
    print('\t' + '>>> print(color("yellow", "some text"))')
    print('\t' + color("yellow", "some text"))
    print()
    print('or define helper functions for most frequently used params:')
    print()
    print('\t' + '>>> yellow = lambda text: color("yellow", text)')
    print('\t' + '>>> print(yellow("some text"))')
    yellow = lambda text: color("yellow", text)
    print('\t' + yellow("some text"))
    print()
