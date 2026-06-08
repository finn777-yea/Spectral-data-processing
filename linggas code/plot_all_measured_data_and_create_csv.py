# -*- coding: utf-8 -*-
"""
Project:        FlexBioNeuro

@University     Technical University of Munich
@Professorship  Regenerative Energy Systems
@Institute      Biotechnology and Sustainability

@Supervisor     Prof. Dr.-Ing. Matthias Gaderer
                Bernhard Huber, M.Sc.

@Author         Lingga Aksara Putra

@Date           02.08.2022

@Description    First measurement for classification
                Class: 0 = <2g/l
                       1 = >2g/l


Index       Name         acetic-acid concentration     class
I,0     I_0_sample_1           0.375 g/l                 0
I,0     I_0_sample_2           0.510 g/l                 0
I,0     I_0_sample_3           0.650 g/l                 0
I,0     I_0_sample_5           1.020 g/l                 0
I,0     I_0_sample_6           1.421 g/l                 0
I,0     I_0_sample_7           1.451 g/l                 0
I,0     I_0_sample_8           1.270 g/l                 0

I,1     I_0_sample_a0          0.149 g/l                 0
I,1     I_0_sample_a1          2.202 g/l                 1
I,1     I_0_sample_a2          2.124 g/l                 1
I,1     I_0_sample_a3          2.467 g/l                 1
I,1     I_0_sample_b0          0.460 g/l                 0
I,1     I_0_sample_b1          3.350 g/l                 1
I,1     I_0_sample_b2          2.699 g/l                 1
I,1     I_0_sample_b3          2.768 g/l                 1

I       I_sample_01          ? + 0.000 g/l               0
I       I_sample_02          ? + 0.549 g/l               0
I       I_sample_03          ? + 1.027 g/l               0
I       I_sample_04          ? + 1.266 g/l               0
I       I_sample_05          ? + 2.342 g/l               1
I       I_sample_06          ? + 2.402 g/l               1
I       I_sample_07          ? + 2.462 g/l               1
I       I_sample_08          ? + 2.522 g/l               1
I       I_sample_09          ? + 2.582 g/l               1
I       I_sample_10          ? + 2.641 g/l               1
I       I_sample_11          ? + 2.701 g/l               1
I       I_sample_12          ? + 2.761 g/l               1
I       I_sample_13          ? + 2.821 g/l               1
I       I_sample_14          ? + 2.880 g/l               1
I       I_sample_15          ? + 2.940 g/l               1
I       I_sample_16          ? + 3.000 g/l               1

J       J_sample_01          ? + 0.000 g/l               0
J       J_sample_02          ? + 0.250 g/l               0
J       J_sample_03          ? + 0.310 g/l               0
J       J_sample_04          ? + 0.370 g/l               0
J       J_sample_05          ? + 0.429 g/l               0
J       J_sample_06          ? + 0.489 g/l               0
J       J_sample_07          ? + 0.549 g/l               0
J       J_sample_08          ? + 0.609 g/l               0
J       J_sample_09          ? + 0.668 g/l               0
J       J_sample_10          ? + 0.728 g/l               0
J       J_sample_11          ? + 0.788 g/l               0
J       J_sample_12          ? + 0.848 g/l               0
J       J_sample_13          ? + 0.908 g/l               0
J       J_sample_14          ? + 0.967 g/l               0
J       J_sample_15          ? + 1.027 g/l               0
J       J_sample_16          ? + 1.087 g/l               0
J       J_sample_17          ? + 1.147 g/l               0
J       J_sample_18          ? + 1.207 g/l               0
J       J_sample_19          ? + 2.342 g/l               1
J       J_sample_20          ? + 2.402 g/l               1
J       J_sample_21          ? + 2.462 g/l               1
J       J_sample_22          ? + 2.522 g/l               1
J       J_sample_23          ? + 2.582 g/l               1
J       J_sample_24          ? + 2.641 g/l               1
J       J_sample_25          ? + 2.701 g/l               1
J       J_sample_26          ? + 2.761 g/l               1
J       J_sample_27          ? + 2.821 g/l               1
J       J_sample_28          ? + 2.880 g/l               1
J       J_sample_29          ? + 2.940 g/l               1
J       J_sample_30          ? + 3.000 g/l               1

K       K_sample_01          ? + 0.000 g/l               0
K       K_sample_02          ? + 1.266 g/l               0
K       K_sample_03          ? + 1.326 g/l               0
K       K_sample_04          ? + 1.386 g/l               0
K       K_sample_05          ? + 1.446 g/l               0
K       K_sample_06          ? + 1.505 g/l               0
K       K_sample_07          ? + 1.565 g/l               0
K       K_sample_08          ? + 1.625 g/l               0
K       K_sample_09          ? + 1.685 g/l               0
K       K_sample_10          ? + 1.745 g/l               0
K       K_sample_11          ? + 1.804 g/l               1
K       K_sample_12          ? + 1.864 g/l               1
K       K_sample_13          ? + 1.924 g/l               1
K       K_sample_14          ? + 1.984 g/l               1
K       K_sample_15          ? + 2.043 g/l               1
K       K_sample_16          ? + 2.103 g/l               1
K       K_sample_17          ? + 2.163 g/l               1
K       K_sample_18          ? + 2.223 g/l               1
K       K_sample_19          ? + 2.283 g/l               1
K       K_sample_20          ? + 1.266 g/l               0
K       K_sample_21          ? + 1.326 g/l               0
K       K_sample_22          ? + 1.386 g/l               0
K       K_sample_23          ? + 1.446 g/l               0
K       K_sample_24          ? + 1.505 g/l               0
K       K_sample_25          ? + 1.984 g/l               1
K       K_sample_26          ? + 2.043 g/l               1
K       K_sample_27          ? + 2.103 g/l               1
K       K_sample_28          ? + 2.163 g/l               1
K       K_sample_29          ? + 2.223 g/l               1
K       K_sample_30          ? + 2.283 g/l               1

A       A_sample_01          ? + 0.000 g/l               0
A       A_sample_02          ? + 0.250 g/l               0
A       A_sample_03          ? + 0.310 g/l               0
A       A_sample_04          ? + 0.370 g/l               0
A       A_sample_05          ? + 0.429 g/l               0
A       A_sample_06          ? + 0.489 g/l               0
A       A_sample_07          ? + 0.549 g/l               0
A       A_sample_08          ? + 0.609 g/l               0
A       A_sample_09          ? + 0.668 g/l               0
A       A_sample_10          ? + 0.728 g/l               0
A       A_sample_11          ? + 0.788 g/l               0
A       A_sample_12          ? + 0.848 g/l               0
A       A_sample_13          ? + 0.908 g/l               0
A       A_sample_14          ? + 0.967 g/l               0
A       A_sample_15          ? + 1.027 g/l               0
A       A_sample_16          ? + 1.087 g/l               0
A       A_sample_17          ? + 1.147 g/l               0
A       A_sample_18          ? + 1.207 g/l               0
A       A_sample_19          ? + 1.266 g/l               0
A       A_sample_20          ? + 1.326 g/l               0
A       A_sample_21          ? + 1.386 g/l               0
A       A_sample_22          ? + 1.446 g/l               0
A       A_sample_23          ? + 1.505 g/l               0
A       A_sample_24          ? + 1.565 g/l               0
A       A_sample_25          ? + 1.625 g/l               1
A       A_sample_26          ? + 1.685 g/l               1
A       A_sample_27          ? + 1.745 g/l               1
A       A_sample_28          ? + 1.804 g/l               1
A       A_sample_29          ? + 1.864 g/l               1
A       A_sample_30          ? + 1.924 g/l               1
A       A_sample_31          ? + 1.984 g/l               1
A       A_sample_32          ? + 2.043 g/l               1
A       A_sample_33          ? + 2.103 g/l               1
A       A_sample_34          ? + 2.163 g/l               1
A       A_sample_35          ? + 2.223 g/l               1
A       A_sample_36          ? + 2.283 g/l               1
A       A_sample_37          ? + 2.342 g/l               1
A       A_sample_38          ? + 2.402 g/l               1
A       A_sample_39          ? + 2.462 g/l               1
A       A_sample_40          ? + 2.522 g/l               1
A       A_sample_41          ? + 2.582 g/l               1
A       A_sample_42          ? + 2.641 g/l               1
A       A_sample_43          ? + 2.701 g/l               1
A       A_sample_44          ? + 2.761 g/l               1
A       A_sample_45          ? + 2.821 g/l               1
A       A_sample_46          ? + 2.880 g/l               1
A       A_sample_47          ? + 2.940 g/l               1
A       A_sample_48          ? + 3.000 g/l               1
A       A_sample_49          ? + 1.147 g/l               0
A       A_sample_50          ? + 1.745 g/l               1

B       B_sample_01          ? + 0.000 g/l               0
B       B_sample_02          ? + 0.250 g/l               0
B       B_sample_03          ? + 0.310 g/l               0
B       B_sample_04          ? + 0.370 g/l               0
B       B_sample_05          ? + 0.429 g/l               0
B       B_sample_06          ? + 0.489 g/l               0
B       B_sample_07          ? + 0.549 g/l               0
B       B_sample_08          ? + 0.609 g/l               0
B       B_sample_09          ? + 0.668 g/l               0
B       B_sample_10          ? + 0.728 g/l               0
B       B_sample_11          ? + 0.788 g/l               0
B       B_sample_12          ? + 0.848 g/l               0
B       B_sample_13          ? + 0.908 g/l               0
B       B_sample_14          ? + 0.967 g/l               0
B       B_sample_15          ? + 1.027 g/l               0
B       B_sample_16          ? + 1.087 g/l               0
B       B_sample_17          ? + 1.147 g/l               0
B       B_sample_18          ? + 1.207 g/l               0
B       B_sample_19          ? + 1.266 g/l               0
B       B_sample_20          ? + 1.326 g/l               0
B       B_sample_21          ? + 1.386 g/l               0
B       B_sample_22          ? + 1.446 g/l               0
B       B_sample_23          ? + 1.505 g/l               0
B       B_sample_24          ? + 1.565 g/l               0
B       B_sample_25          ? + 1.625 g/l               1
B       B_sample_26          ? + 1.685 g/l               1
B       B_sample_27          ? + 1.745 g/l               1
B       B_sample_28          ? + 1.804 g/l               1
B       B_sample_29          ? + 1.864 g/l               1
B       B_sample_30          ? + 1.924 g/l               1
B       B_sample_31          ? + 1.984 g/l               1
B       B_sample_32          ? + 2.043 g/l               1
B       B_sample_33          ? + 2.103 g/l               1
B       B_sample_34          ? + 2.163 g/l               1
B       B_sample_35          ? + 2.223 g/l               1
B       B_sample_36          ? + 2.283 g/l               1
B       B_sample_37          ? + 2.342 g/l               1
B       B_sample_38          ? + 2.402 g/l               1
B       B_sample_39          ? + 2.462 g/l               1
B       B_sample_40          ? + 2.522 g/l               1
B       B_sample_41          ? + 2.582 g/l               1
B       B_sample_42          ? + 2.641 g/l               1
B       B_sample_43          ? + 2.701 g/l               1
B       B_sample_44          ? + 2.761 g/l               1
B       B_sample_45          ? + 2.821 g/l               1

C       C_sample_03          ? + 0.310 g/l               0
C       C_sample_04          ? + 0.370 g/l               0
C       C_sample_05          ? + 0.429 g/l               0
C       C_sample_06          ? + 0.489 g/l               0
C       C_sample_07          ? + 0.549 g/l               0
C       C_sample_08          ? + 0.609 g/l               0
C       C_sample_09          ? + 0.668 g/l               0
C       C_sample_10          ? + 0.728 g/l               0
C       C_sample_11          ? + 0.788 g/l               0
C       C_sample_12          ? + 0.848 g/l               0
C       C_sample_13          ? + 0.908 g/l               0
C       C_sample_14          ? + 0.967 g/l               0
C       C_sample_15          ? + 1.027 g/l               0
C       C_sample_16          ? + 1.087 g/l               0
C       C_sample_17          ? + 1.147 g/l               0
C       C_sample_18          ? + 1.207 g/l               0
C       C_sample_19          ? + 1.266 g/l               0
C       C_sample_20          ? + 1.326 g/l               0
C       C_sample_21          ? + 1.386 g/l               0
C       C_sample_22          ? + 1.446 g/l               0
C       C_sample_23          ? + 1.505 g/l               0
C       C_sample_24          ? + 1.565 g/l               0
C       C_sample_25          ? + 1.625 g/l               1
C       C_sample_26          ? + 1.685 g/l               1
C       C_sample_27          ? + 1.745 g/l               1
C       C_sample_28          ? + 1.804 g/l               1
C       C_sample_29          ? + 1.864 g/l               1
C       C_sample_30          ? + 1.924 g/l               1
C       C_sample_31          ? + 1.984 g/l               1
C       C_sample_32          ? + 2.043 g/l               1
C       C_sample_33          ? + 2.103 g/l               1
C       C_sample_34          ? + 2.163 g/l               1
C       C_sample_35          ? + 2.223 g/l               1
C       C_sample_36          ? + 2.283 g/l               1
C       C_sample_37          ? + 2.342 g/l               1
C       C_sample_38          ? + 2.402 g/l               1
C       C_sample_39          ? + 2.462 g/l               1
C       C_sample_40          ? + 2.522 g/l               1
C       C_sample_41          ? + 2.582 g/l               1
C       C_sample_42          ? + 2.641 g/l               1
C       C_sample_43          ? + 2.701 g/l               1
C       C_sample_44          ? + 2.761 g/l               1
C       C_sample_45          ? + 2.821 g/l               1
C       C_sample_46          ? + 2.880 g/l               1
C       C_sample_47          ? + 2.940 g/l               1
C       C_sample_48          ? + 3.000 g/l               1

D       D_sample_01          ? + 0.000 g/l               0
D       D_sample_02          ? + 0.250 g/l               0
D       D_sample_03          ? + 0.310 g/l               0
D       D_sample_04          ? + 0.370 g/l               0
D       D_sample_05          ? + 0.429 g/l               0
D       D_sample_06          ? + 0.489 g/l               0
D       D_sample_07          ? + 0.549 g/l               0
D       D_sample_08          ? + 0.609 g/l               0
D       D_sample_09          ? + 0.668 g/l               0
D       D_sample_10          ? + 0.728 g/l               0
D       D_sample_11          ? + 0.788 g/l               0
D       D_sample_12          ? + 0.848 g/l               0
D       D_sample_13          ? + 0.908 g/l               0
D       D_sample_14          ? + 0.967 g/l               0
D       D_sample_15          ? + 1.027 g/l               0
D       D_sample_16          ? + 1.087 g/l               0

D       D_sample_33          ? + 2.103 g/l               1
D       D_sample_34          ? + 2.163 g/l               1
D       D_sample_35          ? + 2.223 g/l               1
D       D_sample_36          ? + 2.283 g/l               1
D       D_sample_37          ? + 2.342 g/l               1
D       D_sample_38          ? + 2.402 g/l               1
D       D_sample_39          ? + 2.462 g/l               1
D       D_sample_40          ? + 2.522 g/l               1
D       D_sample_41          ? + 2.582 g/l               1
D       D_sample_42          ? + 2.641 g/l               1
D       D_sample_43          ? + 2.701 g/l               1
D       D_sample_44          ? + 2.761 g/l               1
D       D_sample_45          ? + 2.821 g/l               1
D       D_sample_46          ? + 2.880 g/l               1
D       D_sample_47          ? + 2.940 g/l               1
D       D_sample_48          ? + 3.000 g/l               1

Class 0 = 132 samples
Class 1 = 131 samples
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches
import copy
import matplotlib.lines as mlines


def read_csv_data(path, range_I):
    wavelength = []
    intensity = []
    df = pd.read_csv(path, encoding='ISO-8859-1')
    j = 1
    for i in range_I:
        wavelength.append(i)
        intensity.append(np.mean(df.iloc[:,j].values))
        j += 1
    return wavelength, intensity

def plot_based_on_classes(S1_4_WL,S1_7_WL,S2_0_WL,S2_2_WL,S1_4_I,S1_7_I,S2_0_I,S2_2_I,
                          output_classes,plot_label,suptitle,xlabel,ylabel,show_plot):
    font_size_title  = 10
    font_size_ylabel = 8
    font_size_xlabel = 8
    font_size_ticks  = 6
    font_size_legend = 6
    grid_line_width  = 0.5
    plot_line_width  = 0.5
    
    color1 = 'green'
    color2 = 'magenta'
    
    TUMBlau   = '#0091FF'
    TUMOrange = '#FF590D'
    
    #pop_a = mpatches.Patch(color=TUMBlau, label = plot_label[0])
    #pop_b = mpatches.Patch(color=TUMOrange,   label = plot_label[1], linestyle = 'dotted')
    
    pop_a = mlines.Line2D([], [], color=TUMBlau, linestyle='-', linewidth=2, label=plot_label[0])
    pop_b = mlines.Line2D([], [], color=TUMOrange, linestyle=':', linewidth=2, label=plot_label[1])

    
    #plt.rc('font', family='serif')
    plt.rcParams.update({
        "text.usetex": True,            # Use LaTeX to write all text
        "text.latex.preamble": r"\usepackage{siunitx}\sisetup{per-mode=symbol}",
        "font.family": "serif",         # Match the standard LaTeX serif look
        "font.serif": ["Computer Modern Roman"],
        "font.size": 10,                # Match your document's font size
    })
    

    if show_plot == "yes":
        fig = plt.figure(figsize=(7.00,3.20), dpi = 300)
        #fig.suptitle(suptitle, fontsize = 8)

        ax1 = fig.add_subplot(2,2,1)
        # Hide the top and right spines of the axis
        ax1.spines['right'].set_visible(False)
        ax1.spines['top'].set_visible(False)
        # Edit the major and minor ticks of the x and y axes
        ax1.xaxis.set_tick_params(which='major', size=5, width=1.0, direction='in', top=False)
        ax1.yaxis.set_tick_params(which='major', size=5, width=1.0, direction='in', right=False)
        for i in range(np.shape(S1_4_I)[0]):
            if output_classes[i] == 0:
                ax1.plot(S1_4_WL, S1_4_I[i], color=TUMBlau, linewidth = plot_line_width)
            elif output_classes[i] == 1:
                ax1.plot(S1_4_WL, S1_4_I[i], color=TUMOrange, linewidth = plot_line_width, linestyle = 'dotted')
                
        ax1.set_ylabel(ylabel, fontsize = font_size_ylabel)
        ax1.set_xlabel(xlabel, fontsize = font_size_xlabel)
        ax1.set_title("Sensor S1.4", fontsize = font_size_title)
        ax1.legend(handles=[pop_a,pop_b], prop={'size': font_size_legend})
        #ax1.legend(fontsize = font_size_legend)
        ax1.tick_params(axis = 'both', which = 'major', labelsize = font_size_ticks)
        ax1.grid(True, linewidth = grid_line_width, ls = '--')


        ax2 = fig.add_subplot(2,2,2)
        # Hide the top and right spines of the axis
        ax2.spines['right'].set_visible(False)
        ax2.spines['top'].set_visible(False)
        # Edit the major and minor ticks of the x and y axes
        ax2.xaxis.set_tick_params(which='major', size=5, width=1.0, direction='in', top=False)
        ax2.yaxis.set_tick_params(which='major', size=5, width=1.0, direction='in', right=False)
        for i in range(np.shape(S1_7_I)[0]):
            if output_classes[i] == 0:
                ax2.plot(S1_7_WL, S1_7_I[i], color=TUMBlau, linewidth = plot_line_width)
            elif output_classes[i] == 1:
                ax2.plot(S1_7_WL, S1_7_I[i], color=TUMOrange, linewidth = plot_line_width, linestyle = 'dotted')

        ax2.set_ylabel(ylabel, fontsize = font_size_ylabel)
        ax2.set_xlabel(xlabel, fontsize = font_size_xlabel)
        ax2.set_title("Sensor S1.7", fontsize = font_size_title)
        ax2.legend(handles=[pop_a,pop_b], prop={'size': font_size_legend})
        ax2.tick_params(axis = 'both', which = 'major', labelsize = font_size_ticks)
        ax2.grid(True, linewidth = grid_line_width, ls = '--')


        ax3 = fig.add_subplot(2,2,3)
        # Hide the top and right spines of the axis
        ax3.spines['right'].set_visible(False)
        ax3.spines['top'].set_visible(False)
        # Edit the major and minor ticks of the x and y axes
        ax3.xaxis.set_tick_params(which='major', size=5, width=1.0, direction='in', top=False)
        ax3.yaxis.set_tick_params(which='major', size=5, width=1.0, direction='in', right=False)
        for i in range(np.shape(S2_0_I)[0]):
            if output_classes[i] == 0:
                ax3.plot(S2_0_WL, S2_0_I[i], color=TUMBlau, linewidth = plot_line_width)
            elif output_classes[i] == 1:
                ax3.plot(S2_0_WL, S2_0_I[i], color=TUMOrange, linewidth = plot_line_width, linestyle = 'dotted')

        ax3.set_ylabel(ylabel, fontsize = font_size_ylabel)
        ax3.set_xlabel(xlabel, fontsize = font_size_xlabel)
        ax3.set_title("Sensor S2.0", fontsize = font_size_title)
        ax3.legend(handles=[pop_a,pop_b], prop={'size': font_size_legend})
        ax3.tick_params(axis = 'both', which = 'major', labelsize = font_size_ticks)
        ax3.grid(True, linewidth = grid_line_width, ls = '--')


        ax4 = fig.add_subplot(2,2,4)
        # Hide the top and right spines of the axis
        ax4.spines['right'].set_visible(False)
        ax4.spines['top'].set_visible(False)
        # Edit the major and minor ticks of the x and y axes
        ax4.xaxis.set_tick_params(which='major', size=5, width=1.0, direction='in', top=False)
        ax4.yaxis.set_tick_params(which='major', size=5, width=1.0, direction='in', right=False)
        for i in range(np.shape(S2_2_I)[0]):
            if output_classes[i] == 0:
                ax4.plot(S2_2_WL, S2_2_I[i], color=TUMBlau, linewidth = plot_line_width)
            elif output_classes[i] == 1:
                ax4.plot(S2_2_WL, S2_2_I[i], color=TUMOrange, linewidth = plot_line_width, linestyle = 'dotted')

        ax4.set_ylabel(ylabel, fontsize = font_size_ylabel)
        ax4.set_xlabel(xlabel, fontsize = font_size_xlabel)
        ax4.set_title("Sensor S2.2", fontsize = font_size_title)
        ax4.legend(handles=[pop_a,pop_b], prop={'size': font_size_legend})
        ax4.tick_params(axis = 'both', which = 'major', labelsize = font_size_ticks)
        ax4.grid(True, linewidth = grid_line_width, ls = '--')


        fig.set_tight_layout(True)
        # Save as a vector PDF
        plt.savefig('Figure_3.pdf', format='pdf', bbox_inches='tight', transparent=True)
        plt.show()
        
    else:
        fig = []
    return fig



def signaltonoise(Arr, axis=0, ddof=0):
    Arr = np.asanyarray(Arr)
    me = Arr.mean(axis)
    sd = Arr.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, me/sd)

S1_4_range = range(1100,1352,2)
S1_7_range = range(1350,1652,2)
S2_0_range = range(1550,1952,2)
S2_2_range = range(1750,2152,2)



load_data_sample      = "yes"
load_data_calibration = "no"
del_var               = "yes"





#%% Read CSV data from sample "Probe I,0"
"""
######################################################################################################
# S1.4, Sensor 2, 1100 - 1350 nm
######################################################################################################
"""
### S1.4, Sensor 2, 1100 - 1350 nm
# load data for calibration
if load_data_calibration == "yes":
    I0_S1_4_WL, I0_S1_4_I_light_on = read_csv_data(path = 'Probe I,0/sensor_2_lamp_on.csv', range_I = S1_4_range)
    _, I0_S1_4_I_light_off         = read_csv_data(path = 'Probe I,0/sensor_2_lamp_off.csv', range_I = S1_4_range)
    _, I0_S1_4_I_cuvette           = read_csv_data(path = 'Probe I,0/sensor_2_empty_cuvette.csv', range_I = S1_4_range)
else:
    I0_S1_4_WL, _                  = read_csv_data(path = 'Probe I,0/sensor_2_lamp_on.csv', range_I = S1_4_range)



# load sample data
if load_data_sample == "yes":
    _, I0_S1_4_I_sample_1 = read_csv_data(path = 'Probe I,0/sensor_2_sample_1.csv', range_I = S1_4_range)
    _, I0_S1_4_I_sample_2 = read_csv_data(path = 'Probe I,0/sensor_2_sample_2.csv', range_I = S1_4_range)
    _, I0_S1_4_I_sample_3 = read_csv_data(path = 'Probe I,0/sensor_2_sample_3.csv', range_I = S1_4_range)
    _, I0_S1_4_I_sample_5 = read_csv_data(path = 'Probe I,0/sensor_2_sample_5.csv', range_I = S1_4_range)
    _, I0_S1_4_I_sample_6 = read_csv_data(path = 'Probe I,0/sensor_2_sample_6.csv', range_I = S1_4_range)
    _, I0_S1_4_I_sample_7 = read_csv_data(path = 'Probe I,0/sensor_2_sample_7.csv', range_I = S1_4_range)
    _, I0_S1_4_I_sample_8 = read_csv_data(path = 'Probe I,0/sensor_2_sample_8.csv', range_I = S1_4_range)



# combine sample intensity into one matrix
I0_S1_4_I = [I0_S1_4_I_sample_1, 
             I0_S1_4_I_sample_2, 
             I0_S1_4_I_sample_3, 
             I0_S1_4_I_sample_5, 
             I0_S1_4_I_sample_6, 
             I0_S1_4_I_sample_7, 
             I0_S1_4_I_sample_8]



del I0_S1_4_I_sample_1, I0_S1_4_I_sample_2, I0_S1_4_I_sample_3, I0_S1_4_I_sample_5
del I0_S1_4_I_sample_6, I0_S1_4_I_sample_7, I0_S1_4_I_sample_8



"""
######################################################################################################
# S1.7, Sensor 1, 1350 - 1650 nm
######################################################################################################
"""
### S1.7, Sensor 1, 1350 - 1650 nm
# load data for calibration
if load_data_calibration == "yes":
    I0_S1_7_WL, I0_S1_7_I_light_on = read_csv_data(path = 'Probe I,0/sensor_1_lamp_on.csv', range_I = S1_7_range)
    _, I0_S1_7_I_light_off         = read_csv_data(path = 'Probe I,0/sensor_1_lamp_off.csv', range_I = S1_7_range)
    _, I0_S1_7_I_cuvette           = read_csv_data(path = 'Probe I,0/sensor_1_empty_cuvette.csv', range_I = S1_7_range)
else:
    I0_S1_7_WL, _                  = read_csv_data(path = 'Probe I,0/sensor_1_lamp_on.csv', range_I = S1_7_range)



# load sample data
if load_data_sample == "yes":
    _, I0_S1_7_I_sample_1 = read_csv_data(path = 'Probe I,0/sensor_1_sample_1.csv', range_I = S1_7_range)
    _, I0_S1_7_I_sample_2 = read_csv_data(path = 'Probe I,0/sensor_1_sample_2.csv', range_I = S1_7_range)
    _, I0_S1_7_I_sample_3 = read_csv_data(path = 'Probe I,0/sensor_1_sample_3.csv', range_I = S1_7_range)
    _, I0_S1_7_I_sample_5 = read_csv_data(path = 'Probe I,0/sensor_1_sample_5.csv', range_I = S1_7_range)
    _, I0_S1_7_I_sample_6 = read_csv_data(path = 'Probe I,0/sensor_1_sample_6.csv', range_I = S1_7_range)
    _, I0_S1_7_I_sample_7 = read_csv_data(path = 'Probe I,0/sensor_1_sample_7.csv', range_I = S1_7_range)
    _, I0_S1_7_I_sample_8 = read_csv_data(path = 'Probe I,0/sensor_1_sample_8.csv', range_I = S1_7_range)



# combine sample intensity into one matrix
I0_S1_7_I = [I0_S1_7_I_sample_1, 
             I0_S1_7_I_sample_2, 
             I0_S1_7_I_sample_3, 
             I0_S1_7_I_sample_5, 
             I0_S1_7_I_sample_6, 
             I0_S1_7_I_sample_7, 
             I0_S1_7_I_sample_8]



del I0_S1_7_I_sample_1, I0_S1_7_I_sample_2, I0_S1_7_I_sample_3, I0_S1_7_I_sample_5
del I0_S1_7_I_sample_6, I0_S1_7_I_sample_7, I0_S1_7_I_sample_8



"""
######################################################################################################
# S2.0, Sensor 4, 1550 - 1950 nm
######################################################################################################
"""
### S2.0, Sensor 4, 1550 - 1950 nm
# load data for calibration
if load_data_calibration == "yes":
    I0_S2_0_WL, I0_S2_0_I_light_on = read_csv_data(path = 'Probe I,0/sensor_4_lamp_on.csv', range_I = S2_0_range)
    _, I0_S2_0_I_light_off         = read_csv_data(path = 'Probe I,0/sensor_4_lamp_off.csv', range_I = S2_0_range)
    _, I0_S2_0_I_cuvette           = read_csv_data(path = 'Probe I,0/sensor_4_empty_cuvette.csv', range_I = S2_0_range)
else:
    I0_S2_0_WL, _                  = read_csv_data(path = 'Probe I,0/sensor_4_lamp_on.csv', range_I = S2_0_range)



# load sample data
if load_data_sample == "yes":
    _, I0_S2_0_I_sample_1 = read_csv_data(path = 'Probe I,0/sensor_4_sample_1.csv', range_I = S2_0_range)
    _, I0_S2_0_I_sample_2 = read_csv_data(path = 'Probe I,0/sensor_4_sample_2.csv', range_I = S2_0_range)
    _, I0_S2_0_I_sample_3 = read_csv_data(path = 'Probe I,0/sensor_4_sample_3.csv', range_I = S2_0_range)
    _, I0_S2_0_I_sample_5 = read_csv_data(path = 'Probe I,0/sensor_4_sample_5.csv', range_I = S2_0_range)
    _, I0_S2_0_I_sample_6 = read_csv_data(path = 'Probe I,0/sensor_4_sample_6.csv', range_I = S2_0_range)
    _, I0_S2_0_I_sample_7 = read_csv_data(path = 'Probe I,0/sensor_4_sample_7.csv', range_I = S2_0_range)
    _, I0_S2_0_I_sample_8 = read_csv_data(path = 'Probe I,0/sensor_4_sample_8.csv', range_I = S2_0_range)



# combine sample intensity into one matrix
I0_S2_0_I = [I0_S2_0_I_sample_1, 
             I0_S2_0_I_sample_2, 
             I0_S2_0_I_sample_3, 
             I0_S2_0_I_sample_5, 
             I0_S2_0_I_sample_6, 
             I0_S2_0_I_sample_7, 
             I0_S2_0_I_sample_8]



del I0_S2_0_I_sample_1, I0_S2_0_I_sample_2, I0_S2_0_I_sample_3, I0_S2_0_I_sample_5
del I0_S2_0_I_sample_6, I0_S2_0_I_sample_7, I0_S2_0_I_sample_8



"""
######################################################################################################
# S2.2, Sensor 3, 1750 - 2150 nm
######################################################################################################
"""
### S2.2, Sensor 3, 1750 - 2150 nm
# load data for calibration
if load_data_calibration == "yes":
    I0_S2_2_WL, I0_S2_2_I_light_on = read_csv_data(path = 'Probe I,0/sensor_3_lamp_on.csv', range_I = S2_2_range)
    _, I0_S2_2_I_light_off         = read_csv_data(path = 'Probe I,0/sensor_3_lamp_off.csv', range_I = S2_2_range)
    _, I0_S2_2_I_cuvette           = read_csv_data(path = 'Probe I,0/sensor_3_empty_cuvette.csv', range_I = S2_2_range)
else:
    I0_S2_2_WL, _                  = read_csv_data(path = 'Probe I,0/sensor_3_lamp_on.csv', range_I = S2_2_range)



# load sample data
if load_data_sample == "yes":
    _, I0_S2_2_I_sample_1 = read_csv_data(path = 'Probe I,0/sensor_3_sample_1.csv', range_I = S2_2_range)
    _, I0_S2_2_I_sample_2 = read_csv_data(path = 'Probe I,0/sensor_3_sample_2.csv', range_I = S2_2_range)
    _, I0_S2_2_I_sample_3 = read_csv_data(path = 'Probe I,0/sensor_3_sample_3.csv', range_I = S2_2_range)
    _, I0_S2_2_I_sample_5 = read_csv_data(path = 'Probe I,0/sensor_3_sample_5.csv', range_I = S2_2_range)
    _, I0_S2_2_I_sample_6 = read_csv_data(path = 'Probe I,0/sensor_3_sample_6.csv', range_I = S2_2_range)
    _, I0_S2_2_I_sample_7 = read_csv_data(path = 'Probe I,0/sensor_3_sample_7.csv', range_I = S2_2_range)
    _, I0_S2_2_I_sample_8 = read_csv_data(path = 'Probe I,0/sensor_3_sample_8.csv', range_I = S2_2_range)



# combine sample intensity into one matrix
I0_S2_2_I = [I0_S2_2_I_sample_1, 
             I0_S2_2_I_sample_2, 
             I0_S2_2_I_sample_3, 
             I0_S2_2_I_sample_5, 
             I0_S2_2_I_sample_6, 
             I0_S2_2_I_sample_7, 
             I0_S2_2_I_sample_8]



del I0_S2_2_I_sample_1, I0_S2_2_I_sample_2, I0_S2_2_I_sample_3, I0_S2_2_I_sample_5
del I0_S2_2_I_sample_6, I0_S2_2_I_sample_7, I0_S2_2_I_sample_8





#%% Read CSV data from sample "Probe I,1"
"""
######################################################################################################
# S1.4, Sensor 2, 1100 - 1350 nm
######################################################################################################
"""
### S1.4, Sensor 2, 1100 - 1350 nm
# load data for calibration
if load_data_calibration == "yes":
    I1_S1_4_WL, I1_S1_4_I_light_on = read_csv_data(path = 'Probe I,1/sensor_2_lamp_on.csv', range_I = S1_4_range)
    _, I1_S1_4_I_light_off         = read_csv_data(path = 'Probe I,1/sensor_2_lamp_off.csv', range_I = S1_4_range)
    _, I1_S1_4_I_cuvette           = read_csv_data(path = 'Probe I,1/sensor_2_empty_cuvette.csv', range_I = S1_4_range)
else:
    I1_S1_4_WL, _                  = read_csv_data(path = 'Probe I,1/sensor_2_lamp_on.csv', range_I = S1_4_range)



# load sample data
if load_data_sample == "yes":
    _, I1_S1_4_I_sample_a0 = read_csv_data(path = 'Probe I,1/sensor_2_sample_a0.csv', range_I = S1_4_range)
    _, I1_S1_4_I_sample_a1 = read_csv_data(path = 'Probe I,1/sensor_2_sample_a1.csv', range_I = S1_4_range)
    _, I1_S1_4_I_sample_a2 = read_csv_data(path = 'Probe I,1/sensor_2_sample_a1.csv', range_I = S1_4_range)
    _, I1_S1_4_I_sample_a3 = read_csv_data(path = 'Probe I,1/sensor_2_sample_a3.csv', range_I = S1_4_range)
    _, I1_S1_4_I_sample_b0 = read_csv_data(path = 'Probe I,1/sensor_2_sample_b0.csv', range_I = S1_4_range)
    _, I1_S1_4_I_sample_b1 = read_csv_data(path = 'Probe I,1/sensor_2_sample_b1.csv', range_I = S1_4_range)
    _, I1_S1_4_I_sample_b2 = read_csv_data(path = 'Probe I,1/sensor_2_sample_b2.csv', range_I = S1_4_range)
    _, I1_S1_4_I_sample_b3 = read_csv_data(path = 'Probe I,1/sensor_2_sample_b3.csv', range_I = S1_4_range)



# combine sample intensity into one matrix
I1_S1_4_I = [I1_S1_4_I_sample_a0, 
             I1_S1_4_I_sample_a1, 
             I1_S1_4_I_sample_a2, 
             I1_S1_4_I_sample_a3, 
             I1_S1_4_I_sample_b0, 
             I1_S1_4_I_sample_b1, 
             I1_S1_4_I_sample_b2,
             I1_S1_4_I_sample_b3]



del I1_S1_4_I_sample_a0, I1_S1_4_I_sample_a1, I1_S1_4_I_sample_a2, I1_S1_4_I_sample_a3
del I1_S1_4_I_sample_b0, I1_S1_4_I_sample_b1, I1_S1_4_I_sample_b2, I1_S1_4_I_sample_b3




"""
######################################################################################################
# S1.7, Sensor 1, 1350 - 1650 nm
######################################################################################################
"""
### S1.7, Sensor 1, 1350 - 1650 nm
# load data for calibration
if load_data_calibration == "yes":
    I1_S1_7_WL, I1_S1_7_I_light_on = read_csv_data(path = 'Probe I,1/sensor_1_lamp_on.csv', range_I = S1_7_range)
    _, I1_S1_7_I_light_off         = read_csv_data(path = 'Probe I,1/sensor_1_lamp_off.csv', range_I = S1_7_range)
    _, I1_S1_7_I_cuvette           = read_csv_data(path = 'Probe I,1/sensor_1_empty_cuvette.csv', range_I = S1_7_range)
else:
    I1_S1_7_WL, _                  = read_csv_data(path = 'Probe I,1/sensor_1_lamp_on.csv', range_I = S1_7_range)



# load sample data
if load_data_sample == "yes":
    _, I1_S1_7_I_sample_a0 = read_csv_data(path = 'Probe I,1/sensor_1_sample_a0.csv', range_I = S1_7_range)
    _, I1_S1_7_I_sample_a1 = read_csv_data(path = 'Probe I,1/sensor_1_sample_a1.csv', range_I = S1_7_range)
    _, I1_S1_7_I_sample_a2 = read_csv_data(path = 'Probe I,1/sensor_1_sample_a1.csv', range_I = S1_7_range)
    _, I1_S1_7_I_sample_a3 = read_csv_data(path = 'Probe I,1/sensor_1_sample_a3.csv', range_I = S1_7_range)
    _, I1_S1_7_I_sample_b0 = read_csv_data(path = 'Probe I,1/sensor_1_sample_b0.csv', range_I = S1_7_range)
    _, I1_S1_7_I_sample_b1 = read_csv_data(path = 'Probe I,1/sensor_1_sample_b1.csv', range_I = S1_7_range)
    _, I1_S1_7_I_sample_b2 = read_csv_data(path = 'Probe I,1/sensor_1_sample_b2.csv', range_I = S1_7_range)
    _, I1_S1_7_I_sample_b3 = read_csv_data(path = 'Probe I,1/sensor_1_sample_b3.csv', range_I = S1_7_range)



# combine sample intensity into one matrix
I1_S1_7_I = [I1_S1_7_I_sample_a0, 
             I1_S1_7_I_sample_a1, 
             I1_S1_7_I_sample_a2, 
             I1_S1_7_I_sample_a3, 
             I1_S1_7_I_sample_b0, 
             I1_S1_7_I_sample_b1, 
             I1_S1_7_I_sample_b2,
             I1_S1_7_I_sample_b3]



del I1_S1_7_I_sample_a0, I1_S1_7_I_sample_a1, I1_S1_7_I_sample_a2, I1_S1_7_I_sample_a3
del I1_S1_7_I_sample_b0, I1_S1_7_I_sample_b1, I1_S1_7_I_sample_b2, I1_S1_7_I_sample_b3



"""
######################################################################################################
# S2.0, Sensor 4, 1550 - 1950 nm
######################################################################################################
"""
### S2.0, Sensor 4, 1550 - 1950 nm
# load data for calibration
if load_data_calibration == "yes":
    I1_S2_0_WL, I1_S2_0_I_light_on = read_csv_data(path = 'Probe I,1/sensor_4_lamp_on.csv', range_I = S2_0_range)
    _, I1_S2_0_I_light_off         = read_csv_data(path = 'Probe I,1/sensor_4_lamp_off.csv', range_I = S2_0_range)
    _, I1_S2_0_I_cuvette           = read_csv_data(path = 'Probe I,1/sensor_4_empty_cuvette.csv', range_I = S2_0_range)
else:
    I1_S2_0_WL, _                  = read_csv_data(path = 'Probe I,1/sensor_4_lamp_on.csv', range_I = S2_0_range)



# load sample data
if load_data_sample == "yes":
    _, I1_S2_0_I_sample_a0 = read_csv_data(path = 'Probe I,1/sensor_4_sample_a0.csv', range_I = S2_0_range)
    _, I1_S2_0_I_sample_a1 = read_csv_data(path = 'Probe I,1/sensor_4_sample_a1.csv', range_I = S2_0_range)
    _, I1_S2_0_I_sample_a2 = read_csv_data(path = 'Probe I,1/sensor_4_sample_a1.csv', range_I = S2_0_range)
    _, I1_S2_0_I_sample_a3 = read_csv_data(path = 'Probe I,1/sensor_4_sample_a3.csv', range_I = S2_0_range)
    _, I1_S2_0_I_sample_b0 = read_csv_data(path = 'Probe I,1/sensor_4_sample_b0.csv', range_I = S2_0_range)
    _, I1_S2_0_I_sample_b1 = read_csv_data(path = 'Probe I,1/sensor_4_sample_b1.csv', range_I = S2_0_range)
    _, I1_S2_0_I_sample_b2 = read_csv_data(path = 'Probe I,1/sensor_4_sample_b2.csv', range_I = S2_0_range)
    _, I1_S2_0_I_sample_b3 = read_csv_data(path = 'Probe I,1/sensor_4_sample_b3.csv', range_I = S2_0_range)



# combine sample intensity into one matrix
I1_S2_0_I = [I1_S2_0_I_sample_a0, 
             I1_S2_0_I_sample_a1, 
             I1_S2_0_I_sample_a2, 
             I1_S2_0_I_sample_a3, 
             I1_S2_0_I_sample_b0, 
             I1_S2_0_I_sample_b1, 
             I1_S2_0_I_sample_b2,
             I1_S2_0_I_sample_b3]



del I1_S2_0_I_sample_a0, I1_S2_0_I_sample_a1, I1_S2_0_I_sample_a2, I1_S2_0_I_sample_a3
del I1_S2_0_I_sample_b0, I1_S2_0_I_sample_b1, I1_S2_0_I_sample_b2, I1_S2_0_I_sample_b3



"""
######################################################################################################
# S2.2, Sensor 3, 1750 - 2150 nm
######################################################################################################
"""
### S2.2, Sensor 3, 1750 - 2150 nm
# load data for calibration
if load_data_calibration == "yes":
    I1_S2_2_WL, I1_S2_2_I_light_on = read_csv_data(path = 'Probe I,1/sensor_3_lamp_on.csv', range_I = S2_2_range)
    _, I1_S2_2_I_light_off         = read_csv_data(path = 'Probe I,1/sensor_3_lamp_off.csv', range_I = S2_2_range)
    _, I1_S2_2_I_cuvette           = read_csv_data(path = 'Probe I,1/sensor_3_empty_cuvette.csv', range_I = S2_2_range)
else:
    I1_S2_2_WL, _                  = read_csv_data(path = 'Probe I,1/sensor_3_lamp_on.csv', range_I = S2_2_range)



# load sample data
if load_data_sample == "yes":
    _, I1_S2_2_I_sample_a0 = read_csv_data(path = 'Probe I,1/sensor_3_sample_a0.csv', range_I = S2_2_range)
    _, I1_S2_2_I_sample_a1 = read_csv_data(path = 'Probe I,1/sensor_3_sample_a1.csv', range_I = S2_2_range)
    _, I1_S2_2_I_sample_a2 = read_csv_data(path = 'Probe I,1/sensor_3_sample_a1.csv', range_I = S2_2_range)
    _, I1_S2_2_I_sample_a3 = read_csv_data(path = 'Probe I,1/sensor_3_sample_a3.csv', range_I = S2_2_range)
    _, I1_S2_2_I_sample_b0 = read_csv_data(path = 'Probe I,1/sensor_3_sample_b0.csv', range_I = S2_2_range)
    _, I1_S2_2_I_sample_b1 = read_csv_data(path = 'Probe I,1/sensor_3_sample_b1.csv', range_I = S2_2_range)
    _, I1_S2_2_I_sample_b2 = read_csv_data(path = 'Probe I,1/sensor_3_sample_b2.csv', range_I = S2_2_range)
    _, I1_S2_2_I_sample_b3 = read_csv_data(path = 'Probe I,1/sensor_3_sample_b3.csv', range_I = S2_2_range)



# combine sample intensity into one matrix
I1_S2_2_I = [I1_S2_2_I_sample_a0, 
             I1_S2_2_I_sample_a1, 
             I1_S2_2_I_sample_a2, 
             I1_S2_2_I_sample_a3, 
             I1_S2_2_I_sample_b0, 
             I1_S2_2_I_sample_b1, 
             I1_S2_2_I_sample_b2,
             I1_S2_2_I_sample_b3]



del I1_S2_2_I_sample_a0, I1_S2_2_I_sample_a1, I1_S2_2_I_sample_a2, I1_S2_2_I_sample_a3
del I1_S2_2_I_sample_b0, I1_S2_2_I_sample_b1, I1_S2_2_I_sample_b2, I1_S2_2_I_sample_b3





#%% Read CSV data from sample "Probe I"
"""
######################################################################################################
# S1.4, Sensor 2, 1100 - 1350 nm
######################################################################################################
"""
### S1.4, Sensor 2, 1100 - 1350 nm
# load data for calibration
if load_data_calibration == "yes":
    I_S1_4_WL, I_S1_4_I_light_on = read_csv_data(path = 'Probe I/sensor_2_lamp_on.csv', range_I = S1_4_range)
    _, I_S1_4_I_light_off        = read_csv_data(path = 'Probe I/sensor_2_lamp_off.csv', range_I = S1_4_range)
    _, I_S1_4_I_cuvette          = read_csv_data(path = 'Probe I/sensor_2_empty_cuvette.csv', range_I = S1_4_range)
else:
    I_S1_4_WL, _                 = read_csv_data(path = 'Probe I/sensor_2_lamp_on.csv', range_I = S1_4_range)



# load sample data
if load_data_sample == "yes":
    _, I_S1_4_I_sample_01 = read_csv_data(path = 'Probe I/sensor_2_sample_01.csv', range_I = S1_4_range)
    _, I_S1_4_I_sample_02 = read_csv_data(path = 'Probe I/sensor_2_sample_02.csv', range_I = S1_4_range)
    _, I_S1_4_I_sample_03 = read_csv_data(path = 'Probe I/sensor_2_sample_03.csv', range_I = S1_4_range)
    _, I_S1_4_I_sample_04 = read_csv_data(path = 'Probe I/sensor_2_sample_04.csv', range_I = S1_4_range)
    _, I_S1_4_I_sample_05 = read_csv_data(path = 'Probe I/sensor_2_sample_05.csv', range_I = S1_4_range)
    _, I_S1_4_I_sample_06 = read_csv_data(path = 'Probe I/sensor_2_sample_06.csv', range_I = S1_4_range)
    _, I_S1_4_I_sample_07 = read_csv_data(path = 'Probe I/sensor_2_sample_07.csv', range_I = S1_4_range)
    _, I_S1_4_I_sample_08 = read_csv_data(path = 'Probe I/sensor_2_sample_08.csv', range_I = S1_4_range)
    _, I_S1_4_I_sample_09 = read_csv_data(path = 'Probe I/sensor_2_sample_09.csv', range_I = S1_4_range)
    _, I_S1_4_I_sample_10 = read_csv_data(path = 'Probe I/sensor_2_sample_10.csv', range_I = S1_4_range)
    _, I_S1_4_I_sample_11 = read_csv_data(path = 'Probe I/sensor_2_sample_11.csv', range_I = S1_4_range)
    _, I_S1_4_I_sample_12 = read_csv_data(path = 'Probe I/sensor_2_sample_12.csv', range_I = S1_4_range)
    _, I_S1_4_I_sample_13 = read_csv_data(path = 'Probe I/sensor_2_sample_13.csv', range_I = S1_4_range)
    _, I_S1_4_I_sample_14 = read_csv_data(path = 'Probe I/sensor_2_sample_14.csv', range_I = S1_4_range)
    _, I_S1_4_I_sample_15 = read_csv_data(path = 'Probe I/sensor_2_sample_15.csv', range_I = S1_4_range)
    _, I_S1_4_I_sample_16 = read_csv_data(path = 'Probe I/sensor_2_sample_16.csv', range_I = S1_4_range)



# combine sample intensity into one matrix
I_S1_4_I = [I_S1_4_I_sample_01, 
            I_S1_4_I_sample_02, 
            I_S1_4_I_sample_03, 
            I_S1_4_I_sample_04, 
            I_S1_4_I_sample_05, 
            I_S1_4_I_sample_06, 
            I_S1_4_I_sample_07,
            I_S1_4_I_sample_08,
            I_S1_4_I_sample_09, 
            I_S1_4_I_sample_10, 
            I_S1_4_I_sample_11, 
            I_S1_4_I_sample_12, 
            I_S1_4_I_sample_13, 
            I_S1_4_I_sample_14, 
            I_S1_4_I_sample_15,
            I_S1_4_I_sample_16]



del I_S1_4_I_sample_01, I_S1_4_I_sample_02, I_S1_4_I_sample_03, I_S1_4_I_sample_04
del I_S1_4_I_sample_05, I_S1_4_I_sample_06, I_S1_4_I_sample_07, I_S1_4_I_sample_08
del I_S1_4_I_sample_09, I_S1_4_I_sample_10, I_S1_4_I_sample_11, I_S1_4_I_sample_12
del I_S1_4_I_sample_13, I_S1_4_I_sample_14, I_S1_4_I_sample_15, I_S1_4_I_sample_16



"""
######################################################################################################
# S1.7, Sensor 1, 1350 - 1650 nm
######################################################################################################
"""
### S1.7, Sensor 1, 1350 - 1650 nm
# load data for calibration
if load_data_calibration == "yes":
    I_S1_7_WL, I_S1_7_I_light_on = read_csv_data(path = 'Probe I/sensor_1_lamp_on.csv', range_I = S1_7_range)
    _, I_S1_7_I_light_off        = read_csv_data(path = 'Probe I/sensor_1_lamp_off.csv', range_I = S1_7_range)
    _, I_S1_7_I_cuvette          = read_csv_data(path = 'Probe I/sensor_1_empty_cuvette.csv', range_I = S1_7_range)
else:
    I_S1_7_WL, _                 = read_csv_data(path = 'Probe I/sensor_1_lamp_on.csv', range_I = S1_7_range)



# load sample data
if load_data_sample == "yes":
    _, I_S1_7_I_sample_01 = read_csv_data(path = 'Probe I/sensor_1_sample_01.csv', range_I = S1_7_range)
    _, I_S1_7_I_sample_02 = read_csv_data(path = 'Probe I/sensor_1_sample_02.csv', range_I = S1_7_range)
    _, I_S1_7_I_sample_03 = read_csv_data(path = 'Probe I/sensor_1_sample_03.csv', range_I = S1_7_range)
    _, I_S1_7_I_sample_04 = read_csv_data(path = 'Probe I/sensor_1_sample_04.csv', range_I = S1_7_range)
    _, I_S1_7_I_sample_05 = read_csv_data(path = 'Probe I/sensor_1_sample_05.csv', range_I = S1_7_range)
    _, I_S1_7_I_sample_06 = read_csv_data(path = 'Probe I/sensor_1_sample_06.csv', range_I = S1_7_range)
    _, I_S1_7_I_sample_07 = read_csv_data(path = 'Probe I/sensor_1_sample_07.csv', range_I = S1_7_range)
    _, I_S1_7_I_sample_08 = read_csv_data(path = 'Probe I/sensor_1_sample_08.csv', range_I = S1_7_range)
    _, I_S1_7_I_sample_09 = read_csv_data(path = 'Probe I/sensor_1_sample_09.csv', range_I = S1_7_range)
    _, I_S1_7_I_sample_10 = read_csv_data(path = 'Probe I/sensor_1_sample_10.csv', range_I = S1_7_range)
    _, I_S1_7_I_sample_11 = read_csv_data(path = 'Probe I/sensor_1_sample_11.csv', range_I = S1_7_range)
    _, I_S1_7_I_sample_12 = read_csv_data(path = 'Probe I/sensor_1_sample_12.csv', range_I = S1_7_range)
    _, I_S1_7_I_sample_13 = read_csv_data(path = 'Probe I/sensor_1_sample_13.csv', range_I = S1_7_range)
    _, I_S1_7_I_sample_14 = read_csv_data(path = 'Probe I/sensor_1_sample_14.csv', range_I = S1_7_range)
    _, I_S1_7_I_sample_15 = read_csv_data(path = 'Probe I/sensor_1_sample_15.csv', range_I = S1_7_range)
    _, I_S1_7_I_sample_16 = read_csv_data(path = 'Probe I/sensor_1_sample_16.csv', range_I = S1_7_range)



# combine sample intensity into one matrix
I_S1_7_I = [I_S1_7_I_sample_01, 
            I_S1_7_I_sample_02, 
            I_S1_7_I_sample_03, 
            I_S1_7_I_sample_04, 
            I_S1_7_I_sample_05, 
            I_S1_7_I_sample_06, 
            I_S1_7_I_sample_07,
            I_S1_7_I_sample_08,
            I_S1_7_I_sample_09, 
            I_S1_7_I_sample_10, 
            I_S1_7_I_sample_11, 
            I_S1_7_I_sample_12, 
            I_S1_7_I_sample_13, 
            I_S1_7_I_sample_14, 
            I_S1_7_I_sample_15,
            I_S1_7_I_sample_16]



del I_S1_7_I_sample_01, I_S1_7_I_sample_02, I_S1_7_I_sample_03, I_S1_7_I_sample_04
del I_S1_7_I_sample_05, I_S1_7_I_sample_06, I_S1_7_I_sample_07, I_S1_7_I_sample_08
del I_S1_7_I_sample_09, I_S1_7_I_sample_10, I_S1_7_I_sample_11, I_S1_7_I_sample_12
del I_S1_7_I_sample_13, I_S1_7_I_sample_14, I_S1_7_I_sample_15, I_S1_7_I_sample_16



"""
######################################################################################################
# S2.0, Sensor 4, 1550 - 1950 nm
######################################################################################################
"""
### S2.0, Sensor 4, 1550 - 1950 nm
# load data for calibration
if load_data_calibration == "yes":
    I_S2_0_WL, I_S2_0_I_light_on = read_csv_data(path = 'Probe I/sensor_4_lamp_on.csv', range_I = S2_0_range)
    _, I_S2_0_I_light_off        = read_csv_data(path = 'Probe I/sensor_4_lamp_off.csv', range_I = S2_0_range)
    _, I_S2_0_I_cuvette          = read_csv_data(path = 'Probe I/sensor_4_empty_cuvette.csv', range_I = S2_0_range)
else:
    I_S2_0_WL, _                 = read_csv_data(path = 'Probe I/sensor_4_lamp_on.csv', range_I = S2_0_range)



# load sample data
if load_data_sample == "yes":
    _, I_S2_0_I_sample_01 = read_csv_data(path = 'Probe I/sensor_4_sample_01.csv', range_I = S2_0_range)
    _, I_S2_0_I_sample_02 = read_csv_data(path = 'Probe I/sensor_4_sample_02.csv', range_I = S2_0_range)
    _, I_S2_0_I_sample_03 = read_csv_data(path = 'Probe I/sensor_4_sample_03.csv', range_I = S2_0_range)
    _, I_S2_0_I_sample_04 = read_csv_data(path = 'Probe I/sensor_4_sample_04.csv', range_I = S2_0_range)
    _, I_S2_0_I_sample_05 = read_csv_data(path = 'Probe I/sensor_4_sample_05.csv', range_I = S2_0_range)
    _, I_S2_0_I_sample_06 = read_csv_data(path = 'Probe I/sensor_4_sample_06.csv', range_I = S2_0_range)
    _, I_S2_0_I_sample_07 = read_csv_data(path = 'Probe I/sensor_4_sample_07.csv', range_I = S2_0_range)
    _, I_S2_0_I_sample_08 = read_csv_data(path = 'Probe I/sensor_4_sample_08.csv', range_I = S2_0_range)
    _, I_S2_0_I_sample_09 = read_csv_data(path = 'Probe I/sensor_4_sample_09.csv', range_I = S2_0_range)
    _, I_S2_0_I_sample_10 = read_csv_data(path = 'Probe I/sensor_4_sample_10.csv', range_I = S2_0_range)
    _, I_S2_0_I_sample_11 = read_csv_data(path = 'Probe I/sensor_4_sample_11.csv', range_I = S2_0_range)
    _, I_S2_0_I_sample_12 = read_csv_data(path = 'Probe I/sensor_4_sample_12.csv', range_I = S2_0_range)
    _, I_S2_0_I_sample_13 = read_csv_data(path = 'Probe I/sensor_4_sample_13.csv', range_I = S2_0_range)
    _, I_S2_0_I_sample_14 = read_csv_data(path = 'Probe I/sensor_4_sample_14.csv', range_I = S2_0_range)
    _, I_S2_0_I_sample_15 = read_csv_data(path = 'Probe I/sensor_4_sample_15.csv', range_I = S2_0_range)
    _, I_S2_0_I_sample_16 = read_csv_data(path = 'Probe I/sensor_4_sample_16.csv', range_I = S2_0_range)



# combine sample intensity into one matrix
I_S2_0_I = [I_S2_0_I_sample_01, 
            I_S2_0_I_sample_02, 
            I_S2_0_I_sample_03, 
            I_S2_0_I_sample_04, 
            I_S2_0_I_sample_05, 
            I_S2_0_I_sample_06, 
            I_S2_0_I_sample_07,
            I_S2_0_I_sample_08,
            I_S2_0_I_sample_09, 
            I_S2_0_I_sample_10, 
            I_S2_0_I_sample_11, 
            I_S2_0_I_sample_12, 
            I_S2_0_I_sample_13, 
            I_S2_0_I_sample_14, 
            I_S2_0_I_sample_15,
            I_S2_0_I_sample_16]



del I_S2_0_I_sample_01, I_S2_0_I_sample_02, I_S2_0_I_sample_03, I_S2_0_I_sample_04
del I_S2_0_I_sample_05, I_S2_0_I_sample_06, I_S2_0_I_sample_07, I_S2_0_I_sample_08
del I_S2_0_I_sample_09, I_S2_0_I_sample_10, I_S2_0_I_sample_11, I_S2_0_I_sample_12
del I_S2_0_I_sample_13, I_S2_0_I_sample_14, I_S2_0_I_sample_15, I_S2_0_I_sample_16



"""
######################################################################################################
# S2.2, Sensor 3, 1750 - 2150 nm
######################################################################################################
"""
### S2.2, Sensor 3, 1750 - 2150 nm
# load data for calibration
if load_data_calibration == "yes":
    I_S2_2_WL, I_S2_2_I_light_on = read_csv_data(path = 'Probe I/sensor_3_lamp_on.csv', range_I = S2_2_range)
    _, I_S2_2_I_light_off        = read_csv_data(path = 'Probe I/sensor_3_lamp_off.csv', range_I = S2_2_range)
    _, I_S2_2_I_cuvette          = read_csv_data(path = 'Probe I/sensor_3_empty_cuvette.csv', range_I = S2_2_range)
else:
    I_S2_2_WL, _                 = read_csv_data(path = 'Probe I/sensor_3_lamp_on.csv', range_I = S2_2_range)



# load sample data
if load_data_sample == "yes":
    _, I_S2_2_I_sample_01 = read_csv_data(path = 'Probe I/sensor_3_sample_01.csv', range_I = S2_2_range)
    _, I_S2_2_I_sample_02 = read_csv_data(path = 'Probe I/sensor_3_sample_02.csv', range_I = S2_2_range)
    _, I_S2_2_I_sample_03 = read_csv_data(path = 'Probe I/sensor_3_sample_03.csv', range_I = S2_2_range)
    _, I_S2_2_I_sample_04 = read_csv_data(path = 'Probe I/sensor_3_sample_04.csv', range_I = S2_2_range)
    _, I_S2_2_I_sample_05 = read_csv_data(path = 'Probe I/sensor_3_sample_05.csv', range_I = S2_2_range)
    _, I_S2_2_I_sample_06 = read_csv_data(path = 'Probe I/sensor_3_sample_06.csv', range_I = S2_2_range)
    _, I_S2_2_I_sample_07 = read_csv_data(path = 'Probe I/sensor_3_sample_07.csv', range_I = S2_2_range)
    _, I_S2_2_I_sample_08 = read_csv_data(path = 'Probe I/sensor_3_sample_08.csv', range_I = S2_2_range)
    _, I_S2_2_I_sample_09 = read_csv_data(path = 'Probe I/sensor_3_sample_09.csv', range_I = S2_2_range)
    _, I_S2_2_I_sample_10 = read_csv_data(path = 'Probe I/sensor_3_sample_10.csv', range_I = S2_2_range)
    _, I_S2_2_I_sample_11 = read_csv_data(path = 'Probe I/sensor_3_sample_11.csv', range_I = S2_2_range)
    _, I_S2_2_I_sample_12 = read_csv_data(path = 'Probe I/sensor_3_sample_12.csv', range_I = S2_2_range)
    _, I_S2_2_I_sample_13 = read_csv_data(path = 'Probe I/sensor_3_sample_13.csv', range_I = S2_2_range)
    _, I_S2_2_I_sample_14 = read_csv_data(path = 'Probe I/sensor_3_sample_14.csv', range_I = S2_2_range)
    _, I_S2_2_I_sample_15 = read_csv_data(path = 'Probe I/sensor_3_sample_15.csv', range_I = S2_2_range)
    _, I_S2_2_I_sample_16 = read_csv_data(path = 'Probe I/sensor_3_sample_16.csv', range_I = S2_2_range)



# combine sample intensity into one matrix
I_S2_2_I = [I_S2_2_I_sample_01, 
            I_S2_2_I_sample_02, 
            I_S2_2_I_sample_03, 
            I_S2_2_I_sample_04, 
            I_S2_2_I_sample_05, 
            I_S2_2_I_sample_06, 
            I_S2_2_I_sample_07,
            I_S2_2_I_sample_08,
            I_S2_2_I_sample_09, 
            I_S2_2_I_sample_10, 
            I_S2_2_I_sample_11, 
            I_S2_2_I_sample_12, 
            I_S2_2_I_sample_13, 
            I_S2_2_I_sample_14, 
            I_S2_2_I_sample_15,
            I_S2_2_I_sample_16]



del I_S2_2_I_sample_01, I_S2_2_I_sample_02, I_S2_2_I_sample_03, I_S2_2_I_sample_04
del I_S2_2_I_sample_05, I_S2_2_I_sample_06, I_S2_2_I_sample_07, I_S2_2_I_sample_08
del I_S2_2_I_sample_09, I_S2_2_I_sample_10, I_S2_2_I_sample_11, I_S2_2_I_sample_12
del I_S2_2_I_sample_13, I_S2_2_I_sample_14, I_S2_2_I_sample_15, I_S2_2_I_sample_16





#%% Read CSV data from sample "Probe J"
"""
######################################################################################################
# S1.4, Sensor 2, 1100 - 1350 nm
######################################################################################################
"""
### S1.4, Sensor 2, 1100 - 1350 nm
# load data for calibration
if load_data_calibration == "yes":
    J_S1_4_WL, J_S1_4_I_light_on = read_csv_data(path = 'Probe J/sensor_2_lamp_on.csv', range_I = S1_4_range)
    _, J_S1_4_I_light_off        = read_csv_data(path = 'Probe J/sensor_2_lamp_off.csv', range_I = S1_4_range)
    _, J_S1_4_I_cuvette          = read_csv_data(path = 'Probe J/sensor_2_empty_cuvette.csv', range_I = S1_4_range)
else:
    J_S1_4_WL, _                 = read_csv_data(path = 'Probe J/sensor_2_lamp_on.csv', range_I = S1_4_range)



# load sample data
if load_data_sample == "yes":
    _, J_S1_4_I_sample_01 = read_csv_data(path = 'Probe J/sensor_2_sample_01.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_02 = read_csv_data(path = 'Probe J/sensor_2_sample_02.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_03 = read_csv_data(path = 'Probe J/sensor_2_sample_03.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_04 = read_csv_data(path = 'Probe J/sensor_2_sample_04.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_05 = read_csv_data(path = 'Probe J/sensor_2_sample_05.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_06 = read_csv_data(path = 'Probe J/sensor_2_sample_06.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_07 = read_csv_data(path = 'Probe J/sensor_2_sample_07.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_08 = read_csv_data(path = 'Probe J/sensor_2_sample_08.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_09 = read_csv_data(path = 'Probe J/sensor_2_sample_09.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_10 = read_csv_data(path = 'Probe J/sensor_2_sample_10.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_11 = read_csv_data(path = 'Probe J/sensor_2_sample_11.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_12 = read_csv_data(path = 'Probe J/sensor_2_sample_12.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_13 = read_csv_data(path = 'Probe J/sensor_2_sample_13.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_14 = read_csv_data(path = 'Probe J/sensor_2_sample_14.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_15 = read_csv_data(path = 'Probe J/sensor_2_sample_15.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_16 = read_csv_data(path = 'Probe J/sensor_2_sample_16.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_17 = read_csv_data(path = 'Probe J/sensor_2_sample_17.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_18 = read_csv_data(path = 'Probe J/sensor_2_sample_18.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_19 = read_csv_data(path = 'Probe J/sensor_2_sample_19.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_20 = read_csv_data(path = 'Probe J/sensor_2_sample_20.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_21 = read_csv_data(path = 'Probe J/sensor_2_sample_21.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_22 = read_csv_data(path = 'Probe J/sensor_2_sample_22.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_23 = read_csv_data(path = 'Probe J/sensor_2_sample_23.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_24 = read_csv_data(path = 'Probe J/sensor_2_sample_24.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_25 = read_csv_data(path = 'Probe J/sensor_2_sample_25.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_26 = read_csv_data(path = 'Probe J/sensor_2_sample_26.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_27 = read_csv_data(path = 'Probe J/sensor_2_sample_27.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_28 = read_csv_data(path = 'Probe J/sensor_2_sample_28.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_29 = read_csv_data(path = 'Probe J/sensor_2_sample_29.csv', range_I = S1_4_range)
    _, J_S1_4_I_sample_30 = read_csv_data(path = 'Probe J/sensor_2_sample_30.csv', range_I = S1_4_range)



# combine sample intensity into one matrix
J_S1_4_I = [J_S1_4_I_sample_01,
            J_S1_4_I_sample_02,
            J_S1_4_I_sample_03,
            J_S1_4_I_sample_04,
            J_S1_4_I_sample_05,
            J_S1_4_I_sample_06,
            J_S1_4_I_sample_07,
            J_S1_4_I_sample_08,
            J_S1_4_I_sample_09,
            J_S1_4_I_sample_10,
            J_S1_4_I_sample_11,
            J_S1_4_I_sample_12,
            J_S1_4_I_sample_13,
            J_S1_4_I_sample_14,
            J_S1_4_I_sample_15,
            J_S1_4_I_sample_16,
            J_S1_4_I_sample_17,
            J_S1_4_I_sample_18,
            J_S1_4_I_sample_19,
            J_S1_4_I_sample_20,
            J_S1_4_I_sample_21,
            J_S1_4_I_sample_22,
            J_S1_4_I_sample_23,
            J_S1_4_I_sample_24,
            J_S1_4_I_sample_25,
            J_S1_4_I_sample_26,
            J_S1_4_I_sample_27,
            J_S1_4_I_sample_28,
            J_S1_4_I_sample_29,
            J_S1_4_I_sample_30]



del J_S1_4_I_sample_01, J_S1_4_I_sample_02, J_S1_4_I_sample_03, J_S1_4_I_sample_04
del J_S1_4_I_sample_05, J_S1_4_I_sample_06, J_S1_4_I_sample_07, J_S1_4_I_sample_08
del J_S1_4_I_sample_09, J_S1_4_I_sample_10, J_S1_4_I_sample_11, J_S1_4_I_sample_12
del J_S1_4_I_sample_13, J_S1_4_I_sample_14, J_S1_4_I_sample_15, J_S1_4_I_sample_16
del J_S1_4_I_sample_17, J_S1_4_I_sample_18, J_S1_4_I_sample_19, J_S1_4_I_sample_20
del J_S1_4_I_sample_21, J_S1_4_I_sample_22, J_S1_4_I_sample_23, J_S1_4_I_sample_24
del J_S1_4_I_sample_25, J_S1_4_I_sample_26, J_S1_4_I_sample_27, J_S1_4_I_sample_28
del J_S1_4_I_sample_29, J_S1_4_I_sample_30



"""
######################################################################################################
# S1.7, Sensor 1, 1350 - 1650 nm
######################################################################################################
"""
### S1.7, Sensor 1, 1350 - 1650 nm
# load data for calibration
if load_data_calibration == "yes":
    J_S1_7_WL, J_S1_7_I_light_on = read_csv_data(path = 'Probe J/sensor_1_lamp_on.csv', range_I = S1_7_range)
    _, J_S1_7_I_light_off        = read_csv_data(path = 'Probe J/sensor_1_lamp_off.csv', range_I = S1_7_range)
    _, J_S1_7_I_cuvette          = read_csv_data(path = 'Probe J/sensor_1_empty_cuvette.csv', range_I = S1_7_range)
else:
    J_S1_7_WL, _                 = read_csv_data(path = 'Probe J/sensor_1_lamp_on.csv', range_I = S1_7_range)



# load sample data
if load_data_sample == "yes":
    _, J_S1_7_I_sample_01 = read_csv_data(path = 'Probe J/sensor_1_sample_01.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_02 = read_csv_data(path = 'Probe J/sensor_1_sample_02.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_03 = read_csv_data(path = 'Probe J/sensor_1_sample_03.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_04 = read_csv_data(path = 'Probe J/sensor_1_sample_04.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_05 = read_csv_data(path = 'Probe J/sensor_1_sample_05.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_06 = read_csv_data(path = 'Probe J/sensor_1_sample_06.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_07 = read_csv_data(path = 'Probe J/sensor_1_sample_07.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_08 = read_csv_data(path = 'Probe J/sensor_1_sample_08.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_09 = read_csv_data(path = 'Probe J/sensor_1_sample_09.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_10 = read_csv_data(path = 'Probe J/sensor_1_sample_10.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_11 = read_csv_data(path = 'Probe J/sensor_1_sample_11.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_12 = read_csv_data(path = 'Probe J/sensor_1_sample_12.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_13 = read_csv_data(path = 'Probe J/sensor_1_sample_13.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_14 = read_csv_data(path = 'Probe J/sensor_1_sample_14.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_15 = read_csv_data(path = 'Probe J/sensor_1_sample_15.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_16 = read_csv_data(path = 'Probe J/sensor_1_sample_16.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_17 = read_csv_data(path = 'Probe J/sensor_1_sample_17.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_18 = read_csv_data(path = 'Probe J/sensor_1_sample_18.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_19 = read_csv_data(path = 'Probe J/sensor_1_sample_19.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_20 = read_csv_data(path = 'Probe J/sensor_1_sample_20.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_21 = read_csv_data(path = 'Probe J/sensor_1_sample_21.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_22 = read_csv_data(path = 'Probe J/sensor_1_sample_22.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_23 = read_csv_data(path = 'Probe J/sensor_1_sample_23.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_24 = read_csv_data(path = 'Probe J/sensor_1_sample_24.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_25 = read_csv_data(path = 'Probe J/sensor_1_sample_25.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_26 = read_csv_data(path = 'Probe J/sensor_1_sample_26.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_27 = read_csv_data(path = 'Probe J/sensor_1_sample_27.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_28 = read_csv_data(path = 'Probe J/sensor_1_sample_28.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_29 = read_csv_data(path = 'Probe J/sensor_1_sample_29.csv', range_I = S1_7_range)
    _, J_S1_7_I_sample_30 = read_csv_data(path = 'Probe J/sensor_1_sample_30.csv', range_I = S1_7_range)



# combine sample intensity into one matrix
J_S1_7_I = [J_S1_7_I_sample_01,
            J_S1_7_I_sample_02,
            J_S1_7_I_sample_03,
            J_S1_7_I_sample_04,
            J_S1_7_I_sample_05,
            J_S1_7_I_sample_06,
            J_S1_7_I_sample_07,
            J_S1_7_I_sample_08,
            J_S1_7_I_sample_09,
            J_S1_7_I_sample_10,
            J_S1_7_I_sample_11,
            J_S1_7_I_sample_12,
            J_S1_7_I_sample_13,
            J_S1_7_I_sample_14,
            J_S1_7_I_sample_15,
            J_S1_7_I_sample_16,
            J_S1_7_I_sample_17,
            J_S1_7_I_sample_18,
            J_S1_7_I_sample_19,
            J_S1_7_I_sample_20,
            J_S1_7_I_sample_21,
            J_S1_7_I_sample_22,
            J_S1_7_I_sample_23,
            J_S1_7_I_sample_24,
            J_S1_7_I_sample_25,
            J_S1_7_I_sample_26,
            J_S1_7_I_sample_27,
            J_S1_7_I_sample_28,
            J_S1_7_I_sample_29,
            J_S1_7_I_sample_30]



del J_S1_7_I_sample_01, J_S1_7_I_sample_02, J_S1_7_I_sample_03, J_S1_7_I_sample_04
del J_S1_7_I_sample_05, J_S1_7_I_sample_06, J_S1_7_I_sample_07, J_S1_7_I_sample_08
del J_S1_7_I_sample_09, J_S1_7_I_sample_10, J_S1_7_I_sample_11, J_S1_7_I_sample_12
del J_S1_7_I_sample_13, J_S1_7_I_sample_14, J_S1_7_I_sample_15, J_S1_7_I_sample_16
del J_S1_7_I_sample_17, J_S1_7_I_sample_18, J_S1_7_I_sample_19, J_S1_7_I_sample_20
del J_S1_7_I_sample_21, J_S1_7_I_sample_22, J_S1_7_I_sample_23, J_S1_7_I_sample_24
del J_S1_7_I_sample_25, J_S1_7_I_sample_26, J_S1_7_I_sample_27, J_S1_7_I_sample_28
del J_S1_7_I_sample_29, J_S1_7_I_sample_30



"""
######################################################################################################
# S2.0, Sensor 4, 1550 - 1950 nm
######################################################################################################
"""
### S2.0, Sensor 4, 1550 - 1950 nm
# load data for calibration
if load_data_calibration == "yes":
    J_S2_0_WL, J_S2_0_I_light_on = read_csv_data(path = 'Probe J/sensor_4_lamp_on.csv', range_I = S2_0_range)
    _, J_S2_0_I_light_off        = read_csv_data(path = 'Probe J/sensor_4_lamp_off.csv', range_I = S2_0_range)
    _, J_S2_0_I_cuvette          = read_csv_data(path = 'Probe J/sensor_4_empty_cuvette.csv', range_I = S2_0_range)
else:
    J_S2_0_WL, _                 = read_csv_data(path = 'Probe J/sensor_4_lamp_on.csv', range_I = S2_0_range)



# load sample data
if load_data_sample == "yes":
    _, J_S2_0_I_sample_01 = read_csv_data(path = 'Probe J/sensor_4_sample_01.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_02 = read_csv_data(path = 'Probe J/sensor_4_sample_02.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_03 = read_csv_data(path = 'Probe J/sensor_4_sample_03.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_04 = read_csv_data(path = 'Probe J/sensor_4_sample_04.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_05 = read_csv_data(path = 'Probe J/sensor_4_sample_05.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_06 = read_csv_data(path = 'Probe J/sensor_4_sample_06.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_07 = read_csv_data(path = 'Probe J/sensor_4_sample_07.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_08 = read_csv_data(path = 'Probe J/sensor_4_sample_08.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_09 = read_csv_data(path = 'Probe J/sensor_4_sample_09.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_10 = read_csv_data(path = 'Probe J/sensor_4_sample_10.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_11 = read_csv_data(path = 'Probe J/sensor_4_sample_11.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_12 = read_csv_data(path = 'Probe J/sensor_4_sample_12.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_13 = read_csv_data(path = 'Probe J/sensor_4_sample_13.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_14 = read_csv_data(path = 'Probe J/sensor_4_sample_14.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_15 = read_csv_data(path = 'Probe J/sensor_4_sample_15.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_16 = read_csv_data(path = 'Probe J/sensor_4_sample_16.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_17 = read_csv_data(path = 'Probe J/sensor_4_sample_17.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_18 = read_csv_data(path = 'Probe J/sensor_4_sample_18.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_19 = read_csv_data(path = 'Probe J/sensor_4_sample_19.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_20 = read_csv_data(path = 'Probe J/sensor_4_sample_20.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_21 = read_csv_data(path = 'Probe J/sensor_4_sample_21.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_22 = read_csv_data(path = 'Probe J/sensor_4_sample_22.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_23 = read_csv_data(path = 'Probe J/sensor_4_sample_23.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_24 = read_csv_data(path = 'Probe J/sensor_4_sample_24.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_25 = read_csv_data(path = 'Probe J/sensor_4_sample_25.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_26 = read_csv_data(path = 'Probe J/sensor_4_sample_26.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_27 = read_csv_data(path = 'Probe J/sensor_4_sample_27.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_28 = read_csv_data(path = 'Probe J/sensor_4_sample_28.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_29 = read_csv_data(path = 'Probe J/sensor_4_sample_29.csv', range_I = S2_0_range)
    _, J_S2_0_I_sample_30 = read_csv_data(path = 'Probe J/sensor_4_sample_30.csv', range_I = S2_0_range)



# combine sample intensity into one matrix
J_S2_0_I = [J_S2_0_I_sample_01,
            J_S2_0_I_sample_02,
            J_S2_0_I_sample_03,
            J_S2_0_I_sample_04,
            J_S2_0_I_sample_05,
            J_S2_0_I_sample_06,
            J_S2_0_I_sample_07,
            J_S2_0_I_sample_08,
            J_S2_0_I_sample_09,
            J_S2_0_I_sample_10,
            J_S2_0_I_sample_11,
            J_S2_0_I_sample_12,
            J_S2_0_I_sample_13,
            J_S2_0_I_sample_14,
            J_S2_0_I_sample_15,
            J_S2_0_I_sample_16,
            J_S2_0_I_sample_17,
            J_S2_0_I_sample_18,
            J_S2_0_I_sample_19,
            J_S2_0_I_sample_20,
            J_S2_0_I_sample_21,
            J_S2_0_I_sample_22,
            J_S2_0_I_sample_23,
            J_S2_0_I_sample_24,
            J_S2_0_I_sample_25,
            J_S2_0_I_sample_26,
            J_S2_0_I_sample_27,
            J_S2_0_I_sample_28,
            J_S2_0_I_sample_29,
            J_S2_0_I_sample_30]



del J_S2_0_I_sample_01, J_S2_0_I_sample_02, J_S2_0_I_sample_03, J_S2_0_I_sample_04
del J_S2_0_I_sample_05, J_S2_0_I_sample_06, J_S2_0_I_sample_07, J_S2_0_I_sample_08
del J_S2_0_I_sample_09, J_S2_0_I_sample_10, J_S2_0_I_sample_11, J_S2_0_I_sample_12
del J_S2_0_I_sample_13, J_S2_0_I_sample_14, J_S2_0_I_sample_15, J_S2_0_I_sample_16
del J_S2_0_I_sample_17, J_S2_0_I_sample_18, J_S2_0_I_sample_19, J_S2_0_I_sample_20
del J_S2_0_I_sample_21, J_S2_0_I_sample_22, J_S2_0_I_sample_23, J_S2_0_I_sample_24
del J_S2_0_I_sample_25, J_S2_0_I_sample_26, J_S2_0_I_sample_27, J_S2_0_I_sample_28
del J_S2_0_I_sample_29, J_S2_0_I_sample_30



"""
######################################################################################################
# S2.2, Sensor 3, 1750 - 2150 nm
######################################################################################################
"""
### S2.2, Sensor 3, 1750 - 2150 nm
# load data for calibration
if load_data_calibration == "yes":
    J_S2_2_WL, J_S2_2_I_light_on = read_csv_data(path = 'Probe J/sensor_3_lamp_on.csv', range_I = S2_2_range)
    _, J_S2_2_I_light_off        = read_csv_data(path = 'Probe J/sensor_3_lamp_off.csv', range_I = S2_2_range)
    _, J_S2_2_I_cuvette          = read_csv_data(path = 'Probe J/sensor_3_empty_cuvette.csv', range_I = S2_2_range)
else:
    J_S2_2_WL, _                 = read_csv_data(path = 'Probe J/sensor_3_lamp_on.csv', range_I = S2_2_range)



# load sample data
if load_data_sample == "yes":
    _, J_S2_2_I_sample_01 = read_csv_data(path = 'Probe J/sensor_3_sample_01.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_02 = read_csv_data(path = 'Probe J/sensor_3_sample_02.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_03 = read_csv_data(path = 'Probe J/sensor_3_sample_03.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_04 = read_csv_data(path = 'Probe J/sensor_3_sample_04.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_05 = read_csv_data(path = 'Probe J/sensor_3_sample_05.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_06 = read_csv_data(path = 'Probe J/sensor_3_sample_06.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_07 = read_csv_data(path = 'Probe J/sensor_3_sample_07.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_08 = read_csv_data(path = 'Probe J/sensor_3_sample_08.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_09 = read_csv_data(path = 'Probe J/sensor_3_sample_09.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_10 = read_csv_data(path = 'Probe J/sensor_3_sample_10.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_11 = read_csv_data(path = 'Probe J/sensor_3_sample_11.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_12 = read_csv_data(path = 'Probe J/sensor_3_sample_12.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_13 = read_csv_data(path = 'Probe J/sensor_3_sample_13.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_14 = read_csv_data(path = 'Probe J/sensor_3_sample_14.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_15 = read_csv_data(path = 'Probe J/sensor_3_sample_15.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_16 = read_csv_data(path = 'Probe J/sensor_3_sample_16.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_17 = read_csv_data(path = 'Probe J/sensor_3_sample_17.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_18 = read_csv_data(path = 'Probe J/sensor_3_sample_18.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_19 = read_csv_data(path = 'Probe J/sensor_3_sample_19.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_20 = read_csv_data(path = 'Probe J/sensor_3_sample_20.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_21 = read_csv_data(path = 'Probe J/sensor_3_sample_21.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_22 = read_csv_data(path = 'Probe J/sensor_3_sample_22.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_23 = read_csv_data(path = 'Probe J/sensor_3_sample_23.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_24 = read_csv_data(path = 'Probe J/sensor_3_sample_24.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_25 = read_csv_data(path = 'Probe J/sensor_3_sample_25.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_26 = read_csv_data(path = 'Probe J/sensor_3_sample_26.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_27 = read_csv_data(path = 'Probe J/sensor_3_sample_27.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_28 = read_csv_data(path = 'Probe J/sensor_3_sample_28.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_29 = read_csv_data(path = 'Probe J/sensor_3_sample_29.csv', range_I = S2_2_range)
    _, J_S2_2_I_sample_30 = read_csv_data(path = 'Probe J/sensor_3_sample_30.csv', range_I = S2_2_range)



# combine sample intensity into one matrix
J_S2_2_I = [J_S2_2_I_sample_01,
            J_S2_2_I_sample_02,
            J_S2_2_I_sample_03,
            J_S2_2_I_sample_04,
            J_S2_2_I_sample_05,
            J_S2_2_I_sample_06,
            J_S2_2_I_sample_07,
            J_S2_2_I_sample_08,
            J_S2_2_I_sample_09,
            J_S2_2_I_sample_10,
            J_S2_2_I_sample_11,
            J_S2_2_I_sample_12,
            J_S2_2_I_sample_13,
            J_S2_2_I_sample_14,
            J_S2_2_I_sample_15,
            J_S2_2_I_sample_16,
            J_S2_2_I_sample_17,
            J_S2_2_I_sample_18,
            J_S2_2_I_sample_19,
            J_S2_2_I_sample_20,
            J_S2_2_I_sample_21,
            J_S2_2_I_sample_22,
            J_S2_2_I_sample_23,
            J_S2_2_I_sample_24,
            J_S2_2_I_sample_25,
            J_S2_2_I_sample_26,
            J_S2_2_I_sample_27,
            J_S2_2_I_sample_28,
            J_S2_2_I_sample_29,
            J_S2_2_I_sample_30]



del J_S2_2_I_sample_01, J_S2_2_I_sample_02, J_S2_2_I_sample_03, J_S2_2_I_sample_04
del J_S2_2_I_sample_05, J_S2_2_I_sample_06, J_S2_2_I_sample_07, J_S2_2_I_sample_08
del J_S2_2_I_sample_09, J_S2_2_I_sample_10, J_S2_2_I_sample_11, J_S2_2_I_sample_12
del J_S2_2_I_sample_13, J_S2_2_I_sample_14, J_S2_2_I_sample_15, J_S2_2_I_sample_16
del J_S2_2_I_sample_17, J_S2_2_I_sample_18, J_S2_2_I_sample_19, J_S2_2_I_sample_20
del J_S2_2_I_sample_21, J_S2_2_I_sample_22, J_S2_2_I_sample_23, J_S2_2_I_sample_24
del J_S2_2_I_sample_25, J_S2_2_I_sample_26, J_S2_2_I_sample_27, J_S2_2_I_sample_28
del J_S2_2_I_sample_29, J_S2_2_I_sample_30





#%% Read CSV data from sample "Probe K"
"""
######################################################################################################
# S1.4, Sensor 2, 1100 - 1350 nm
######################################################################################################
"""
### S1.4, Sensor 2, 1100 - 1350 nm
# load data for calibration
if load_data_calibration == "yes":
    K_S1_4_WL, K_S1_4_I_light_on = read_csv_data(path = 'Probe K/sensor_2_lamp_on.csv', range_I = S1_4_range)
    _, K_S1_4_I_light_off        = read_csv_data(path = 'Probe K/sensor_2_lamp_off.csv', range_I = S1_4_range)
    _, K_S1_4_I_cuvette          = read_csv_data(path = 'Probe K/sensor_2_empty_cuvette.csv', range_I = S1_4_range)
else:
    K_S1_4_WL, _                 = read_csv_data(path = 'Probe K/sensor_2_lamp_on.csv', range_I = S1_4_range)



# load sample data
if load_data_sample == "yes":
    _, K_S1_4_I_sample_01 = read_csv_data(path = 'Probe K/sensor_2_sample_01.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_02 = read_csv_data(path = 'Probe K/sensor_2_sample_02.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_03 = read_csv_data(path = 'Probe K/sensor_2_sample_03.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_04 = read_csv_data(path = 'Probe K/sensor_2_sample_04.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_05 = read_csv_data(path = 'Probe K/sensor_2_sample_05.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_06 = read_csv_data(path = 'Probe K/sensor_2_sample_06.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_07 = read_csv_data(path = 'Probe K/sensor_2_sample_07.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_08 = read_csv_data(path = 'Probe K/sensor_2_sample_08.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_09 = read_csv_data(path = 'Probe K/sensor_2_sample_09.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_10 = read_csv_data(path = 'Probe K/sensor_2_sample_10.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_11 = read_csv_data(path = 'Probe K/sensor_2_sample_11.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_12 = read_csv_data(path = 'Probe K/sensor_2_sample_12.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_13 = read_csv_data(path = 'Probe K/sensor_2_sample_13.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_14 = read_csv_data(path = 'Probe K/sensor_2_sample_14.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_15 = read_csv_data(path = 'Probe K/sensor_2_sample_15.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_16 = read_csv_data(path = 'Probe K/sensor_2_sample_16.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_17 = read_csv_data(path = 'Probe K/sensor_2_sample_17.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_18 = read_csv_data(path = 'Probe K/sensor_2_sample_18.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_19 = read_csv_data(path = 'Probe K/sensor_2_sample_19.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_20 = read_csv_data(path = 'Probe K/sensor_2_sample_20.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_21 = read_csv_data(path = 'Probe K/sensor_2_sample_21.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_22 = read_csv_data(path = 'Probe K/sensor_2_sample_22.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_23 = read_csv_data(path = 'Probe K/sensor_2_sample_23.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_24 = read_csv_data(path = 'Probe K/sensor_2_sample_24.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_25 = read_csv_data(path = 'Probe K/sensor_2_sample_25.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_26 = read_csv_data(path = 'Probe K/sensor_2_sample_26.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_27 = read_csv_data(path = 'Probe K/sensor_2_sample_27.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_28 = read_csv_data(path = 'Probe K/sensor_2_sample_28.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_29 = read_csv_data(path = 'Probe K/sensor_2_sample_29.csv', range_I = S1_4_range)
    _, K_S1_4_I_sample_30 = read_csv_data(path = 'Probe K/sensor_2_sample_30.csv', range_I = S1_4_range)



# combine sample intensity into one matrix
K_S1_4_I = [K_S1_4_I_sample_01,
            K_S1_4_I_sample_02,
            K_S1_4_I_sample_03,
            K_S1_4_I_sample_04,
            K_S1_4_I_sample_05,
            K_S1_4_I_sample_06,
            K_S1_4_I_sample_07,
            K_S1_4_I_sample_08,
            K_S1_4_I_sample_09,
            K_S1_4_I_sample_10,
            K_S1_4_I_sample_11,
            K_S1_4_I_sample_12,
            K_S1_4_I_sample_13,
            K_S1_4_I_sample_14,
            K_S1_4_I_sample_15,
            K_S1_4_I_sample_16,
            K_S1_4_I_sample_17,
            K_S1_4_I_sample_18,
            K_S1_4_I_sample_19,
            K_S1_4_I_sample_20,
            K_S1_4_I_sample_21,
            K_S1_4_I_sample_22,
            K_S1_4_I_sample_23,
            K_S1_4_I_sample_24,
            K_S1_4_I_sample_25,
            K_S1_4_I_sample_26,
            K_S1_4_I_sample_27,
            K_S1_4_I_sample_28,
            K_S1_4_I_sample_29,
            K_S1_4_I_sample_30]



del K_S1_4_I_sample_01, K_S1_4_I_sample_02, K_S1_4_I_sample_03, K_S1_4_I_sample_04
del K_S1_4_I_sample_05, K_S1_4_I_sample_06, K_S1_4_I_sample_07, K_S1_4_I_sample_08
del K_S1_4_I_sample_09, K_S1_4_I_sample_10, K_S1_4_I_sample_11, K_S1_4_I_sample_12
del K_S1_4_I_sample_13, K_S1_4_I_sample_14, K_S1_4_I_sample_15, K_S1_4_I_sample_16
del K_S1_4_I_sample_17, K_S1_4_I_sample_18, K_S1_4_I_sample_19, K_S1_4_I_sample_20
del K_S1_4_I_sample_21, K_S1_4_I_sample_22, K_S1_4_I_sample_23, K_S1_4_I_sample_24
del K_S1_4_I_sample_25, K_S1_4_I_sample_26, K_S1_4_I_sample_27, K_S1_4_I_sample_28
del K_S1_4_I_sample_29, K_S1_4_I_sample_30



"""
######################################################################################################
# S1.7, Sensor 1, 1350 - 1650 nm
######################################################################################################
"""
### S1.7, Sensor 1, 1350 - 1650 nm
# load data for calibration
if load_data_calibration == "yes":
    K_S1_7_WL, K_S1_7_I_light_on = read_csv_data(path = 'Probe K/sensor_1_lamp_on.csv', range_I = S1_7_range)
    _, K_S1_7_I_light_off        = read_csv_data(path = 'Probe K/sensor_1_lamp_off.csv', range_I = S1_7_range)
    _, K_S1_7_I_cuvette          = read_csv_data(path = 'Probe K/sensor_1_empty_cuvette.csv', range_I = S1_7_range)
else:
    K_S1_7_WL, _                 = read_csv_data(path = 'Probe K/sensor_1_lamp_on.csv', range_I = S1_7_range)



# load sample data
if load_data_sample == "yes":
    _, K_S1_7_I_sample_01 = read_csv_data(path = 'Probe K/sensor_1_sample_01.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_02 = read_csv_data(path = 'Probe K/sensor_1_sample_02.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_03 = read_csv_data(path = 'Probe K/sensor_1_sample_03.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_04 = read_csv_data(path = 'Probe K/sensor_1_sample_04.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_05 = read_csv_data(path = 'Probe K/sensor_1_sample_05.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_06 = read_csv_data(path = 'Probe K/sensor_1_sample_06.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_07 = read_csv_data(path = 'Probe K/sensor_1_sample_07.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_08 = read_csv_data(path = 'Probe K/sensor_1_sample_08.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_09 = read_csv_data(path = 'Probe K/sensor_1_sample_09.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_10 = read_csv_data(path = 'Probe K/sensor_1_sample_10.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_11 = read_csv_data(path = 'Probe K/sensor_1_sample_11.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_12 = read_csv_data(path = 'Probe K/sensor_1_sample_12.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_13 = read_csv_data(path = 'Probe K/sensor_1_sample_13.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_14 = read_csv_data(path = 'Probe K/sensor_1_sample_14.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_15 = read_csv_data(path = 'Probe K/sensor_1_sample_15.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_16 = read_csv_data(path = 'Probe K/sensor_1_sample_16.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_17 = read_csv_data(path = 'Probe K/sensor_1_sample_17.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_18 = read_csv_data(path = 'Probe K/sensor_1_sample_18.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_19 = read_csv_data(path = 'Probe K/sensor_1_sample_19.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_20 = read_csv_data(path = 'Probe K/sensor_1_sample_20.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_21 = read_csv_data(path = 'Probe K/sensor_1_sample_21.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_22 = read_csv_data(path = 'Probe K/sensor_1_sample_22.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_23 = read_csv_data(path = 'Probe K/sensor_1_sample_23.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_24 = read_csv_data(path = 'Probe K/sensor_1_sample_24.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_25 = read_csv_data(path = 'Probe K/sensor_1_sample_25.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_26 = read_csv_data(path = 'Probe K/sensor_1_sample_26.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_27 = read_csv_data(path = 'Probe K/sensor_1_sample_27.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_28 = read_csv_data(path = 'Probe K/sensor_1_sample_28.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_29 = read_csv_data(path = 'Probe K/sensor_1_sample_29.csv', range_I = S1_7_range)
    _, K_S1_7_I_sample_30 = read_csv_data(path = 'Probe K/sensor_1_sample_30.csv', range_I = S1_7_range)



# combine sample intensity into one matrix
K_S1_7_I = [K_S1_7_I_sample_01,
            K_S1_7_I_sample_02,
            K_S1_7_I_sample_03,
            K_S1_7_I_sample_04,
            K_S1_7_I_sample_05,
            K_S1_7_I_sample_06,
            K_S1_7_I_sample_07,
            K_S1_7_I_sample_08,
            K_S1_7_I_sample_09,
            K_S1_7_I_sample_10,
            K_S1_7_I_sample_11,
            K_S1_7_I_sample_12,
            K_S1_7_I_sample_13,
            K_S1_7_I_sample_14,
            K_S1_7_I_sample_15,
            K_S1_7_I_sample_16,
            K_S1_7_I_sample_17,
            K_S1_7_I_sample_18,
            K_S1_7_I_sample_19,
            K_S1_7_I_sample_20,
            K_S1_7_I_sample_21,
            K_S1_7_I_sample_22,
            K_S1_7_I_sample_23,
            K_S1_7_I_sample_24,
            K_S1_7_I_sample_25,
            K_S1_7_I_sample_26,
            K_S1_7_I_sample_27,
            K_S1_7_I_sample_28,
            K_S1_7_I_sample_29,
            K_S1_7_I_sample_30]



del K_S1_7_I_sample_01, K_S1_7_I_sample_02, K_S1_7_I_sample_03, K_S1_7_I_sample_04
del K_S1_7_I_sample_05, K_S1_7_I_sample_06, K_S1_7_I_sample_07, K_S1_7_I_sample_08
del K_S1_7_I_sample_09, K_S1_7_I_sample_10, K_S1_7_I_sample_11, K_S1_7_I_sample_12
del K_S1_7_I_sample_13, K_S1_7_I_sample_14, K_S1_7_I_sample_15, K_S1_7_I_sample_16
del K_S1_7_I_sample_17, K_S1_7_I_sample_18, K_S1_7_I_sample_19, K_S1_7_I_sample_20
del K_S1_7_I_sample_21, K_S1_7_I_sample_22, K_S1_7_I_sample_23, K_S1_7_I_sample_24
del K_S1_7_I_sample_25, K_S1_7_I_sample_26, K_S1_7_I_sample_27, K_S1_7_I_sample_28
del K_S1_7_I_sample_29, K_S1_7_I_sample_30



"""
######################################################################################################
# S2.0, Sensor 4, 1550 - 1950 nm
######################################################################################################
"""
### S2.0, Sensor 4, 1550 - 1950 nm
# load data for calibration
if load_data_calibration == "yes":
    K_S2_0_WL, K_S2_0_I_light_on = read_csv_data(path = 'Probe K/sensor_4_lamp_on.csv', range_I = S2_0_range)
    _, K_S2_0_I_light_off        = read_csv_data(path = 'Probe K/sensor_4_lamp_off.csv', range_I = S2_0_range)
    _, K_S2_0_I_cuvette          = read_csv_data(path = 'Probe K/sensor_4_empty_cuvette.csv', range_I = S2_0_range)
else:
    K_S2_0_WL, _                 = read_csv_data(path = 'Probe K/sensor_4_lamp_on.csv', range_I = S2_0_range)



# load sample data
if load_data_sample == "yes":
    _, K_S2_0_I_sample_01 = read_csv_data(path = 'Probe K/sensor_4_sample_01.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_02 = read_csv_data(path = 'Probe K/sensor_4_sample_02.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_03 = read_csv_data(path = 'Probe K/sensor_4_sample_03.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_04 = read_csv_data(path = 'Probe K/sensor_4_sample_04.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_05 = read_csv_data(path = 'Probe K/sensor_4_sample_05.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_06 = read_csv_data(path = 'Probe K/sensor_4_sample_06.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_07 = read_csv_data(path = 'Probe K/sensor_4_sample_07.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_08 = read_csv_data(path = 'Probe K/sensor_4_sample_08.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_09 = read_csv_data(path = 'Probe K/sensor_4_sample_09.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_10 = read_csv_data(path = 'Probe K/sensor_4_sample_10.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_11 = read_csv_data(path = 'Probe K/sensor_4_sample_11.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_12 = read_csv_data(path = 'Probe K/sensor_4_sample_12.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_13 = read_csv_data(path = 'Probe K/sensor_4_sample_13.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_14 = read_csv_data(path = 'Probe K/sensor_4_sample_14.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_15 = read_csv_data(path = 'Probe K/sensor_4_sample_15.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_16 = read_csv_data(path = 'Probe K/sensor_4_sample_16.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_17 = read_csv_data(path = 'Probe K/sensor_4_sample_17.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_18 = read_csv_data(path = 'Probe K/sensor_4_sample_18.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_19 = read_csv_data(path = 'Probe K/sensor_4_sample_19.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_20 = read_csv_data(path = 'Probe K/sensor_4_sample_20.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_21 = read_csv_data(path = 'Probe K/sensor_4_sample_21.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_22 = read_csv_data(path = 'Probe K/sensor_4_sample_22.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_23 = read_csv_data(path = 'Probe K/sensor_4_sample_23.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_24 = read_csv_data(path = 'Probe K/sensor_4_sample_24.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_25 = read_csv_data(path = 'Probe K/sensor_4_sample_25.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_26 = read_csv_data(path = 'Probe K/sensor_4_sample_26.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_27 = read_csv_data(path = 'Probe K/sensor_4_sample_27.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_28 = read_csv_data(path = 'Probe K/sensor_4_sample_28.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_29 = read_csv_data(path = 'Probe K/sensor_4_sample_29.csv', range_I = S2_0_range)
    _, K_S2_0_I_sample_30 = read_csv_data(path = 'Probe K/sensor_4_sample_30.csv', range_I = S2_0_range)



# combine sample intensity into one matrix
K_S2_0_I = [K_S2_0_I_sample_01,
            K_S2_0_I_sample_02,
            K_S2_0_I_sample_03,
            K_S2_0_I_sample_04,
            K_S2_0_I_sample_05,
            K_S2_0_I_sample_06,
            K_S2_0_I_sample_07,
            K_S2_0_I_sample_08,
            K_S2_0_I_sample_09,
            K_S2_0_I_sample_10,
            K_S2_0_I_sample_11,
            K_S2_0_I_sample_12,
            K_S2_0_I_sample_13,
            K_S2_0_I_sample_14,
            K_S2_0_I_sample_15,
            K_S2_0_I_sample_16,
            K_S2_0_I_sample_17,
            K_S2_0_I_sample_18,
            K_S2_0_I_sample_19,
            K_S2_0_I_sample_20,
            K_S2_0_I_sample_21,
            K_S2_0_I_sample_22,
            K_S2_0_I_sample_23,
            K_S2_0_I_sample_24,
            K_S2_0_I_sample_25,
            K_S2_0_I_sample_26,
            K_S2_0_I_sample_27,
            K_S2_0_I_sample_28,
            K_S2_0_I_sample_29,
            K_S2_0_I_sample_30]



del K_S2_0_I_sample_01, K_S2_0_I_sample_02, K_S2_0_I_sample_03, K_S2_0_I_sample_04
del K_S2_0_I_sample_05, K_S2_0_I_sample_06, K_S2_0_I_sample_07, K_S2_0_I_sample_08
del K_S2_0_I_sample_09, K_S2_0_I_sample_10, K_S2_0_I_sample_11, K_S2_0_I_sample_12
del K_S2_0_I_sample_13, K_S2_0_I_sample_14, K_S2_0_I_sample_15, K_S2_0_I_sample_16
del K_S2_0_I_sample_17, K_S2_0_I_sample_18, K_S2_0_I_sample_19, K_S2_0_I_sample_20
del K_S2_0_I_sample_21, K_S2_0_I_sample_22, K_S2_0_I_sample_23, K_S2_0_I_sample_24
del K_S2_0_I_sample_25, K_S2_0_I_sample_26, K_S2_0_I_sample_27, K_S2_0_I_sample_28
del K_S2_0_I_sample_29, K_S2_0_I_sample_30



"""
######################################################################################################
# S2.2, Sensor 3, 1750 - 2150 nm
######################################################################################################
"""
### S2.2, Sensor 3, 1750 - 2150 nm
# load data for calibration
if load_data_calibration == "yes":
    K_S2_2_WL, K_S2_2_I_light_on = read_csv_data(path = 'Probe K/sensor_3_lamp_on.csv', range_I = S2_2_range)
    _, K_S2_2_I_light_off        = read_csv_data(path = 'Probe K/sensor_3_lamp_off.csv', range_I = S2_2_range)
    _, K_S2_2_I_cuvette          = read_csv_data(path = 'Probe K/sensor_3_empty_cuvette.csv', range_I = S2_2_range)
else:
    K_S2_2_WL, _                 = read_csv_data(path = 'Probe K/sensor_3_lamp_on.csv', range_I = S2_2_range)



# load sample data
if load_data_sample == "yes":
    _, K_S2_2_I_sample_01 = read_csv_data(path = 'Probe K/sensor_3_sample_01.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_02 = read_csv_data(path = 'Probe K/sensor_3_sample_02.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_03 = read_csv_data(path = 'Probe K/sensor_3_sample_03.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_04 = read_csv_data(path = 'Probe K/sensor_3_sample_04.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_05 = read_csv_data(path = 'Probe K/sensor_3_sample_05.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_06 = read_csv_data(path = 'Probe K/sensor_3_sample_06.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_07 = read_csv_data(path = 'Probe K/sensor_3_sample_07.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_08 = read_csv_data(path = 'Probe K/sensor_3_sample_08.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_09 = read_csv_data(path = 'Probe K/sensor_3_sample_09.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_10 = read_csv_data(path = 'Probe K/sensor_3_sample_10.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_11 = read_csv_data(path = 'Probe K/sensor_3_sample_11.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_12 = read_csv_data(path = 'Probe K/sensor_3_sample_12.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_13 = read_csv_data(path = 'Probe K/sensor_3_sample_13.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_14 = read_csv_data(path = 'Probe K/sensor_3_sample_14.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_15 = read_csv_data(path = 'Probe K/sensor_3_sample_15.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_16 = read_csv_data(path = 'Probe K/sensor_3_sample_16.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_17 = read_csv_data(path = 'Probe K/sensor_3_sample_17.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_18 = read_csv_data(path = 'Probe K/sensor_3_sample_18.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_19 = read_csv_data(path = 'Probe K/sensor_3_sample_19.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_20 = read_csv_data(path = 'Probe K/sensor_3_sample_20.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_21 = read_csv_data(path = 'Probe K/sensor_3_sample_21.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_22 = read_csv_data(path = 'Probe K/sensor_3_sample_22.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_23 = read_csv_data(path = 'Probe K/sensor_3_sample_23.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_24 = read_csv_data(path = 'Probe K/sensor_3_sample_24.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_25 = read_csv_data(path = 'Probe K/sensor_3_sample_25.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_26 = read_csv_data(path = 'Probe K/sensor_3_sample_26.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_27 = read_csv_data(path = 'Probe K/sensor_3_sample_27.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_28 = read_csv_data(path = 'Probe K/sensor_3_sample_28.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_29 = read_csv_data(path = 'Probe K/sensor_3_sample_29.csv', range_I = S2_2_range)
    _, K_S2_2_I_sample_30 = read_csv_data(path = 'Probe K/sensor_3_sample_30.csv', range_I = S2_2_range)



# combine sample intensity into one matrix
K_S2_2_I = [K_S2_2_I_sample_01,
            K_S2_2_I_sample_02,
            K_S2_2_I_sample_03,
            K_S2_2_I_sample_04,
            K_S2_2_I_sample_05,
            K_S2_2_I_sample_06,
            K_S2_2_I_sample_07,
            K_S2_2_I_sample_08,
            K_S2_2_I_sample_09,
            K_S2_2_I_sample_10,
            K_S2_2_I_sample_11,
            K_S2_2_I_sample_12,
            K_S2_2_I_sample_13,
            K_S2_2_I_sample_14,
            K_S2_2_I_sample_15,
            K_S2_2_I_sample_16,
            K_S2_2_I_sample_17,
            K_S2_2_I_sample_18,
            K_S2_2_I_sample_19,
            K_S2_2_I_sample_20,
            K_S2_2_I_sample_21,
            K_S2_2_I_sample_22,
            K_S2_2_I_sample_23,
            K_S2_2_I_sample_24,
            K_S2_2_I_sample_25,
            K_S2_2_I_sample_26,
            K_S2_2_I_sample_27,
            K_S2_2_I_sample_28,
            K_S2_2_I_sample_29,
            K_S2_2_I_sample_30]



del K_S2_2_I_sample_01, K_S2_2_I_sample_02, K_S2_2_I_sample_03, K_S2_2_I_sample_04
del K_S2_2_I_sample_05, K_S2_2_I_sample_06, K_S2_2_I_sample_07, K_S2_2_I_sample_08
del K_S2_2_I_sample_09, K_S2_2_I_sample_10, K_S2_2_I_sample_11, K_S2_2_I_sample_12
del K_S2_2_I_sample_13, K_S2_2_I_sample_14, K_S2_2_I_sample_15, K_S2_2_I_sample_16
del K_S2_2_I_sample_17, K_S2_2_I_sample_18, K_S2_2_I_sample_19, K_S2_2_I_sample_20
del K_S2_2_I_sample_21, K_S2_2_I_sample_22, K_S2_2_I_sample_23, K_S2_2_I_sample_24
del K_S2_2_I_sample_25, K_S2_2_I_sample_26, K_S2_2_I_sample_27, K_S2_2_I_sample_28
del K_S2_2_I_sample_29, K_S2_2_I_sample_30





#%% Read CSV data from sample "Probe A"
"""
######################################################################################################
# S1.4, Sensor 2, 1100 - 1350 nm
######################################################################################################
"""
### S1.4, Sensor 2, 1100 - 1350 nm
# load data for calibration
if load_data_calibration == "yes":
    A_S1_4_WL, A_S1_4_I_light_on = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_lamp_on.csv', range_I = S1_4_range)
    _, A_S1_4_I_light_off        = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_lamp_off.csv', range_I = S1_4_range)
    _, A_S1_4_I_cuvette          = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_empty_cuvette.csv', range_I = S1_4_range)
else:
    A_S1_4_WL, _                 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_lamp_on.csv', range_I = S1_4_range)



# load sample data
if load_data_sample == "yes":
    _, A_S1_4_I_sample_01 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_01.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_02 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_02.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_03 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_03.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_04 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_04.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_05 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_05.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_06 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_06.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_07 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_07.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_08 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_08.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_09 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_09.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_10 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_10.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_11 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_11.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_12 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_12.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_13 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_13.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_14 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_14.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_15 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_15.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_16 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_16.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_17 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_17.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_18 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_18.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_19 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_19.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_20 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_20.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_21 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_21.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_22 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_22.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_23 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_23.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_24 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_24.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_25 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_25.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_26 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_26.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_27 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_27.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_28 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_28.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_29 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_29.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_30 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_30.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_31 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_31.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_32 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_32.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_33 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_33.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_34 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_34.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_35 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_35.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_36 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_36.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_37 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_37.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_38 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_38.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_39 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_39.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_40 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_40.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_41 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_41.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_42 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_42.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_43 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_43.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_44 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_44.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_45 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_45.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_46 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_46.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_47 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_47.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_48 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_48.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_49 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_49.csv', range_I = S1_4_range)
    _, A_S1_4_I_sample_50 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_2_sample_50.csv', range_I = S1_4_range)


# combine sample intensity into one matrix
A_S1_4_I = [A_S1_4_I_sample_01,
            A_S1_4_I_sample_02,
            A_S1_4_I_sample_03,
            A_S1_4_I_sample_04,
            A_S1_4_I_sample_05,
            A_S1_4_I_sample_06,
            A_S1_4_I_sample_07,
            A_S1_4_I_sample_08,
            A_S1_4_I_sample_09,
            A_S1_4_I_sample_10,
            A_S1_4_I_sample_11,
            A_S1_4_I_sample_12,
            A_S1_4_I_sample_13,
            A_S1_4_I_sample_14,
            A_S1_4_I_sample_15,
            A_S1_4_I_sample_16,
            A_S1_4_I_sample_17,
            A_S1_4_I_sample_18,
            A_S1_4_I_sample_19,
            A_S1_4_I_sample_20,
            A_S1_4_I_sample_21,
            A_S1_4_I_sample_22,
            A_S1_4_I_sample_23,
            A_S1_4_I_sample_24,
            A_S1_4_I_sample_25,
            A_S1_4_I_sample_26,
            A_S1_4_I_sample_27,
            A_S1_4_I_sample_28,
            A_S1_4_I_sample_29,
            A_S1_4_I_sample_30,
            A_S1_4_I_sample_31,
            A_S1_4_I_sample_32,
            A_S1_4_I_sample_33,
            A_S1_4_I_sample_34,
            A_S1_4_I_sample_35,
            A_S1_4_I_sample_36,
            A_S1_4_I_sample_37,
            A_S1_4_I_sample_38,
            A_S1_4_I_sample_39,
            A_S1_4_I_sample_40,
            A_S1_4_I_sample_41,
            A_S1_4_I_sample_42,
            A_S1_4_I_sample_43,
            A_S1_4_I_sample_44,
            A_S1_4_I_sample_45,
            A_S1_4_I_sample_46,
            A_S1_4_I_sample_47,
            A_S1_4_I_sample_48,
            A_S1_4_I_sample_49,
            A_S1_4_I_sample_50]


if del_var == "yes":
    del A_S1_4_I_sample_01, A_S1_4_I_sample_02, A_S1_4_I_sample_03, A_S1_4_I_sample_04, A_S1_4_I_sample_05
    del A_S1_4_I_sample_06, A_S1_4_I_sample_07, A_S1_4_I_sample_08, A_S1_4_I_sample_09, A_S1_4_I_sample_10
    del A_S1_4_I_sample_11, A_S1_4_I_sample_12, A_S1_4_I_sample_13, A_S1_4_I_sample_14, A_S1_4_I_sample_15
    del A_S1_4_I_sample_16, A_S1_4_I_sample_17, A_S1_4_I_sample_18, A_S1_4_I_sample_19, A_S1_4_I_sample_20
    del A_S1_4_I_sample_21, A_S1_4_I_sample_22, A_S1_4_I_sample_23, A_S1_4_I_sample_24, A_S1_4_I_sample_25
    del A_S1_4_I_sample_26, A_S1_4_I_sample_27, A_S1_4_I_sample_28, A_S1_4_I_sample_29, A_S1_4_I_sample_30
    del A_S1_4_I_sample_31, A_S1_4_I_sample_32, A_S1_4_I_sample_33, A_S1_4_I_sample_34, A_S1_4_I_sample_35
    del A_S1_4_I_sample_36, A_S1_4_I_sample_37, A_S1_4_I_sample_38, A_S1_4_I_sample_39, A_S1_4_I_sample_40
    del A_S1_4_I_sample_41, A_S1_4_I_sample_42, A_S1_4_I_sample_43, A_S1_4_I_sample_44, A_S1_4_I_sample_45
    del A_S1_4_I_sample_46, A_S1_4_I_sample_47, A_S1_4_I_sample_48, A_S1_4_I_sample_49, A_S1_4_I_sample_50



"""
######################################################################################################
# S1.7, Sensor 1, 1350 - 1650 nm
######################################################################################################
"""
### S1.7, Sensor 1, 1350 - 1650 nm
# load data for calibration
if load_data_calibration == "yes":
    A_S1_7_WL, A_S1_7_I_light_on = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_lamp_on.csv', range_I = S1_7_range)
    _, A_S1_7_I_light_off        = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_lamp_off.csv', range_I = S1_7_range)
    _, A_S1_7_I_cuvette          = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_empty_cuvette.csv', range_I = S1_7_range)
else:
    A_S1_7_WL, _                 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_lamp_on.csv', range_I = S1_7_range)



# load sample data
if load_data_sample == "yes":
    _, A_S1_7_I_sample_01 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_01.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_02 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_02.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_03 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_03.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_04 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_04.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_05 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_05.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_06 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_06.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_07 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_07.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_08 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_08.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_09 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_09.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_10 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_10.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_11 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_11.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_12 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_12.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_13 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_13.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_14 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_14.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_15 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_15.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_16 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_16.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_17 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_17.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_18 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_18.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_19 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_19.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_20 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_20.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_21 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_21.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_22 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_22.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_23 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_23.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_24 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_24.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_25 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_25.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_26 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_26.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_27 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_27.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_28 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_28.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_29 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_29.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_30 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_30.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_31 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_31.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_32 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_32.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_33 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_33.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_34 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_34.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_35 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_35.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_36 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_36.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_37 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_37.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_38 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_38.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_39 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_39.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_40 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_40.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_41 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_41.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_42 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_42.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_43 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_43.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_44 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_44.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_45 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_45.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_46 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_46.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_47 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_47.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_48 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_48.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_49 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_49.csv', range_I = S1_7_range)
    _, A_S1_7_I_sample_50 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_1_sample_50.csv', range_I = S1_7_range)

# combine sample intensity into one matrix
A_S1_7_I = [A_S1_7_I_sample_01,
            A_S1_7_I_sample_02,
            A_S1_7_I_sample_03,
            A_S1_7_I_sample_04,
            A_S1_7_I_sample_05,
            A_S1_7_I_sample_06,
            A_S1_7_I_sample_07,
            A_S1_7_I_sample_08,
            A_S1_7_I_sample_09,
            A_S1_7_I_sample_10,
            A_S1_7_I_sample_11,
            A_S1_7_I_sample_12,
            A_S1_7_I_sample_13,
            A_S1_7_I_sample_14,
            A_S1_7_I_sample_15,
            A_S1_7_I_sample_16,
            A_S1_7_I_sample_17,
            A_S1_7_I_sample_18,
            A_S1_7_I_sample_19,
            A_S1_7_I_sample_20,
            A_S1_7_I_sample_21,
            A_S1_7_I_sample_22,
            A_S1_7_I_sample_23,
            A_S1_7_I_sample_24,
            A_S1_7_I_sample_25,
            A_S1_7_I_sample_26,
            A_S1_7_I_sample_27,
            A_S1_7_I_sample_28,
            A_S1_7_I_sample_29,
            A_S1_7_I_sample_30,
            A_S1_7_I_sample_31,
            A_S1_7_I_sample_32,
            A_S1_7_I_sample_33,
            A_S1_7_I_sample_34,
            A_S1_7_I_sample_35,
            A_S1_7_I_sample_36,
            A_S1_7_I_sample_37,
            A_S1_7_I_sample_38,
            A_S1_7_I_sample_39,
            A_S1_7_I_sample_40,
            A_S1_7_I_sample_41,
            A_S1_7_I_sample_42,
            A_S1_7_I_sample_43,
            A_S1_7_I_sample_44,
            A_S1_7_I_sample_45,
            A_S1_7_I_sample_46,
            A_S1_7_I_sample_47,
            A_S1_7_I_sample_48,
            A_S1_7_I_sample_49,
            A_S1_7_I_sample_50]



if del_var == "yes":
    del A_S1_7_I_sample_01, A_S1_7_I_sample_02, A_S1_7_I_sample_03, A_S1_7_I_sample_04, A_S1_7_I_sample_05
    del A_S1_7_I_sample_06, A_S1_7_I_sample_07, A_S1_7_I_sample_08, A_S1_7_I_sample_09, A_S1_7_I_sample_10
    del A_S1_7_I_sample_11, A_S1_7_I_sample_12, A_S1_7_I_sample_13, A_S1_7_I_sample_14, A_S1_7_I_sample_15
    del A_S1_7_I_sample_16, A_S1_7_I_sample_17, A_S1_7_I_sample_18, A_S1_7_I_sample_19, A_S1_7_I_sample_20
    del A_S1_7_I_sample_21, A_S1_7_I_sample_22, A_S1_7_I_sample_23, A_S1_7_I_sample_24, A_S1_7_I_sample_25
    del A_S1_7_I_sample_26, A_S1_7_I_sample_27, A_S1_7_I_sample_28, A_S1_7_I_sample_29, A_S1_7_I_sample_30
    del A_S1_7_I_sample_31, A_S1_7_I_sample_32, A_S1_7_I_sample_33, A_S1_7_I_sample_34, A_S1_7_I_sample_35
    del A_S1_7_I_sample_36, A_S1_7_I_sample_37, A_S1_7_I_sample_38, A_S1_7_I_sample_39, A_S1_7_I_sample_40
    del A_S1_7_I_sample_41, A_S1_7_I_sample_42, A_S1_7_I_sample_43, A_S1_7_I_sample_44, A_S1_7_I_sample_45
    del A_S1_7_I_sample_46, A_S1_7_I_sample_47, A_S1_7_I_sample_48, A_S1_7_I_sample_49, A_S1_7_I_sample_50



"""
######################################################################################################
# S2.0, Sensor 4, 1550 - 1950 nm
######################################################################################################
"""
### S2.0, Sensor 4, 1550 - 1950 nm
# load data for calibration
if load_data_calibration == "yes":
    A_S2_0_WL, A_S2_0_I_light_on = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_lamp_on.csv', range_I = S2_0_range)
    _, A_S2_0_I_light_off        = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_lamp_off.csv', range_I = S2_0_range)
    _, A_S2_0_I_cuvette          = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_empty_cuvette.csv', range_I = S2_0_range)
else:
    A_S2_0_WL, _                 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_lamp_on.csv', range_I = S2_0_range)



# load sample data
if load_data_sample == "yes":
    _, A_S2_0_I_sample_01 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_01.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_02 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_02.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_03 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_03.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_04 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_04.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_05 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_05.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_06 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_06.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_07 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_07.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_08 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_08.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_09 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_09.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_10 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_10.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_11 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_11.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_12 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_12.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_13 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_13.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_14 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_14.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_15 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_15.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_16 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_16.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_17 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_17.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_18 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_18.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_19 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_19.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_20 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_20.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_21 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_21.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_22 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_22.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_23 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_23.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_24 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_24.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_25 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_25.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_26 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_26.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_27 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_27.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_28 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_28.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_29 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_29.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_30 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_30.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_31 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_31.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_32 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_32.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_33 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_33.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_34 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_34.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_35 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_35.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_36 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_36.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_37 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_37.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_38 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_38.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_39 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_39.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_40 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_40.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_41 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_41.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_42 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_42.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_43 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_43.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_44 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_44.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_45 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_45.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_46 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_46.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_47 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_47.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_48 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_48.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_49 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_49.csv', range_I = S2_0_range)
    _, A_S2_0_I_sample_50 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_4_sample_50.csv', range_I = S2_0_range)


# combine sample intensity into one matrix
A_S2_0_I = [A_S2_0_I_sample_01,
            A_S2_0_I_sample_02,
            A_S2_0_I_sample_03,
            A_S2_0_I_sample_04,
            A_S2_0_I_sample_05,
            A_S2_0_I_sample_06,
            A_S2_0_I_sample_07,
            A_S2_0_I_sample_08,
            A_S2_0_I_sample_09,
            A_S2_0_I_sample_10,
            A_S2_0_I_sample_11,
            A_S2_0_I_sample_12,
            A_S2_0_I_sample_13,
            A_S2_0_I_sample_14,
            A_S2_0_I_sample_15,
            A_S2_0_I_sample_16,
            A_S2_0_I_sample_17,
            A_S2_0_I_sample_18,
            A_S2_0_I_sample_19,
            A_S2_0_I_sample_20,
            A_S2_0_I_sample_21,
            A_S2_0_I_sample_22,
            A_S2_0_I_sample_23,
            A_S2_0_I_sample_24,
            A_S2_0_I_sample_25,
            A_S2_0_I_sample_26,
            A_S2_0_I_sample_27,
            A_S2_0_I_sample_28,
            A_S2_0_I_sample_29,
            A_S2_0_I_sample_30,
            A_S2_0_I_sample_31,
            A_S2_0_I_sample_32,
            A_S2_0_I_sample_33,
            A_S2_0_I_sample_34,
            A_S2_0_I_sample_35,
            A_S2_0_I_sample_36,
            A_S2_0_I_sample_37,
            A_S2_0_I_sample_38,
            A_S2_0_I_sample_39,
            A_S2_0_I_sample_40,
            A_S2_0_I_sample_41,
            A_S2_0_I_sample_42,
            A_S2_0_I_sample_43,
            A_S2_0_I_sample_44,
            A_S2_0_I_sample_45,
            A_S2_0_I_sample_46,
            A_S2_0_I_sample_47,
            A_S2_0_I_sample_48,
            A_S2_0_I_sample_49,
            A_S2_0_I_sample_50]



if del_var == "yes":
    del A_S2_0_I_sample_01, A_S2_0_I_sample_02, A_S2_0_I_sample_03, A_S2_0_I_sample_04, A_S2_0_I_sample_05
    del A_S2_0_I_sample_06, A_S2_0_I_sample_07, A_S2_0_I_sample_08, A_S2_0_I_sample_09, A_S2_0_I_sample_10
    del A_S2_0_I_sample_11, A_S2_0_I_sample_12, A_S2_0_I_sample_13, A_S2_0_I_sample_14, A_S2_0_I_sample_15
    del A_S2_0_I_sample_16, A_S2_0_I_sample_17, A_S2_0_I_sample_18, A_S2_0_I_sample_19, A_S2_0_I_sample_20
    del A_S2_0_I_sample_21, A_S2_0_I_sample_22, A_S2_0_I_sample_23, A_S2_0_I_sample_24, A_S2_0_I_sample_25
    del A_S2_0_I_sample_26, A_S2_0_I_sample_27, A_S2_0_I_sample_28, A_S2_0_I_sample_29, A_S2_0_I_sample_30
    del A_S2_0_I_sample_31, A_S2_0_I_sample_32, A_S2_0_I_sample_33, A_S2_0_I_sample_34, A_S2_0_I_sample_35
    del A_S2_0_I_sample_36, A_S2_0_I_sample_37, A_S2_0_I_sample_38, A_S2_0_I_sample_39, A_S2_0_I_sample_40
    del A_S2_0_I_sample_41, A_S2_0_I_sample_42, A_S2_0_I_sample_43, A_S2_0_I_sample_44, A_S2_0_I_sample_45
    del A_S2_0_I_sample_46, A_S2_0_I_sample_47, A_S2_0_I_sample_48, A_S2_0_I_sample_49, A_S2_0_I_sample_50



"""
######################################################################################################
# S2.2, Sensor 3, 1750 - 2150 nm
######################################################################################################
"""
### S2.2, Sensor 3, 1750 - 2150 nm
# load data for calibration
if load_data_calibration == "yes":
    A_S2_2_WL, A_S2_2_I_light_on = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_lamp_on.csv', range_I = S2_2_range)
    _, A_S2_2_I_light_off        = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_lamp_off.csv', range_I = S2_2_range)
    _, A_S2_2_I_cuvette          = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_empty_cuvette.csv', range_I = S2_2_range)
else:
    A_S2_2_WL, _                 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_lamp_on.csv', range_I = S2_2_range)



# load sample data
if load_data_sample == "yes":
    _, A_S2_2_I_sample_01 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_01.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_02 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_02.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_03 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_03.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_04 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_04.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_05 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_05.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_06 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_06.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_07 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_07.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_08 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_08.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_09 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_09.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_10 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_10.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_11 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_11.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_12 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_12.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_13 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_13.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_14 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_14.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_15 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_15.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_16 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_16.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_17 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_17.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_18 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_18.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_19 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_19.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_20 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_20.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_21 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_21.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_22 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_22.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_23 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_23.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_24 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_24.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_25 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_25.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_26 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_26.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_27 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_27.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_28 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_28.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_29 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_29.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_30 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_30.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_31 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_31.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_32 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_32.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_33 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_33.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_34 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_34.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_35 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_35.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_36 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_36.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_37 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_37.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_38 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_38.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_39 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_39.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_40 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_40.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_41 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_41.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_42 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_42.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_43 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_43.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_44 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_44.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_45 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_45.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_46 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_46.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_47 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_47.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_48 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_48.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_49 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_49.csv', range_I = S2_2_range)
    _, A_S2_2_I_sample_50 = read_csv_data(path = 'Probe A (21.-22.06.2022)/sensor_3_sample_50.csv', range_I = S2_2_range)



# combine sample intensity into one matrix
A_S2_2_I = [A_S2_2_I_sample_01,
            A_S2_2_I_sample_02,
            A_S2_2_I_sample_03,
            A_S2_2_I_sample_04,
            A_S2_2_I_sample_05,
            A_S2_2_I_sample_06,
            A_S2_2_I_sample_07,
            A_S2_2_I_sample_08,
            A_S2_2_I_sample_09,
            A_S2_2_I_sample_10,
            A_S2_2_I_sample_11,
            A_S2_2_I_sample_12,
            A_S2_2_I_sample_13,
            A_S2_2_I_sample_14,
            A_S2_2_I_sample_15,
            A_S2_2_I_sample_16,
            A_S2_2_I_sample_17,
            A_S2_2_I_sample_18,
            A_S2_2_I_sample_19,
            A_S2_2_I_sample_20,
            A_S2_2_I_sample_21,
            A_S2_2_I_sample_22,
            A_S2_2_I_sample_23,
            A_S2_2_I_sample_24,
            A_S2_2_I_sample_25,
            A_S2_2_I_sample_26,
            A_S2_2_I_sample_27,
            A_S2_2_I_sample_28,
            A_S2_2_I_sample_29,
            A_S2_2_I_sample_30,
            A_S2_2_I_sample_31,
            A_S2_2_I_sample_32,
            A_S2_2_I_sample_33,
            A_S2_2_I_sample_34,
            A_S2_2_I_sample_35,
            A_S2_2_I_sample_36,
            A_S2_2_I_sample_37,
            A_S2_2_I_sample_38,
            A_S2_2_I_sample_39,
            A_S2_2_I_sample_40,
            A_S2_2_I_sample_41,
            A_S2_2_I_sample_42,
            A_S2_2_I_sample_43,
            A_S2_2_I_sample_44,
            A_S2_2_I_sample_45,
            A_S2_2_I_sample_46,
            A_S2_2_I_sample_47,
            A_S2_2_I_sample_48,
            A_S2_2_I_sample_49,
            A_S2_2_I_sample_50]



if del_var == "yes":
    del A_S2_2_I_sample_01, A_S2_2_I_sample_02, A_S2_2_I_sample_03, A_S2_2_I_sample_04, A_S2_2_I_sample_05
    del A_S2_2_I_sample_06, A_S2_2_I_sample_07, A_S2_2_I_sample_08, A_S2_2_I_sample_09, A_S2_2_I_sample_10
    del A_S2_2_I_sample_11, A_S2_2_I_sample_12, A_S2_2_I_sample_13, A_S2_2_I_sample_14, A_S2_2_I_sample_15
    del A_S2_2_I_sample_16, A_S2_2_I_sample_17, A_S2_2_I_sample_18, A_S2_2_I_sample_19, A_S2_2_I_sample_20
    del A_S2_2_I_sample_21, A_S2_2_I_sample_22, A_S2_2_I_sample_23, A_S2_2_I_sample_24, A_S2_2_I_sample_25
    del A_S2_2_I_sample_26, A_S2_2_I_sample_27, A_S2_2_I_sample_28, A_S2_2_I_sample_29, A_S2_2_I_sample_30
    del A_S2_2_I_sample_31, A_S2_2_I_sample_32, A_S2_2_I_sample_33, A_S2_2_I_sample_34, A_S2_2_I_sample_35
    del A_S2_2_I_sample_36, A_S2_2_I_sample_37, A_S2_2_I_sample_38, A_S2_2_I_sample_39, A_S2_2_I_sample_40
    del A_S2_2_I_sample_41, A_S2_2_I_sample_42, A_S2_2_I_sample_43, A_S2_2_I_sample_44, A_S2_2_I_sample_45
    del A_S2_2_I_sample_46, A_S2_2_I_sample_47, A_S2_2_I_sample_48, A_S2_2_I_sample_49, A_S2_2_I_sample_50





#%% Read CSV data from sample "Probe B"
"""
######################################################################################################
# S1.4, Sensor 2, 1100 - 1350 nm
######################################################################################################
"""
### S1.4, Sensor 2, 1100 - 1350 nm
# load data for calibration
if load_data_calibration == "yes":
    B_S1_4_WL, B_S1_4_I_light_on = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_lamp_on.csv', range_I = S1_4_range)
    _, B_S1_4_I_light_off        = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_lamp_off.csv', range_I = S1_4_range)
    _, B_S1_4_I_cuvette          = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_empty_cuvette.csv', range_I = S1_4_range)
else:
    B_S1_4_WL, _                 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_lamp_on.csv', range_I = S1_4_range)



# load sample data
if load_data_sample == "yes":
    _, B_S1_4_I_sample_01 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_01.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_02 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_02.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_03 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_03.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_04 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_04.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_05 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_05.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_06 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_06.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_07 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_07.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_08 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_08.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_09 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_09.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_10 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_10.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_11 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_11.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_12 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_12.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_13 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_13.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_14 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_14.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_15 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_15.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_16 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_16.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_17 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_17.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_18 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_18.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_19 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_19.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_20 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_20.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_21 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_21.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_22 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_22.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_23 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_23.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_24 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_24.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_25 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_25.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_26 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_26.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_27 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_27.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_28 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_28.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_29 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_29.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_30 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_30.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_31 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_31.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_32 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_32.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_33 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_33.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_34 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_34.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_35 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_35.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_36 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_36.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_37 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_37.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_38 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_38.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_39 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_39.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_40 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_40.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_41 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_41.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_42 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_42.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_43 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_43.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_44 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_44.csv', range_I = S1_4_range)
    _, B_S1_4_I_sample_45 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_2_sample_45.csv', range_I = S1_4_range)



# combine sample intensity into one matrix
B_S1_4_I = [B_S1_4_I_sample_01,
            B_S1_4_I_sample_02,
            B_S1_4_I_sample_03,
            B_S1_4_I_sample_04,
            B_S1_4_I_sample_05,
            B_S1_4_I_sample_06,
            B_S1_4_I_sample_07,
            B_S1_4_I_sample_08,
            B_S1_4_I_sample_09,
            B_S1_4_I_sample_10,
            B_S1_4_I_sample_11,
            B_S1_4_I_sample_12,
            B_S1_4_I_sample_13,
            B_S1_4_I_sample_14,
            B_S1_4_I_sample_15,
            B_S1_4_I_sample_16,
            B_S1_4_I_sample_17,
            B_S1_4_I_sample_18,
            B_S1_4_I_sample_19,
            B_S1_4_I_sample_20,
            B_S1_4_I_sample_21,
            B_S1_4_I_sample_22,
            B_S1_4_I_sample_23,
            B_S1_4_I_sample_24,
            B_S1_4_I_sample_25,
            B_S1_4_I_sample_26,
            B_S1_4_I_sample_27,
            B_S1_4_I_sample_28,
            B_S1_4_I_sample_29,
            B_S1_4_I_sample_30,
            B_S1_4_I_sample_31,
            B_S1_4_I_sample_32,
            B_S1_4_I_sample_33,
            B_S1_4_I_sample_34,
            B_S1_4_I_sample_35,
            B_S1_4_I_sample_36,
            B_S1_4_I_sample_37,
            B_S1_4_I_sample_38,
            B_S1_4_I_sample_39,
            B_S1_4_I_sample_40,
            B_S1_4_I_sample_41,
            B_S1_4_I_sample_42,
            B_S1_4_I_sample_43,
            B_S1_4_I_sample_44,
            B_S1_4_I_sample_45]


if del_var == "yes":
    del B_S1_4_I_sample_01, B_S1_4_I_sample_02, B_S1_4_I_sample_03, B_S1_4_I_sample_04, B_S1_4_I_sample_05
    del B_S1_4_I_sample_06, B_S1_4_I_sample_07, B_S1_4_I_sample_08, B_S1_4_I_sample_09, B_S1_4_I_sample_10
    del B_S1_4_I_sample_11, B_S1_4_I_sample_12, B_S1_4_I_sample_13, B_S1_4_I_sample_14, B_S1_4_I_sample_15
    del B_S1_4_I_sample_16, B_S1_4_I_sample_17, B_S1_4_I_sample_18, B_S1_4_I_sample_19, B_S1_4_I_sample_20
    del B_S1_4_I_sample_21, B_S1_4_I_sample_22, B_S1_4_I_sample_23, B_S1_4_I_sample_24, B_S1_4_I_sample_25
    del B_S1_4_I_sample_26, B_S1_4_I_sample_27, B_S1_4_I_sample_28, B_S1_4_I_sample_29, B_S1_4_I_sample_30
    del B_S1_4_I_sample_31, B_S1_4_I_sample_32, B_S1_4_I_sample_33, B_S1_4_I_sample_34, B_S1_4_I_sample_35
    del B_S1_4_I_sample_36, B_S1_4_I_sample_37, B_S1_4_I_sample_38, B_S1_4_I_sample_39, B_S1_4_I_sample_40
    del B_S1_4_I_sample_41, B_S1_4_I_sample_42, B_S1_4_I_sample_43, B_S1_4_I_sample_44, B_S1_4_I_sample_45



"""
######################################################################################################
# S1.7, Sensor 1, 1350 - 1650 nm
######################################################################################################
"""
### S1.7, Sensor 1, 1350 - 1650 nm
# load data for calibration
if load_data_calibration == "yes":
    B_S1_7_WL, B_S1_7_I_light_on = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_lamp_on.csv', range_I = S1_7_range)
    _, B_S1_7_I_light_off        = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_lamp_off.csv', range_I = S1_7_range)
    _, B_S1_7_I_cuvette          = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_empty_cuvette.csv', range_I = S1_7_range)
else:
    B_S1_7_WL, _                 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_lamp_on.csv', range_I = S1_7_range)



# load sample data
if load_data_sample == "yes":
    _, B_S1_7_I_sample_01 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_01.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_02 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_02.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_03 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_03.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_04 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_04.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_05 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_05.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_06 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_06.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_07 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_07.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_08 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_08.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_09 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_09.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_10 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_10.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_11 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_11.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_12 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_12.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_13 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_13.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_14 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_14.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_15 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_15.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_16 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_16.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_17 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_17.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_18 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_18.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_19 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_19.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_20 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_20.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_21 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_21.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_22 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_22.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_23 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_23.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_24 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_24.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_25 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_25.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_26 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_26.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_27 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_27.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_28 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_28.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_29 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_29.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_30 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_30.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_31 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_31.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_32 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_32.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_33 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_33.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_34 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_34.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_35 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_35.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_36 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_36.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_37 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_37.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_38 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_38.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_39 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_39.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_40 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_40.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_41 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_41.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_42 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_42.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_43 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_43.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_44 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_44.csv', range_I = S1_7_range)
    _, B_S1_7_I_sample_45 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_1_sample_45.csv', range_I = S1_7_range)




# combine sample intensity into one matrix
B_S1_7_I = [B_S1_7_I_sample_01,
            B_S1_7_I_sample_02,
            B_S1_7_I_sample_03,
            B_S1_7_I_sample_04,
            B_S1_7_I_sample_05,
            B_S1_7_I_sample_06,
            B_S1_7_I_sample_07,
            B_S1_7_I_sample_08,
            B_S1_7_I_sample_09,
            B_S1_7_I_sample_10,
            B_S1_7_I_sample_11,
            B_S1_7_I_sample_12,
            B_S1_7_I_sample_13,
            B_S1_7_I_sample_14,
            B_S1_7_I_sample_15,
            B_S1_7_I_sample_16,
            B_S1_7_I_sample_17,
            B_S1_7_I_sample_18,
            B_S1_7_I_sample_19,
            B_S1_7_I_sample_20,
            B_S1_7_I_sample_21,
            B_S1_7_I_sample_22,
            B_S1_7_I_sample_23,
            B_S1_7_I_sample_24,
            B_S1_7_I_sample_25,
            B_S1_7_I_sample_26,
            B_S1_7_I_sample_27,
            B_S1_7_I_sample_28,
            B_S1_7_I_sample_29,
            B_S1_7_I_sample_30,
            B_S1_7_I_sample_31,
            B_S1_7_I_sample_32,
            B_S1_7_I_sample_33,
            B_S1_7_I_sample_34,
            B_S1_7_I_sample_35,
            B_S1_7_I_sample_36,
            B_S1_7_I_sample_37,
            B_S1_7_I_sample_38,
            B_S1_7_I_sample_39,
            B_S1_7_I_sample_40,
            B_S1_7_I_sample_41,
            B_S1_7_I_sample_42,
            B_S1_7_I_sample_43,
            B_S1_7_I_sample_44,
            B_S1_7_I_sample_45]



if del_var == "yes":
    del B_S1_7_I_sample_01, B_S1_7_I_sample_02, B_S1_7_I_sample_03, B_S1_7_I_sample_04, B_S1_7_I_sample_05
    del B_S1_7_I_sample_06, B_S1_7_I_sample_07, B_S1_7_I_sample_08, B_S1_7_I_sample_09, B_S1_7_I_sample_10
    del B_S1_7_I_sample_11, B_S1_7_I_sample_12, B_S1_7_I_sample_13, B_S1_7_I_sample_14, B_S1_7_I_sample_15
    del B_S1_7_I_sample_16, B_S1_7_I_sample_17, B_S1_7_I_sample_18, B_S1_7_I_sample_19, B_S1_7_I_sample_20
    del B_S1_7_I_sample_21, B_S1_7_I_sample_22, B_S1_7_I_sample_23, B_S1_7_I_sample_24, B_S1_7_I_sample_25
    del B_S1_7_I_sample_26, B_S1_7_I_sample_27, B_S1_7_I_sample_28, B_S1_7_I_sample_29, B_S1_7_I_sample_30
    del B_S1_7_I_sample_31, B_S1_7_I_sample_32, B_S1_7_I_sample_33, B_S1_7_I_sample_34, B_S1_7_I_sample_35
    del B_S1_7_I_sample_36, B_S1_7_I_sample_37, B_S1_7_I_sample_38, B_S1_7_I_sample_39, B_S1_7_I_sample_40
    del B_S1_7_I_sample_41, B_S1_7_I_sample_42, B_S1_7_I_sample_43, B_S1_7_I_sample_44, B_S1_7_I_sample_45



"""
######################################################################################################
# S2.0, Sensor 4, 1550 - 1950 nm
######################################################################################################
"""
### S2.0, Sensor 4, 1550 - 1950 nm
# load data for calibration
if load_data_calibration == "yes":
    B_S2_0_WL, B_S2_0_I_light_on = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_lamp_on.csv', range_I = S2_0_range)
    _, B_S2_0_I_light_off        = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_lamp_off.csv', range_I = S2_0_range)
    _, B_S2_0_I_cuvette          = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_empty_cuvette.csv', range_I = S2_0_range)
else:
    B_S2_0_WL, _                 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_lamp_on.csv', range_I = S2_0_range)



# load sample data
if load_data_sample == "yes":
    _, B_S2_0_I_sample_01 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_01.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_02 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_02.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_03 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_03.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_04 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_04.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_05 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_05.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_06 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_06.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_07 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_07.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_08 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_08.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_09 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_09.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_10 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_10.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_11 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_11.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_12 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_12.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_13 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_13.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_14 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_14.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_15 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_15.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_16 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_16.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_17 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_17.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_18 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_18.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_19 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_19.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_20 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_20.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_21 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_21.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_22 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_22.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_23 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_23.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_24 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_24.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_25 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_25.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_26 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_26.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_27 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_27.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_28 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_28.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_29 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_29.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_30 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_30.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_31 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_31.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_32 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_32.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_33 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_33.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_34 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_34.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_35 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_35.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_36 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_36.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_37 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_37.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_38 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_38.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_39 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_39.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_40 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_40.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_41 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_41.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_42 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_42.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_43 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_43.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_44 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_44.csv', range_I = S2_0_range)
    _, B_S2_0_I_sample_45 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_4_sample_45.csv', range_I = S2_0_range)




# combine sample intensity into one matrix
B_S2_0_I = [B_S2_0_I_sample_01,
            B_S2_0_I_sample_02,
            B_S2_0_I_sample_03,
            B_S2_0_I_sample_04,
            B_S2_0_I_sample_05,
            B_S2_0_I_sample_06,
            B_S2_0_I_sample_07,
            B_S2_0_I_sample_08,
            B_S2_0_I_sample_09,
            B_S2_0_I_sample_10,
            B_S2_0_I_sample_11,
            B_S2_0_I_sample_12,
            B_S2_0_I_sample_13,
            B_S2_0_I_sample_14,
            B_S2_0_I_sample_15,
            B_S2_0_I_sample_16,
            B_S2_0_I_sample_17,
            B_S2_0_I_sample_18,
            B_S2_0_I_sample_19,
            B_S2_0_I_sample_20,
            B_S2_0_I_sample_21,
            B_S2_0_I_sample_22,
            B_S2_0_I_sample_23,
            B_S2_0_I_sample_24,
            B_S2_0_I_sample_25,
            B_S2_0_I_sample_26,
            B_S2_0_I_sample_27,
            B_S2_0_I_sample_28,
            B_S2_0_I_sample_29,
            B_S2_0_I_sample_30,
            B_S2_0_I_sample_31,
            B_S2_0_I_sample_32,
            B_S2_0_I_sample_33,
            B_S2_0_I_sample_34,
            B_S2_0_I_sample_35,
            B_S2_0_I_sample_36,
            B_S2_0_I_sample_37,
            B_S2_0_I_sample_38,
            B_S2_0_I_sample_39,
            B_S2_0_I_sample_40,
            B_S2_0_I_sample_41,
            B_S2_0_I_sample_42,
            B_S2_0_I_sample_43,
            B_S2_0_I_sample_44,
            B_S2_0_I_sample_45]



if del_var == "yes":
    del B_S2_0_I_sample_01, B_S2_0_I_sample_02, B_S2_0_I_sample_03, B_S2_0_I_sample_04, B_S2_0_I_sample_05
    del B_S2_0_I_sample_06, B_S2_0_I_sample_07, B_S2_0_I_sample_08, B_S2_0_I_sample_09, B_S2_0_I_sample_10
    del B_S2_0_I_sample_11, B_S2_0_I_sample_12, B_S2_0_I_sample_13, B_S2_0_I_sample_14, B_S2_0_I_sample_15
    del B_S2_0_I_sample_16, B_S2_0_I_sample_17, B_S2_0_I_sample_18, B_S2_0_I_sample_19, B_S2_0_I_sample_20
    del B_S2_0_I_sample_21, B_S2_0_I_sample_22, B_S2_0_I_sample_23, B_S2_0_I_sample_24, B_S2_0_I_sample_25
    del B_S2_0_I_sample_26, B_S2_0_I_sample_27, B_S2_0_I_sample_28, B_S2_0_I_sample_29, B_S2_0_I_sample_30
    del B_S2_0_I_sample_31, B_S2_0_I_sample_32, B_S2_0_I_sample_33, B_S2_0_I_sample_34, B_S2_0_I_sample_35
    del B_S2_0_I_sample_36, B_S2_0_I_sample_37, B_S2_0_I_sample_38, B_S2_0_I_sample_39, B_S2_0_I_sample_40
    del B_S2_0_I_sample_41, B_S2_0_I_sample_42, B_S2_0_I_sample_43, B_S2_0_I_sample_44, B_S2_0_I_sample_45



"""
######################################################################################################
# S2.2, Sensor 3, 1750 - 2150 nm
######################################################################################################
"""
### S2.2, Sensor 3, 1750 - 2150 nm
# load data for calibration
if load_data_calibration == "yes":
    B_S2_2_WL, B_S2_2_I_light_on = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_lamp_on.csv', range_I = S2_2_range)
    _, B_S2_2_I_light_off        = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_lamp_off.csv', range_I = S2_2_range)
    _, B_S2_2_I_cuvette          = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_empty_cuvette.csv', range_I = S2_2_range)
else:
    B_S2_2_WL, _                 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_lamp_on.csv', range_I = S2_2_range)



# load sample data
if load_data_sample == "yes":
    _, B_S2_2_I_sample_01 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_01.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_02 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_02.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_03 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_03.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_04 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_04.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_05 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_05.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_06 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_06.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_07 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_07.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_08 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_08.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_09 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_09.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_10 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_10.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_11 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_11.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_12 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_12.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_13 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_13.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_14 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_14.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_15 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_15.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_16 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_16.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_17 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_17.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_18 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_18.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_19 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_19.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_20 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_20.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_21 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_21.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_22 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_22.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_23 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_23.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_24 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_24.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_25 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_25.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_26 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_26.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_27 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_27.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_28 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_28.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_29 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_29.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_30 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_30.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_31 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_31.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_32 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_32.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_33 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_33.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_34 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_34.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_35 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_35.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_36 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_36.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_37 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_37.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_38 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_38.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_39 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_39.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_40 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_40.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_41 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_41.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_42 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_42.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_43 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_43.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_44 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_44.csv', range_I = S2_2_range)
    _, B_S2_2_I_sample_45 = read_csv_data(path = 'Probe B(19.-20.07.2022)/sensor_3_sample_45.csv', range_I = S2_2_range)




# combine sample intensity into one matrix
B_S2_2_I = [B_S2_2_I_sample_01,
            B_S2_2_I_sample_02,
            B_S2_2_I_sample_03,
            B_S2_2_I_sample_04,
            B_S2_2_I_sample_05,
            B_S2_2_I_sample_06,
            B_S2_2_I_sample_07,
            B_S2_2_I_sample_08,
            B_S2_2_I_sample_09,
            B_S2_2_I_sample_10,
            B_S2_2_I_sample_11,
            B_S2_2_I_sample_12,
            B_S2_2_I_sample_13,
            B_S2_2_I_sample_14,
            B_S2_2_I_sample_15,
            B_S2_2_I_sample_16,
            B_S2_2_I_sample_17,
            B_S2_2_I_sample_18,
            B_S2_2_I_sample_19,
            B_S2_2_I_sample_20,
            B_S2_2_I_sample_21,
            B_S2_2_I_sample_22,
            B_S2_2_I_sample_23,
            B_S2_2_I_sample_24,
            B_S2_2_I_sample_25,
            B_S2_2_I_sample_26,
            B_S2_2_I_sample_27,
            B_S2_2_I_sample_28,
            B_S2_2_I_sample_29,
            B_S2_2_I_sample_30,
            B_S2_2_I_sample_31,
            B_S2_2_I_sample_32,
            B_S2_2_I_sample_33,
            B_S2_2_I_sample_34,
            B_S2_2_I_sample_35,
            B_S2_2_I_sample_36,
            B_S2_2_I_sample_37,
            B_S2_2_I_sample_38,
            B_S2_2_I_sample_39,
            B_S2_2_I_sample_40,
            B_S2_2_I_sample_41,
            B_S2_2_I_sample_42,
            B_S2_2_I_sample_43,
            B_S2_2_I_sample_44,
            B_S2_2_I_sample_45]



if del_var == "yes":
    del B_S2_2_I_sample_01, B_S2_2_I_sample_02, B_S2_2_I_sample_03, B_S2_2_I_sample_04, B_S2_2_I_sample_05
    del B_S2_2_I_sample_06, B_S2_2_I_sample_07, B_S2_2_I_sample_08, B_S2_2_I_sample_09, B_S2_2_I_sample_10
    del B_S2_2_I_sample_11, B_S2_2_I_sample_12, B_S2_2_I_sample_13, B_S2_2_I_sample_14, B_S2_2_I_sample_15
    del B_S2_2_I_sample_16, B_S2_2_I_sample_17, B_S2_2_I_sample_18, B_S2_2_I_sample_19, B_S2_2_I_sample_20
    del B_S2_2_I_sample_21, B_S2_2_I_sample_22, B_S2_2_I_sample_23, B_S2_2_I_sample_24, B_S2_2_I_sample_25
    del B_S2_2_I_sample_26, B_S2_2_I_sample_27, B_S2_2_I_sample_28, B_S2_2_I_sample_29, B_S2_2_I_sample_30
    del B_S2_2_I_sample_31, B_S2_2_I_sample_32, B_S2_2_I_sample_33, B_S2_2_I_sample_34, B_S2_2_I_sample_35
    del B_S2_2_I_sample_36, B_S2_2_I_sample_37, B_S2_2_I_sample_38, B_S2_2_I_sample_39, B_S2_2_I_sample_40
    del B_S2_2_I_sample_41, B_S2_2_I_sample_42, B_S2_2_I_sample_43, B_S2_2_I_sample_44, B_S2_2_I_sample_45





#%% Read CSV data from sample "Probe C"
"""
######################################################################################################
# S1.4, Sensor 2, 1100 - 1350 nm
######################################################################################################
"""
### S1.4, Sensor 2, 1100 - 1350 nm
# load data for calibration
if load_data_calibration == "yes":
    C_S1_4_WL, C_S1_4_I_light_on = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_lamp_on.csv', range_I = S1_4_range)
    _, C_S1_4_I_light_off        = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_lamp_off.csv', range_I = S1_4_range)
    _, C_S1_4_I_cuvette          = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_empty_cuvette.csv', range_I = S1_4_range)
else:
    C_S1_4_WL, _                 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_lamp_on.csv', range_I = S1_4_range)



# load sample data
if load_data_sample == "yes":
    _, C_S1_4_I_sample_03 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_03.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_04 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_04.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_05 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_05.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_06 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_06.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_07 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_07.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_08 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_08.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_09 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_09.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_10 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_10.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_11 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_11.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_12 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_12.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_13 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_13.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_14 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_14.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_15 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_15.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_16 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_16.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_17 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_17.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_18 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_18.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_19 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_19.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_20 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_20.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_21 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_21.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_22 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_22.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_23 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_23.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_24 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_24.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_25 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_25.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_26 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_26.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_27 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_27.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_28 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_28.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_29 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_29.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_30 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_30.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_31 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_31.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_32 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_32.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_33 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_33.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_34 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_34.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_35 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_35.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_36 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_36.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_37 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_37.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_38 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_38.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_39 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_39.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_40 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_40.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_41 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_41.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_42 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_42.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_43 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_43.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_44 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_44.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_45 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_45.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_46 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_46.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_47 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_47.csv', range_I = S1_4_range)
    _, C_S1_4_I_sample_48 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_2_sample_48.csv', range_I = S1_4_range)



# combine sample intensity into one matrix
C_S1_4_I = [C_S1_4_I_sample_03,
            C_S1_4_I_sample_04,
            C_S1_4_I_sample_05,
            C_S1_4_I_sample_06,
            C_S1_4_I_sample_07,
            C_S1_4_I_sample_08,
            C_S1_4_I_sample_09,
            C_S1_4_I_sample_10,
            C_S1_4_I_sample_11,
            C_S1_4_I_sample_12,
            C_S1_4_I_sample_13,
            C_S1_4_I_sample_14,
            C_S1_4_I_sample_15,
            C_S1_4_I_sample_16,
            C_S1_4_I_sample_17,
            C_S1_4_I_sample_18,
            C_S1_4_I_sample_19,
            C_S1_4_I_sample_20,
            C_S1_4_I_sample_21,
            C_S1_4_I_sample_22,
            C_S1_4_I_sample_23,
            C_S1_4_I_sample_24,
            C_S1_4_I_sample_25,
            C_S1_4_I_sample_26,
            C_S1_4_I_sample_27,
            C_S1_4_I_sample_28,
            C_S1_4_I_sample_29,
            C_S1_4_I_sample_30,
            C_S1_4_I_sample_31,
            C_S1_4_I_sample_32,
            C_S1_4_I_sample_33,
            C_S1_4_I_sample_34,
            C_S1_4_I_sample_35,
            C_S1_4_I_sample_36,
            C_S1_4_I_sample_37,
            C_S1_4_I_sample_38,
            C_S1_4_I_sample_39,
            C_S1_4_I_sample_40,
            C_S1_4_I_sample_41,
            C_S1_4_I_sample_42,
            C_S1_4_I_sample_43,
            C_S1_4_I_sample_44,
            C_S1_4_I_sample_45,
            C_S1_4_I_sample_46,
            C_S1_4_I_sample_47,
            C_S1_4_I_sample_48]


if del_var == "yes":
    del C_S1_4_I_sample_03, C_S1_4_I_sample_04, C_S1_4_I_sample_05
    del C_S1_4_I_sample_06, C_S1_4_I_sample_07, C_S1_4_I_sample_08, C_S1_4_I_sample_09, C_S1_4_I_sample_10
    del C_S1_4_I_sample_11, C_S1_4_I_sample_12, C_S1_4_I_sample_13, C_S1_4_I_sample_14, C_S1_4_I_sample_15
    del C_S1_4_I_sample_16, C_S1_4_I_sample_17, C_S1_4_I_sample_18, C_S1_4_I_sample_19, C_S1_4_I_sample_20
    del C_S1_4_I_sample_21, C_S1_4_I_sample_22, C_S1_4_I_sample_23, C_S1_4_I_sample_24, C_S1_4_I_sample_25
    del C_S1_4_I_sample_26, C_S1_4_I_sample_27, C_S1_4_I_sample_28, C_S1_4_I_sample_29, C_S1_4_I_sample_30
    del C_S1_4_I_sample_31, C_S1_4_I_sample_32, C_S1_4_I_sample_33, C_S1_4_I_sample_34, C_S1_4_I_sample_35
    del C_S1_4_I_sample_36, C_S1_4_I_sample_37, C_S1_4_I_sample_38, C_S1_4_I_sample_39, C_S1_4_I_sample_40
    del C_S1_4_I_sample_41, C_S1_4_I_sample_42, C_S1_4_I_sample_43, C_S1_4_I_sample_44, C_S1_4_I_sample_45
    del C_S1_4_I_sample_46, C_S1_4_I_sample_47, C_S1_4_I_sample_48



"""
######################################################################################################
# S1.7, Sensor 1, 1350 - 1650 nm
######################################################################################################
"""
### S1.7, Sensor 1, 1350 - 1650 nm
# load data for calibration
if load_data_calibration == "yes":
    C_S1_7_WL, C_S1_7_I_light_on = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_lamp_on.csv', range_I = S1_7_range)
    _, C_S1_7_I_light_off        = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_lamp_off.csv', range_I = S1_7_range)
    _, C_S1_7_I_cuvette          = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_empty_cuvette.csv', range_I = S1_7_range)
else:
    C_S1_7_WL, _                 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_lamp_on.csv', range_I = S1_7_range)



# load sample data
if load_data_sample == "yes":
    _, C_S1_7_I_sample_03 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_03.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_04 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_04.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_05 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_05.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_06 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_06.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_07 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_07.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_08 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_08.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_09 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_09.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_10 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_10.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_11 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_11.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_12 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_12.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_13 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_13.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_14 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_14.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_15 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_15.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_16 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_16.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_17 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_17.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_18 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_18.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_19 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_19.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_20 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_20.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_21 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_21.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_22 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_22.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_23 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_23.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_24 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_24.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_25 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_25.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_26 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_26.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_27 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_27.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_28 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_28.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_29 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_29.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_30 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_30.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_31 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_31.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_32 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_32.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_33 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_33.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_34 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_34.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_35 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_35.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_36 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_36.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_37 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_37.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_38 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_38.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_39 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_39.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_40 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_40.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_41 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_41.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_42 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_42.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_43 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_43.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_44 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_44.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_45 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_45.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_46 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_46.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_47 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_47.csv', range_I = S1_7_range)
    _, C_S1_7_I_sample_48 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_1_sample_48.csv', range_I = S1_7_range)


# combine sample intensity into one matrix
C_S1_7_I = [C_S1_7_I_sample_03,
            C_S1_7_I_sample_04,
            C_S1_7_I_sample_05,
            C_S1_7_I_sample_06,
            C_S1_7_I_sample_07,
            C_S1_7_I_sample_08,
            C_S1_7_I_sample_09,
            C_S1_7_I_sample_10,
            C_S1_7_I_sample_11,
            C_S1_7_I_sample_12,
            C_S1_7_I_sample_13,
            C_S1_7_I_sample_14,
            C_S1_7_I_sample_15,
            C_S1_7_I_sample_16,
            C_S1_7_I_sample_17,
            C_S1_7_I_sample_18,
            C_S1_7_I_sample_19,
            C_S1_7_I_sample_20,
            C_S1_7_I_sample_21,
            C_S1_7_I_sample_22,
            C_S1_7_I_sample_23,
            C_S1_7_I_sample_24,
            C_S1_7_I_sample_25,
            C_S1_7_I_sample_26,
            C_S1_7_I_sample_27,
            C_S1_7_I_sample_28,
            C_S1_7_I_sample_29,
            C_S1_7_I_sample_30,
            C_S1_7_I_sample_31,
            C_S1_7_I_sample_32,
            C_S1_7_I_sample_33,
            C_S1_7_I_sample_34,
            C_S1_7_I_sample_35,
            C_S1_7_I_sample_36,
            C_S1_7_I_sample_37,
            C_S1_7_I_sample_38,
            C_S1_7_I_sample_39,
            C_S1_7_I_sample_40,
            C_S1_7_I_sample_41,
            C_S1_7_I_sample_42,
            C_S1_7_I_sample_43,
            C_S1_7_I_sample_44,
            C_S1_7_I_sample_45,
            C_S1_7_I_sample_46,
            C_S1_7_I_sample_47,
            C_S1_7_I_sample_48]



if del_var == "yes":
    del C_S1_7_I_sample_03, C_S1_7_I_sample_04, C_S1_7_I_sample_05
    del C_S1_7_I_sample_06, C_S1_7_I_sample_07, C_S1_7_I_sample_08, C_S1_7_I_sample_09, C_S1_7_I_sample_10
    del C_S1_7_I_sample_11, C_S1_7_I_sample_12, C_S1_7_I_sample_13, C_S1_7_I_sample_14, C_S1_7_I_sample_15
    del C_S1_7_I_sample_16, C_S1_7_I_sample_17, C_S1_7_I_sample_18, C_S1_7_I_sample_19, C_S1_7_I_sample_20
    del C_S1_7_I_sample_21, C_S1_7_I_sample_22, C_S1_7_I_sample_23, C_S1_7_I_sample_24, C_S1_7_I_sample_25
    del C_S1_7_I_sample_26, C_S1_7_I_sample_27, C_S1_7_I_sample_28, C_S1_7_I_sample_29, C_S1_7_I_sample_30
    del C_S1_7_I_sample_31, C_S1_7_I_sample_32, C_S1_7_I_sample_33, C_S1_7_I_sample_34, C_S1_7_I_sample_35
    del C_S1_7_I_sample_36, C_S1_7_I_sample_37, C_S1_7_I_sample_38, C_S1_7_I_sample_39, C_S1_7_I_sample_40
    del C_S1_7_I_sample_41, C_S1_7_I_sample_42, C_S1_7_I_sample_43, C_S1_7_I_sample_44, C_S1_7_I_sample_45
    del C_S1_7_I_sample_46, C_S1_7_I_sample_47, C_S1_7_I_sample_48



"""
######################################################################################################
# S2.0, Sensor 4, 1550 - 1950 nm
######################################################################################################
"""
### S2.0, Sensor 4, 1550 - 1950 nm
# load data for calibration
if load_data_calibration == "yes":
    C_S2_0_WL, C_S2_0_I_light_on = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_lamp_on.csv', range_I = S2_0_range)
    _, C_S2_0_I_light_off        = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_lamp_off.csv', range_I = S2_0_range)
    _, C_S2_0_I_cuvette          = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_empty_cuvette.csv', range_I = S2_0_range)
else:
    C_S2_0_WL, _                 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_lamp_on.csv', range_I = S2_0_range)



# load sample data
if load_data_sample == "yes":
    _, C_S2_0_I_sample_03 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_03.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_04 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_04.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_05 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_05.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_06 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_06.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_07 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_07.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_08 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_08.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_09 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_09.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_10 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_10.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_11 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_11.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_12 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_12.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_13 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_13.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_14 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_14.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_15 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_15.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_16 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_16.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_17 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_17.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_18 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_18.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_19 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_19.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_20 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_20.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_21 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_21.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_22 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_22.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_23 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_23.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_24 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_24.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_25 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_25.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_26 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_26.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_27 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_27.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_28 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_28.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_29 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_29.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_30 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_30.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_31 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_31.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_32 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_32.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_33 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_33.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_34 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_34.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_35 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_35.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_36 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_36.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_37 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_37.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_38 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_38.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_39 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_39.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_40 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_40.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_41 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_41.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_42 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_42.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_43 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_43.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_44 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_44.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_45 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_45.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_46 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_46.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_47 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_47.csv', range_I = S2_0_range)
    _, C_S2_0_I_sample_48 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_4_sample_48.csv', range_I = S2_0_range)



# combine sample intensity into one matrix
C_S2_0_I = [C_S2_0_I_sample_03,
            C_S2_0_I_sample_04,
            C_S2_0_I_sample_05,
            C_S2_0_I_sample_06,
            C_S2_0_I_sample_07,
            C_S2_0_I_sample_08,
            C_S2_0_I_sample_09,
            C_S2_0_I_sample_10,
            C_S2_0_I_sample_11,
            C_S2_0_I_sample_12,
            C_S2_0_I_sample_13,
            C_S2_0_I_sample_14,
            C_S2_0_I_sample_15,
            C_S2_0_I_sample_16,
            C_S2_0_I_sample_17,
            C_S2_0_I_sample_18,
            C_S2_0_I_sample_19,
            C_S2_0_I_sample_20,
            C_S2_0_I_sample_21,
            C_S2_0_I_sample_22,
            C_S2_0_I_sample_23,
            C_S2_0_I_sample_24,
            C_S2_0_I_sample_25,
            C_S2_0_I_sample_26,
            C_S2_0_I_sample_27,
            C_S2_0_I_sample_28,
            C_S2_0_I_sample_29,
            C_S2_0_I_sample_30,
            C_S2_0_I_sample_31,
            C_S2_0_I_sample_32,
            C_S2_0_I_sample_33,
            C_S2_0_I_sample_34,
            C_S2_0_I_sample_35,
            C_S2_0_I_sample_36,
            C_S2_0_I_sample_37,
            C_S2_0_I_sample_38,
            C_S2_0_I_sample_39,
            C_S2_0_I_sample_40,
            C_S2_0_I_sample_41,
            C_S2_0_I_sample_42,
            C_S2_0_I_sample_43,
            C_S2_0_I_sample_44,
            C_S2_0_I_sample_45,
            C_S2_0_I_sample_46,
            C_S2_0_I_sample_47,
            C_S2_0_I_sample_48]



if del_var == "yes":
    del C_S2_0_I_sample_03, C_S2_0_I_sample_04, C_S2_0_I_sample_05
    del C_S2_0_I_sample_06, C_S2_0_I_sample_07, C_S2_0_I_sample_08, C_S2_0_I_sample_09, C_S2_0_I_sample_10
    del C_S2_0_I_sample_11, C_S2_0_I_sample_12, C_S2_0_I_sample_13, C_S2_0_I_sample_14, C_S2_0_I_sample_15
    del C_S2_0_I_sample_16, C_S2_0_I_sample_17, C_S2_0_I_sample_18, C_S2_0_I_sample_19, C_S2_0_I_sample_20
    del C_S2_0_I_sample_21, C_S2_0_I_sample_22, C_S2_0_I_sample_23, C_S2_0_I_sample_24, C_S2_0_I_sample_25
    del C_S2_0_I_sample_26, C_S2_0_I_sample_27, C_S2_0_I_sample_28, C_S2_0_I_sample_29, C_S2_0_I_sample_30
    del C_S2_0_I_sample_31, C_S2_0_I_sample_32, C_S2_0_I_sample_33, C_S2_0_I_sample_34, C_S2_0_I_sample_35
    del C_S2_0_I_sample_36, C_S2_0_I_sample_37, C_S2_0_I_sample_38, C_S2_0_I_sample_39, C_S2_0_I_sample_40
    del C_S2_0_I_sample_41, C_S2_0_I_sample_42, C_S2_0_I_sample_43, C_S2_0_I_sample_44, C_S2_0_I_sample_45
    del C_S2_0_I_sample_46, C_S2_0_I_sample_47, C_S2_0_I_sample_48



"""
######################################################################################################
# S2.2, Sensor 3, 1750 - 2150 nm
######################################################################################################
"""
### S2.2, Sensor 3, 1750 - 2150 nm
# load data for calibration
if load_data_calibration == "yes":
    C_S2_2_WL, C_S2_2_I_light_on = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_lamp_on.csv', range_I = S2_2_range)
    _, C_S2_2_I_light_off        = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_lamp_off.csv', range_I = S2_2_range)
    _, C_S2_2_I_cuvette          = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_empty_cuvette.csv', range_I = S2_2_range)
else:
    C_S2_2_WL, _                 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_lamp_on.csv', range_I = S2_2_range)



# load sample data
if load_data_sample == "yes":
    _, C_S2_2_I_sample_03 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_03.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_04 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_04.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_05 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_05.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_06 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_06.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_07 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_07.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_08 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_08.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_09 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_09.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_10 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_10.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_11 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_11.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_12 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_12.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_13 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_13.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_14 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_14.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_15 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_15.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_16 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_16.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_17 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_17.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_18 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_18.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_19 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_19.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_20 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_20.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_21 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_21.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_22 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_22.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_23 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_23.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_24 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_24.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_25 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_25.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_26 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_26.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_27 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_27.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_28 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_28.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_29 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_29.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_30 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_30.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_31 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_31.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_32 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_32.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_33 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_33.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_34 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_34.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_35 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_35.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_36 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_36.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_37 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_37.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_38 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_38.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_39 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_39.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_40 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_40.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_41 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_41.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_42 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_42.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_43 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_43.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_44 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_44.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_45 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_45.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_46 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_46.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_47 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_47.csv', range_I = S2_2_range)
    _, C_S2_2_I_sample_48 = read_csv_data(path = 'Probe C (29.07.2022)/sensor_3_sample_48.csv', range_I = S2_2_range)



# combine sample intensity into one matrix
C_S2_2_I = [C_S2_2_I_sample_03,
            C_S2_2_I_sample_04,
            C_S2_2_I_sample_05,
            C_S2_2_I_sample_06,
            C_S2_2_I_sample_07,
            C_S2_2_I_sample_08,
            C_S2_2_I_sample_09,
            C_S2_2_I_sample_10,
            C_S2_2_I_sample_11,
            C_S2_2_I_sample_12,
            C_S2_2_I_sample_13,
            C_S2_2_I_sample_14,
            C_S2_2_I_sample_15,
            C_S2_2_I_sample_16,
            C_S2_2_I_sample_17,
            C_S2_2_I_sample_18,
            C_S2_2_I_sample_19,
            C_S2_2_I_sample_20,
            C_S2_2_I_sample_21,
            C_S2_2_I_sample_22,
            C_S2_2_I_sample_23,
            C_S2_2_I_sample_24,
            C_S2_2_I_sample_25,
            C_S2_2_I_sample_26,
            C_S2_2_I_sample_27,
            C_S2_2_I_sample_28,
            C_S2_2_I_sample_29,
            C_S2_2_I_sample_30,
            C_S2_2_I_sample_31,
            C_S2_2_I_sample_32,
            C_S2_2_I_sample_33,
            C_S2_2_I_sample_34,
            C_S2_2_I_sample_35,
            C_S2_2_I_sample_36,
            C_S2_2_I_sample_37,
            C_S2_2_I_sample_38,
            C_S2_2_I_sample_39,
            C_S2_2_I_sample_40,
            C_S2_2_I_sample_41,
            C_S2_2_I_sample_42,
            C_S2_2_I_sample_43,
            C_S2_2_I_sample_44,
            C_S2_2_I_sample_45,
            C_S2_2_I_sample_46,
            C_S2_2_I_sample_47,
            C_S2_2_I_sample_48]



if del_var == "yes":
    del C_S2_2_I_sample_03, C_S2_2_I_sample_04, C_S2_2_I_sample_05
    del C_S2_2_I_sample_06, C_S2_2_I_sample_07, C_S2_2_I_sample_08, C_S2_2_I_sample_09, C_S2_2_I_sample_10
    del C_S2_2_I_sample_11, C_S2_2_I_sample_12, C_S2_2_I_sample_13, C_S2_2_I_sample_14, C_S2_2_I_sample_15
    del C_S2_2_I_sample_16, C_S2_2_I_sample_17, C_S2_2_I_sample_18, C_S2_2_I_sample_19, C_S2_2_I_sample_20
    del C_S2_2_I_sample_21, C_S2_2_I_sample_22, C_S2_2_I_sample_23, C_S2_2_I_sample_24, C_S2_2_I_sample_25
    del C_S2_2_I_sample_26, C_S2_2_I_sample_27, C_S2_2_I_sample_28, C_S2_2_I_sample_29, C_S2_2_I_sample_30
    del C_S2_2_I_sample_31, C_S2_2_I_sample_32, C_S2_2_I_sample_33, C_S2_2_I_sample_34, C_S2_2_I_sample_35
    del C_S2_2_I_sample_36, C_S2_2_I_sample_37, C_S2_2_I_sample_38, C_S2_2_I_sample_39, C_S2_2_I_sample_40
    del C_S2_2_I_sample_41, C_S2_2_I_sample_42, C_S2_2_I_sample_43, C_S2_2_I_sample_44, C_S2_2_I_sample_45
    del C_S2_2_I_sample_46, C_S2_2_I_sample_47, C_S2_2_I_sample_48





#%% Read CSV data from sample "Probe D"
"""
######################################################################################################
# S1.4, Sensor 2, 1100 - 1350 nm
######################################################################################################
"""
### S1.4, Sensor 2, 1100 - 1350 nm
# load data for calibration
if load_data_calibration == "yes":
    D_S1_4_WL, D_S1_4_I_light_on = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_lamp_on.csv', range_I = S1_4_range)
    _, D_S1_4_I_light_off        = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_lamp_off.csv', range_I = S1_4_range)
    _, D_S1_4_I_cuvette          = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_empty_cuvette.csv', range_I = S1_4_range)
else:
    D_S1_4_WL, _                 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_lamp_on.csv', range_I = S1_4_range)



# load sample data
if load_data_sample == "yes":
    _, D_S1_4_I_sample_01 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_01.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_02 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_02.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_03 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_03.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_04 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_04.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_05 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_05.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_06 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_06.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_07 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_07.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_08 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_08.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_09 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_09.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_10 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_10.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_11 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_11.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_12 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_12.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_13 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_13.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_14 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_14.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_15 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_15.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_16 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_16.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_33 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_33.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_34 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_34.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_35 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_35.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_36 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_36.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_37 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_37.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_38 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_38.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_39 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_39.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_40 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_40.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_41 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_41.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_42 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_42.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_43 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_43.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_44 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_44.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_45 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_45.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_46 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_46.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_47 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_47.csv', range_I = S1_4_range)
    _, D_S1_4_I_sample_48 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_2_sample_48.csv', range_I = S1_4_range)


# combine sample intensity into one matrix
D_S1_4_I = [D_S1_4_I_sample_01,
            D_S1_4_I_sample_02,
            D_S1_4_I_sample_03,
            D_S1_4_I_sample_04,
            D_S1_4_I_sample_05,
            D_S1_4_I_sample_06,
            D_S1_4_I_sample_07,
            D_S1_4_I_sample_08,
            D_S1_4_I_sample_09,
            D_S1_4_I_sample_10,
            D_S1_4_I_sample_11,
            D_S1_4_I_sample_12,
            D_S1_4_I_sample_13,
            D_S1_4_I_sample_14,
            D_S1_4_I_sample_15,
            D_S1_4_I_sample_16,
            D_S1_4_I_sample_33,
            D_S1_4_I_sample_34,
            D_S1_4_I_sample_35,
            D_S1_4_I_sample_36,
            D_S1_4_I_sample_37,
            D_S1_4_I_sample_38,
            D_S1_4_I_sample_39,
            D_S1_4_I_sample_40,
            D_S1_4_I_sample_41,
            D_S1_4_I_sample_42,
            D_S1_4_I_sample_43,
            D_S1_4_I_sample_44,
            D_S1_4_I_sample_45,
            D_S1_4_I_sample_46,
            D_S1_4_I_sample_47,
            D_S1_4_I_sample_48]


if del_var == "yes":
    del D_S1_4_I_sample_01, D_S1_4_I_sample_02, D_S1_4_I_sample_03, D_S1_4_I_sample_04, D_S1_4_I_sample_05
    del D_S1_4_I_sample_06, D_S1_4_I_sample_07, D_S1_4_I_sample_08, D_S1_4_I_sample_09, D_S1_4_I_sample_10
    del D_S1_4_I_sample_11, D_S1_4_I_sample_12, D_S1_4_I_sample_13, D_S1_4_I_sample_14, D_S1_4_I_sample_15
    del D_S1_4_I_sample_16, D_S1_4_I_sample_33, D_S1_4_I_sample_34, D_S1_4_I_sample_35
    del D_S1_4_I_sample_36, D_S1_4_I_sample_37, D_S1_4_I_sample_38, D_S1_4_I_sample_39, D_S1_4_I_sample_40
    del D_S1_4_I_sample_41, D_S1_4_I_sample_42, D_S1_4_I_sample_43, D_S1_4_I_sample_44, D_S1_4_I_sample_45
    del D_S1_4_I_sample_46, D_S1_4_I_sample_47, D_S1_4_I_sample_48



"""
######################################################################################################
# S1.7, Sensor 1, 1350 - 1650 nm
######################################################################################################
"""
### S1.7, Sensor 1, 1350 - 1650 nm
# load data for calibration
if load_data_calibration == "yes":
    D_S1_7_WL, D_S1_7_I_light_on = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_lamp_on.csv', range_I = S1_7_range)
    _, D_S1_7_I_light_off        = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_lamp_off.csv', range_I = S1_7_range)
    _, D_S1_7_I_cuvette          = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_empty_cuvette.csv', range_I = S1_7_range)
else:
    D_S1_7_WL, _                 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_lamp_on.csv', range_I = S1_7_range)



# load sample data
if load_data_sample == "yes":
    _, D_S1_7_I_sample_01 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_01.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_02 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_02.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_03 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_03.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_04 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_04.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_05 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_05.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_06 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_06.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_07 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_07.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_08 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_08.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_09 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_09.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_10 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_10.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_11 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_11.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_12 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_12.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_13 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_13.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_14 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_14.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_15 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_15.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_16 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_16.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_33 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_33.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_34 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_34.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_35 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_35.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_36 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_36.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_37 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_37.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_38 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_38.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_39 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_39.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_40 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_40.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_41 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_41.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_42 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_42.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_43 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_43.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_44 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_44.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_45 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_45.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_46 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_46.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_47 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_47.csv', range_I = S1_7_range)
    _, D_S1_7_I_sample_48 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_1_sample_48.csv', range_I = S1_7_range)


# combine sample intensity into one matrix
D_S1_7_I = [D_S1_7_I_sample_01,
            D_S1_7_I_sample_02,
            D_S1_7_I_sample_03,
            D_S1_7_I_sample_04,
            D_S1_7_I_sample_05,
            D_S1_7_I_sample_06,
            D_S1_7_I_sample_07,
            D_S1_7_I_sample_08,
            D_S1_7_I_sample_09,
            D_S1_7_I_sample_10,
            D_S1_7_I_sample_11,
            D_S1_7_I_sample_12,
            D_S1_7_I_sample_13,
            D_S1_7_I_sample_14,
            D_S1_7_I_sample_15,
            D_S1_7_I_sample_16,
            D_S1_7_I_sample_33,
            D_S1_7_I_sample_34,
            D_S1_7_I_sample_35,
            D_S1_7_I_sample_36,
            D_S1_7_I_sample_37,
            D_S1_7_I_sample_38,
            D_S1_7_I_sample_39,
            D_S1_7_I_sample_40,
            D_S1_7_I_sample_41,
            D_S1_7_I_sample_42,
            D_S1_7_I_sample_43,
            D_S1_7_I_sample_44,
            D_S1_7_I_sample_45,
            D_S1_7_I_sample_46,
            D_S1_7_I_sample_47,
            D_S1_7_I_sample_48]



if del_var == "yes":
    del D_S1_7_I_sample_01, D_S1_7_I_sample_02, D_S1_7_I_sample_03, D_S1_7_I_sample_04, D_S1_7_I_sample_05
    del D_S1_7_I_sample_06, D_S1_7_I_sample_07, D_S1_7_I_sample_08, D_S1_7_I_sample_09, D_S1_7_I_sample_10
    del D_S1_7_I_sample_11, D_S1_7_I_sample_12, D_S1_7_I_sample_13, D_S1_7_I_sample_14, D_S1_7_I_sample_15
    del D_S1_7_I_sample_16, D_S1_7_I_sample_33, D_S1_7_I_sample_34, D_S1_7_I_sample_35
    del D_S1_7_I_sample_36, D_S1_7_I_sample_37, D_S1_7_I_sample_38, D_S1_7_I_sample_39, D_S1_7_I_sample_40
    del D_S1_7_I_sample_41, D_S1_7_I_sample_42, D_S1_7_I_sample_43, D_S1_7_I_sample_44, D_S1_7_I_sample_45
    del D_S1_7_I_sample_46, D_S1_7_I_sample_47, D_S1_7_I_sample_48



"""
######################################################################################################
# S2.0, Sensor 4, 1550 - 1950 nm
######################################################################################################
"""
### S2.0, Sensor 4, 1550 - 1950 nm
# load data for calibration
if load_data_calibration == "yes":
    D_S2_0_WL, D_S2_0_I_light_on = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_lamp_on.csv', range_I = S2_0_range)
    _, D_S2_0_I_light_off        = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_lamp_off.csv', range_I = S2_0_range)
    _, D_S2_0_I_cuvette          = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_empty_cuvette.csv', range_I = S2_0_range)
else:
    D_S2_0_WL, _                 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_lamp_on.csv', range_I = S2_0_range)



# load sample data
if load_data_sample == "yes":
    _, D_S2_0_I_sample_01 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_01.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_02 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_02.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_03 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_03.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_04 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_04.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_05 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_05.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_06 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_06.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_07 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_07.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_08 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_08.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_09 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_09.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_10 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_10.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_11 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_11.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_12 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_12.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_13 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_13.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_14 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_14.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_15 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_15.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_16 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_16.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_33 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_33.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_34 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_34.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_35 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_35.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_36 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_36.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_37 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_37.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_38 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_38.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_39 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_39.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_40 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_40.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_41 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_41.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_42 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_42.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_43 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_43.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_44 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_44.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_45 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_45.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_46 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_46.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_47 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_47.csv', range_I = S2_0_range)
    _, D_S2_0_I_sample_48 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_4_sample_48.csv', range_I = S2_0_range)


# combine sample intensity into one matrix
D_S2_0_I = [D_S2_0_I_sample_01,
            D_S2_0_I_sample_02,
            D_S2_0_I_sample_03,
            D_S2_0_I_sample_04,
            D_S2_0_I_sample_05,
            D_S2_0_I_sample_06,
            D_S2_0_I_sample_07,
            D_S2_0_I_sample_08,
            D_S2_0_I_sample_09,
            D_S2_0_I_sample_10,
            D_S2_0_I_sample_11,
            D_S2_0_I_sample_12,
            D_S2_0_I_sample_13,
            D_S2_0_I_sample_14,
            D_S2_0_I_sample_15,
            D_S2_0_I_sample_16,
            D_S2_0_I_sample_33,
            D_S2_0_I_sample_34,
            D_S2_0_I_sample_35,
            D_S2_0_I_sample_36,
            D_S2_0_I_sample_37,
            D_S2_0_I_sample_38,
            D_S2_0_I_sample_39,
            D_S2_0_I_sample_40,
            D_S2_0_I_sample_41,
            D_S2_0_I_sample_42,
            D_S2_0_I_sample_43,
            D_S2_0_I_sample_44,
            D_S2_0_I_sample_45,
            D_S2_0_I_sample_46,
            D_S2_0_I_sample_47,
            D_S2_0_I_sample_48]



if del_var == "yes":
    del D_S2_0_I_sample_01, D_S2_0_I_sample_02, D_S2_0_I_sample_03, D_S2_0_I_sample_04, D_S2_0_I_sample_05
    del D_S2_0_I_sample_06, D_S2_0_I_sample_07, D_S2_0_I_sample_08, D_S2_0_I_sample_09, D_S2_0_I_sample_10
    del D_S2_0_I_sample_11, D_S2_0_I_sample_12, D_S2_0_I_sample_13, D_S2_0_I_sample_14, D_S2_0_I_sample_15
    del D_S2_0_I_sample_16, D_S2_0_I_sample_33, D_S2_0_I_sample_34, D_S2_0_I_sample_35
    del D_S2_0_I_sample_36, D_S2_0_I_sample_37, D_S2_0_I_sample_38, D_S2_0_I_sample_39, D_S2_0_I_sample_40
    del D_S2_0_I_sample_41, D_S2_0_I_sample_42, D_S2_0_I_sample_43, D_S2_0_I_sample_44, D_S2_0_I_sample_45
    del D_S2_0_I_sample_46, D_S2_0_I_sample_47, D_S2_0_I_sample_48



"""
######################################################################################################
# S2.2, Sensor 3, 1750 - 2150 nm
######################################################################################################
"""
### S2.2, Sensor 3, 1750 - 2150 nm
# load data for calibration
if load_data_calibration == "yes":
    D_S2_2_WL, D_S2_2_I_light_on = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_lamp_on.csv', range_I = S2_2_range)
    _, D_S2_2_I_light_off        = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_lamp_off.csv', range_I = S2_2_range)
    _, D_S2_2_I_cuvette          = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_empty_cuvette.csv', range_I = S2_2_range)
else:
    D_S2_2_WL, _                 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_lamp_on.csv', range_I = S2_2_range)



# load sample data
if load_data_sample == "yes":
    _, D_S2_2_I_sample_01 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_01.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_02 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_02.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_03 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_03.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_04 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_04.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_05 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_05.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_06 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_06.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_07 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_07.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_08 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_08.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_09 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_09.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_10 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_10.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_11 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_11.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_12 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_12.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_13 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_13.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_14 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_14.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_15 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_15.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_16 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_16.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_33 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_33.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_34 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_34.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_35 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_35.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_36 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_36.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_37 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_37.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_38 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_38.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_39 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_39.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_40 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_40.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_41 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_41.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_42 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_42.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_43 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_43.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_44 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_44.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_45 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_45.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_46 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_46.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_47 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_47.csv', range_I = S2_2_range)
    _, D_S2_2_I_sample_48 = read_csv_data(path = 'Probe D (04.08.2022)/sensor_3_sample_48.csv', range_I = S2_2_range)


# combine sample intensity into one matrix
D_S2_2_I = [D_S2_2_I_sample_01,
            D_S2_2_I_sample_02,
            D_S2_2_I_sample_03,
            D_S2_2_I_sample_04,
            D_S2_2_I_sample_05,
            D_S2_2_I_sample_06,
            D_S2_2_I_sample_07,
            D_S2_2_I_sample_08,
            D_S2_2_I_sample_09,
            D_S2_2_I_sample_10,
            D_S2_2_I_sample_11,
            D_S2_2_I_sample_12,
            D_S2_2_I_sample_13,
            D_S2_2_I_sample_14,
            D_S2_2_I_sample_15,
            D_S2_2_I_sample_16,
            D_S2_2_I_sample_33,
            D_S2_2_I_sample_34,
            D_S2_2_I_sample_35,
            D_S2_2_I_sample_36,
            D_S2_2_I_sample_37,
            D_S2_2_I_sample_38,
            D_S2_2_I_sample_39,
            D_S2_2_I_sample_40,
            D_S2_2_I_sample_41,
            D_S2_2_I_sample_42,
            D_S2_2_I_sample_43,
            D_S2_2_I_sample_44,
            D_S2_2_I_sample_45,
            D_S2_2_I_sample_46,
            D_S2_2_I_sample_47,
            D_S2_2_I_sample_48]



if del_var == "yes":
    del D_S2_2_I_sample_01, D_S2_2_I_sample_02, D_S2_2_I_sample_03, D_S2_2_I_sample_04, D_S2_2_I_sample_05
    del D_S2_2_I_sample_06, D_S2_2_I_sample_07, D_S2_2_I_sample_08, D_S2_2_I_sample_09, D_S2_2_I_sample_10
    del D_S2_2_I_sample_11, D_S2_2_I_sample_12, D_S2_2_I_sample_13, D_S2_2_I_sample_14, D_S2_2_I_sample_15
    del D_S2_2_I_sample_16, D_S2_2_I_sample_33, D_S2_2_I_sample_34, D_S2_2_I_sample_35
    del D_S2_2_I_sample_36, D_S2_2_I_sample_37, D_S2_2_I_sample_38, D_S2_2_I_sample_39, D_S2_2_I_sample_40
    del D_S2_2_I_sample_41, D_S2_2_I_sample_42, D_S2_2_I_sample_43, D_S2_2_I_sample_44, D_S2_2_I_sample_45
    del D_S2_2_I_sample_46, D_S2_2_I_sample_47, D_S2_2_I_sample_48







#%% Plot data based on class
"""
######################################################################################################
# acetic acid concentration < 2 g/l = Green
# acetic acid concentration > 2 g/l = Red
######################################################################################################
"""

output_class_IJK = [0,0,0,0,0,0,0,                                                 # sample I,0
                    0,1,1,1,0,1,1,1,                                               # sample I,1
                    0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,                               # sample I
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,   # sample J
                    0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1]   # sample K

output_class_A = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,               # sample 1-24
                  1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,               # sample 25-48
                  0,1]                                                           # sample 49(17) and 50(27)

output_class_B = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,               # sample 1-24
                  1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]                     # sample 25-45 

output_class_C = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,                   # sample 3-24
                  1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]               # sample 25-48

output_class_D = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,                               # sample 1-16
                  1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]                               # sample 33-48


### data preparation, combine data into one matrix
S1_4_I = copy.deepcopy(I0_S1_4_I)
S1_4_I.extend(I1_S1_4_I)
S1_4_I.extend(I_S1_4_I)
S1_4_I.extend(J_S1_4_I)
S1_4_I.extend(K_S1_4_I)
S1_4_I.extend(A_S1_4_I)
S1_4_I.extend(B_S1_4_I)
S1_4_I.extend(C_S1_4_I)
S1_4_I.extend(D_S1_4_I)

S1_7_I = copy.deepcopy(I0_S1_7_I)
S1_7_I.extend(I1_S1_7_I)
S1_7_I.extend(I_S1_7_I)
S1_7_I.extend(J_S1_7_I)
S1_7_I.extend(K_S1_7_I)
S1_7_I.extend(A_S1_7_I)
S1_7_I.extend(B_S1_7_I)
S1_7_I.extend(C_S1_7_I)
S1_7_I.extend(D_S1_7_I)

S2_0_I = copy.deepcopy(I0_S2_0_I)
S2_0_I.extend(I1_S2_0_I)
S2_0_I.extend(I_S2_0_I)
S2_0_I.extend(J_S2_0_I)
S2_0_I.extend(K_S2_0_I)
S2_0_I.extend(A_S2_0_I)
S2_0_I.extend(B_S2_0_I)
S2_0_I.extend(C_S2_0_I)
S2_0_I.extend(D_S2_0_I)

S2_2_I = copy.deepcopy(I0_S2_2_I)
S2_2_I.extend(I1_S2_2_I)
S2_2_I.extend(I_S2_2_I)
S2_2_I.extend(J_S2_2_I)
S2_2_I.extend(K_S2_2_I)
S2_2_I.extend(A_S2_2_I)
S2_2_I.extend(B_S2_2_I)
S2_2_I.extend(C_S2_2_I)
S2_2_I.extend(D_S2_2_I)

output_class = copy.deepcopy(output_class_IJK)
output_class.extend(output_class_A)
output_class.extend(output_class_B)
output_class.extend(output_class_C)
output_class.extend(output_class_D)



### plot
plot_based_on_classes(S1_4_WL        = D_S1_4_WL,
                      S1_7_WL        = D_S1_7_WL,
                      S2_0_WL        = D_S2_0_WL,
                      S2_2_WL        = D_S2_2_WL,
                      S1_4_I         = S1_4_I,
                      S1_7_I         = S1_7_I,
                      S2_0_I         = S2_0_I,
                      S2_2_I         = S2_2_I,
                      output_classes = output_class,
                      plot_label     = [rf'$<$ \SI{{2}}{{\gram\per\litre}}',rf'$>$ \SI{{2}}{{\gram\per\litre}}'],
                      suptitle       = "Plot based on classes",
                      xlabel         = "Wavelength (nm)",
                      ylabel         = "Intensity (DN)",
                      show_plot      = "yes")





#%% Create CSV data for each sensor
write_csv = "yes"

"""
######################################################################################################
# Sensor S1.4
######################################################################################################
"""
### Sensor S1.4
if write_csv == "yes":
    f = open("NIR_Data_S1_4.csv","w")
    
    str_header_S1_4 = ""
    for i in S1_4_range:
        str_header_S1_4 += str(i)+","
    str_header_S1_4 = str_header_S1_4 + "class\n"
    f.write(str_header_S1_4)
    
    for ind_files in range(len(S1_4_I)):
        str_body_S1_4 = ""
        for j in range(len(S1_4_I[0])):
            str_body_S1_4 += "%.2f"%S1_4_I[ind_files][j]+","
        str_body_S1_4 += str(output_class[ind_files])+"\n"
        f.write(str_body_S1_4)
    
    f.close()


"""
######################################################################################################
# Sensor S1.7
######################################################################################################
"""
### Sensor S1.7
if write_csv == "yes":
    f = open("NIR_Data_S1_7.csv","w")
    
    str_header_S1_7 = ""
    for i in S1_7_range:
        str_header_S1_7 += str(i)+","
    str_header_S1_7 = str_header_S1_7 + "concentration\n"
    f.write(str_header_S1_7)
    
    for ind_files in range(len(S1_7_I)):
        str_body_S1_7 = ""
        for j in range(len(S1_7_I[0])):
            str_body_S1_7 += "%.2f"%S1_7_I[ind_files][j]+","
        str_body_S1_7 += str(output_class[ind_files])+"\n"
        f.write(str_body_S1_7)
    
    f.close()


"""
######################################################################################################
# Sensor S2.0
######################################################################################################
"""
### Sensor S2.0
if write_csv == "yes":
    f = open("NIR_Data_S2_0.csv","w")
    
    str_header_S2_0 = ""
    for i in S2_0_range:
        str_header_S2_0 += str(i)+","
    str_header_S2_0 = str_header_S2_0 + "concentration\n"
    f.write(str_header_S2_0)
    
    for ind_files in range(len(S2_0_I)):
        str_body_S2_0 = ""
        for j in range(len(S2_0_I[0])):
            str_body_S2_0 += "%.2f"%S2_0_I[ind_files][j]+","
        str_body_S2_0 += str(output_class[ind_files])+"\n"
        f.write(str_body_S2_0)
    
    f.close()


"""
######################################################################################################
# Sensor S2.2
######################################################################################################
"""
### Sensor S2.2
if write_csv == "yes":
    f = open("NIR_Data_S2_2.csv","w")
    
    str_header_S2_2 = ""
    for i in S2_2_range:
        str_header_S2_2 += str(i)+","
    str_header_S2_2 = str_header_S2_2 + "concentration\n"
    f.write(str_header_S2_2)
    
    for ind_files in range(len(S2_2_I)):
        str_body_S2_2 = ""
        for j in range(len(S2_2_I[0])):
            str_body_S2_2 += "%.2f"%S2_2_I[ind_files][j]+","
        str_body_S2_2 += str(output_class[ind_files])+"\n"
        f.write(str_body_S2_2)
    
    f.close()


del write_csv, str_header_S1_4, str_body_S1_4, str_header_S1_7, str_body_S1_7
del str_header_S2_0, str_body_S2_0, str_header_S2_2, str_body_S2_2
del i, j, ind_files





#%% Create CSV data combine sensors
write_csv = "yes"
"""
######################################################################################################
# Sensor S1.4, S1.7, S2.0 and S2.2
######################################################################################################
"""
if write_csv == "yes":
    f = open("NIR_Data.csv","w")
    
    str_header = ""
    for i in S1_4_range:
        str_header += str(i)+","
    for i in S1_7_range:
        str_header += str(i)+","
    for i in S2_0_range:
        str_header += str(i)+","
    for i in S2_2_range:
        str_header += str(i)+","
    str_header = str_header + "class\n"
    f.write(str_header)
    
    for ind_files in range(len(S1_4_I)):
        str_body = ""
        for j in range(len(S1_4_I[0])):
            str_body += "%.2f"%S1_4_I[ind_files][j]+","
        for j in range(len(S1_7_I[0])):
            str_body += "%.2f"%S1_7_I[ind_files][j]+","
        for j in range(len(S2_0_I[0])):
            str_body += "%.2f"%S2_0_I[ind_files][j]+","
        for j in range(len(S2_2_I[0])):
            str_body += "%.2f"%S2_2_I[ind_files][j]+","
        str_body += str(output_class[ind_files])+"\n"
        f.write(str_body)
    
    f.close()

del write_csv, str_header, str_body, i, j, ind_files