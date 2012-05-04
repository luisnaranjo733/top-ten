from os import popen

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

for page_number in filenames:
    write(page_number, [
        'Event %d' % page_number,
        'Synopsis',
        'What effects did it have?',
       'Why I chose this event'
        ])
