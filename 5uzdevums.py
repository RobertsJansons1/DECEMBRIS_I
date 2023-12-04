laiks=int(input("Ievadi laiku!(raksti tikai stundas):"))

if 5 <= int(laiks) < 12:
    teiciens = "Labrīt!"
elif 13 <= int(laiks) <19:
    teiciens = "Labdien!"
else:
    teiciens = "Labvakar!"

print(teiciens)