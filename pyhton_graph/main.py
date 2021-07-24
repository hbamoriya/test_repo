import histogram
import pie_chart
import scatter_plot
def main():
    #pie = pie_chart.piee()
    #his = histogram.hiss()
    c = input("enter your graph choice : \n 1-Pie Chart \n 2- Histogram \n 3-Scatter Plot: ")
    if c=='1':
        return pie_chart.piee()
    elif c=='2':
        return histogram.hiss()
    elif c=='3':
        return scatter_plot.sca()
    pass
if __name__ == '__main__':
    main()

