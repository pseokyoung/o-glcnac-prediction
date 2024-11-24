import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def lineplot(data, x, y, color='k', label=None,
             linewidth = 1.5, linestyle = '-', linemarker = 'o', markersize = 3, linealpha = 1):
        plt.plot(data[x].values, data[y].values, label=label,
             color = color, linewidth=linewidth, linestyle=linestyle, alpha=linealpha, 
             marker=linemarker, markersize=markersize)

def linerrbarplot(data, x, y, color='k', label=None,
                linewidth = 1.5, linestyle = '-', linemarker = 'o', markersize = 3, linealpha = 1,
                errwidth = 1, errstyle = '-', errmarker = 's', errsize = 1, erralpha = 0.5):
    data = data.copy()
    mean = data.groupby(by=x).mean()[y]
    std  = data.groupby(by=x).std()[y]
    assert all(mean.index == std.index), 'index inconsistency'
    
    xticks = mean.index
    mean_values = mean.values
    std_values = std.values
    
    plt.plot(xticks, mean_values, label=label,
             color = color, linewidth=linewidth, linestyle=linestyle, alpha=linealpha, 
             marker=linemarker, markersize=markersize)
    for i in range(len(mean_values)):
        plt.plot([xticks[i], xticks[i]], [mean_values[i]-std_values[i], mean_values[i]+std_values[i]],
                color = color, linewidth = errwidth, linestyle=errstyle, alpha=erralpha, 
                marker=errmarker, markersize=errsize)
        
def linerrfillplot(data, x, y, color='k', label=None,
                linewidth = 1.5, linestyle = '-', linemarker = 'o', markersize = 3, linealpha = 1,
                errwidth = 0.2, errstyle = '-', erralpha = 0.1):
    data = data.copy()
    mean = data.filter(items=[x,y]).groupby(by=x).mean()[y]
    std  = data.filter(items=[x,y]).groupby(by=x).std()[y]
    assert all(mean.index == std.index), 'index inconsistency'
    
    xticks = mean.index
    mean_values = mean.values
    std_values = std.values
    
    plt.plot(xticks, mean_values, label=label,
             color = color, linewidth=linewidth, linestyle=linestyle, alpha=linealpha, 
             marker=linemarker, markersize=markersize)
    plt.fill_between(xticks, y1=mean_values - std_values, y2=mean_values + std_values, where=None,
            color = color, edgecolor='k', linewidth = errwidth, linestyle=errstyle, alpha=erralpha)

def scatergoryplot(data, xticks, xkey, xitems, y, label=None,
                   color='k', s=20, alpha=1, marker='o'):
    data = data.copy()
    data = pd.concat([data[data[xkey] == x] for x in xitems])
    plt.scatter(xticks, data[y].values, label=label,
                color=color, s=s, alpha=alpha, marker=marker)
        
def setaxis(xlabel=None, ylabel=None, 
            labelsize = 12, labelpad=5, title=None, titlesize = 12,
            xticks = None, yticks = None, ticksize=8,
            xtickslabels = None, ytickslabels = None,
            xlim = (), ylim = ()):
    plt.title(title, fontsize=titlesize)    
    
    plt.xlabel(xlabel, fontsize=labelsize, labelpad=labelpad)
    plt.ylabel(ylabel, fontsize=labelsize, labelpad=labelpad)
    
    plt.xticks(xticks, labels=xtickslabels, fontsize=ticksize)
    plt.yticks(yticks, labels=ytickslabels, fontsize=ticksize)
    
    plt.xlim(*xlim)
    plt.ylim(*ylim)
    
def setlegend(loc=None, fontsize=8, title=None, titlesize='small',
              borderpad=0.4, labelspacing=0.2, markersacle=1,
              edgecolor='0', facecolor='1'):
    plt.legend(loc = loc, fontsize=fontsize, title=title, title_fontsize=titlesize,
               borderpad=borderpad, labelspacing=labelspacing, edgecolor=edgecolor, facecolor=facecolor, 
               markerscale=markersacle)
    
def setgrid(grid=True, which='major', axis='both', 
            color='gray', linestyle = '--', linewidth = 0.2, zorder = 0):
    plt.grid(grid, which=which, axis=axis, 
             color=color, linestyle=linestyle, linewidth=linewidth, zorder=zorder)
    