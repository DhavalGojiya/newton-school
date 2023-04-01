$("button[data-type='delete']").click( function (){
    let id = $(this).attr('id')

    $.ajax({
    type: 'DELETE' ,
    url: `/teachers/courses/manage/delete/${id}/`,
    headers: {
        "X-CSRFToken": WindowCSRF,
    },
    success:function(){
    $(`#card-item-${id}`).remove();
    console.log("Success!" +  "and token" + `${WindowCSRF}`);
  }
    });
});




$('form[id="update-course-form"]').submit(function(event) {
  event.preventDefault(); // Prevent the form from being submitted
  console.log("I am Serialize++", $(this).serialize())

  $.ajax({
    url: $(this).attr('action'),
    type: 'POST',
    data: $(this).serialize(),
    success: function(response) {
            console.log("M RESPONSE++", typeof(response))
             var alertDanger = document.querySelector('.alert-danger');
            if (response.status === 'success') {
                location.reload();

            } else {
                for (let key in response.errors) {
                    let error_message = response.errors[key];
                    alertDanger.innerHTML = `${response.status}! ${key.toUpperCase()} - ${error_message}`;
                }
                alertDanger.classList.add('msg-failed-show');
            };
    }
  });
});

