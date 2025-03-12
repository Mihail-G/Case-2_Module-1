# Part of case-study #2
# Case has been done by Mihail Gordeev and Sergey Chirkov
# Collatz conjecture
# Idea was taking from this video: https://www.youtube.com/watch?v=QgzBDZwanWA&ab_channel=VertDider


#main module for graphical display of calculations
import matplotlib.pyplot as plt


#module localization for Russian language
import ru_local as ru


def graf(y_ax):
    '''def for graphical display
       y_ax - list of coordinates of the sequence (3n+1)'''

    #setting up the display field
    plt.figure(figsize=(8, 5), dpi=100)

    #setting up the graph line
    plt.plot(range(1, len(y_ax)+1), y_ax, color='red')

    #setting the labels of the abscissa and ordinate axes
    plt.xlabel(ru.Q_NUMBERS)
    plt.ylabel(ru.V_NUMBERS)

    #setting the title of the function graph
    plt.title(ru.GRAPH_INTER, fontdict={'fontname': 'Arial', 'fontsize': 20})

    #function graph display
    plt.show()



def main():
    '''def for calculation and graphical display of the sequence (3n+1) or the Collatz hypothesis'''

    print(ru.COLLATZ_GREETINGS, ru.INTRODUCTION_COLLATZ, sep='\n')
    number = int(input(ru.ENTER_NUMBER))
    inter_res = [number]
    i = 0

    while inter_res[i] != 1:
        if inter_res[i]%2 == 0:
            inter_res.append(inter_res[i]//2)
            i+=1

        else:
            inter_res.append((inter_res[i]*3)+1)
            i+=1

    print(inter_res)
    graf(inter_res)


if __name__ == '__main__':
    main()
