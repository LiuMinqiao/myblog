

$('#userName').on('blur', function () {
// $.ajaxSetup({
//         data:{csrfmiddlewaretoken:'{{ csrf_token }}'}
// })
var csrf = $('input[name="csrfmiddlewaretoken"]').val();
$.ajax({
        url: 'checkRegister',
        type: 'POST',

        data: {
            'csrfmiddlewaretoken':csrf,
            key:'name',
            username:document.getElementById('userName').value
        },
        dataType: 'json',
        timeout: 1000,
        success: function(result) {
            console.log(result)
            // alert(result['queryKey'])

            document.getElementById('#nameTips').innerText= result.queryKey
        }
       });
  });
$('#inputEmail').on('blur', function () {
var regm = /^\w+([\.\-]\w+)*\@\w+([\.\-]\w+)*\.\w+$/
var csrf = $('input[name="csrfmiddlewaretoken"]').val();
email = $('#inputEmail').val()
// $('#inputEmail').innerText

 if (! email.match(regm)){
     // alert("incorrect email format!!")
     document.getElementById('#emailTips').innerText=  "incorrect email format!!"
 }
 else {
     // document.getElementById('#emailTips').innerText=  ""
// var csrf = $('input[name="csrfmiddlewaretoken"]').val();
$.ajax({
        url: 'checkRegister',
        type: 'POST',

        data: {
            'csrfmiddlewaretoken':csrf,
            key:'email',
            email:document.getElementById('inputEmail').value
        },
        dataType: 'json',
        timeout: 1000,
        success: function(result) {
            console.log(result)
            // alert(result['queryKey'])

            document.getElementById('#emailTips').innerText= result.queryKey
        }
       });

 }
// $.ajax({
//         url: 'checkRegister',
//         type: 'POST',
//
//         data: {
//             'csrfmiddlewaretoken':csrf,
//             key:'name',
//             username:document.getElementById('userName').value
//         },
//         dataType: 'json',
//         timeout: 1000,
//         success: function(result) {
//             console.log(result)
//             // alert(result['queryKey'])
//             document.getElementById('#nameTips').innerText= result.queryKey
//         }
//        });
  });

