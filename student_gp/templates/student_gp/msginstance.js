$chat.append('<div class="incoming">' +
             '<strong style="color:black">' + name + '</strong> ' +
             '<span style="color:black">' + datetime + '</span><br>' +
             '<span style="float:right">'+
             '<a href="#" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">'+
               '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-more-vertical"><circle cx="12" cy="12" r="1"></circle><circle cx="12" cy="5" r="1"></circle><circle cx="12" cy="19" r="1"></circle></svg>'+'</a>'+
               '<div class="dropdown-menu dropdown-menu-right" aria-labelledby="dropdownMenuLink-2">'+
                 '<button class="dropdown-item Qbutton">Mark as Ques?</button>'+
                 '<button class="dropdown-item Abutton" href="javascript:void(0);">Mark your Answer </button>'+
               '</div>'+
             '</span>' +
             '<p>'+ message +'</p>'+ '</div>');
