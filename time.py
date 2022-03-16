import re
time_reg = re.compile(r'^([0-9]|1[012]):(0?[0-9]|[1-5][0-9])$')

num_digits = range(0,13)
num_words = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
digit_and_word = list(zip(num_digits,num_words)) #[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), etc ]

def hr_to_str(num):
    for item in digit_and_word:
        if num == item[0]:
            return item[1]
        

def wordy_time(time):

    confirm_time = time_reg.search(time)

    if not confirm_time:
        return 'The time input format is not correct'

    else:
        time_list = time.split(':')

        hr = int(time_list[0])
        minutes = int(time_list[1])

        hr_str = hr_to_str(hr)

        if minutes == 0:
            return f"{hr_str} O'clock'"

        elif minutes/60 == 0.25:
            return f'Quater past {hr_str}'

        elif minutes/60 == 0.25:
            return f'Quater past {hr_str}'

        elif minutes/60 == 0.5:
            return f'Half past {hr_str}'

        elif minutes/60 == 0.75:
            return f'Quater to {hr_to_str(hr+1)}'

        if minutes <= 30:
            return f'{minutes} minutes past {hr_str}'
        else:
            return f'{60 - minutes} minutes to {hr_to_str(hr+1)}'

print(wordy_time('5:30'))
print(wordy_time('5:00'))
print(wordy_time('5:15'))
print(wordy_time('5:45'))
print(wordy_time('5:20'))
print(wordy_time('5:50'))
print(wordy_time('5:80'))
