# imports

def main():
    with open("input.txt", "r") as f:
        inputs = f.readlines()
        inputs = [int(i.strip()) for i in inputs]

    n_increased = 0

    for i in range(3, len(inputs)):
        current_sum = inputs[i] + inputs[i-1] + inputs[i-2]
        prev_sum = inputs[i-1] + inputs[i-2] + inputs[i-3]

        if current_sum > prev_sum:
            n_increased += 1

    print(n_increased)
    
if __name__ == "__main__":
    main()