#  CS 1XA3 Project03 - sharifj

## Usage
	1) Install conda enivornment with _conda activate djangoenv_
	2) Run locally with : _python manage.py runserver localhost: 8000_
	   Run on mac1xa3 server with : _python manage.py runserver localhost: 10092_
	3) Create an account  with "TestUser", Password: "mis+GDKY5+"

## Objective 01
	**Description**

	1) This feature is rendered by 'signup_view' which routes to  _'signup.djhtml'_
	2) It makes a POST request to https://mac1xa3.ca/e/sharifj/ which is handled by signup_view
	3) Had to make use of the built in _cleaneddata_ operation. I also had to import authenticate and make use of 
	   the redirect operation. 
	4) Added code to handle the POST request sent by the form to create a new user, and logs the new user into the messages page.

	**Exception**

	1) If _https://mac1xa3.ca/e/sharifj/_ is called without any arguments, we are redirected to the login page.

## Objective 02
	** Description **
	
	1) The template social_base.djhtml renders the left_column used by messages.djhtml,people.djhtmland account.djhtml.
	2) Edited social_base.djhtml to implement a real Profile and Inter-ests corresponding to the currently logged in user 
	   by using Django Template Variables.
	
	** Exception **

	1) Clicking on the messages icon would redirect you to _https://mac1xa3.ca/e/sharifj/social/messages/_

## Objective 03
	** Description **
	1) Clicking the top right icon on the Navbar brings you to the Account Settings Page, rendered by 
	   - The function def account_view in Project03/social/views.py
	   - The template Project03/social/templates/account.djhtml
	2) Made use of the Password Change Form and had to create a new function to update the user_info.
	3) Provided forms to change the user's current password and provided forms to update the user_info.
	4) Handled POST requests sent by the form’s to update the UserInfo object accordingly
	
	** Exception**
	1) Need to click on the top right icon on the Navbar. This will only redirect the user to _https://mac1xa3.ca/e/sharifj/social/account/_

## Objective 04
	** Description **
	1) Clicking the people icon on the Navbar brings you to the People Page, rendered by
	   – The function def people_view in _Project03/social/views.py_
	   – The template _Project03/social/templates/people.djhtml_
	   – The javascript code in  _Project03/social/static/people.js_
	2) Displays user's in the middle column who are not friends with the current user.
	3) Made use of Django Session Variables to increase the number of users shown when the 'More' button is clicked.

## Objective 05
	** Description**
	1) All Friend Request buttons are linked to a JQuery event in people.js, which uses its id to send a 
	   POST request to the function def friend_request_view
	2) Configured the Friend Request button so it’s id contains the userwho sent the friend request.
	3) Made use of _models.FriendRequest.objects.create_ function and returned an empty HttpResponse.

	** Exception **
	1) Unlike expected, my friend request button is placed under the name of the user rather than to the right.
	2) It is known who sent a request as the ID is placed under the name of the user.

# Objective 06
	** Description **
	1) Pushing the accept or decline button sends a POST to accept_decline_viewwith the appropriate button id.
	2) Edited the  accept_decline_view to handle the POST request, deleted the corresponding Friend Request entry.
	3) If the friend request was accepted, both user's friends relation in the UserInfo table should be excepted.
	4) Made use of _models.UserInfo.objects.get_ to handle the POST request, and removing the corresponsing Friend Request Entry.

	** Exception **
	1) Continuing from the bug in  Objective 5, the user_id and the friend request button is placed under the user's name.
	2) The Accept and Decline button works successfully, however, The no.of buttons increase following each click. 

## Objective 07
	** Description **
	1) Clicking on the messages icon brings you to the Messages page, rendered by :
	   - The function def messages_view in Project03/social/views.py
	   – The template Project03/social/templates/messages.djhtml
	   – The javascript code Project03/social/static/messages.js
	2) Edited messages.djhtml to display all of the friends of the current user. 
	3) This is obtained by iterating over the objects returned by all of the friends relation in the user_info variable.

	** Exception **
	1) No Exceptions in this case.

## Objective 08
	** Description **
	1) Edited messages.js to submit a AJAX POST request when post-button is clicked, sending the content sof post-text to post_submit_view.
	2) Had to create a new function and location.reload()  to acheive this cause.
	3) Edited post_submit_view to handle the post submission, by adding a new entry to the Post mode
	
	** Exception **
	1) After running _python manage.py collectstatic_, messages.js does not get read properly, hence there are no changes to the messages screen.

## Objective 09 
	** Description **
	1) Edited messages.djhtml to display real posts given by messages_view.
	2) Sorted the posts from newest to oldest by specifying the _timestamp_ within the function
	3) Made use of session variables to display a certain number of posts and gradually increase as we click the "More" Button

	** Exception **
	1) After running _python manage.py collectstatic_, messages.js does not get read properly, hence there are no changes to the messages screen.
	2) The like button does not appear as a result of the static files failing to be read correctly.

## Objective 10
	** Description **
	1) Updated the codebase to allows users to like posts and display a real like count.
	2) Prevented User's from Double Liking the Post by adding an extra boolean statement in message_view to check
	   if a post has aldready been liked or not
	3) I have set the button class to w3-disabled and removethe like-button class so the JQuery event no longer responds to it.

	** Exception **
        1) After running _python manage.py collectstatic_, messages.js does not get read properly, hence there are no changes to the messages screen.
        2) The like button does not appear as a result of the static files failing to be read correctly.
