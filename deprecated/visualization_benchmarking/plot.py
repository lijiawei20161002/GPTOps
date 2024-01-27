'''
import matplotlib.pyplot as plt
import numpy as np

# Data for Microsoft Philly
philly_data = [
    {'Compression Ratio': 0.17777777777777778, 'Keyword Coverage': 0.8, 'Coherence': 0.21378278138581663, 'Consistency': 1.0},
    {'Compression Ratio': 0.19722222222222222, 'Keyword Coverage': 0.8, 'Coherence': 0.24288863688707352, 'Consistency': 1.0},
    {'Compression Ratio': 0.21944444444444444, 'Keyword Coverage': 1.0, 'Coherence': 0.32127072662115097, 'Consistency': 1.0},
    {'Compression Ratio': 0.21666666666666667, 'Keyword Coverage': 0.8, 'Coherence': 0.23380118076290404, 'Consistency': 1.0},
    {'Compression Ratio': 0.2222222222222222, 'Keyword Coverage': 1.0, 'Coherence': 0.21764526143670082, 'Consistency': 1.0},
    {'Compression Ratio': 0.19166666666666668, 'Keyword Coverage': 0.8, 'Coherence': 0.19449343656500181, 'Consistency': 1.0},
    {'Compression Ratio': 0.18055555555555555, 'Keyword Coverage': 1.0, 'Coherence': 0.35197418089956045, 'Consistency': 1.0},
]

# Data for Google
google_data = [
    {'Compression Ratio': 0.75, 'Keyword Coverage': 0.8, 'Coherence': 0.3701722212135792, 'Consistency': 1.0},
    {'Compression Ratio': 0.8333333333333334, 'Keyword Coverage': 0.8, 'Coherence': 0.35845327164445606, 'Consistency': 1.0},
    {'Compression Ratio': 0.7583333333333333, 'Keyword Coverage': 0.8, 'Coherence': 0.4197416177817753, 'Consistency': 1.0},
    {'Compression Ratio': 0.7666666666666667, 'Keyword Coverage': 0.8, 'Coherence': 0.5180843412876129, 'Consistency': 1.0},
    {'Compression Ratio': 0.5583333333333333, 'Keyword Coverage': 0.8, 'Coherence': 0.39758314564824104, 'Consistency': 1.0},
    {'Compression Ratio': 0.8083333333333333, 'Keyword Coverage': 0.6, 'Coherence': 0.4495258629322052, 'Consistency': 1.0},
    {'Compression Ratio': 0.5333333333333333, 'Keyword Coverage': 0.8, 'Coherence': 0.5539767444133759, 'Consistency': 1.0},
    {'Compression Ratio': 0.6666666666666666, 'Keyword Coverage': 0.6, 'Coherence': 0.3481554239988327, 'Consistency': 1.0},
    {'Compression Ratio': 0.7083333333333334, 'Keyword Coverage': 0.6, 'Coherence': 0.46765619250280516, 'Consistency': 1.0},
    {'Compression Ratio': 0.575, 'Keyword Coverage': 0.8, 'Coherence': 0.4553368613123894, 'Consistency': 1.0},
    {'Compression Ratio': 0.5333333333333333, 'Keyword Coverage': 0.8, 'Coherence': 0.2682238593697548, 'Consistency': 1.0},
    {'Compression Ratio': 0.6, 'Keyword Coverage': 1.0, 'Coherence': 0.4084796868264675, 'Consistency': 1.0},
    {'Compression Ratio': 0.8083333333333333, 'Keyword Coverage': 0.8, 'Coherence': 0.4286588728427887, 'Consistency': 1.0},
    {'Compression Ratio': 0.6166666666666667, 'Keyword Coverage': 0.6, 'Coherence': 0.3745698630809784, 'Consistency': 1.0},
    {'Compression Ratio': 0.6833333333333333, 'Keyword Coverage': 0.6, 'Coherence': 0.43573516820158276, 'Consistency': 1.0},
    {'Compression Ratio': 0.8166666666666667, 'Keyword Coverage': 0.6, 'Coherence': 0.3935476038604975, 'Consistency': 1.0},
    {'Compression Ratio': 0.7416666666666667, 'Keyword Coverage': 0.8, 'Coherence': 0.3410151666030288, 'Consistency': 1.0},
    {'Compression Ratio': 0.48333333333333334, 'Keyword Coverage': 0.6, 'Coherence': 0.21919954381883144, 'Consistency': 1.0},
    {'Compression Ratio': 0.6833333333333333, 'Keyword Coverage': 0.8, 'Coherence': 0.3247965037822723, 'Consistency': 1.0},
    {'Compression Ratio': 0.6666666666666666, 'Keyword Coverage': 1.0, 'Coherence': 0.3566593199968338, 'Consistency': 1.0},
    {'Compression Ratio': 0.7083333333333334, 'Keyword Coverage': 0.8, 'Coherence': 0.5140129774808884, 'Consistency': 1.0},
    {'Compression Ratio': 0.8083333333333333, 'Keyword Coverage': 0.8, 'Coherence': 0.3764305993914604, 'Consistency': 1.0},
    {'Compression Ratio': 0.6833333333333333, 'Keyword Coverage': 0.6, 'Coherence': 0.3371141832321882, 'Consistency': 1.0},
    {'Compression Ratio': 1.0, 'Keyword Coverage': 1.0, 'Coherence': 0.4528310876339674, 'Consistency': 1.0},
    {'Compression Ratio': 0.7083333333333334, 'Keyword Coverage': 0.6, 'Coherence': 0.3946269580296108, 'Consistency': 1.0},
    {'Compression Ratio': 0.675, 'Keyword Coverage': 1.0, 'Coherence': 0.47393527839865, 'Consistency': 1.0},
    {'Compression Ratio': 0.625, 'Keyword Coverage': 0.8, 'Coherence': 0.5097645265715463, 'Consistency': 1.0},
    {'Compression Ratio': 0.6166666666666667, 'Keyword Coverage': 1.0, 'Coherence': 0.32877930253744125, 'Consistency': 1.0},
    {'Compression Ratio': 0.8083333333333333, 'Keyword Coverage': 0.8, 'Coherence': 0.3701722212135792, 'Consistency': 1.0},
    {'Compression Ratio': 0.7166666666666667, 'Keyword Coverage': 0.8, 'Coherence': 0.4653483852810764, 'Consistency': 1.0},
    {'Compression Ratio': 0.7333333333333333, 'Keyword Coverage': 0.8, 'Coherence': 0.4302812548730226, 'Consistency': 1.0},
    {'Compression Ratio': 0.7916666666666666, 'Keyword Coverage': 0.8, 'Coherence': 0.3453452426458895, 'Consistency': 1.0},
    {'Compression Ratio': 0.6833333333333333, 'Keyword Coverage': 0.8, 'Coherence': 0.3451424376885134, 'Consistency': 1.0},
    {'Compression Ratio': 0.7416666666666667, 'Keyword Coverage': 0.8, 'Coherence': 0.4108702353739866, 'Consistency': 1.0},
    {'Compression Ratio': 0.8333333333333334, 'Keyword Coverage': 0.8, 'Coherence': 0.4567344345740309, 'Consistency': 1.0},
    {'Compression Ratio': 0.8083333333333333, 'Keyword Coverage': 0.8, 'Coherence': 0.3756401017065635, 'Consistency': 1.0},
    {'Compression Ratio': 0.8083333333333333, 'Keyword Coverage': 0.8, 'Coherence': 0.4400933286377411, 'Consistency': 1.0},
    {'Compression Ratio': 0.8083333333333333, 'Keyword Coverage': 0.8, 'Coherence': 0.4108905949155092, 'Consistency': 1.0},
    {'Compression Ratio': 0.6833333333333333, 'Keyword Coverage': 0.8, 'Coherence': 0.35845327164445606, 'Consistency': 1.0},
    {'Compression Ratio': 0.7083333333333334, 'Keyword Coverage': 0.8, 'Coherence': 0.4561344356625089, 'Consistency': 1.0},
    {'Compression Ratio': 0.7583333333333333, 'Keyword Coverage': 0.8, 'Coherence': 0.4781329874565601, 'Consistency': 1.0},
    {'Compression Ratio': 0.8166666666666667, 'Keyword Coverage': 0.8, 'Coherence': 0.4158905949155092, 'Consistency': 1.0},
    {'Compression Ratio': 0.8083333333333333, 'Keyword Coverage': 0.8, 'Coherence': 0.4158905949155092, 'Consistency': 1.0},
    {'Compression Ratio': 0.8333333333333334, 'Keyword Coverage': 0.8, 'Coherence': 0.4653483852810764, 'Consistency': 1.0},
    {'Compression Ratio': 0.8083333333333333, 'Keyword Coverage': 0.8, 'Coherence': 0.4756401017065635, 'Consistency': 1.0},
    {'Compression Ratio': 0.7583333333333333, 'Keyword Coverage': 0.8, 'Coherence': 0.35845327164445606, 'Consistency': 1.0},
]


# Calculate average metrics for Microsoft Philly
philly_avg_metrics = {
    'Compression Ratio': np.mean([d['Compression Ratio'] for d in philly_data]),
    'Keyword Coverage': np.mean([d['Keyword Coverage'] for d in philly_data]),
    'Coherence': np.mean([d['Coherence'] for d in philly_data]),
    'Consistency': np.mean([d['Consistency'] for d in philly_data]),
}

# Calculate average metrics for Google
google_avg_metrics = {
    'Compression Ratio': np.mean([d['Compression Ratio'] for d in google_data]),
    'Keyword Coverage': np.mean([d['Keyword Coverage'] for d in google_data]),
    'Coherence': np.mean([d['Coherence'] for d in google_data]),
    'Consistency': np.mean([d['Consistency'] for d in google_data]),
}

# Plot results
labels = ['Compression Ratio', 'Keyword Coverage', 'Coherence', 'Consistency']
philly_avgs = list(philly_avg_metrics.values())
google_avgs = list(google_avg_metrics.values())

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, philly_avgs, width, label='Microsoft Philly', color='skyblue')
rects2 = ax.bar(x + width/2, google_avgs, width, label='Google Cluster', color='lightgreen', hatch='/')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores', fontsize=14)
ax.set_title('Average metrics for Microsoft Philly and Google Cluster')
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=12, rotation=15)
ax.legend(fontsize=12)

fig.tight_layout()

plt.grid()
plt.savefig('test.png')
'''

import matplotlib.pyplot as plt
import numpy as np

# Data
models = ['GPTOps', 'Polluted Raw Data', 'Vague Summary', 'Wrong Prediction']
datasets = ['Task 1', 'Task 2', 'Task 3', 'Task 4']
accuracy = np.array([[0.91, 0.85, 0.88, 0.73], [0.92, 0.88, 0.89, 0.69], [0.94, 0.82, 0.87, 0.72], [0.93, 0.8, 0.9, 0.7]])
accuracy = accuracy.transpose()

# Plotting
fig, ax = plt.subplots(figsize=(15, 8))

barWidth = 0.15  # Adjust bar width to fit all bars
r1 = np.arange(len(accuracy[0]))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]

# Plotting each group
bars1 = plt.bar(r1, accuracy[0], width=barWidth, edgecolor='grey', label=models[0], color='lightgreen')
bars2 = plt.bar(r2, accuracy[1], width=barWidth, edgecolor='grey', label=models[1], color='skyblue', hatch='/')
bars3 = plt.bar(r3, accuracy[2], width=barWidth, edgecolor='grey', label=models[2], color='lightpink', hatch='\\')
bars4 = plt.bar(r4, accuracy[3], width=barWidth, edgecolor='grey', label=models[3], color='lightyellow', hatch='-')

# Setting the x-axis labels and title
plt.xlabel('Tasks', fontweight='bold', fontsize=14)
plt.xticks([r + 1.5*barWidth for r in range(len(accuracy[0]))], datasets, fontsize=14)
plt.title('Performance Scores on 4 Tasks with Five Shot Learning', fontsize=16)
plt.ylabel('Score', fontweight='bold', fontsize=14)

# Adjusting the y-axis limit
plt.ylim(0, 1)

# Adding the grid and legend
plt.grid(axis='y')
plt.legend()

# Saving the plot
plt.savefig('accuracy_comparison.png')
plt.show()
