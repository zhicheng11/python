def convert_ms(n):
     hours = n // 3600000
     minutes = (n % 3600000 // 60000)
     seconds = ((n % 3600000) % 60000) // 1000
     print("{0}:{1}:{2}".format(hours,minutes,seconds))

convert_ms(5000)
convert_ms(100000)
convert_ms(555550000)

n = int(input("Please Enter time in milliseconds: "))
convert_ms(n)
