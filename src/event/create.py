from os import popen

filenames = range(1,11)
extension = '.rst'

for name in filenames:
    filename = str(name)+extension
    popen('touch {filename}'.format(filename=filename))
    txt = open(filename,'r+')
    statement = '%d: Title' % name
    txt.write(statement)
    txt.write('\n')
    txt.write('*'*len(statement))


