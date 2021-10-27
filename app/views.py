from django.shortcuts import render
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

# Create your views here.

from django.shortcuts import redirect

def github(request):
    return redirect("https://github.com/ellongley/duckie/")

def rowestats(request):

    #Graph X & Y coordinates
    #x = [ 1,2,3,4,5 ]
    #y = [ 1,2,3,4,5 ]

    #Setup graph plot for displaying line Graph
    #plot = figure(title = 'Line Graph', x_axis_label= 'X-Axis', y_axis_label='Y-Axis',plot_width=400,plot_height=400)

    #plot line
    #plot.line(x,y,line_width=2)

    #Store components
    #script,div = components(plot)

    import pandas as pd
    import h5py as h
    from bokeh.palettes import Bokeh5
    from bokeh.plotting import figure, output_file, show
    from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT

    rowe_stats = h.File('/Users/Emily/Desktop/TXPipe/data/example/outputs/rowe_stats.hdf5', 'r+')['rowe_statistics']
    import matplotlib.transforms as mtrans
    from bokeh.layouts import column

    STAR_TYPES = ['PSF-reserved','PSF-used']

    # plot the points
    STAR_TYPE = STAR_TYPES[0]
    p1 = figure(title='rowe stats '+STAR_TYPE, width=800, height=400,y_axis_type="log",x_axis_type="log")
    for j,i in enumerate([2,5]):
        df = {}
        theta =  rowe_stats['rowe_'+str(i)+'_'+STAR_TYPE]['theta'][()]
        xi = rowe_stats['rowe_'+str(i)+'_'+STAR_TYPE]['xi_plus'][()]
        err = rowe_stats['rowe_'+str(i)+'_'+STAR_TYPE]['xi_err'][()]
        df['theta'] = theta
        df['xi'] = xi
        df['err'] = err

        p1.xaxis.axis_label = "theta (arcmin)"
        p1.yaxis.axis_label = STAR_TYPE


        p1.circle(theta, xi, color=Bokeh5[i-1], size=5, line_alpha=0, alpha=0.8, legend_label='rowe_'+str(i)+'_'+STAR_TYPE)


        # create the coordinates for the errorbars
        err_xs = []
        err_ys = []

        for x, y, yerr in zip(theta, xi, err):
            err_xs.append((x, x))
            if y>0:
                err_ys.append((y - yerr, y + yerr))
            elif y<=0 and y-yerr>0:
                y = abs(y)
                yerr = abs(yerr)
                err_ys.append((y - yerr, y + yerr))
            elif y<=0 and y-yerr<=0:
                y = abs(y)
                yerr = abs(yerr)
                err_ys.append((min(abs(xi)), y + yerr))

        # plot them
        p1.multi_line(err_xs, err_ys, color=Bokeh5[i-1], legend_label='rowe_'+str(i)+'_'+STAR_TYPE)

    p1.legend.location = "top_left"
    p1.legend.click_policy="hide"


    STAR_TYPE = STAR_TYPES[1]
    p2 = figure(title='rowe stats '+STAR_TYPE, width=800, height=400,y_axis_type="log",x_axis_type="log")
    for j,i in enumerate([2,5]):
        df = {}
        theta =  rowe_stats['rowe_'+str(i)+'_'+STAR_TYPE]['theta'][()]
        xi = rowe_stats['rowe_'+str(i)+'_'+STAR_TYPE]['xi_plus'][()]
        err = rowe_stats['rowe_'+str(i)+'_'+STAR_TYPE]['xi_err'][()]
        df['theta'] = theta
        df['xi'] = xi
        df['err'] = err

        p2.xaxis.axis_label = "theta (arcmin)"
        p2.yaxis.axis_label = STAR_TYPE


        p2.circle(theta, xi, color=Bokeh5[i-1], size=5, line_alpha=0, alpha=0.8, legend_label='rowe_'+str(i)+'_'+STAR_TYPE)


        # create the coordinates for the errorbars
        err_xs = []
        err_ys = []

        for x, y, yerr in zip(theta, xi, err):
            err_xs.append((x, x))
            if y>0:
                err_ys.append((y - yerr, y + yerr))
            elif y<=0 and y-yerr>0:
                y = abs(y)
                yerr = abs(yerr)
                err_ys.append((y - yerr, y + yerr))
            elif y<=0 and y-yerr<=0:
                y = abs(y)
                yerr = abs(yerr)
                err_ys.append((min(abs(xi)), y + yerr))

        # plot them
        p2.multi_line(err_xs, err_ys, color=Bokeh5[i-1], legend_label='rowe_'+str(i)+'_'+STAR_TYPE)


    p2.legend.location = "top_left"
    p2.legend.click_policy="hide"

    ##################################
    STAR_TYPE = STAR_TYPES[1]
    p3 = figure(title='rowe stats '+STAR_TYPE, width=800, height=400,y_axis_type="log",x_axis_type="log")
    for j,i in enumerate([1,3,4]):
        df = {}
        theta =  rowe_stats['rowe_'+str(i)+'_'+STAR_TYPE]['theta'][()]
        xi = rowe_stats['rowe_'+str(i)+'_'+STAR_TYPE]['xi_plus'][()]
        err = rowe_stats['rowe_'+str(i)+'_'+STAR_TYPE]['xi_err'][()]
        df['theta'] = theta
        df['xi'] = xi
        df['err'] = err

        p3.xaxis.axis_label = "theta (arcmin)"
        p3.yaxis.axis_label = STAR_TYPE


        p3.circle(theta, xi, color=Bokeh5[i-1], size=5, line_alpha=0, alpha=0.8, legend_label='rowe_'+str(i)+'_'+STAR_TYPE)


        # create the coordinates for the errorbars
        err_xs = []
        err_ys = []

        for x, y, yerr in zip(theta, xi, err):
            err_xs.append((x, x))
            if y>0:
                err_ys.append((y - yerr, y + yerr))
            elif y<=0 and y-yerr>0:
                y = abs(y)
                yerr = abs(yerr)
                err_ys.append((y - yerr, y + yerr))
            elif y<=0 and y-yerr<=0:
                y = abs(y)
                yerr = abs(yerr)
                err_ys.append((min(abs(xi)), y + yerr))


        # plot them
        p3.multi_line(err_xs, err_ys, color=Bokeh5[i-1], legend_label='rowe_'+str(i)+'_'+STAR_TYPE)


    p3.legend.location = "top_left"
    p3.legend.click_policy="hide"

    #############################

    STAR_TYPE = STAR_TYPES[1]
    p4 = figure(title='rowe stats '+STAR_TYPE, width=800, height=400,y_axis_type="log",x_axis_type="log")
    for j,i in enumerate([1,3,4]):
        df = {}
        theta =  rowe_stats['rowe_'+str(i)+'_'+STAR_TYPE]['theta'][()]
        xi = rowe_stats['rowe_'+str(i)+'_'+STAR_TYPE]['xi_plus'][()]
        err = rowe_stats['rowe_'+str(i)+'_'+STAR_TYPE]['xi_err'][()]
        df['theta'] = theta
        df['xi'] = xi
        df['err'] = err

        p4.xaxis.axis_label = "theta (arcmin)"
        p4.yaxis.axis_label = STAR_TYPE


        p4.circle(theta, xi, color=Bokeh5[i-1], size=5, line_alpha=0, alpha=0.8, legend_label='rowe_'+str(i)+'_'+STAR_TYPE)


        # create the coordinates for the errorbars
        err_xs = []
        err_ys = []

        for x, y, yerr in zip(theta, xi, err):
            err_xs.append((x, x))
            if y>0:
                err_ys.append((y - yerr, y + yerr))
            elif y<=0 and y-yerr>0:
                y = abs(y)
                yerr = abs(yerr)
                err_ys.append((y - yerr, y + yerr))
            elif y<=0 and y-yerr<=0:
                y = abs(y)
                yerr = abs(yerr)
                err_ys.append((min(abs(xi)), y + yerr))

        # plot them
        p4.multi_line(err_xs, err_ys, color=Bokeh5[i-1], legend_label='rowe_'+str(i)+'_'+STAR_TYPE)


    p4.legend.location = "top_left"
    p4.legend.click_policy="hide"


    # put all the plots in a VBox
    p = column(p1,p2,p3,p4)

    script,div = components(p)

    #TODO: reference the database


    #Return to django homepage with components sent as arguments which will then be displayed
    return render(request,'pages/base.html',{'script' : script, 'div': div})
