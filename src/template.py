import os
import sys

filenames = range(1,11)
extension = '.rst'


def write(page_number, messages):
    filename = str(page_number) + extension
    filename = os.path.join('event', filename)

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
    'The dropping of the atomic bomb',
    r'The attacks on 9\11',
    'The Wright Brothers take to the skies',
    'Apollo 11',
    'The New Deal',
    'Pearl Harbor',
    'The C Programming Language',
    'Cuban Missile Crisis',
    '\"I have a dream\"',
    'Arpanet',
]

total_titles = len(titles)

if total_titles != 10:
    missing = 10 - total_titles
    print("You need %d more title/s!" % missing)
    print total_titles
    sys.exit(1)

titles.reverse()
filenames.reverse()

if not os.path.isdir('event'):
    os.mkdir('event')

for title, page_number in zip(titles, filenames):

    write(page_number, [
        #'Event %d' % page_number,
        '{number}: {title}'.format(number=page_number, title=title),
        'Synopsis',
        'What effects did it have?',
        'Media'
        ])

txt = open(os.path.join('event','cite.rst'), 'a')
title = "Works Cited\n"
buff = '*' * len(title)
txt.write(title)
txt.write(buff + '\n')
for title in titles:
    txt.write('\n')
    txt.write(title + '\n')
    buff = '=' * len(title)
    txt.write(buff + '\n')

txt.close()

