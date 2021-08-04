//for solo play
function on() {
    document.getElementById("overlay").style.display = "block";
}
  
function off() {
    document.getElementById("overlay").style.display = "none";
}


//For create multiplayer
function on_1() {
    document.getElementById("overlay_1").style.display = "block";
}
  
function off_1() {
    document.getElementById("overlay_1").style.display = "none";
}


//For join game
function on_2() {
    document.getElementById("overlay_2").style.display = "block";
}
  
function off_2() {
    document.getElementById("overlay_2").style.display = "none";
}


//Websockets for multiplayer
//function to start the quiz
//const newGameBtn = document.getElementById('create_game');
//const joinGameBtn = document.getElementById('join_game');
//create game session

var socket = io()
var $startForm = $('#create_game_id')
var $closebutton = $('#closebtn')
var $newRoomField = $('#createCodeInput')
var $beginButton = $('#begin')
var $panel = $('#panel')
var newData = { room: null }
var count = 0


$('body').addClass('body--admin')



$startForm.on('submit', function(event) {
    event.preventDefault()
    newData.room = $newRoomField.val()
    
    socket.emit('create', newData)
});

socket.on('create', function(success) {
    if (success) {
        $closebutton.hide()
        $startForm.hide()
        $panel.show()
    }
    else {
        alert('That room is taken')
    }
});

$beginButton.on('click', async function() { 
    let reset_data = newData
    socket.emit('reset', reset_data)

    var data = $startForm.serialize();

    //$.post( "/quiz" + newData, data);

    $.ajax({
        url: "/quiz" + newData,
        type: "POST",
        data:data,
        dataType: "json",
        success: function(response) {
            window.location.href = response.redirect
        }
    });

});


socket.on('join', function(newData) {
    count++
    //$roomCount.text(count === 1 ? count + ' person' : count + ' people')
    //$leaderboard.append(`<li class="panel__header">${data.name}<span>0</span></li>`)
    //leaderboard[data.name] = 0
})


//Join game session
var $joinForm = $('#join_game_id')
var $roomField = $('#gameCodeInput')
var $name = $('#name')
var data = {
    room: $roomField, // get the first path
    name: $name
}

$('body').addClass('center')

$joinForm.on('submit', function(event) {
  event.preventDefault()
  data.room = $roomField.val()
  
  socket.emit('exists', data)
})

socket.on('exists', function(exists) {
  if (exists) {
      socket.emit('join', data);
      alert("You have joined a room. Wait for moderator to begin game");
      socket.emit('begin', data);
      /*$.ajax({
        url: "/quiz_2",
        success: function(response) {
            window.location.href = response.redirect
        }
      });*/

      //window.location.href = '/quiz_2'


    /*var data = $joinForm.serialize();

    //$.post( "/quiz" + newData, data);

    $.ajax({
        url: "/quiz_2" + newData,
        type: "POST",
        data:data,
        dataType: "json",
        success: function(response) {
            window.location.href = response.redirect
        }
    });*/

  }
  else {
    alert('That game doesn\'t exist!')
  }
})

//start game session 
//socket.on('begin', function() {

    /*var data = $startForm.serialize();

    //$.post( "/quiz" + newData, data);

    $.ajax({
        url: "/quiz" + newData,
        type: "POST",
        data:data,
        dataType: "json",
        success: function(response) {
            window.location.href = response.redirect
        }
    });
    // $state.hide()*/
//.})
