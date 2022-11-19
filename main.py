import matplotlib.pyplot as plt
import psutil as p
app_name_dict = {}
COUNT = 0
for x in p.process_iter():
    COUNT = COUNT + 1
    if COUNT <= 6 :
        name = x.name()
        cpu_usage = p.cpu_percent()
        print("Name: "+name+"--Usage: "+str(cpu_usage))
        app_name_dict.update({name:cpu_usage})
        keymax = max(app_name_dict,key=app_name_dict.get)
        keymin = min(app_name_dict,key=app_name_dict.get)
        name_list = [keymin,keymax]
        print(name_list)
        app = app_name_dict.values()
        MAXAPP = 100 #max(app)
        minapp = min(app)
        print(str(MAXAPP)+" | "+str(minapp))
        minax_list = [minapp,MAXAPP]
plt.figure(figsize=(19,10))
plt.xlabel("App")
plt.ylabel("Usage")
plt.bar(name_list,minax_list,0.5,color = ("blue","red"))
plt.show()
