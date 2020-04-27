from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

from . import models

def messages_view(request):
    """Private Page Only an Authorized User Can View, renders messages page
       Displays all posts and friends, also allows user to make new posts and like posts
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render private.djhtml
    """
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)
        count = request.session.get("post_view")
        # user_info = models.UserInfo.objects(request.user)
        #for post in models.Post.objects.all().order_by("-timestamp"):
        # posts.append(post)
        # TODO Objective 9: query for posts (HINT only return posts needed to be displayed)
        posts = []
        for post in models.Post.objects.all().order_by("-timestamp"):
            posts.append(post)

        # TODO Objective 10: check if user has like post, attach as a new attribute to each post



        context = { 'user_info' : user_info
                , 'posts' : posts[:count] }
        return render(request,'messages.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def account_view(request):
    """Private Page Only an Authorized User Can View, allows user to update
       their account information (i.e UserInfo fields), including changing
       their password
    Parameters
    ---------
      request: (HttpRequest) should be either a GET or POST
    Returns
    --------
      out: (HttpResponse)
                 GET - if user is authenticated, will render account.djhtml
                 POST - handle form submissions for changing password, or User Info
                        (if handled in this view)
    """
    if request.user.is_authenticated:

        # TODO Objective 3: Create Forms and Handle POST to Update UserInfo / Password
        
        user_info = models.UserInfo.objects.get(user = request.user)
        #context = { 'user_info' : user_info,
                    #'form' : form }
        if request.method == "POST":
            form = PasswordChangeForm(request.user,request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request,user)
                return redirect("login:login_view")
        else:
            form = PasswordChangeForm(request.user)
        #return render(request,'account.djhtml',context)
        context = { 'user_info' : user_info,
                    'form' : form }

        return render(request,'account.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def update_view(request):
  if request.user.is_authenticated:
      user_info = models.UserInfo.objects.get(user = request.user)
      if request.method == "GET":
        # if request.methof == "POST":
         #user_info.employment = request.POST.get("employment")
         # user_info.location = request.POST.get("location")
         # user_info.birthday = request.POST.get("birthday")
         # user_info.interests.add(models.Interest.objects.create(label = request.POST.get("interest")))
         #  user_info.save()         
          user_info.employment = request.GET.get("employment")
          user_info.location = request.GET.get("location")
          user_info.birthday = request.GET.get("birthday")
          user_info.interests.add(models.Interest.objects.create(label = request.GET.get("interest")))
          user_info.save()

          return redirect("social:account_view")

def people_view(request):
    """Private Page Only an Authorized User Can View, renders people page
       Displays all users who are not friends of the current user and friend requests
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render people.djhtml
    """
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)
        # TODO Objective 4: create a list of all users who aren't friends to the current user (and limit size)
        all_people = []
        count = request.session.get("ppl_view")
        #count = request.session["ppl_view"]
        for user in models.UserInfo.objects.all():
            if user not in user_info.friends.all():
                if user != user_info:
                    all_people.append(user)

        # TODO Objective 5: create a list of all friend requests to current user
        friend_requests = []
        # this_obj = models.UserInfo.objects.get(user_id)
        this_obj = models.UserInfo.objects.get(user_id = request.user.id)
        for friend in models.FriendRequest.objects.filter(to_user = this_obj):
            friend_requests.append(friend)

        sent_requests = []
        for user in models.FriendRequest.objects.filter(from_user = this_obj):
            sent_requests.append(user)

        context = { 'user_info' : user_info,
                    'all_people' : all_people[:count],
                    'friend_requests' : friend_requests,
                    'sent_requests': sent_requests}

        return render(request,'people.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def like_view(request):
    '''Handles POST Request recieved from clicking Like button in messages.djhtml,
       sent by messages.js, by updating the corrresponding entry in the Post Model
       by adding user to its likes field
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postID,
                                a string of format post-n where n is an id in the
                                Post model

	Returns
	-------
   	  out : (HttpResponse) - queries the Post model for the corresponding postID, and
                             adds the current user to the likes attribute, then returns
                             an empty HttpResponse, 404 if any error occurs
    '''
    postIDReq = request.POST.get('postID')
    if postIDReq is not None:
        # remove 'post-' from postID and convert to int
        # TODO Objective 10: parse post id from postIDReq
        #postID = 0
        if request.user.is_authenticated:
            # TODO Objective 10: update Post model entry to add user to likes field
            # user_info = models.UserInfo.objects.get(request.user)
            user_info = models.UserInfo.objects.get(user=request.user)
            if user_info not in models.Post.objects.get(id = postIDReq).likes.all():
                models.Post.objects.get(id = postIDReq).likes.add(user_info)
            else:
                models.Post.objects.get(id = postIDReq).likes.remove(user_info)
            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('like_view called without postID in POST')

def post_submit_view(request):
    '''Handles POST Request recieved from submitting a post in messages.djhtml by adding an entry
       to the Post Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postContent, a string of content

	Returns
	-------
   	  out : (HttpResponse) - after adding a new entry to the POST model, returns an empty HttpResponse,
                             or 404 if any error occurs
    '''
    user_in = models.UserInfo.objects.get(user = request.user)
    #postContent = request.POST.get('postContent')
    postContent = request.POST.get('post_text')
    if postContent is not None:
        if request.user.is_authenticated:

            # TODO Objective 8: Add a new entry to the Post model
            models.Post.objects.create(owner = user_in , content = postContent)
            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('post_submit_view called without postContent in POST')

def more_post_view(request):
    '''Handles POST Request requesting to increase the amount of Post's displayed in messages.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating hte num_posts sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of posts dispalyed

        # TODO Objective 9: update how many posts are displayed/returned by messages_view
        posts = request.session.get("post_view",1)
        request.session["post_view"] = posts + 1
        # return status='success'
        return HttpResponse()

    return redirect('login:login_view')

def more_ppl_view(request):
    '''Handles POST Request requesting to increase the amount of People displayed in people.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating the num ppl sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of people dispalyed

        # TODO Objective 4: increment session variable for keeping track of num ppl displayed

        # return status='success'
        ppl = request.session.get('ppl_view',1)
        request.session["ppl_view"] = ppl + 1
        return HttpResponse()

    return redirect('login:login_view')

def friend_request_view(request):
    '''Handles POST Request recieved from clicking Friend Request button in people.djhtml,
       sent by people.js, by adding an entry to the FriendRequest Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute frID,
                                a string of format fr-name where name is a valid username

	Returns
	-------
   	  out : (HttpResponse) - adds an etnry to the FriendRequest Model, then returns
                             an empty HttpResponse, 404 if POST data doesn't contain frID
    '''
    frID = request.POST.get('frID')
    if frID is not None:
        # remove 'fr-' from frID
        username = frID[3:]

        if request.user.is_authenticated:
            # TODO Objective 5: add new entry to FriendRequest
            friend_id = models.User.objects.get(username=username).id
            friend_obj = models.UserInfo.objects.get(user_id = friend_id)
            
            this_obj = models.UserInfo.objects.get(user_id = request.user.id)

            models.FriendRequest.objects.create(to_user = friend_obj, from_user = this_obj)
            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('friend_request_view called without frID in POST')

def accept_decline_view(request):
    '''Handles POST Request recieved from accepting or declining a friend request in people.djhtml,
       sent by people.js, deletes corresponding FriendRequest entry and adds to users friends relation
       if accepted
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute decision,
                                a string of format A-name or D-name where name is
                                a valid username (the user who sent the request)

	Returns
	-------
   	  out : (HttpResponse) - deletes entry to FriendRequest table, appends friends in UserInfo Models,
                             then returns an empty HttpResponse, 404 if POST data doesn't contain decision
    '''
    data = request.POST.get("accept")
    if data is not None:
        # TODO Objective 6: parse decision from data

        if request.user.is_authenticated:
            # (HttpResponse) - deletes entry to FriendRequest table, appends friends in UserInfo Models
            friend_id = models.User.objects.get(username=request.POST.get("sender")).id
            friend_obj = models.UserInfo.objects.get(user_id = friend_id)
            # friend_obj = models.UserInfo.objects.get(friend_id)
            # friend_id = models.User.objects.get(username=request.GET.get("sender")).id
            this_obj = models.UserInfo.objects.get(user_id = request.user.id)
            # print(request.POST.get("accept"))
            # TODO Objective 6: delete FriendRequest entry and update friends in both Users
            if request.POST.get("accept") == "yes":
                this_obj.friends.add(friend_obj)
                friend_obj.friends.add(this_obj)
                # deletes entry to FriendRequest table
            remove = models.FriendRequest.objects.get(from_user = friend_obj, to_user = this_obj)
            # models.FriendRequest.objects.create(to_user = friend_obj, from_user = this_obj)
            remove.delete()
            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('accept-decline-view called without decision in POST')
