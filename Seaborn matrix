rs = np.random.RandomState(33)
d = pd.DataFrame(data=rs.normal(size=(100, 26)),
                 columns=list(letters[:26]))
tcorr = d.corr()

#Draw matrix SNS
def sns_heatmap(input_data, graph_title):
    sns.set(style="white")
    temp = input_data    
    xcorr = temp
    mask = np.zeros_like(xcorr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    f, ax = plt.subplots(figsize=(20, 15))
    #cmap = sns.diverging_palette(240, 10, l=25, as_cmap=True)
    sns.set(font_scale=1.5)
    #annot=True/False (Adds Values in squares)
    sns.heatmap(xcorr, vmin=-0.4, vmax=0.9, center=0, annot=False, annot_kws={"size":10}, fmt=".2f", 
                mask=mask, cmap='RdBu_r', square=True, xticklabels=True, 
                yticklabels=True, label='big', linewidths=0.1, cbar_kws={"shrink": 0.5}, ax=ax) 
    plt.yticks(fontsize=13)
    plt.xticks(fontsize=13)
    plt.xlabel('Location', fontsize=16)
    plt.ylabel('Location', fontsize=16)
    plt.title(graph_title)
