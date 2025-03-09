# Part of case-study #2
# Collatz conjecture
import ru_local as ru
import matplotlib.pyplot as plt


def main():
    print(ru.COLLATZ_GREETINGS, ru.INTRODUCTION_COLLATZ, sep='\n')
    number = int(input(ru.ENTER_NUMBER))
    inter_res = [number]
    i = 0
    while inter_res[i] != 1:
        if inter_res[i]%2 == 0:
            inter_res.append(inter_res[i]/2)
            i+=1
        else:
            inter_res.append((inter_res[i]*3)+1)
            i+=1
    print(inter_res)
    graf(inter_res)


def graf(y_ax):
    plt.figure(figsize=(8, 5), dpi=100)
    plt.plot(range(1, 1+len(y_ax)), y_ax, 'r', label='numbers')
    plt.xlabel(ru.Q_NUMBERS)
    plt.ylabel(ru.V_NUMBERS)
    plt.title(ru.GRAPH_INTER, fontdict={'fontname': 'Arial', 'fontsize': 20})
    plt.show()


if __name__ == '__main__':
    main()
