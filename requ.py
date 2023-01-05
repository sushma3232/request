
import requests
import json
def request():
    ax= requests.get("http://saral.navgurukul.org/api/courses")
    x=ax.json()
    # print("")
    with open("courses.json","w") as f:
        json.dump(x,f,indent=4)
    with open("courses.json","r") as f:
        data = json.load(f)
    id= [] 
    i = 0
    while i < len(data['availableCourses'])-1:
        print(i+1,"",data['availableCourses'][i]['name'],"=",data['availableCourses'][i]['id'])
        id.append(data['availableCourses'][i]['id'])
        i+=1 
    
    user= int(input("enter the id number:"))
    n1=requests.get("http://saral.navgurukul.org/api/courses/"+str(id[user])+"/exercises")
    a=n1.json()
    j=0
    l=0
    slug=[]
    # child=[]
    while j<len(a["data"]):
        print(l+1,"=",a["data"][j]["name"])
        slug.append(a['data'][j]["slug"])
        # child.append(a['data'][j]["childExercises"])
        
        l=l+1
        j=j+1
    # Child=int(input("enter the child number:"))
    slugname=int(input("Enter your slug number:"))
    list=requests.get("http://saral.navgurukul.org/api/courses/"+ str(user)+"/exercise/getBySlug?slug=" + slug[slugname])
    b=list.json()
    # with open("course_id.json","w") as f:
    #     json.dump(b,f,indent=4)
    # with open("slunglist.json","r") as f:
    #     d=json.load(f)
        
    print(b["name"])
    print(b["slug"])
    print("CONTENT",b["content"])
    for i in range(len(slug)):
        # while i<len(Child):
            s = input("enter the 'n' for next : ")
            if s == "n":
                i=0
                if i < len(slug):
                    # while i<len(Child):
                    print(slug[i])
                        # print(Child[i])
                    print(b["content"]) 
                    break
            else:
                print(":( your page is not  found")
                i=i+1
                print("*")
            g=input("your request accpect:")
            if  g=="yes":
                print("oke then your exist ")
            else:
                print("your req not accpect")
        # elif 
        #     i=0
        #     if i>= 0: 
        #         print(slug[i])
        #         print(b["content"])
        #     else:
        #         print("page not found")
        #         break
        #     i=i-1
        #     print("*")
        # else:
        #     print("invalid input")
        #     break
request()