
def read_file(any_file):
    # use strip to strip out spaces and trim the line.
    return [line.strip() for line in open(any_file, 'r')]

def get_commits(data):
    sep = 72*'-'
    commits = []
    index = 0
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            # the author with spaces at end removed.
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip().split(' ')[0],
                'time': details[2].strip().split(' ')[1],
                'number_of_lines': int(details[3].strip().split(' ')[0])
            }
            change_file_end_index = data.index('', index + 1)
            commit['changed_path'] = data[index + 3 : change_file_end_index]
            commit['comment'] = data[change_file_end_index + 1 : 
                    change_file_end_index + 1 + commit['number_of_lines']]
            # add details to the list of commits.
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            index = len(data)
    return commits

def save_commits(commits, any_file):
    my_file = open(any_file, 'w')
    my_file.write("revision,author,date,time,number_of_lines,comment\n")
    for commit in commits:
        my_file.write(commit['revision'] + ',' + commit['author'] +
                ',' + commit['date'] + ',' + commit['time'] + ',' +
				str(commit['number_of_lines']) + ',' + ' '.join(commit['comment']) + '\n')
    my_file.close()

def get_authors(data):   
    authors = {}
    x = 0    
    while x < len(commits):
        if authors.has_key(commits[x]['author']):
            authors[commits[x]['author']]+=1
        else: 
            authors[commits[x]['author']]=1
        x += 1
    return authors  
    
    
def get_lines(data): 
    lines = {}
    x = 0    
    while x < len(commits):
        if lines.has_key(commits[x]['number_of_lines']):
            lines[commits[x]['number_of_lines']]+=1
        else: 
            lines[commits[x]['number_of_lines']]=1
        x += 1
    return lines  
    
def get_dates(data): 
    dates = {}
    x = 0    
    while x < len(commits):
        if dates.has_key(commits[x]['date']):
            dates[commits[x]['date']]+=1
        else: 
            dates[commits[x]['date']]=1
        x += 1
    return dates
    
#if __name__ == '__main__':
    # open the file - and read all of the lines.
changes_file = 'changes_python.log'
data = read_file(changes_file)
print len(data)
commits = get_commits(data)
print len(commits)
#print commits[1]['author']
save_commits(commits, 'changes.csv')

  
authors = get_authors(get_commits(data))  
print authors

lines = get_lines(commits)
print lines   
  
dates = get_dates(commits) 
print dates
