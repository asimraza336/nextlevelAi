

window.addEventListener('scroll', function () {
   var header = document.querySelector('.fixed-header');
   var content = document.querySelector('.content');
   if (window.pageYOffset > 0) {
      header.classList.add('shadow');
      content.style.paddingTop = (header.offsetHeight + 20) + 'px';
   } else {
      header.classList.remove('shadow');
      content.style.paddingTop = '80px'; // Adjust this value to accommodate the fixed header's height
   }
});

function changeBackgroundColor(card, url) {
   card.style.backgroundColor = "lightblue";
   selectImage(url);
}

function resetBackgroundColor(card) {
   card.style.backgroundColor = "";
}

function selectImage(url) {
   var selectedImage = document.getElementById("selectedImage");
   selectedImage.src = url;
}

// Add event listener to the form

var form = document.getElementById('myForm'); // Replace 'myForm' with the ID of your form element
form.addEventListener('submit', handleFormSubmit);


function handleFormSubmit(event) {
   event.preventDefault(); // Prevent the default form submission behavior

   // Retrieve the form data or perform any necessary validation
   // ...

   // Redirect to another page
   window.location.href = 'path/to/another/page.html';
}

function toggleButton(btn) {
   if (btn === 1) {
      document.getElementById('btn1').classList.add('btn-active');
      document.getElementById('btn2').classList.remove('btn-active');
      document.getElementById('heading1').classList.remove('hidden');
      document.getElementById('heading2').classList.add('hidden');
   } else if (btn === 2) {
      document.getElementById('btn1').classList.remove('btn-active');
      document.getElementById('btn2').classList.add('btn-active');
      document.getElementById('heading1').classList.add('hidden');
      document.getElementById('heading2').classList.remove('hidden');
   }
}

function redirectToAvator() {
   window.location.href = "../pages/avatar/Avatar.html";
}

$(document).ready(function () {
   $("#quizForm").submit(function (e) {
      e.preventDefault(); // Prevent form submission
      var answers = {};

      // Retrieve selected answers
      $('input[type=radio]:checked').each(function () {
         var question = $(this).attr('name');
         var answer = $(this).val();
         answers[question] = answer;
      });

      // Process the answers
      console.log(answers); // You can customize this code to handle the answers

      // Clear selected answers
      $('input[type=radio]').prop('checked', false);
   });
});