#!python3

import csv, sys, os
import matplotlib.pyplot as plt
import pandas as pd
from cycler import cycler
 
output_path = ""
input_path = ""

color1 = "#FF2400"
color2 = "#007FFF"
color3 = "#3CB464"
color4 = "#FFA500"
color5 = "#9400D3"
color6 = "#20D9A5"
color7 = "#D2691E"
color8 = "#2A52BE"
color9 = "#FF00FF"

def tpcc_throughput():
    epic_df = pd.read_csv(f"{input_path}/epic/epic_tpcc.csv")
    epic_df = epic_df[['num_warehouses', 'throughput']]
    epic_df['database'] = 'epic'
    print(epic_df)
 
    gacco_df = pd.read_csv(f"{input_path}/epic/gacco_tpcc_default.csv")
    gacco_df = gacco_df[['num_warehouses', 'throughput']]
    gacco_df['database'] = 'gacco'
    print(gacco_df)

    caracal_df = pd.read_csv(f"{input_path}/caracal/tpcc/caracal_tpcc.csv")
    caracal_df = caracal_df[['num_warehouses', 'throughput']]
    caracal_df['database'] = 'caracal'
    print(caracal_df)

    osto_df = pd.read_csv(f"{input_path}/sto/tpcc_default.csv")
    osto_df = osto_df[['num_warehouses', 'throughput']]
    osto_df['database'] = 'osto'
    print(osto_df)

    tsto_df = pd.read_csv(f"{input_path}/sto/tpcc_tictoc.csv")
    tsto_df = tsto_df[['num_warehouses', 'throughput']]
    tsto_df['database'] = 'tsto'
    print(tsto_df)

    msto_df = pd.read_csv(f"{input_path}/sto/tpcc_mvcc.csv")
    msto_df = msto_df[['num_warehouses', 'throughput']]
    msto_df['database'] = 'msto'
    print(msto_df)

    df = pd.concat([epic_df, gacco_df, caracal_df, osto_df, tsto_df, msto_df]) 
    print(df)

    colors = [color1, color2, color3, color4, color5, color6, color7]
    hatches = ['////', '----', 'xxxx', 'OOOO', '++++', '....', r'\\\\']

    pivot_df = df.pivot(index='num_warehouses', columns='database', values='throughput')
    pivot_df = pivot_df[['epic', 'gacco', 'osto', 'tsto', 'msto', 'caracal']]

    fig, ax = plt.subplots(figsize=(12, 10))
    bars = pivot_df.plot(kind='bar', width=0.8, edgecolor=colors, ax=ax)

    # Applying hatches and making bars' face color transparent
    for bar_container, hatch, edge_color in zip(ax.containers, hatches, colors):
        for bar in bar_container:
            bar.set_hatch(hatch)
            bar.set_facecolor('none')  # Making the face color transparent
            bar.set_edgecolor(edge_color)  # Set the edge color the same as hatch

    ax.set_ylabel("Throughput (txn/s)")
    ax.set_xlabel("Number of Warehouses")
    ax.set_title("TPCC NP Throughput")
    ax.legend(loc='upper left')
    ax.set_ylim(0, 35)
    for container in ax.containers:
        ax.bar_label(container, label_type='edge', rotation=90, padding=3)
        
    fig = ax.get_figure()
    fig.savefig(f"{output_path}/05a_tpccnp_throughput.png", dpi=600)

def tpcc_gacco_commutative():
    gacco_df = pd.read_csv(f"{input_path}/epic/gacco_tpcc_commutative.csv")
    gacco_df = gacco_df[['num_warehouses', 'throughput']]
    gacco_df['database'] = 'gacco commutative'
    print(gacco_df)
    
    pivot_df = gacco_df.pivot(index='num_warehouses', columns='database', values='throughput')
    ax = pivot_df.plot(kind='bar', figsize=(12, 10), width=0.8, hatch='xx', facecolor='none', edgecolor=color8)
    ax.set_ylabel("Throughput (txn/s)")
    ax.set_xlabel("Number of Warehouses")
    ax.set_title("TPCC NP Throughput")
    ax.legend(loc='upper left')
    ax.set_ylim(0, pivot_df.values.max() * 1.2)
    for container in ax.containers:
        ax.bar_label(container, label_type='edge', rotation=90, padding=3)
    fig = ax.get_figure()
    fig.savefig(f"{output_path}/05b_tpccnp_throughput_gacco_commutative.png", dpi=600)
    

def tpccfull_throughput():
    epic_df = pd.read_csv(f"{input_path}/epic/epic_tpccfull.csv")
    epic_df = epic_df[['num_warehouses', 'throughput']]
    epic_df['database'] = 'epic'
    print(epic_df)

    caracal_df = pd.read_csv(f"{input_path}/caracal/tpccfull/caracal_tpcc.csv")
    caracal_df = caracal_df[['num_warehouses', 'throughput']]
    caracal_df['database'] = 'caracal'
    print(caracal_df)

    osto_df = pd.read_csv(f"{input_path}/sto/tpccfull_default.csv")
    osto_df = osto_df[['num_warehouses', 'throughput']]
    osto_df['database'] = 'osto'
    print(osto_df)

    tsto_df = pd.read_csv(f"{input_path}/sto/tpccfull_tictoc.csv")
    tsto_df = tsto_df[['num_warehouses', 'throughput']]
    tsto_df['database'] = 'tsto'
    print(tsto_df)

    msto_df = pd.read_csv(f"{input_path}/sto/tpccfull_mvcc.csv")
    msto_df = msto_df[['num_warehouses', 'throughput']]
    msto_df['database'] = 'msto'
    print(msto_df)

    df = pd.concat([epic_df, caracal_df, osto_df, tsto_df, msto_df]) 
    print(df)

    colors = [color1, color3, color4, color5, color6, color7]
    hatches = ['////', 'xxxx', 'OOOO', '++++', '....', r'\\\\']

    pivot_df = df.pivot(index='num_warehouses', columns='database', values='throughput')
    pivot_df = pivot_df[['epic', 'osto', 'tsto', 'msto', 'caracal']]

    fig, ax = plt.subplots(figsize=(12, 10))
    bars = pivot_df.plot(kind='bar', width=0.8, edgecolor=colors, ax=ax)

    # Applying hatches and making bars' face color transparent
    for bar_container, hatch, edge_color in zip(ax.containers, hatches, colors):
        for bar in bar_container:
            bar.set_hatch(hatch)
            bar.set_facecolor('none')  # Making the face color transparent
            bar.set_edgecolor(edge_color)  # Set the edge color the same as hatch

    ax.set_ylabel("Throughput (txn/s)")
    ax.set_xlabel("Number of Warehouses")
    ax.set_title("TPCC Throughput")
    ax.legend(loc='upper left')
    ax.set_ylim(0, 35)
    for container in ax.containers:
        ax.bar_label(container, label_type='edge', rotation=90, padding=3)
        
    fig = ax.get_figure()
    fig.savefig(f"{output_path}/04_tpccfull_throughput.png", dpi=600)

def ycsb_throughput():
    def ycsb_workload(ax, workload):
        epic_df = pd.read_csv(f"{input_path}/epic/epic_{workload}_default.csv")
        epic_df = epic_df[['alpha', 'throughput']]
        epic_df['database'] = 'epic'
        epic_df['index'] = range(1, 9)
        print(epic_df)

        epic_split_df = pd.read_csv(f"{input_path}/epic/epic_{workload}_split.csv")
        epic_split_df = epic_split_df[['alpha', 'throughput']]
        epic_split_df['database'] = 'epic+field split'
        epic_split_df['index'] = range(1, 9)
        print(epic_split_df)
    
        gacco_df = pd.read_csv(f"{input_path}/epic/gacco_{workload}.csv")
        gacco_df = gacco_df[['alpha', 'throughput']]
        gacco_df['database'] = 'gacco'
        gacco_df['index'] = range(1, 9)
        print(gacco_df)

        caracal_df = pd.read_csv(f"{input_path}/caracal/ycsb/caracal_{workload}_full.csv")
        caracal_df = caracal_df[['alpha', 'throughput']]
        caracal_df['database'] = 'caracal'
        caracal_df['index'] = range(1, 9)
        print(caracal_df)

        osto_df = pd.read_csv(f"{input_path}/sto/default_{workload}_full.csv")
        osto_df = osto_df[['alpha', 'throughput']]
        osto_df['database'] = 'osto'
        osto_df['index'] = range(1, 9)
        print(osto_df)

        tsto_df = pd.read_csv(f"{input_path}/sto/tictoc_{workload}_full.csv")
        tsto_df = tsto_df[['alpha', 'throughput']]
        tsto_df['database'] = 'tsto'
        tsto_df['index'] = range(1, 9)
        print(tsto_df)

        msto_df = pd.read_csv(f"{input_path}/sto/mvcc_{workload}_full.csv")
        msto_df = msto_df[['alpha', 'throughput']]
        msto_df['database'] = 'msto'
        msto_df['index'] = range(1, 9)
        print(msto_df)

        df = pd.concat([epic_df, gacco_df, epic_split_df, caracal_df, osto_df, tsto_df, msto_df])

        colors = [color1, color9, color2, color3, color4, color5, color6]
        markers = ['s', 's', 'd', '*', '2', 'x', 'o']  # Circle, Square, Triangle up, Diamond, Pentagon, Star, Hexagon
        fillstyles = ['full', 'none', 'none', 'full', 'full', 'full', 'none']  # Various fill styles
        line_cycler = cycler(color=colors) + cycler(marker=markers) + cycler(fillstyle=fillstyles)

        # Pivot the DataFrame
        pivot_df = df.pivot(index='index', columns='database', values='throughput')
        pivot_df = pivot_df[['epic', 'epic+field split', 'gacco', 'osto', 'tsto', 'msto', 'caracal']]

        ax.set_prop_cycle(line_cycler)
        pivot_df.plot(ax=ax)

        # Customizing x-ticks
        ax.set_xticks(range(1, 9))  # Setting x-ticks to range from 1 to 9
        ax.set_xticklabels(epic_df['alpha'].to_list())  # Labeling x-ticks from 1 to 9
        ax.set_title(workload.upper())
        ax.set_ylabel("Throughput (txn/s)")
        ax.set_xlabel("Zipfian Contention Factor $\\theta$")
        ax.set_ylim(0, 50)
        h, l = ax.get_legend_handles_labels()
        reorder = lambda l, nc: sum((l[i::nc] for i in range(nc)), []) # Reorder the legend to row major order
        ax.legend(reorder(h, 3), reorder(l, 3), loc='upper center', bbox_to_anchor=(0.5, 1.5), ncol=3)

    fig, axs = plt.subplots(1, 4, figsize=(20, 7))
    ycsb_workload(axs[0], "ycsba")
    ycsb_workload(axs[1], "ycsbb")
    ycsb_workload(axs[2], "ycsbc")
    ycsb_workload(axs[3], "ycsbf")
    fig.tight_layout(rect=[0, 0.03, 1, 0.98])
    fig.suptitle("YCSB Throughput")
    fig.savefig(f"{output_path}/06_ycsb_throughput.png", dpi=600)

def cpu_throughput():
    def tpcc_workload(ax, workload, workload_name):
        epic_df = pd.read_csv(f"{input_path}/epic/epic_{workload}.csv")
        epic_df = epic_df[['num_warehouses', 'throughput']]
        epic_df['database'] = 'epic'
        print(epic_df)

        epic_cpu_df = pd.read_csv(f"{input_path}/epic/epic_cpu_{workload}.csv")
        epic_cpu_df = epic_cpu_df[['num_warehouses', 'throughput']]
        epic_cpu_df['database'] = 'epic cpu'
        print(epic_df)

        colors = [color1, color9]
        hatches = ['////', r'\\\\']

        df = pd.concat([epic_df, epic_cpu_df])
        pivot_df = df.pivot(index='num_warehouses', columns='database', values='throughput')
        pivot_df = pivot_df[['epic', 'epic cpu']]
        bars = pivot_df.plot(kind='bar', width=0.8, edgecolor=colors, ax=ax)

        # Applying hatches and making bars' face color transparent
        for bar_container, hatch, edge_color in zip(ax.containers, hatches, colors):
            for bar in bar_container:
                bar.set_hatch(hatch)
                bar.set_facecolor('none')  # Making the face color transparent
                bar.set_edgecolor(edge_color)  # Set the edge color the same as hatch

        ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=2)
        ax.set_xlabel("Number of Warehouses")
        ax.set_title(workload_name)
        ax.set_ylim(0, 35)
        for container in ax.containers:
            ax.bar_label(container, label_type='edge', rotation=90, padding=3)

        
    def ycsb_workload(ax, workload):
        epic_df = pd.read_csv(f"{input_path}/epic/epic_{workload}_default.csv")
        epic_df = epic_df[['alpha', 'throughput']]
        epic_df['database'] = 'epic'
        epic_df['index'] = range(1, 9)
        print(epic_df)

        epic_cpu_df = pd.read_csv(f"{input_path}/epic/epic_cpu_{workload}.csv")
        epic_cpu_df = epic_cpu_df[['alpha', 'throughput']]
        epic_cpu_df['database'] = 'epic cpu'
        epic_cpu_df['index'] = range(1, 9)
        print(epic_cpu_df)

        df = pd.concat([epic_df, epic_cpu_df])
        # Pivot the DataFrame
        pivot_df = df.pivot(index='index', columns='database', values='throughput')
        pivot_df = pivot_df[['epic', 'epic cpu']]

        colors = [color1, color9]
        markers = ['s', 's']  # Circle, Square, Triangle up, Diamond, Pentagon, Star, Hexagon
        fillstyles = ['full', 'none']  # Various fill styles
        line_cycler = cycler(color=colors) + cycler(marker=markers) + cycler(fillstyle=fillstyles)

        ax.set_prop_cycle(line_cycler)
        pivot_df.plot(ax=ax)

        # Customizing x-ticks
        ax.set_xticks(range(1, 9))  # Setting x-ticks to range from 1 to 9
        ax.set_xticklabels(epic_df['alpha'].to_list())  # Labeling x-ticks from 1 to 9
        ax.set_title(workload.upper())
        ax.set_ylabel("Throughput (txn/s)")
        ax.set_xlabel("Zipfian Contention Factor $\\theta$")
        ax.set_ylim(0, 50)
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=4)
        
    fig, axs = plt.subplots(2, 2, figsize=(14, 14))
    tpcc_workload(axs[0,0], "tpccfull", "TPCC")
    tpcc_workload(axs[0,1], "tpcc", "TPCC NP")
    ycsb_workload(axs[1,0], "ycsbc")
    ycsb_workload(axs[1,1], "ycsbf")
    fig.tight_layout(rect=[0, 0.03, 1, 0.98])
    fig.suptitle("Epic CPU vs. GPU Throughput")
    fig.savefig(f"{output_path}/07_cpu_throughput.png", dpi=600)

def latency(): 
    def ycsb_workload(ax, workload, caracal_workload, ymax, workload_name):
        epic_df = pd.read_csv(f"{input_path}/epic/epic_{workload}_epoch_size.csv")
        epic_df = epic_df[['latency', 'throughput']]
        epic_df['database'] = 'epic'
        print(epic_df)

        gacco_df = pd.read_csv(f"{input_path}/epic/gacco_{workload}_epoch_size.csv")
        gacco_df = gacco_df[['latency', 'throughput']]
        gacco_df['database'] = 'gacco'
        print(gacco_df)

        caracal_df = pd.read_csv(f"{input_path}/caracal/{caracal_workload[0]}/caracal_{caracal_workload[1]}_latency.csv")
        caracal_df = caracal_df[['latency', 'throughput']]
        caracal_df['database'] = 'caracal'
        print(caracal_df)

        colors = [color1, color2, color6]
        markers = ['s', 'd', 'o']  # Circle, Square, Triangle up, Diamond, Pentagon, Star, Hexagon
        fillstyles = ['full', 'none', 'none']  # Various fill styles
        line_cycler = cycler(color=colors) + cycler(marker=markers) + cycler(fillstyle=fillstyles)

        ax.set_prop_cycle(line_cycler)
        ax.plot(epic_df['throughput'], epic_df['latency'], label='epic')
        ax.plot(gacco_df['throughput'], gacco_df['latency'], label='gacco')
        ax.plot(caracal_df['throughput'], caracal_df['latency'], label='caracal')

        # Customizing x-ticks
        ax.set_title(workload_name)
        ax.set_ylabel("Latency (ms)")
        ax.set_xlabel("Throughput (MTxns/s)")
        ax.set_ylim(0, ymax)
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=4)
        
    fig, axs = plt.subplots(2, 2, figsize=(14, 14))
    ycsb_workload(axs[0,0], "tpcc_1", ["tpcc", "tpcc_1"], 25, r"TPC-C NP Single Warehouse")
    ycsb_workload(axs[0,1], "tpcc_64", ["tpcc", "tpcc_64"], 10, r"TPC-C NP 64 Warehouses")
    ycsb_workload(axs[1,0], "ycsbf_0.99", ["ycsb", "ycsbf_99"], 25, r"YCSB F Zipfian $\theta = 0.99$")
    ycsb_workload(axs[1,1], "ycsbf_0.0", ["ycsb", "ycsbf_0"], 10, r"YCSB F Zipfian $\theta = 0.0$")
    fig.tight_layout(rect=[0, 0.03, 1, 0.98])
    fig.suptitle("Latency vs. Throughput")
    fig.savefig(f"{output_path}/09_latency.png", dpi=600)
    

def microbenchmark():
    fig, axs = plt.subplots(1, 2, figsize=(14, 7))

    micro_df = pd.read_csv(f"{input_path}/epic/epic_microbenchmark.csv")

    axs[0].plot(micro_df['abort_rate'][:5], micro_df['throughput'][:5], marker='2', markersize=10)
    _, ymax = axs[0].get_ylim()
    axs[0].set_ylim([0, ymax * 1.2])
    axs[0].set_ylabel("Throughput (MTxn/s)")
    axs[0].set_xlabel("Abort Rate (%)")
    axs[0].set_xticks(range(0, 25, 5))

    axs[1].plot(micro_df['abort_rate'][:5], micro_df['latency'][:5], marker='2', markersize=10)
    _, ymax = axs[1].get_ylim()
    axs[1].set_ylim([0, ymax * 1.2])
    axs[1].set_ylabel("Average Latency (ms)")
    axs[1].set_xlabel("Abort Rate (%)")
    axs[1].set_xticks(range(0, 25, 5))

    fig.suptitle("Impact of Abort Rate")

    fig.savefig(f"{output_path}/10_microbenchmark.png", dpi=600)

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python3 generate_plots.py <input_dir> <output_dir>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"The directory {input_path} does not exist.")

    # Check if the directory exists
    if not os.path.exists(output_path):
        # If not, create the directory
        os.makedirs(output_path)
    
    microbenchmark()
    latency()
    cpu_throughput()
    ycsb_throughput()
    tpcc_throughput()
    tpcc_gacco_commutative()
    tpccfull_throughput()