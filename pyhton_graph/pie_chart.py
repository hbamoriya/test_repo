import matplotlib.pyplot as mp
def piee():
    x=['eat','sleep','code','bing']
    y=[3,8,8,5]
    colors=['red','blue','skyblue','orange']
    mp.pie(y, labels = x , colors = colors, startangle = 90, shadow=True, explode=(0,0,0.1,0),radius=1.2,autopct='%1.1f%%')
    mp.legend()
    mp.show()