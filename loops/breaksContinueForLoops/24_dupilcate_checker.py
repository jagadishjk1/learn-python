files = ['report.csv',
         'dblogs.csv',
         'duplicate.pdf',
         'data.csv',
         'duplicate.pdf'
]

for file in files:
    if files.count(file) > 1:
        print(f'{file}: Duplicate found.')
else:
    print("All files are unique.")