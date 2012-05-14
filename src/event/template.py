from os import popen
import sys

filenames = range(1,11)
extension = '.rst'


def write(page_number, messages):
    filename = str(page_number) + extension

    if type(messages) == str:
        messages = [messages]

    for content in messages:
        if content == messages[0]:
            buffer_char = '*'

        if content != messages[0]:
            buffer_char = '='

        txt = open(filename,'a')
        txt.write(content)
        txt.write('\n')
        txt.write(buffer_char*len(content))
        txt.write('\n\n')
        txt.close()
        del txt

titles = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eigth',
    'nine',
    'ten'
]

assert len(titles) == 10
titles.reverse()
filenames.reverse()


for title, page_number in zip(titles, filenames):

    write(page_number, [
        #'Event %d' % page_number,
        '{number}: {title}'.format(number=page_number, title=title),
        'Synopsis',
        'What effects did it have?',
        'Media'
        ])
