from django.shortcuts import render,redirect

from .forms import PostForm, ContributionForm
from .models import Post,Contribution
# Create your views here.


#create Post view
def create_view(request):

    if request.method == 'POST':

        obj = PostForm(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('home-path')

    return render(request, 'blog/create.html', {'form' : PostForm()})


#list Post view

def list_view(request):


    return render(request, 'blog/list.html', {'posts': Post.objects.all()})



#detail Post view

def detail_view(request, post_pk):


    return render(request, 'blog/detail.html', {'post': Post.objects.get(id = post_pk)})



# update Post view

def update_view(request, post_pk):

    if request.method == 'POST':
        obj = PostForm(request.POST, instance = Post.objects.get(id = post_pk))
        if obj.is_valid():
            obj.save()
            return redirect('home-path')

    return render(request, 'blog/update.html', {'form' : PostForm(instance = Post.objects.get(id = post_pk))})



# delete Post view

def delete_view(request, post_pk):



    obj = Post.objects.get(id = post_pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('home-path')
    return render(request, 'blog/delete.html', {'post' : Post.objects.get(id = post_pk) })
    #############################################################################
    
    #list the post's contributions

def contributionlist_view(request, post_pk):
    #get the post we want to fetch its contributers
    obj = Post.objects.get(id = post_pk)

    #get the contributions registered for that Post
    contribs = Contribution.objects.filter(post = obj)

    # sending it to the template

    return render(request,'blog/contributionlist.html',{'contribs' : contribs,'post':obj})


#adding a contribution to a post

def contributioncreate_view(request, post_pk):
    if request.method == 'POST':
        #catch the created contribution 
        obj_contrib = ContributionForm(request.POST)
        if obj_contrib.is_valid():
            #create a Contribution object but  not saving it because it does not contain
            #the post object yet
            contrib = obj_contrib.save(False)
            #create the Post object and add it to the Contribution object
            contrib.post = Post.objects.get(id = post_pk)
            # save the new  Contribution
            contrib.save()
            #show  the list of contributions of the specific post
            return redirect('contributionlist-path',contrib.post.pk)
    return render(request, 'blog/contributioncreate.html', {'form' : ContributionForm()})

# def contributionupdate_view(request, post_pk):
    
#     if request.method == 'POST':
#         obj = ContributionForm(request.POST)
#         if obj.is_valid():
#             obj.save()
#             return redirect('home-path')

#     return render(request, 'blog/contributionlist.html', {'form' : ContributionForm()})


