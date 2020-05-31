from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
import numpy as np

def timelineplot(fname, stop_time, tasks, tick_delta):
    fig, axeses = plt.subplots(len(tasks), sharex='col')
    if not isinstance(axeses, np.ndarray):
        axeses = [axeses]
    fig.set_size_inches(10,len(tasks))
    for task, axes in zip(tasks, axeses):
        rects = []
        axes.tick_params(axis='y', left=False, labelleft=False)
        axes.set_xticks(range(0, stop_time, 1))
        for spine in 'top left right'.split():
            axes.spines[spine].set_visible(False)
        labels = ['']*stop_time

        axes.text(-2, 0.5, f"${task['name']}$", fontsize='x-large')

        if (task['type'] == 'periodic'):
            for i in range(task['activation_start'], stop_time, task['activation_delta']):
                axes.add_line(Line2D((i, i), (0, 2), linewidth=1, color='black'))
        else:
            axes.arrow(task['activation_start'], 0, 0, 2, length_includes_head=True, head_width=0.3, head_length=0.3, fc='k', ec='k')
            axes.arrow(task['activation_end'], 2, 0, -2, length_includes_head=True, head_width=0.3, head_length=0.3, fc='k', ec='k')

        for i in range(0, stop_time, tick_delta):
            labels[i] = str(i)
        axes.set_xticklabels(labels)
        axes.set_xlim(0, stop_time)
        axes.set_ylim(0, 2)
        for (start, end) in task['times']:
            rects.append(Rectangle((start, 0), end - start, 1, color='grey', ec='black'))
        for rect in rects:
            axes.add_patch(rect)
    fig.savefig(fname)
    plt.show()

def job(name, times, activation, deadline):
    return {'name': name, 'times': times, 'activation_start': activation, 'activation_end': deadline, 'type': 'aperiodic'}

def task(name, times, activation_delta):
    return {'name': name, 'times': times, 'activation_start': 0, 'activation_delta': activation_delta, 'type': 'periodic'}

#timelineplot("worstcasedeadline.eps",
#        22, [task(r"\tau_1", ((12, 13), (11, 12), (8,9), (5,6), (1,2), (16,17), (19,20)), 3),
#             task(r"\tau_2", ((9, 11), (6, 8), (2,4), (14,16), (17,19)), 4),
#             job(r"j_k", [(4,5), (13,14)], 2, 14)], 2)

#timelineplot("edfdeadline.eps",
#        22, [task(r"\tau_1", ((0,1), (3,4), (6,7), (10, 11), (12, 13), (15,16), (18,19)), 3),
#             task(r"\tau_2", ((1,3), (4,6), (8,10), (13,15), (16,18)), 4),
#             job(r"j_k", ((7,8), (11,12)), 2, 14)], 2)

#timelineplot("optimaldeadline.eps",
#        22, [task(r"\tau_1", ((0,1), (5,6), (8,9), (11,12), (12,13), (15,16), (18,19)), 3),
#             task(r"\tau_2", ((1,3), (6,8), (9,11), (13,15), (16,18)), 4),
#             job(r"j_k", ((3,5),), 2, 5)], 2)

#timelineplot("taskcharacteristics.svg",
#        22, [job(r"\tau_1", ((6, 16),), 2, 20)], 2)

timelineplot("rmexample.eps",
        36, [task(r"\tau_1", ((0,3), (5,8), (10,13), (15,18), (20,23), (25,28), (30,33)), 5),
             task(r"\tau_2", ((3, 5), (8,10), (14,15), (18,19), (23,25), (28,30)), 7)], 2)

timelineplot("rmfail.eps",
        35, [task(r"\tau_1", ((0,2), (5,7), (10,12), (15,17), (20,22), (25,27), (30,32)), 5),

             task(r"\tau_2", ((2,5), (7,10), (12,15), (17,20), (22,25), (27,30), (32,34)), 7)], 2)

timelineplot("edfsucc.eps",
        35, [task(r"\tau_1", ((0,2), (6,8), (12,14), (15,17), (20,22), (25,27), (32, 34)), 5),

             task(r"\tau_2", ((2,6), (8,12), (14,15), (17,20), (21,25), (28,32)), 7)], 2)


