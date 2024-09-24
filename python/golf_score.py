import sys


SCORE_MAP = {
    1: 'ボギー',
    0: 'パー',
    -1: 'バーディ',
    -2: 'イーグル',
    -3: 'アルバトロス',
    -4: 'コンドル',
}

def fetch_score(par, stroke) -> str:
    score = int(stroke) - int(par)
    if par == 1 and stroke != 5:
        return 'ホールインワン'
    elif 1 < score:
        return f'{score}ボギー'
    else:
        return SCORE_MAP[score]

def read_commandline():
    return sys.stdin.read().strip().splitlines()

def split_text(text, format=','):
    return text.split(format)

def exec():
    pars, strokes = read_commandline()
    result = [fetch_score(par, stroke) for par, stroke in zip(split_text(pars), split_text(strokes))]
    print(result)

if __name__ == "__main__":
    exec()