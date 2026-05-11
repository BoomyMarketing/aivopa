with open('industries/hair-salon.html', 'rb') as f:
    data = f.read()
idx = data.find(b'<title>')
print('hex:', data[idx:idx+80].hex())
print('repr:', repr(data[idx:idx+80]))
