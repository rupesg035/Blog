from django.shortcuts import render
from datetime import date

# Create your views here.

all_posts=[
            {
                "slug":"hike-in-the-mountains",
                "image":"mountains.jpg",
                "author":"RR",
                "date": date(2023,4,15),
                "title":"Mountain Hiking",
                "excerpt":      """There's nothing like views of mountain hiking
                                There's nothing like views of mountain hiking
                                There's nothing like views of mountain hiking""",

                "content":"""Where can we find the courage to act in spite of fear?
                        Trying to eliminate that which we react to fearfully is a fool's errand 
                        because it locates the source of our fear outside ourselves, 
                        rather than within our own hearts."""


            },
            {
                "slug":"hike-in-the-mountains-2",
                "image":"mountains.jpg",
                "author":"RR",
                "date": date(2023,1,15),
                "title":"Mountain Hiking-2",
                "excerpt":      """2-There's nothing like views of mountain hiking
                                There's nothing like views of mountain hiking
                                There's nothing like views of mountain hiking""",

                "content":"""2-Where can we find the courage to act in spite of fear?
                        Trying to eliminate that which we react to fearfully is a fool's errand 
                        because it locates the source of our fear outside ourselves, 
                        rather than within our own hearts."""


            },

            {
                "slug":"hike-in-the-mountains-3",
                "image":"mountains.jpg",
                "author":"RR",
                "date": date(2023,8,15),
                "title":"Mountain Hiking-3",
                "excerpt":      """3-There's nothing like views of mountain hiking
                                There's nothing like views of mountain hiking
                                There's nothing like views of mountain hiking""",

                "content":"""3-Where can we find the courage to act in spite of fear?
                        Trying to eliminate that which we react to fearfully is a fool's errand 
                        because it locates the source of our fear outside ourselves, 
                        rather than within our own hearts."""


             }
]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts=sorted(all_posts ,key=get_date)
    latest_posts=sorted_posts[-3:]
    return render(request , "blog/index.html" , 
                  {"posts":latest_posts})
                  


def posts(request):
    return render(request,"blog/all-posts.html")

def post_detail(request , slug):
    return render(request,"blog/post-detail.html")