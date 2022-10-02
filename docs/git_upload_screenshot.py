# defaults write com.apple.screencapture "include-date" 0

date = '10-02'
time = '17.30.05'
symbols = ['!', '[', ']', ':', '/', ' ', '"', '-', '%', '(', ')']

def mov():
    print('mv ~/Desktop/Screen\ Shot\ 2022-10-02\ at\ 17.30.05.png ./screenshots/\n')

def readme():
    link = '![2nd-edition-2](https://github.com/stella-vir/vehicleAutomation/blob/main/screenshots/Screen%20Shot%202022-10-02%20at%2017.30.05.png)'
    # escape '\' the escape sign: double '\\'
    esc = '\\'
    res = []

    for s in link:
        if s in symbols:
            print('Before ', s)
            res.append(esc)
        res.append(s)
    res = 'echo ' + ''.join(res) + ' >> README.md'
    print(res)
    return res
mov()
readme()
