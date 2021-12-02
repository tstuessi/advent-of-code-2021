# imports

def main():
    with open("input.txt", "r") as f:
        inputs = f.readlines()
        inputs = [i.strip() for i in inputs]

    n_increased = 0
    for i in range(1, len(inputs)):
        if int(inputs[i]) > int(inputs[i-1]):
            n_increased += 1
    print(n_increased)
    
if __name__ == "__main__":
    main()