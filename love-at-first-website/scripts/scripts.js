$( document ).ready(function() {
  
  	$('.info').tooltipster({
	    trigger: 'click',
	    maxWidth: 300
	});

  	$('.overlay-message .keep-swiping').click(function() {
  		$('.overlay-message').fadeOut();
  		var section_num = $('.send-message').attr('data-count');
  		console.log(section_num);
  		section_num = section_num - 1;
  		$('.send-message').attr('data-count', section_num);
  	});

  /**
	 * jTinder initialization
	 */
	$("#tinderslide").jTinder({
		// dislike callback
	    onDislike: function (item) {
		    // set the status text
		    box_num = item.index()+1;
		    //console.log(box_num);
		    if (box_num == 1) {
		    	$('a.keep-swiping').hide();
		    }
		    tooltip_num = item.index();
		    tooltip_class = '.actions .info' + tooltip_num +'';
		    $('.actions .info').removeClass('active');
		    $(tooltip_class).addClass('active');
		    message_class = '.dislike-message-' + box_num + '';
	        message_content = $(message_class).html();
	        $('.overlay-message.dislike-overlay .message-container').html(message_content);
	        $('.overlay-message.dislike-overlay').fadeIn();
	        if (box_num == 1) {
	        	$('.actions').fadeOut();
	        }
	    },
		// like callback
	    onLike: function (item) {
		    // set the status text
	        box_num = item.index()+1;
	        //console.log(box_num);
	        if (box_num == 1) {
		    	$('a.keep-swiping').hide();
		    }
	        tooltip_num = item.index();
		    tooltip_class = '.actions .info' + tooltip_num +'';
		    $('.actions .info').removeClass('active');
		    $(tooltip_class).addClass('active');
		    message_class = '.like-message-' + box_num + '';
	        message_content = $(message_class).html();
	        $('.overlay-message.like-overlay .message-container').html(message_content);
	        $('.overlay-message.like-overlay').fadeIn();
	        if (box_num == 1) {
	        	$('.actions').fadeOut();
	        }
	    },
		animationRevertSpeed: 200,
		animationSpeed: 400,
		threshold: 1,
		likeSelector: '.like',
		dislikeSelector: '.dislike'
	});

	/**
	 * Set button action to trigger jTinder like & dislike.
	 */
	$('.actions .like, .actions .dislike').click(function(e){
		e.preventDefault();
		$("#tinderslide").jTinder($(this).attr('class'));
	});

	$('.btn.send-message').click(function() {
		$('.overlay-message').fadeOut();
		var section_num = $('.send-message').attr('data-count');
		var target_chat = '.chat-' +  section_num + '';
		//console.log(target_chat);
		$(target_chat).addClass('active');
		delay = 0;
		date_num = 0;
		$(target_chat).find('.chat-message-container').each(function() {
			var delay_add = parseInt($(this).attr('data-delay'));
			//console.log(delay_add);
			delay = delay + delay_add;
			//console.log(delay);
			$(this).delay(delay).queue(function() { 
				$(this).addClass('active');
				$(this).find('.date1').hide();
				$(this).find('.date1').fadeIn();
				if ($(this).find('.date').length) {
					//console.log('has date');
					//console.log(date_num);
					$('.chat-message-container').find('.date' + date_num + '').hide();
					date_num = date_num + 1;
					$('.chat-message-container').find('.date' + date_num + '').show();
				}
				//console.log(target_chat);
				var chat_container = $(target_chat).find('.container');
				var chat_container_height = $(chat_container).height();
				//$(target_chat).find('.container').scrollTop($(target_chat).find('.container').scrollHeight);
				console.log(chat_container_height);

				//$(target_chat).scrollTop(chat_container_height);
				//$(target_chat).find('.container').scrollHeight;
				/*$(target_chat).animate({
				    scrollTop: chat_container_height,
				}, 500);​*/
				/*$(target_chat).animate({
		         	scrollTop: chat_container_height
		     	}, 10000, 'swing');*/
			});
		});
	});

	$('.overlay-chat .keep-swiping').click(function() {
  		$('.overlay-chat').removeClass('active');
  		var section_num = $('.send-message').attr('data-count');
  		console.log(section_num);
  		section_num = section_num - 1;
  		$('.send-message').attr('data-count', section_num);
  	});

	//$(".overlay-chat").customScrollbar();
	

});

function refreshPage(){
    window.location.reload();
} 