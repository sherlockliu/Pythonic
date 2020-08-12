# ！/usr/bin/python


def psychologist():
    print('Please tell me your problems')
    while True:
        answer = (yield)
        if answer:
            if answer.endswith('?'):
                print('Donnot ask this question.')
            elif 'good' in answer:
                print('Good')
            elif 'bad' in answer:
                print('bad')


