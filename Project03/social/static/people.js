/* ********************************************************************************************
   | Handle Submiting Friend Requests - called by $('.like-button').click(submitLike)
   ********************************************************************************************
   */
function frResponse(data,status) {
    if (status == 'success') {
        // reload page to update like count
        location.reload();
    }
    else {
        alert('failed to create friend request ' + status);
    }
}

function friendRequest(event) {
    // the id of the current button, should be fr-name where name is valid username
    let frID = event.target.id;
    // console.log(event)
    // console.log(event.target)
    console.log(event.target.id)
    let json_data = { 'frID' : frID };
    // globally defined in messages.djhtml using i{% url 'social:like_view' %}
    let url_path = friend_request_url;

    // AJAX post
    $.post(url_path,
           json_data,
           frResponse);
}

/* ********************************************************************************************
   | Handle Requesting More People - called by $('#more-ppl-button').click(submitMorePpl)
   ********************************************************************************************
   */
function morePplResponse(data,status) {
    if (status == 'success') {
        // reload page to display new Post
        location.reload();
    }
    else {
        alert('failed to request more ppl' + status);
    }
}

function submitMorePpl(event) {
    // submit empty data
    let json_data = { };
    // globally defined in messages.djhtml using i{% url 'social:more_post_view' %}
    let url_path = more_ppl_url;

    // AJAX post
    $.post(url_path,
           json_data,
           morePplResponse);
}

/* ********************************************************************************************
   | Handle Accepting/Declining Friend Requests -
   |                           called by $('.acceptdecline-button').click(acceptDeclineRequest)
   ********************************************************************************************
   */

function acceptDeclineRequest(event) {
    // TODO Objective 6: perform AJAX POST to accept or decline Friend Request
    // alert('Accept/Decline Button Pressed');
    console.log(event)
    console.log(event.target)
    console.log(event.currentTarget)
    let decide = {"accept":"input","sender":"unknown"}

    if (event.currentTarget.title == "Accept"){
    	decide["accept"] = "yes"
	decide["sender"] = event.currentTarget.id
    } else {
	decide["accept"] = "no"
        decide["sender"] = event.currentTarget.id
    }
    $.post(accept_decline_url, decide, Handler);
}

function Handler(data, status) {
    console.log("Got Response")
    if (status == "success") {
   	location.reload(); 
    }
    else {
    	alert("failed to accept request" + status);
    }

}




/* ********************************************************************************************
   | Document Ready (Only Execute After Document Has Been Loaded)
   ********************************************************************************************
   */
$(document).ready(function() {
    // handle requesting more ppl
    $('#more-ppl-button').click(submitMorePpl);
    // handle for creating a friend request
    $('.fr-button').click(friendRequest);
    // handle for accepting/declining a friend request
    $('.acceptdecline-button').click(acceptDeclineRequest);
});
