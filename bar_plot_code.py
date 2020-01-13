def bar_plot(column_name):
    grouped = column_name.groupby(column_name).count()
    bar_df = grouped.to_frame()
    fig = plt.figure(figsize=(5,4))
    plt.title("Title",loc='center')
    plt.bar(bar_df.index, bar_df.iloc[:,0], color = ['#ff5500','#ff5500','#ff5500','#ff5500',
                                                     '#bfbfbf','#bfbfbf','#1a53ff','#1a53ff'],
           edgecolor = "none")
    
    for x,y in zip(bar_df.index, bar_df.iloc[:,0]):

        label = y

        plt.annotate(label, # this is the text
                     (x,y), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,1), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center

    #plt.annotate('v', bar_df.iloc[:,0])
    
    fig.savefig("/Users/kiruthika.sankaran/Desktop/Q4_bar.png")
    
