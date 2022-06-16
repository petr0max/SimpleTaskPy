def fibonacciGenerate():
    message = "yuk coba generate disini: "
    inputGenerate = int(input(message))
    
    fiboNumbs = []
    if (inputGenerate == 1):
        fiboNumbs = [0]
    elif (inputGenerate == 2):
        fiboNumbs = [0, 1]
    else:
        fiboNumbs = [0, 1]
        for i in range(2, inputGenerate):
            fiboNumbs.append(fiboNumbs[i - 2] + fiboNumbs[i - 1])
    
    soutfibo = [str(item) for item in fiboNumbs]
    print(" " . join(soutfibo))


print("Hai selamat datang di program fibonacci")
fibonacciGenerate()